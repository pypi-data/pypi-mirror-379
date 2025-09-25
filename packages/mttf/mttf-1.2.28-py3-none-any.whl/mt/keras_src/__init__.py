from packaging.version import Version

from .base import keras_version, keras_source

if keras_source == "tf_keras":
    from tf_keras import *
elif keras_source == "keras":
    from keras import *
elif keras_source == "tensorflow.keras":
    from tensorflow.keras import *
else:
    raise ImportError(f"Unknown value '{keras_source}' for variable 'keras_source'.")

d_modelFileFormats = {"H5": ".h5", "TF": ".tf"}
if Version(keras_version) >= Version("2.15"):
    d_modelFileFormats["Keras"] = ".keras"
