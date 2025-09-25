import faiss
import numpy as np
from ordeq_faiss import FaissIndex


def test_index(tmp_path):
    vectors = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])

    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)  # ty: ignore[missing-argument]

    k = 1

    _, id_1 = index.search(np.array([[1.1, 1.9, 3.0]]), k)  # ty: ignore[missing-argument]

    dataset = FaissIndex(path=tmp_path / "example.index")
    dataset.save(index)

    loaded_index = dataset.load()
    _, id_2 = loaded_index.search(np.array([[1.1, 1.9, 3.0]]), k)  # ty: ignore[missing-argument]
    assert id_1 == id_2
    assert id_1.tolist() == [[0]]
