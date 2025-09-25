import os
import glob
import torch
from torch_geometric.data import Database, OnDiskDataset, Data

class SpatialRNAOnDiskDatasetSQL(OnDiskDataset):
    def __init__(self, root, pt_dir="subgraph", use_sqlite=False,
                 transform=None, pre_transform=None):
        self.pt_dir = pt_dir

        # If SQLite backend is requested, point it to a database path
        super().__init__(root, transform, pre_transform, backend="sqlite")

    @property
    def processed_file_names(self):
        #os.path.join(root, "sqlite.db")
        #files = glob.glob(os.path.join(self.root, "*", self.pt_dir, "*.pt"))
        #return os.path.join(self.root, "sqlite.db")
        return  "sqlite.db"

    def pt_file_names(self):
        # All .pt files under root/**/pt_dir/
        files = glob.glob(os.path.join(self.root, "*", self.pt_dir, "*.pt"))
        return sorted(files)
    # @property
    # def processed_dir(self) -> str:
    #     return os.path.join(self.root, '/')

    def process(self):
        all_pt_files = self.pt_file_names()
        print(self.processed_paths)
        for pt_file in all_pt_files:
            data = Data(**torch.load(pt_file)[0],weights_only=True)
            self.append(self.serialize(data))

    # def len(self):
    #     return len(self.processed_file_names)

    # def get(self, idx):
    #     path = self.processed_file_names[idx]
    #     return torch.load(path)


class SpatialRNAOnDiskDataset(OnDiskDataset):
    def __init__(self, root, pt_dir="subgraph", transform=None, pre_transform=None):
        self._pt_dir = pt_dir  # use a private var
        super().__init__(root, transform, pre_transform)
        None

    @property
    def processed_file_names(self):
        # Find all .pt files under root/**/processed/
        files = glob.glob(os.path.join(self.root, "*", self._pt_dir, "*_data_tile*.pt"))
        return sorted(files)

    def process(self):
        # Already done – nothing to process.
        pass

    def len(self):
        return len(self.processed_file_names)

    def get(self, idx):
        path = self.processed_file_names[idx]
        data =  torch.load(path,weights_only=True)
        return Data(**data[0])
    def multi_get(self, idx_list):
        """Load multiple graphs at once, similar to SQLite-backed OnDiskDataset."""
        data_list = []
        for idx in idx_list:
            path = self.processed_file_names[idx]
            data = torch.load(path, weights_only=True)
            data_list.append(Data(**data[0]))
        return data_list