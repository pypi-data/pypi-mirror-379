import os
import os.path as osp
import glob
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import joblib

def run_kmeans(
    sample_name_list=None,
    root="../data/",
    downsample_to=None,
    downsample_seed=1024,
    verbose=True,
    split_file_per_sample=True,
    **kwargs
) -> None:
    """
    Cluster embeddings from multiple samples using KMeans.

    Args:
        sample_name_list (list[str], optional): List of sample names to cluster. Defaults to None (auto-detect).
        root (str): Path to data directory containing samples.
        downsample_to (int, optional): Maximum number of rows per sample. Defaults to None (no downsampling).
        downsample_seed (int): Random seed for downsampling.
        verbose (bool, optional): Print progress. Defaults to True.
        split_file_per_sample (bool, optional): Save per-sample CSVs if True; else save one CSV.
        **kwargs: Additional arguments for sklearn KMeans (e.g., n_clusters).

    Returns:
        pd.DataFrame: DataFrame with columns ['sample_name','tx_ids','cluster_labels']
    """

    if sample_name_list is None:
        # Detect sample names with 'embedding' subdir
        sample_name_list = [
            d for d in os.listdir(root)
            if osp.isdir(osp.join(root, d)) and osp.isdir(osp.join(root, d, "embedding"))
        ]

    if verbose:
        print(f"Clustering samples: {sample_name_list}")

    all_embeddings = []
    all_tx_meta = []

    np.random.seed(downsample_seed)

    for sample_name in sample_name_list:
        data_path = osp.join(root, sample_name, "embedding")

        # Load embeddings
        npy_list = glob.glob(osp.join(data_path, "*.npy"))
        #print(npy_list)
        if not npy_list:
            raise FileNotFoundError(f"No .npy files found for sample {sample_name}")
        x_list = [np.load(f) for f in npy_list]
        x_sample = np.concatenate(x_list, axis=0)

        # Load tx_id files, make sure the same order as npy files.
        tx_id_list = [x.replace(".npy","input_tx_id.csv") for x in npy_list]
        #print(tx_id_list)
        if not tx_id_list:
            raise FileNotFoundError(f"No *input_tx_id.csv files found for sample {sample_name}")
        tx_ids_emb = pd.concat([pd.read_csv(f) for f in tx_id_list], axis=0)
        tx_ids_emb['sample_name'] = sample_name

        # Optional downsampling
        if downsample_to is not None and tx_ids_emb.shape[0] > downsample_to:
            tx_ids_emb = tx_ids_emb.sample(n=downsample_to, random_state=downsample_seed).reset_index(drop=True)
            idx = np.random.choice(x_sample.shape[0], downsample_to, replace=False)
            x_sample = x_sample[idx, :]

        all_embeddings.append(x_sample)
        all_tx_meta.append(tx_ids_emb)

        if verbose:
            print(f"{sample_name}: embeddings {x_sample.shape}, tx_ids {tx_ids_emb.shape}")

    # Concatenate all samples
    X_all = np.concatenate(all_embeddings, axis=0)
    tx_meta_all = pd.concat(all_tx_meta, axis=0).reset_index(drop=True)

    # KMeans parameters, default 10
    n_clusters = kwargs.pop('n_clusters', 10)
    km = KMeans(n_clusters=n_clusters, **kwargs)
    km.fit(X_all)

    # Build result DataFrame
    res_all = pd.DataFrame({
        'sample_name': tx_meta_all['sample_name'],
        'tx_ids': tx_meta_all['tx_id'],
        'cluster_labels': km.labels_.astype(str)
    })

    # Save results
    if split_file_per_sample:
        for sample_name in tx_meta_all['sample_name'].unique():
            out_dir = osp.join(root, sample_name, "clusters")
            os.makedirs(out_dir, exist_ok=True)
            res_all[res_all['sample_name'] == sample_name].to_csv(
                osp.join(out_dir, f"{sample_name}.{n_clusters}clusters.csv"),
                index=False
            )
    else:
        out_file = osp.join(root, f'kmeans.{n_clusters}clusters.csv')
        res_all.to_csv(out_file, index=False)

    if verbose:
        print("Clustering completed.")
    joblib.dump(km, osp.join(root, f'kmeans.{n_clusters}clusters.models.joblib'))
    
    None
