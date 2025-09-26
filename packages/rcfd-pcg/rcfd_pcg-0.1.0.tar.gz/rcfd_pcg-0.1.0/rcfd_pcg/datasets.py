from __future__ import annotations

"""
Real dataset loaders for use with the packaged real benchmark CLI.

All loaders return (A, b) where A is either a NumPy ndarray (dense) or a SciPy
CSR sparse matrix, and b is a 1-D NumPy array.

Dependencies: scikit-learn is used for data access and feature hashing.
Install: pip install scikit-learn
"""

from typing import Tuple

import numpy as np


def load_20newsgroups_hashed(n_features: int = 1024, subset: str = "train") -> Tuple["np.ndarray | object", np.ndarray]:
    try:
        from sklearn.datasets import fetch_20newsgroups  # type: ignore
        from sklearn.feature_extraction.text import HashingVectorizer  # type: ignore
    except Exception as e:  # pragma: no cover
        raise RuntimeError("scikit-learn is required: pip install scikit-learn") from e

    data = fetch_20newsgroups(subset=subset, remove=("headers", "footers", "quotes"))
    texts = data.data
    y = np.asarray(data.target, dtype=float)
    vect = HashingVectorizer(n_features=int(n_features), alternate_sign=False, norm=None)
    X = vect.transform(texts)  # sparse CSR
    return X.tocsr(), y


def load_rcv1_hashed(n_features: int = 1024) -> Tuple["np.ndarray | object", np.ndarray]:
    try:
        from sklearn.datasets import fetch_rcv1  # type: ignore
    except Exception as e:  # pragma: no cover
        raise RuntimeError("scikit-learn is required: pip install scikit-learn") from e

    bunch = fetch_rcv1(shuffle=False)  # X: CSR tf-idf, y: multi-label indicator
    X = bunch.data  # CSR
    Y = bunch.target  # CSR multi-label
    # Summarize labels count per sample as a simple regression target
    y = np.asarray(np.ravel(np.sum(Y, axis=1))).astype(float)
    # Project down if needed using a simple Gaussian projection
    if X.shape[1] != int(n_features):
        rng = np.random.default_rng(0)
        R = rng.standard_normal((X.shape[1], int(n_features))) / np.sqrt(int(n_features))
        X = (X @ R)
    return X.tocsr() if hasattr(X, "tocsr") else X, y


def load_yearprediction_msd(sample: int | None = None) -> Tuple[np.ndarray, np.ndarray]:
    try:
        from sklearn.datasets import fetch_openml  # type: ignore
    except Exception as e:  # pragma: no cover
        raise RuntimeError("scikit-learn is required: pip install scikit-learn") from e
    ds = fetch_openml(name="YearPredictionMSD", as_frame=False)
    X = ds["data"].astype(float)
    y = ds["target"].astype(float)
    if sample is not None and int(sample) > 0:
        X = X[: int(sample)]
        y = y[: int(sample)]
    return X, y


def load_california_housing() -> Tuple[np.ndarray, np.ndarray]:
    try:
        from sklearn.datasets import fetch_california_housing  # type: ignore
    except Exception as e:  # pragma: no cover
        raise RuntimeError("scikit-learn is required: pip install scikit-learn") from e
    bunch = fetch_california_housing(as_frame=False)
    return bunch.data.astype(float), bunch.target.astype(float)


