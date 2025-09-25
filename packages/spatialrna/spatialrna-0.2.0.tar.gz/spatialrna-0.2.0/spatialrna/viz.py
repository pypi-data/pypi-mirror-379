import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os
import os.path as osp
from scipy.stats import mode
import cv2

def get_tx_plot_df(root="multi_sample_label_pred",
                   sample_name ="lung1",
                   n_clusters = 10):
    """
    Gather clustering results and transcript meta data into one DataFrame

    Args:
        root (str): Path of root data dir. Transcript meta file is expected in {root}/sample_name/raw/sample_name.csv
        n_clusters: The number of K clusters in previous run_kmeans function call
    """           
    tx_meta_file = osp.join(root,sample_name,"raw",f"{sample_name}.csv")
    assert osp.exists(tx_meta_file)
    tx_meta = pd.read_csv(tx_meta_file)
    tx_meta = tx_meta.reset_index(drop=True)
    tx_meta["tx_ids"] = tx_meta.index
    
    cluster_res = osp.join(root,sample_name,"clusters",f"{sample_name}.{n_clusters}clusters.csv")
    assert osp.exists(cluster_res)
    cluster_res_df = pd.read_csv(cluster_res)
    # --- Reorder cluster_res_df to match tx_meta.index ---
    cluster_res_df = cluster_res_df.set_index("tx_ids").loc[tx_meta.index].reset_index()

    # Now assign labels without reordering tx_meta
    tx_meta["cluster_labels"] = cluster_res_df["cluster_labels"].values
    
    return tx_meta
def plot_pixel(tx_meta,
               pixel_size: float = 10,
               min_points: int = 5,
               x='X',
               y='Y',
               cluster_labels="cluster_labels",
               figsize=(8, 8),
               cmap=None,
               join_method="avg",  # "avg" or "major"
               background_color="white",
               output_path=None,
               **kwargs):
    """
    Pixelate points and color each pixel by either:
      - average RGB of all points ("avg"), or
      - major label color ("major").
    Pixels with < min_points are set to background.
    """
    if not isinstance(cmap, dict):
        raise ValueError("cmap must be a dict mapping cluster labels to hex colors")
    if join_method not in {"avg", "major"}:
        raise ValueError("join_method must be 'avg' or 'major'")

    tx_meta = tx_meta.copy()

    # Map cluster labels → RGB (0-1 range)
    tx_meta['RGB'] = tx_meta[cluster_labels].map(
        lambda lbl: mcolors.to_rgb(cmap.get(lbl, background_color))
    )
    tx_meta[['R', 'G', 'B']] = pd.DataFrame(tx_meta['RGB'].tolist(), index=tx_meta.index)

    # Compute pixel indices
    tx_meta['px'] = (tx_meta[x] // pixel_size).astype(int)
    tx_meta['py'] = (tx_meta[y] // pixel_size).astype(int)

    # Function to compute pixel color per group
    def pixel_color(df):
        if len(df) < min_points:
            return pd.Series([np.nan, np.nan, np.nan], index=['R','G','B'])
        if join_method == "avg":
            return pd.Series([df['R'].mean(), df['G'].mean(), df['B'].mean()], index=['R','G','B'])
        else:  # "major"
            major_label = df[cluster_labels].mode().iloc[0]
            return pd.Series(mcolors.to_rgb(cmap.get(major_label, background_color)), index=['R','G','B'])


    # Only keep the columns needed by pixel_color
    subset = tx_meta[['px', 'py', 'R', 'G', 'B', cluster_labels]]
    # Group by px, py and apply pixel_color
    pixel_df = (
        subset.groupby(['px', 'py'])[['R','G','B', cluster_labels]]
        .apply(pixel_color)
        .reset_index()
    )
    # Pivot into 2D grid
    pivot_r = pixel_df.pivot(index='py', columns='px', values='R').iloc[::-1]
    pivot_g = pixel_df.pivot(index='py', columns='px', values='G').iloc[::-1]
    pivot_b = pixel_df.pivot(index='py', columns='px', values='B').iloc[::-1]

    img = np.dstack([pivot_r, pivot_g, pivot_b])

    # Fill NaNs with background color
    bg_rgb = np.array(mcolors.to_rgb(background_color))
    nan_mask = np.isnan(img)
    img[nan_mask] = np.take(bg_rgb, nan_mask.nonzero()[2])

    if output_path is None:
        fig, ax = plt.subplots(1, 1, figsize=figsize, **kwargs)
        ax.imshow(img, interpolation="none", origin="upper")
        ax.axis("off")
        ax.set_title(f"Pixelated ({join_method}) (min_points={min_points})")
        return fig, ax
    else:
        # Convert to uint8 and BGR for OpenCV
        img_uint8 = np.clip(img*255, 0, 255).astype(np.uint8)
        img_bgr = cv2.cvtColor(img_uint8, cv2.COLOR_RGB2BGR)
        cv2.imwrite(output_path, img_bgr)
        print(f"Saved pixelated RGB image to {output_path}")


def plot_hex_bin(tx_meta,
                 x="X",
                 y="Y",
                 cluster_labels="cluster_labels",
                 bin_thresh=10,
                 bin_width=5,
                 figsize=(12, 10),
                 cmap=None,
                 background_color="white",
                 **kwargs):
    """
    Hex-binning of points, colored by majority cluster label.
    """

    # majority rule
    def get_major_cluster(values):
        if len(values) < bin_thresh:
            return np.nan
        result = mode(values, keepdims=True)
        return result.mode[0] if result.mode.size > 0 else np.nan

    # bin resolution
    x_bins = int((tx_meta[x].max() - tx_meta[x].min()) / bin_width)
    y_bins = int((tx_meta[y].max() - tx_meta[y].min()) / bin_width)

    fig, ax = plt.subplots(figsize=figsize, constrained_layout=True, **kwargs)

    # handle cmap (dict or colormap string)
    if isinstance(cmap, dict):
        # map labels → ints for hexbin
        labels_unique = sorted(tx_meta[cluster_labels].dropna().unique())
        label_to_int = {lbl: i for i, lbl in enumerate(labels_unique)}
        int_to_color = {label_to_int[k]: mcolors.to_rgba(v) for k, v in cmap.items()}
        # convert data to ints
        data_vals = tx_meta[cluster_labels].map(label_to_int)
        cmap_obj = mcolors.ListedColormap([int_to_color.get(i, mcolors.to_rgba(background_color))
                                   for i in range(len(label_to_int))])
        
    else:
        # numeric encoding for labels
        labels_unique = sorted(tx_meta[cluster_labels].dropna().unique())
        label_to_int = {lbl: i for i, lbl in enumerate(labels_unique)}
        data_vals = tx_meta[cluster_labels].map(label_to_int)
        cmap_obj = plt.get_cmap(cmap or "tab10", len(labels_unique))

    # hexbin majority aggregation
    hb = ax.hexbin(
        tx_meta[x],
        tx_meta[y],
        C=data_vals,
        gridsize=(x_bins, y_bins),
        reduce_C_function=get_major_cluster,
        linewidths=0.05,
        cmap=cmap_obj
    )

    # axis cosmetics
    ax.invert_yaxis()
    ax.set_xlabel(x, fontsize=12)
    ax.set_ylabel(y, fontsize=12)
    ax.tick_params(axis='both', which='both', colors='black')
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_linewidth(1.5)
    ax.grid(False)
    ax.set_aspect('equal', adjustable='box') # or 'datalim'

    # colorbar
    cb = fig.colorbar(hb, ax=ax, orientation="vertical")
    cb.set_label("Major Cluster", fontsize=10)

    return fig, ax 
