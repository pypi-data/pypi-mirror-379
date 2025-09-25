from typing import Any

import numpy as np
from sonusai.datatypes import Feature
from sonusai.datatypes import TruthsDict
from torch.utils.data import DataLoader


class AawareDataLoader(DataLoader):
    _cut_len: int = 0

    @property
    def cut_len(self) -> int:
        return self._cut_len

    @cut_len.setter
    def cut_len(self, value: int) -> None:
        self._cut_len = value


def collate_fn(data: list[tuple[Feature, TruthsDict, int]]) -> list[tuple[Feature, TruthsDict, int]]:
    """Use this collate function whenever cut_len == 0 and batch_size > 1.

    Pad mixtures with zeros so that they have the same length and can be concatenated.
    Once the features and truths have been padded to the same length, then call the default Torch collate function.
    """
    from torch.utils.data.dataloader import default_collate

    max_frames = max(item[0].shape[0] for item in data)
    pad_width = [(0, 0)] * 3

    new_data: list[tuple[Feature, TruthsDict, int]] = []
    for n in range(len(data)):
        feature = data[n][0]
        truth = data[n][1]
        mixid = data[n][2]

        this_frames = feature.shape[0]
        pad_len = max_frames - this_frames

        pad_width[0] = (0, pad_len)

        padded_feature = np.pad(feature, list_to_tuple(pad_width), mode="constant", constant_values=0)
        padded_truth = {
            category: {
                key: np.pad(truth[category][key], list_to_tuple(pad_width), mode="constant", constant_values=0)
                for key in truth[category]
            }
            for category in truth
        }
        new_data.append((padded_feature, padded_truth, mixid))

    return default_collate(new_data)


def list_to_tuple(lst: list[Any]) -> tuple[Any, ...]:
    return tuple(tuple(x) for x in lst)
