from .. import constraints


class CenterAround(constraints.Constraint):
    """Constrains the last axis to have values centered around `ref_value`."""

    def __init__(self, ref_value: float = 0.0):
        self.ref_value = ref_value

    def __call__(self, w):
        import tensorflow as tf

        mean = tf.reduce_mean(w, axis=-1, keepdims=True)
        ref_mean = mean - self.ref_value
        ref_mean = tf.expand_dims(ref_mean, -1)
        return w - ref_mean

    def get_config(self):
        return {"ref_value": self.ref_value}
