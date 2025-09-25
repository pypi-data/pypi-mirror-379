import torch
import torch.nn.functional as F
import numpy as np
import random as rn
from torch_geometric.loader import LinkNeighborLoader,NeighborLoader
from torch_geometric.sampler import NegativeSampling
from tqdm import tqdm
import os.path as osp
import os
import pandas as pd
from torch_geometric.data import Data

@torch.no_grad()
def validate(
    model,
    val_loader,
    device,
    num_classes: int,
    batch_size: int = 2048,
    num_neighbors: list[int] = [20, 10],
    verbose: bool = True,
    num_train_edges: int = 5000,
    seed = 42
) -> float:
    """
    Run validation for link prediction task.

    Args:
        model (torch.nn.Module): The GNN model to evaluate.
        val_loader (torch.utils.data.DataLoader): Loader with validation graphs.
        device (torch.device): Device to run evaluation on.
        num_classes (int): Number of node feature classes (for one-hot encoding).
        batch_size (int, optional): Batch size for LinkNeighborLoader. Defaults to 2048.
        num_neighbors (list[int], optional): Neighbor sampling sizes. Defaults to [20, 10].
        verbose (bool, optional): Whether to print progress. Defaults to True.

    Returns:
        float: Mean validation accuracy.
    """
    rn.seed(seed)
    model.eval()
    all_acc = []

    for d_i, d_batch in enumerate(val_loader):
        if verbose:
            print(f"Processing validation on batch graph {d_i}...")
        sampled_edge_index = getattr(d_batch, "edge_label_index", None)
        if sampled_edge_index is None:
            sampled_edge_index  = d_batch.edge_index[:,rn.sample(range(d_batch.edge_index.shape[1]),num_train_edges)]
        val_mini_loader = LinkNeighborLoader(
            d_batch,
            batch_size=batch_size,
            shuffle=False,
            edge_label_index=sampled_edge_index,
            neg_sampling=NegativeSampling(mode="triplet", amount=1),
            num_neighbors=num_neighbors,
            disjoint=False,
            subgraph_type="bidirectional",
        )

        batch_acc = []
        for batch in tqdm(val_mini_loader, desc=f"Val minibatching {d_i}", disable=not verbose):
            batch = batch.to(device)
            # Build edge labels
            pos_edges = torch.stack([batch.src_index, batch.dst_pos_index], dim=0)
            neg_edges = torch.stack([batch.src_index, batch.dst_neg_index], dim=0)
            b_edge_label_index = torch.cat([pos_edges, neg_edges], dim=1)

            b_edge_label = torch.cat([
                torch.ones(batch.src_index.size(0), device=device),
                torch.zeros(batch.src_index.size(0), device=device)
            ])

            # One-hot encoding of features
            batch.x = F.one_hot(batch.x, num_classes=num_classes).float().squeeze(1)

            # Forward pass
            h = model(batch.x, batch.edge_index)
            h_src, h_dst = h[b_edge_label_index[0]], h[b_edge_label_index[1]]
            pred = (h_src * h_dst).sum(dim=-1)

            probabilities = torch.sigmoid(pred)
            predictions = (probabilities >= 0.5).float()

            acc = (predictions == b_edge_label).float().mean().item()
            batch_acc.append(acc)

            del batch  # free GPU memory

        all_acc.append(np.mean(batch_acc))

        del val_mini_loader, d_batch

    return float(np.mean(all_acc))

