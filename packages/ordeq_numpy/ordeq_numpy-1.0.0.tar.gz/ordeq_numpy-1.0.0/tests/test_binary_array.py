from pathlib import Path

import numpy as np
from ordeq_numpy import NumpyBinary


def test_array_binary(tmp_path: Path):
    vectors = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])

    dataset = NumpyBinary(path=tmp_path / "example.npy")
    dataset.save(vectors)

    assert len((tmp_path / "example.npy").read_bytes()) == 200

    loaded_array = dataset.load()
    assert (loaded_array == vectors).all()
