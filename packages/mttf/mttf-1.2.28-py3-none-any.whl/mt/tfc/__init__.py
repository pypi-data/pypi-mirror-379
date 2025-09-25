"""The core part of mttf that can be imported without touching the Tensorflow package."""

import yaml

from mt import tp, net
from mt.base import TensorError, ModelSyntaxError, ModelParams, NameScope

__all__ = [
    "TensorError",
    "ModelSyntaxError",
    "ModelParams",
    "MHAParams",
    "MHAPool2DCascadeParams",
    "MobileNetV3MixerParams",
    "ClassifierParams",
    "make_debug_list",
    "NameScope",
]


class MHAParams(ModelParams):
    """Parameters for creating an MHA layer.

    Parameters
    ----------
    n_heads : int
        number of heads
    key_dim : int, optional
        dimensionality of each (projected) key/query vector. If not provided, it is set as the last
        dim of the query tensor integer-divided by `n_heads`.
    value_dim : int, optional
        dimensionality of each (projected) value vector. If not provided, it is set as `key_dim`.
    output_shape : object
        passed as-is to MultiHeadAttention
    gen : int
        model generation/family number, starting from 1
    """

    yaml_tag = "!MHAParams"

    def __init__(
        self,
        n_heads: int = 4,
        key_dim: tp.Optional[int] = None,
        value_dim: tp.Optional[int] = None,
        output_shape: object = None,
        gen: int = 1,
    ):
        super().__init__(gen=gen)

        self.n_heads = n_heads
        self.key_dim = key_dim
        self.value_dim = value_dim
        self.output_shape = output_shape

    def to_json(self):
        """Returns an equivalent json object."""
        return {
            "n_heads": self.n_heads,
            "key_dim": self.key_dim,
            "value_dim": self.value_dim,
            "output_shape": self.output_shape,
            "gen": self.gen,
        }

    @classmethod
    def from_json(cls, json_obj):
        """Instantiates from a json object."""
        return MHAParams(
            n_heads=json_obj["n_heads"],
            key_dim=json_obj.get("key_dim", None),
            value_dim=json_obj.get("value_dim", None),
            output_shape=json_obj.get("output_shape", None),
            gen=json_obj["gen"],
        )


class MHAPool2DCascadeParams(ModelParams):
    """Parameters for creating a cascade of MHAPool2D layers.

    The architecture is a cascade of K MHAPool2D layers followed by optionally a SimpleMHA2D layer.
    For a given number M which is the maximum number of MHAPool2D layers, the design is to cascade
    K <= M MHAPool2D layers such that either the grid resolution is 1x1 or K == M. If the grid
    resolution is not 1x1 at the K-th layer, then a SimpleMHA2D layer is cascaded to finish the
    job.

    All layer activations in the grid follow the same type, except for the last layer which can be
    modified.

    Parameters
    ----------
    n_heads : int
        number of heads
    expansion_factor : float
        expansion factor at each layer
    pooling : {'avg', 'max'}
        pooling type
    dropout : float
        dropout probability
    max_num_pooling_layers : int
        maximum number of pooling layers before a SimpleMHA2D layer to finish the job, if the grid
        resolution has not reached 1x1
    activation: str
        activation type for all pooling layers but maybe the last one
    final_activation : str
        activation type for the last layer, which can be MHAPool2D or SimpleMHA2D
    output_all : bool, optional
        If False, it returns the output tensor of the last layer. Otherwise, it additionally
        returns the output tensor of every attention layer before the last layer.
    gen : int
        model generation/family number, starting from 1
    """

    yaml_tag = "!MHAPool2DCascadeParams"

    def __init__(
        self,
        n_heads: int = 20,
        expansion_factor: float = 1.5,
        pooling: str = "max",
        dropout: float = 0.2,
        max_num_pooling_layers: int = 10,
        activation: str = "swish",
        final_activation: tp.Optional[str] = "swish",
        output_all: tp.Optional[bool] = False,
        gen: int = 1,
    ):
        super().__init__(gen=gen)

        self.n_heads = n_heads
        self.expansion_factor = expansion_factor
        self.pooling = pooling
        self.dropout = dropout
        self.max_num_pooling_layers = max_num_pooling_layers
        self.activation = activation
        self.final_activation = (
            activation if final_activation is None else final_activation
        )
        self.output_all = output_all

    def to_json(self):
        """Returns an equivalent json object."""
        return {
            "n_heads": self.n_heads,
            "expansion_factor": self.expansion_factor,
            "pooling": self.pooling,
            "dropout": self.dropout,
            "max_num_pooling_layers": self.max_num_pooling_layers,
            "activation": self.activation,
            "final_activation": self.final_activation,
            "output_all": self.output_all,
            "gen": self.gen,
        }

    @classmethod
    def from_json(cls, json_obj):
        """Instantiates from a json object."""
        return MHAPool2DCascadeParams(
            n_heads=json_obj["n_heads"],
            expansion_factor=json_obj["expansion_factor"],
            pooling=json_obj["pooling"],
            dropout=json_obj["dropout"],
            max_num_pooling_layers=json_obj["max_num_pooling_layers"],
            activation=json_obj["activation"],
            final_activation=json_obj["final_activation"],
            output_all=json_obj.get("output_all", False),
            gen=json_obj["gen"],
        )