def train(
    model,
    train_loader,
    device,
    num_classes: int,
    optimizer =None,
    batch_size: int = 2048,
    num_neighbors: list[int] = [20, 10],
    verbose: bool = True,
    num_train_edges: int = 5000,
    seed: int = 42

):
    """
    Run one epoch of training for link prediction.

    Args:
        model (torch.nn.Module): The GNN model to train.
        train_loader (torch.utils.data.DataLoader): Loader with training graphs.
        device (torch.device): Device for computation.
        num_classes (int): Number of node feature classes (for one-hot encoding).Equals the number of unique gene ids in all samples.
        optimizer: Torch optimizer, eg. torch.optim.Adam(model.parameters(), lr=0.001)
        batch_size (int, optional): Mini-batch size. Defaults to 2048.
        num_neighbors (list[int], optional): Neighbor sampling sizes. Defaults to [20, 10].
        verbose (bool, optional): Show progress bars. Defaults to True.

    Returns:
        tuple[float, float]: Mean loss and mean accuracy across batches.
    """
    rn.seed(seed)
    model.train()
    d_batch_loss, d_batch_acc = [], []

    for d_i, d_batch in enumerate(train_loader):
        if verbose:
            print(f"Training on batch graph {d_i}...")
        sampled_edge_index = getattr(d_batch, "edge_label_index", None)
        if sampled_edge_index is None:
            sampled_edge_index  = d_batch.edge_index[:,rn.sample(range(d_batch.edge_index.shape[1]),num_train_edges)]

        train_mini_loader = LinkNeighborLoader(
            d_batch,
            batch_size=batch_size,
            shuffle=True,
            edge_label_index=sampled_edge_index,
            neg_sampling=NegativeSampling(mode="triplet", amount=1),
            num_neighbors=num_neighbors,
            disjoint=False,
            subgraph_type="bidirectional",
        )

        total_loss, correct, total_edges = 0, 0, 0

        for batch in tqdm(train_mini_loader, desc=f"Train minibatching {d_i}", disable=not verbose):
            batch = batch.to(device)
            optimizer.zero_grad()

            # Edge labels
            pos_labels = torch.ones(batch.src_index.size(0), device=device)
            neg_labels = torch.zeros(batch.src_index.size(0), device=device)
            b_edge_label = torch.cat([pos_labels, neg_labels])
            b_edge_label_index = torch.cat([
                torch.stack([batch.src_index, batch.dst_pos_index]),
                torch.stack([batch.src_index, batch.dst_neg_index])
            ], dim=1)

            # Forward
            batch.x = F.one_hot(batch.x, num_classes=num_classes).float().squeeze(1)
            h = model(batch.x, batch.edge_index)
            h_src, h_dst = h[b_edge_label_index[0]], h[b_edge_label_index[1]]
            pred = (h_src * h_dst).sum(dim=-1)

            # Loss
            loss = F.binary_cross_entropy_with_logits(pred, b_edge_label)
            loss.backward()
            optimizer.step()

            # Metrics
            total_loss += loss.item() * pred.size(0)
            probs = torch.sigmoid(pred)
            preds = (probs >= 0.5).float()
            correct += (preds == b_edge_label).sum().item()
            total_edges += pred.size(0)

            del batch  # free GPU memory

        d_batch_loss.append(total_loss / total_edges)
        d_batch_acc.append(correct / total_edges)

        del train_mini_loader, d_batch

    
    return float(np.mean(d_batch_loss)), float(np.mean(d_batch_acc))

def train_label_pred(
    model,
    train_loader,
    device,
    num_classes: int,
    optimizer = None,
    batch_size: int = 2048,
    num_neighbors: list[int] = [20, 10],
    verbose: bool = True,
    num_train_nodes: int = 10000,
    seed: int = 42
):
    """
    Run one epoch of training for link prediction.

    Args:
        model (torch.nn.Module): The GNN model to train.
        train_loader (torch.utils.data.DataLoader): Loader with training graphs.
        device (torch.device): Device for computation.
        num_classes (int): Number of node feature classes (for one-hot encoding).Equals the number of unique gene ids in all samples.
        optimizer:Torch optimier, eg. torch.optim.Adam(model.parameters(), lr=0.001)
        batch_size (int, optional): Mini-batch size. Defaults to 2048.
        num_neighbors (list[int], optional): Neighbor sampling sizes. Defaults to [20, 10].
        verbose (bool, optional): Show progress bars. Defaults to True.

    Returns:
        tuple[float, float]: Mean loss and mean accuracy across batches.
    """
    rn.seed(seed)
    model.train()
    batch_losses, batch_accuracies = [], []

    for d_i, d_batch in enumerate(train_loader):
        if verbose:
            print(f"Training on batch graph {d_i}...")

        train_mask = getattr(d_batch, "train_mask", None)
        if train_mask is None:
            # random subset of nodes for training
            train_mask = torch.tensor(
                rn.sample(range(d_batch.x.shape[0]), num_train_nodes),
                dtype=torch.long
            )
        else:
            train_mask = train_mask.nonzero(as_tuple=False).view(-1)

        # Create mini-batches with neighbor sampling
        train_mini_loader = NeighborLoader(
            d_batch,
            batch_size=batch_size,
            shuffle=True,
            num_neighbors=num_neighbors,
            input_nodes=train_mask,
            subgraph_type = "bidirectional"
        )

        for batch in tqdm(train_mini_loader, disable=not verbose):
            batch = batch.to(device)
            optimizer.zero_grad()
            batch.x = F.one_hot(batch.x, num_classes=num_classes).float().squeeze(1)
            # Restrict loss computation to labeled nodes in the mini-batch. Head nodes of batch_size
            out = model(batch.x, batch.edge_index)[:batch.batch_size]
            y_head = batch.y[:batch.batch_size]

            loss = F.cross_entropy(out, y_head)
            loss.backward()
            optimizer.step()

            batch_losses.append(loss.item())
            preds = out.argmax(dim=1)
            correct = (preds == y_head).sum().item()
            acc = correct / y_head.size(0)
            batch_accuracies.append(acc)

    mean_loss = float(sum(batch_losses) / len(batch_losses))
    mean_acc = float(sum(batch_accuracies) / len(batch_accuracies))
    return mean_loss, mean_acc

    
 
