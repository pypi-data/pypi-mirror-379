from typing import Any, Callable, Dict, Optional, Tuple

from chalk.ml.utils import ModelEncoding, ModelType


def load_xgb_classifier(f: str):
    import xgboost  # pyright: ignore[reportMissingImports]

    model = xgboost.XGBClassifier()
    model.load_model(f)
    return model


def load_xgb_regressor(f: str):
    import xgboost  # pyright: ignore[reportMissingImports]

    model = xgboost.XGBRegressor()
    model.load_model(f)
    return model


MODEL_HOOKS: Dict[Tuple[ModelType, ModelEncoding, Optional[str]], Callable[[str], Any]] = {
    (ModelType.PYTORCH, ModelEncoding.PICKLE, None): lambda f: __import__("torch").load(f),
    (ModelType.SKLEARN, ModelEncoding.PICKLE, None): lambda f: __import__("joblib").load(f),
    (ModelType.TENSORFLOW, ModelEncoding.HDF5, None): lambda f: __import__("tensorflow").keras.models.load_model(f),
    (ModelType.TENSORFLOW, ModelEncoding.SAFETENSOR, None): lambda f: __import__("tensorflow").keras.models.load_model(
        f
    ),
    (ModelType.XGBOOST, ModelEncoding.JSON, None): load_xgb_regressor,
    (ModelType.XGBOOST, ModelEncoding.JSON, "classifier"): load_xgb_classifier,
    (ModelType.XGBOOST, ModelEncoding.JSON, "regressor"): load_xgb_regressor,
    (ModelType.LIGHTGBM, ModelEncoding.TEXT, None): lambda f: __import__("lightgbm").Booster(model_file=f),
    (ModelType.CATBOOST, ModelEncoding.CBM, None): lambda f: __import__("catboost").CatBoost().load_model(f),
    (ModelType.ONNX, ModelEncoding.PROTOBUF, None): lambda f: __import__("onnxruntime").InferenceSession(f),
}

PREDICT_HOOKS: Dict[Tuple[ModelType, ModelEncoding, Optional[str]], Callable[[Any, Any], Any]] = {
    (ModelType.PYTORCH, ModelEncoding.PICKLE, None): lambda model, X: model(X).detach().numpy(),
    (ModelType.SKLEARN, ModelEncoding.PICKLE, None): lambda model, X: model.predict(X),
    (ModelType.TENSORFLOW, ModelEncoding.HDF5, None): lambda model, X: model.predict(X),
    (ModelType.TENSORFLOW, ModelEncoding.SAFETENSOR, None): lambda model, X: model.predict(X),
    (ModelType.XGBOOST, ModelEncoding.JSON, None): lambda model, X: model.predict(X),
    (ModelType.LIGHTGBM, ModelEncoding.TEXT, None): lambda model, X: model.predict(X),
    (ModelType.CATBOOST, ModelEncoding.CBM, None): lambda model, X: model.predict(X),
    (ModelType.ONNX, ModelEncoding.PROTOBUF, None): lambda model, X: model.run(None, {"input": X.astype("float32")})[0],
}
