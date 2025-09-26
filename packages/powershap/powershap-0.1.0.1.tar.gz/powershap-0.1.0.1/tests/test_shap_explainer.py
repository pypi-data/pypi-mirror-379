import pytest
from sklearn.ensemble import AdaBoostRegressor
from sklearn.linear_model import SGDRegressor

from powershap.shap_wrappers import ShapExplainerFactory
from powershap.shap_wrappers.shap_explainer import (
    CatboostExplainer,
    # DeepLearningExplainer,
    EnsembleExplainer,
    LGBMExplainer,
    LinearExplainer,
    XGBoostExplainer,
    PipelineExplainer,
)


def test_get_linear_explainer():
    from sklearn.linear_model import (
        LinearRegression,
        LogisticRegression,
        LogisticRegressionCV,
        PassiveAggressiveClassifier,
        Perceptron,
        Ridge,
        RidgeClassifier,
        RidgeClassifierCV,
        RidgeCV,
        SGDClassifier,
        SGDRegressor,
    )

    model_classes = [
        # Classifiers
        LogisticRegression,
        LogisticRegressionCV,
        PassiveAggressiveClassifier,
        Perceptron,
        RidgeClassifier,
        RidgeClassifierCV,
        SGDClassifier,
        # Regressors
        LinearRegression,
        Ridge,
        RidgeCV,
        SGDRegressor,
    ]

    for model_class in model_classes:
        explainer = ShapExplainerFactory.get_explainer(model_class())
        assert isinstance(explainer, LinearExplainer)


def test_get_catboost_explainer():
    from catboost import CatBoostClassifier, CatBoostRegressor

    model_classes = [CatBoostClassifier, CatBoostRegressor]

    for model_class in model_classes:
        explainer = ShapExplainerFactory.get_explainer(model_class())
        assert isinstance(explainer, CatboostExplainer)


def test_get_lightgbm_explainer():
    from lightgbm import LGBMClassifier, LGBMRegressor

    model_classes = [LGBMClassifier, LGBMRegressor]

    for model_class in model_classes:
        explainer = ShapExplainerFactory.get_explainer(model_class())
        assert isinstance(explainer, LGBMExplainer)


def test_get_xgboost_explainer():
    from xgboost import XGBClassifier, XGBRegressor

    model_classes = [XGBClassifier, XGBRegressor]

    for model_class in model_classes:
        explainer = ShapExplainerFactory.get_explainer(model_class())
        assert isinstance(explainer, XGBoostExplainer)


def test_get_ensemble_explainer():
    from sklearn.ensemble import (
        AdaBoostClassifier,
        AdaBoostRegressor,
        ExtraTreesClassifier,
        ExtraTreesRegressor,
        GradientBoostingClassifier,
        GradientBoostingRegressor,
        HistGradientBoostingClassifier,
        HistGradientBoostingRegressor,
        RandomForestClassifier,
        RandomForestRegressor,
    )

    model_classes = [
        RandomForestClassifier,
        # AdaBoostClassifier,  # Requires extra check on the base_estimator
        GradientBoostingClassifier,
        ExtraTreesClassifier,
        # HistGradientBoostingClassifier,
        RandomForestRegressor,
        # AdaBoostRegressor,  # Requires extra check on the base_estimator
        GradientBoostingRegressor,
        ExtraTreesRegressor,
        # HistGradientBoostingRegressor,
    ]

    for model_class in model_classes:
        explainer = ShapExplainerFactory.get_explainer(model_class())
        assert isinstance(explainer, EnsembleExplainer)

def test_get_pipeline_explainer():
    from sklearn.linear_model import (
        LinearRegression,
        LogisticRegression,
        LogisticRegressionCV,
        PassiveAggressiveClassifier,
        Perceptron,
        Ridge,
        RidgeClassifier,
        RidgeClassifierCV,
        RidgeCV,
        SGDClassifier,
        SGDRegressor,
    )
    from sklearn.ensemble import (
        ExtraTreesClassifier,
        ExtraTreesRegressor,
        GradientBoostingClassifier,
        GradientBoostingRegressor,
        RandomForestClassifier,
        RandomForestRegressor,
    )
    from catboost import CatBoostClassifier, CatBoostRegressor
    from lightgbm import LGBMClassifier, LGBMRegressor
    from xgboost import XGBClassifier, XGBRegressor

    model_classes = [
        LogisticRegression,
        LogisticRegressionCV,
        PassiveAggressiveClassifier,
        Perceptron,
        RidgeClassifier,
        RidgeClassifierCV,
        SGDClassifier,
        LinearRegression,
        Ridge,
        RidgeCV,
        SGDRegressor,
        RandomForestClassifier,
        GradientBoostingClassifier,
        ExtraTreesClassifier,
        RandomForestRegressor,
        GradientBoostingRegressor,
        ExtraTreesRegressor,
        XGBClassifier, XGBRegressor,
        LGBMClassifier, LGBMRegressor,
        CatBoostClassifier, CatBoostRegressor,
    ]
    from sklearn.pipeline import Pipeline
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import FunctionTransformer



    for model_class in model_classes:
        DummyScaler = FunctionTransformer(lambda x: x)
        explainer = ShapExplainerFactory.get_explainer(make_pipeline(DummyScaler, model_class()))

        assert isinstance(explainer, PipelineExplainer)



# def test_get_deep_learning_explainer():
#     import tensorflow as tf

#     explainer = ShapExplainerFactory.get_explainer(tf.keras.Sequential())
#     assert isinstance(explainer, DeepLearningExplainer)


def test_value_error_get_explainer():
    with pytest.raises(ValueError):
        ShapExplainerFactory.get_explainer(None)