@torch.no_grad
def inference(
    model,
    device,
    sample_name,
    root = "../data/",
    tile_id = [0],
    num_neighbors = [20,10],
    num_classes: int = 500,
    batch_size: int = 2048,
    verbose = True) -> None:
    """
    Run one epoch of training for link prediction.

    Args:
        model (torch.nn.Module): The GNN model with trained weights.
        device (torch.device): Device for computation.
        sample_name (str): sample name.
        tile_id ([int]): The tile ids to process for the sample_name.
        num_classes (int): Number of node feature classes (for one-hot encoding).Equals the number of unique gene ids in all samples.
        batch_size (int, optional): Mini-batch size. Defaults to 2048.
        num_neighbors (list[int], optional): Neighbor sampling sizes. Defaults to [20, 10].
        verbose (bool, optional): Show progress bars. Defaults to True.
    """
    for t_id in tile_id:
        data_path = osp.join(root,"processed",f'{sample_name}_data_tile{t_id}.pt')
        assert osp.exists(data_path)
        data = torch.load(data_path)
        data = Data(**data[0])
        subgraph_loader = NeighborLoader(
            data,
            input_nodes=data.core_mask,
            #num_neighbors=[-1],
            num_neighbors=num_neighbors,
            batch_size=batch_size,
            replace=False,
            shuffle=False,
            subgraph_type = "bidirectional"
            )
        xs = []
        for batch in tqdm(subgraph_loader, disable=not verbose):
            batch = batch.to(device)
            batch.x = torch.nn.functional.one_hot(batch.x, num_classes=num_classes).float().squeeze(1) 

            out = model(batch.x, batch.edge_index)
            # NOTE Only consider predictions and labels of seed nodes:
            out = out[:batch.batch_size]
            xs.append(out.cpu())
            
        x_all = torch.cat(xs, dim=0)
        # Define directory for embeddings
        emb_dir = osp.join(root, "embedding")
        os.makedirs(emb_dir, exist_ok=True)
        # Define output .npy file path
        out_embs_npy = osp.join(emb_dir, f"{sample_name}_data_tile{t_id}.npy")
        np.save(out_embs_npy,x_all)
        pd.DataFrame({"tx_id":data.trans_id[data.core_mask.cpu()]}).to_csv(out_embs_npy.replace(".npy","input_tx_id.csv"), index=False)
    None


import torch
from torch_geometric.loader import NeighborLoader
from tqdm import tqdm

def validate_label_pred(
    model,
    val_loader,
    device,
    batch_size: int = 2048,
    num_neighbors: list[int] = [20, 10],
    verbose: bool = True
):
    """
    Run one epoch of validation for node classification.

    Args:
        model (torch.nn.Module): Trained GNN model.
        val_loader (torch.utils.data.DataLoader): Loader with validation graphs.
        device (torch.device): Device for computation.
        batch_size (int, optional): Mini-batch size. Defaults to 2048.
        num_neighbors (list[int], optional): Neighbor sampling sizes. Defaults to [20, 10].
        verbose (bool, optional): Show progress bars. Defaults to True.

    Returns:
        float: Mean accuracy across validation batches.
    """
    model.eval()
    batch_accuracies = []

    with torch.no_grad():
        for d_i, d_batch in enumerate(val_loader):
            if verbose:
                print(f"Validating on batch graph {d_i}...")

            val_mask = getattr(d_batch, "val_mask", None)
            if val_mask is not None:
                val_nodes = val_mask.nonzero(as_tuple=False).view(-1)

            val_mini_loader = NeighborLoader(
                d_batch,
                batch_size=batch_size,
                shuffle=False,
                num_neighbors=num_neighbors,
                input_nodes=val_nodes,
            )

            for batch in tqdm(val_mini_loader, disable=not verbose):
                batch = batch.to(device)
                out = model(batch.x, batch.edge_index)[:batch.batch_size]
                y_head = batch.y[:batch.batch_size]

                preds = out.argmax(dim=1)
                correct = (preds == y_head).sum().item()
                acc = correct / y_head.size(0)
                batch_accuracies.append(acc)
                
    mean_acc = float(sum(batch_accuracies) / len(batch_accuracies))
    return mean_acc