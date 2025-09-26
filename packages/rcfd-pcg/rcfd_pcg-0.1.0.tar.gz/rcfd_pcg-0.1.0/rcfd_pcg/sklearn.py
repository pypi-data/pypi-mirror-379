from __future__ import annotations

from typing import Optional, Tuple, Any

import numpy as np

try:  # optional sklearn-style base classes
    from sklearn.base import BaseEstimator, RegressorMixin  # type: ignore
except Exception:  # pragma: no cover
    class BaseEstimator:  # minimal shim
        pass

    class RegressorMixin:  # minimal shim
        pass

try:
    import scipy.sparse as sp
except Exception:  # pragma: no cover
    sp = None  # type: ignore

from .rcfd import rcfd_pcg_solve


class RCFDRidge(BaseEstimator, RegressorMixin):
    def __init__(
        self,
        lam: float = 0.0,
        eps: float = 0.25,
        tol: float = 1e-6,
        max_iter: int = 200,
        compression: str = "auto",
        oversampling: int = 8,
        power_iters: int = 0,
        batch_size: Optional[int] = 1024,
        shrink_multiple: int = 2,
        fit_intercept: bool = False,
        count_spmv: bool = False,
        sketch_dtype: str = "float32",
        auto_bail_out: bool = True,
        bail_out_threshold: float = 5.0,
    ) -> None:
        self.lam = float(lam)
        self.eps = float(eps)
        self.tol = float(tol)
        self.max_iter = int(max_iter)
        self.compression = compression
        self.oversampling = int(oversampling)
        self.power_iters = int(power_iters)
        self.batch_size = int(batch_size) if batch_size is not None else None
        self.shrink_multiple = int(shrink_multiple)
        self.fit_intercept = bool(fit_intercept)
        self.count_spmv = bool(count_spmv)
        self.sketch_dtype = sketch_dtype
        self.auto_bail_out = bool(auto_bail_out)
        self.bail_out_threshold = float(bail_out_threshold)

        self.coef_: Optional[np.ndarray] = None
        self.intercept_: float = 0.0
        self.diagnostics_: Optional[dict[str, Any]] = None

    def get_params(self, deep: bool = True) -> dict:
        return {
            "lam": self.lam,
            "eps": self.eps,
            "tol": self.tol,
            "max_iter": self.max_iter,
            "compression": self.compression,
            "oversampling": self.oversampling,
            "power_iters": self.power_iters,
            "batch_size": self.batch_size,
            "shrink_multiple": self.shrink_multiple,
            "fit_intercept": self.fit_intercept,
            "count_spmv": self.count_spmv,
            "sketch_dtype": self.sketch_dtype,
            "auto_bail_out": self.auto_bail_out,
            "bail_out_threshold": self.bail_out_threshold,
        }

    def set_params(self, **params):
        for k, v in params.items():
            if not hasattr(self, k):
                continue
            setattr(self, k, v)
        return self

    def _validate_Xy(self, X: np.ndarray, y: np.ndarray) -> Tuple[np.ndarray, np.ndarray, Optional[np.ndarray]]:
        if self.fit_intercept:
            if sp is not None and sp.issparse(X):
                # center y only; sparse X not centered to avoid densification
                y_mean = float(y.mean())
                return X, y - y_mean, np.array([0.0])  # store y_mean separately
            else:
                X = np.asarray(X)
                X_mean = X.mean(axis=0)
                y_mean = float(y.mean())
                Xc = X - X_mean
                yc = y - y_mean
                self._X_mean_ = X_mean
                self._y_mean_ = y_mean
                return Xc, yc, X_mean
        else:
            return X, y, None

    def fit(self, X: np.ndarray, y: np.ndarray):
        y = np.asarray(y).reshape(-1)
        X_proc, y_proc, X_mean = self._validate_Xy(X, y)

        x, diag = rcfd_pcg_solve(
            X_proc,
            y_proc,
            ridge_lambda=self.lam,
            epsilon=self.eps,
            tol=self.tol,
            max_iter=self.max_iter,
            batch_size=self.batch_size,
            shrink_multiple=self.shrink_multiple,
            count_spmv=self.count_spmv,
            compression=self.compression,
            oversampling=self.oversampling,
            power_iters=self.power_iters,
            sketch_dtype=self.sketch_dtype,
            auto_bail_out=self.auto_bail_out,
            bail_out_threshold=self.bail_out_threshold,
            return_diagnostics=True,
        )
        self.coef_ = x
        self.diagnostics_ = diag

        if self.fit_intercept:
            if sp is not None and sp.issparse(X):
                # intercept from y_mean - 0 (since X not centered); best-effort
                self.intercept_ = float(self._y_mean_ if hasattr(self, "_y_mean_") else y.mean())
            else:
                self.intercept_ = float(self._y_mean_ - float(self._X_mean_ @ self.coef_))
        else:
            self.intercept_ = 0.0
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        if self.coef_ is None:
            raise RuntimeError("Model is not fitted")
        yhat = (X @ self.coef_)
        if self.fit_intercept:
            yhat = yhat + self.intercept_
        return yhat

    # Convenience persistence helpers (joblib-compatible while remaining optional)
    def save(self, path: str) -> None:
        try:
            import joblib  # type: ignore
        except Exception as e:  # pragma: no cover
            raise RuntimeError("joblib is required to save models: pip install joblib") from e
        joblib.dump({
            "params": self.get_params(),
            "coef_": self.coef_,
            "intercept_": self.intercept_,
            "diagnostics_": self.diagnostics_,
            "_X_mean_": getattr(self, "_X_mean_", None),
            "_y_mean_": getattr(self, "_y_mean_", None),
        }, path)

    @classmethod
    def load(cls, path: str) -> "RCFDRidge":
        try:
            import joblib  # type: ignore
        except Exception as e:  # pragma: no cover
            raise RuntimeError("joblib is required to load models: pip install joblib") from e
        state = joblib.load(path)
        model = cls(**state.get("params", {}))
        model.coef_ = state.get("coef_")
        model.intercept_ = state.get("intercept_", 0.0)
        model.diagnostics_ = state.get("diagnostics_")
        if state.get("_X_mean_") is not None:
            model._X_mean_ = state["_X_mean_"]
        if state.get("_y_mean_") is not None:
            model._y_mean_ = state["_y_mean_"]
        return model