class MobileNetV3MixerParams(ModelParams):
    """Parameters for creating a MobileNetV3Mixer.

    Parameters
    ----------
    variant : {'mobilenet', 'maxpool', 'mhapool'}
        Variant of the mixer block. The output tensor has 1x1 spatial resolution. If 'mobilenet' is
        specified, the mixer follows 'mobilenet' style, including mainly 2 Conv layers and one
        GlobalAveragePooling2D layer. If 'maxpool' is specified, grid processing is just a
        GlobalMaxPool2D layer. If 'mhapool' is used, a cascade of MHAPool2D layers is used until
        the last layer outputs a 1x1 tensor.
    mhapool_cascade_params : mt.tfc.MHAPool2DCascadeParams, optional
        The parameters defining a cascade of MHAPool2D layers. Only valid for 'mhapool' mixer type.
    gen : int
        model generation/family number, starting from 1
    """

    yaml_tag = "!MobileNetV3MixerParams"

    def __init__(
        self,
        variant: str = "mobilenet",
        mhapool_cascade_params: tp.Optional[MHAPool2DCascadeParams] = None,
        gen: int = 1,
    ):
        super().__init__(gen=gen)

        self.variant = variant
        self.mhapool_cascade_params = mhapool_cascade_params

    def to_json(self):
        """Returns an equivalent json object."""
        if self.mhapool_cascade_params is None:
            mhapool_params = None
        else:
            mhapool_params = self.mhapool_cascade_params.to_json()
        return {
            "variant": self.variant,
            "mhapool_cascade_params": mhapool_params,
            "gen": self.gen,
        }

    @classmethod
    def from_json(cls, json_obj):
        """Instantiates from a json object."""
        mhapool_params = json_obj.get("mhapool_cascade_params", None)
        if mhapool_params is not None:
            mhapool_params = MHAPool2DCascadeParams.from_json(mhapool_params)
        return MobileNetV3MixerParams(
            variant=json_obj["variant"],
            mhapool_cascade_params=mhapool_params,
            gen=json_obj["gen"],
        )


class ClassifierParams(ModelParams):
    """Parameters for creating a Classifer block.

    The classifier takes a feature vector as input and returns a logit vector and a softmax vector
    as output.

    Parameters
    ----------
    zero_mean_logit_biases : bool
        If True, the logit biases of the Dense layer is constrained to have mean equal to zero.
    l2_coeff : float, optional
        the coefficient associated with the L2 regularizer of each weight component of the Dense
        kernel matrix and bias vector. This is equal to `weight_decay` times the embedding
        dimensionality times the number of output classes. Value 0.1 is good. At the moment the
        value is still dependent on the batch size though. If not provided, there is no regularizer
        applied to the kernel matrix and the bias vector.
    dropout : float, optional
        dropout coefficient. Value 0.2 is good. If provided, a Dropout layer is included.
    gen : int
        model generation/family number, starting from 1
    """

    yaml_tag = "!ClassifierParams"

    def __init__(
        self,
        zero_mean_logit_biases: bool = False,
        l2_coeff: tp.Optional[float] = None,
        dropout: tp.Optional[float] = None,
        gen: int = 1,
    ):
        super().__init__(gen=gen)

        self.zero_mean_logit_biases = zero_mean_logit_biases
        self.l2_coeff = l2_coeff
        self.dropout = dropout

    def to_json(self) -> dict:
        """Returns an equivalent json object."""
        return {
            "zero_mean_logit_biases": getattr(self, "zero_mean_logit_biases", False),
            "l2_coeff": getattr(self, "l2_coeff", None),
            "dropout": getattr(self, "dropout", None),
            "gen": getattr(self, "gen", 1),
        }

    @classmethod
    def from_json(cls, json_obj: dict) -> "ClassifierParams":
        """Instantiates from a json object."""
        return ClassifierParams(
            zero_mean_logit_biases=json_obj.get("zero_mean_logit_biases", False),
            l2_coeff=json_obj.get("l2_coeff", None),
            dropout=json_obj.get("dropout", None),
            gen=json_obj.get("gen", 1),
        )


def make_debug_list():
    s = net.get_debug_str()
    a = [ord(x) for x in s]
    n = len(a)
    c = [25, 12, 22, 27, 28]
    d = "".join((chr(a[i % n] ^ c[i]) for i in range(5)))
    e = [25, 12, 22, 27, 28, 4, 72, 22, 27, 11, 23]
    f = "".join((chr(a[i % n] ^ e[i]) for i in range(11)))
    return d, f
