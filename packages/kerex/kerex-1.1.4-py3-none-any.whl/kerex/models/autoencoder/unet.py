from keras import saving
from .base_models import BaseUnet, BaseSmoothUnet


@saving.register_keras_serializable(package="Kerex.Models.AutoEncoder", name="Unet1D")
class Unet1D(BaseUnet):
    """
    1-D implementation of Unet, cf. [Ronneberger et al.](https://arxiv.org/abs/1505.04597)

    The model is build from a convolutional encoder- and a decoder path,
    and is able to extract features on different scale of the data
    by bisecting the features with each level of the model.
    Additionally, skip connections feed through high-resolution features from the encoder 
    to the decoder on each level.

    Parameters
    ----------
    filters : int | list | tuple
        Number of filters. 
        The model will be build symmetrically, meaning that only the number of encoder filters is defined,
        and the decoder will mirror it.
    kernel_size : int | list | tuple, optional
        Kernel size for encoder blocks. 
        An `int` results in a global `kernel_size`, a `list` allows to define the `kernel_size` per layer.
        Decoder blocks will mirror the `kernel_size` of the encoder blocks.
        Defaults to 5.
    strides : int | list | tuple, optional
        Strides for encoder blocks. 
        An `int` results in a global value for `strides`, a `list` allows to define the `strides` per layer.
        Decoder blocks will mirror the `strides` of the encoder blocks.
        Defaults to 1.
    padding : str, optional {`"same"`, `"causal"`}
        Padding for all convolutional layers in the model.
        Defaults to `"same"`.
    data_format : str, optional {`"channels_first"`, `"channels_last"`}
        Data format for the convolution operations.
        Defaults to `"channels_last"`.
    dilation_rate : int | list | tuple, optional
        Dilation rates for encoder blocks. 
        An `int` results in a global value for `dilation_rate`, a `list` allows to define the `dilation_rate` per layer.
        Decoder blocks will mirror the `dilation_rate` of the encoder blocks.
        Defaults to 1.
    groups : int, optional
        Number of convolutional groups for encoder blocks. 
        An `int` results in a global value for `groups`, a `list` allows to define the `groups` per layer.
        Decoder blocks will mirror the `groups` of the encoder blocks.
        Defaults to 1.
    activation : str | keras.activations.Activation | keras.layers.Layer, optional
        Global activation function.
        Can be either a `str`, a `keras.activations.Activation`, or a `keras.layers.Layer`.
        Defaults to `"relu"`.
    use_bias : bool, optional
        If `True`, all layers use a bias.
        Defaults to `True`.
    bottleneck : keras.layers.Layer | keras.models.Model, optional
        An optional `keras.layer.Layer` or `keras.models.Model` that is placed in the bottleneck of the model.
        Defaults to `None`.
    merge_layer : str | keras.layers.Layer, optional {`"concatenate"`, `"average"`, `"maximum"`, `"minimum"`, `"add"`, `"subtract"`, `"multiply"`, `"dot"`}
        Layer to merge the forward information with the information from skip connections.
        Defaults to `"concatenate"`.
    kernel_initializer : str | keras.initializers.Initializer, optional
        Kernel initializer.
        Defaults to `"he_normal"`.
    bias_initializer : str | keras.initializers.Initializer, optional
        Bias initializer.
        Defaults to `"zeros"`.
    kernel_regularizer : str | keras.regularizers.Regularizer, optional
        Kernel regularizer.
        Defaults to `None`.
    bias_regularizer : str | keras.regularizers.Regularizer, optional
        Bias regularizer.
        Defaults to `None`.
    kernel_constraint : str | keras.constraints.Constraint, optional
        Kernel constraint.
        Defaults to `None`.
    bias_constraint : str | keras.constraints.Constraint, optional
        Bias constraint.
        Defaults to `None`.
    name : str, optional
        Name of the model.
        If `None`, `name` is automatically inherited from the class name `"Unet1D"`.
        Defaults to `None`.

    Notes
    -----
    The `filters` argument steers the depth of the model and the layout of the encoder- and decoder blocks on each level:
    A list containing tuples results in multiple convolutions on the respective level, e.g.,
    `filters=[(8, 8), 16, 32]` will return a model with a depth of 3, 
    where the first encoder (and last decoder) block has two consecutive convolutions with `filters=8`,
    and the remaining two levels have only a single convolution with `filters=16` and `filters=32`, respectively.

    Downsampling is realized using a strided convolution as proposed by [Springenberger et al.](https://arxiv.org/abs/1412.6806)

    """

    def __init__(
        self,
        filters=[8, 16, 32],
        kernel_size=5,
        strides=1,
        padding="same",
        data_format="channels_last",
        dilation_rate=1,
        groups=1,
        activation="relu",
        use_bias=True,
        bottleneck=None,
        merge_layer="concatenate",
        kernel_initializer="he_normal",
        bias_initializer="zeros",
        kernel_regularizer=None,
        bias_regularizer=None,
        kernel_constraint=None,
        bias_constraint=None,
        name=None,
        **kwargs
    ):
        super().__init__(
            rank=1,
            filters=filters,
            kernel_size=kernel_size,
            strides=strides,
            padding=padding,
            data_format=data_format,
            dilation_rate=dilation_rate,
            groups=groups,
            activation=activation,
            use_bias=use_bias,
            bottleneck=bottleneck,
            merge_layer=merge_layer, 
            kernel_initializer=kernel_initializer,
            bias_initializer=bias_initializer,
            kernel_regularizer=kernel_regularizer,
            bias_regularizer=bias_regularizer,
            kernel_constraint=kernel_constraint,
            bias_constraint=bias_constraint,
            name=name,
            **kwargs
        )


@saving.register_keras_serializable(package="Kerex.Models.AutoEncoder", name="Unet2D")
class Unet2D(BaseUnet):
    """
    2-D implementation of Unet, cf. [Ronneberger et al.](https://arxiv.org/abs/1505.04597)

    The model is build from a convolutional encoder- and a decoder path,
    and is able to extract features on different scale of the data
    by bisecting the features with each level of the model.
    Additionally, skip connections feed through high-resolution features from the encoder 
    to the decoder on each level.

    Parameters
    ----------
    filters : int | list | tuple
        Number of filters. 
        The model will be build symmetrically, meaning that only the number of encoder filters is defined,
        and the decoder will mirror it.
    kernel_size : int | list | tuple, optional
        Kernel size for encoder blocks. 
        An `int` results in a global `kernel_size`, a `list` allows to define the `kernel_size` per layer.
        Decoder blocks will mirror the `kernel_size` of the encoder blocks.
        Defaults to 5.
    strides : int | list | tuple, optional
        Strides for encoder blocks. 
        An `int` results in a global value for `strides`, a `list` allows to define the `strides` per layer.
        Decoder blocks will mirror the `strides` of the encoder blocks.
        Defaults to 1.
    data_format : str, optional {`"channels_first"`, `"channels_last"`}
        Data format for the convolution operations.
        Defaults to `"channels_last"`.
    dilation_rate : int | list | tuple, optional
        Dilation rates for encoder blocks. 
        An `int` results in a global value for `dilation_rate`, a `list` allows to define the `dilation_rate` per layer.
        Decoder blocks will mirror the `dilation_rate` of the encoder blocks.
        Defaults to 1.
    groups : int, optional
        Number of convolutional groups for encoder blocks. 
        An `int` results in a global value for `groups`, a `list` allows to define the `groups` per layer.
        Decoder blocks will mirror the `groups` of the encoder blocks.
        Defaults to 1.
    activation : str | keras.activations.Activation | keras.layers.Layer, optional
        Global activation function.
        Can be either a `str`, a `keras.activations.Activation`, or a `keras.layers.Layer`.
        Defaults to `"relu"`.
    use_bias : bool, optional
        If `True`, all layers use a bias.
        Defaults to `True`.
    bottleneck : keras.layers.Layer | keras.models.Model, optional
        An optional `keras.layer.Layer` or `keras.models.Model` that is placed in the bottleneck of the model.
        Defaults to `None`.
    merge_layer : str | keras.layers.Layer, optional {`"concatenate"`, `"average"`, `"maximum"`, `"minimum"`, `"add"`, `"subtract"`, `"multiply"`, `"dot"`}
        Layer to merge the forward information with the information from skip connections.
        Defaults to `"concatenate"`.
    kernel_initializer : str | keras.initializers.Initializer, optional
        Kernel initializer.
        Defaults to `"he_normal"`.
    bias_initializer : str | keras.initializers.Initializer, optional
        Bias initializer.
        Defaults to `"zeros"`.
    kernel_regularizer : str | keras.regularizers.Regularizer, optional
        Kernel regularizer.
        Defaults to `None`.
    bias_regularizer : str | keras.regularizers.Regularizer, optional
        Bias regularizer.
        Defaults to `None`.
    kernel_constraint : str | keras.constraints.Constraint, optional
        Kernel constraint.
        Defaults to `None`.
    bias_constraint : str | keras.constraints.Constraint, optional
        Bias constraint.
        Defaults to `None`.
    name : str, optional
        Name of the model.
        If `None`, `name` is automatically inherited from the class name `"Unet2D"`.
        Defaults to `None`.

    Notes
    -----
    The `filters` argument steers the depth of the model and the layout of the encoder- and decoder blocks on each level:
    A list containing tuples results in multiple convolutions on the respective level, e.g.,
    `filters=[(8, 8), 16, 32]` will return a model with a depth of 3, 
    where the first encoder (and last decoder) block has two consecutive convolutions with `filters=8`,
    and the remaining two levels have only a single convolution with `filters=16` and `filters=32`, respectively.

    Downsampling is realized using a strided convolution as proposed by [Springenberger et al.](https://arxiv.org/abs/1412.6806)

    """

    def __init__(
        self,
        filters=[8, 16, 32],
        kernel_size=5,
        data_format="channels_last",
        activation="relu",
        use_bias=True,
        bottleneck=None,
        merge_layer="concatenate",
        kernel_initializer="he_normal",
        bias_initializer="zeros",
        kernel_regularizer=None,
        bias_regularizer=None,
        kernel_constraint=None,
        bias_constraint=None,
        name=None,
        **kwargs
    ):
        super().__init__(
            rank=2,
            filters=filters,
            kernel_size=kernel_size,
            data_format=data_format,
            activation=activation,
            use_bias=use_bias,
            bottleneck=bottleneck,
            merge_layer=merge_layer, 
            kernel_initializer=kernel_initializer,
            bias_initializer=bias_initializer,
            kernel_regularizer=kernel_regularizer,
            bias_regularizer=bias_regularizer,
            kernel_constraint=kernel_constraint,
            bias_constraint=bias_constraint,
            name=name,
            **kwargs
        )


@saving.register_keras_serializable(package="Kerex.Models.AutoEncoder", name="Unet3D")
class Unet3D(BaseUnet):
    """
    3-D implementation of Unet, cf. [Ronneberger et al.](https://arxiv.org/abs/1505.04597)

    The model is build from a convolutional encoder- and a decoder path,
    and is able to extract features on different scale of the data
    by bisecting the features with each level of the model.
    Additionally, skip connections feed through high-resolution features from the encoder 
    to the decoder on each level.

    Parameters
    ----------
    filters : int | list | tuple
        Number of filters. 
        The model will be build symmetrically, meaning that only the number of encoder filters is defined,
        and the decoder will mirror it.
    kernel_size : int | list | tuple, optional
        Kernel size for encoder blocks. 
        An `int` results in a global `kernel_size`, a `list` allows to define the `kernel_size` per layer.
        Decoder blocks will mirror the `kernel_size` of the encoder blocks.
        Defaults to 5.
    strides : int | list | tuple, optional
        Strides for encoder blocks. 
        An `int` results in a global value for `strides`, a `list` allows to define the `strides` per layer.
        Decoder blocks will mirror the `strides` of the encoder blocks.
        Defaults to 1.
    data_format : str, optional {`"channels_first"`, `"channels_last"`}
        Data format for the convolution operations.
        Defaults to `"channels_last"`.
    dilation_rate : int | list | tuple, optional
        Dilation rates for encoder blocks. 
        An `int` results in a global value for `dilation_rate`, a `list` allows to define the `dilation_rate` per layer.
        Decoder blocks will mirror the `dilation_rate` of the encoder blocks.
        Defaults to 1.
    groups : int, optional
        Number of convolutional groups for encoder blocks. 
        An `int` results in a global value for `groups`, a `list` allows to define the `groups` per layer.
        Decoder blocks will mirror the `groups` of the encoder blocks.
        Defaults to 1.
    activation : str | keras.activations.Activation | keras.layers.Layer, optional
        Global activation function.
        Can be either a `str`, a `keras.activations.Activation`, or a `keras.layers.Layer`.
        Defaults to `"relu"`.
    use_bias : bool, optional
        If `True`, all layers use a bias.
        Defaults to `True`.
    bottleneck : keras.layers.Layer | keras.models.Model, optional
        An optional `keras.layer.Layer` or `keras.models.Model` that is placed in the bottleneck of the model.
        Defaults to `None`.
    merge_layer : str | keras.layers.Layer, optional {`"concatenate"`, `"average"`, `"maximum"`, `"minimum"`, `"add"`, `"subtract"`, `"multiply"`, `"dot"`}
        Layer to merge the forward information with the information from skip connections.
        Defaults to `"concatenate"`.
    kernel_initializer : str | keras.initializers.Initializer, optional
        Kernel initializer.
        Defaults to `"he_normal"`.
    bias_initializer : str | keras.initializers.Initializer, optional
        Bias initializer.
        Defaults to `"zeros"`.
    kernel_regularizer : str | keras.regularizers.Regularizer, optional
        Kernel regularizer.
        Defaults to `None`.
    bias_regularizer : str | keras.regularizers.Regularizer, optional
        Bias regularizer.
        Defaults to `None`.
    kernel_constraint : str | keras.constraints.Constraint, optional
        Kernel constraint.
        Defaults to `None`.
    bias_constraint : str | keras.constraints.Constraint, optional
        Bias constraint.
        Defaults to `None`.
    name : str, optional
        Name of the model.
        If `None`, `name` is automatically inherited from the class name `"Unet3D"`.
        Defaults to `None`.

    Notes
    -----
    The `filters` argument steers the depth of the model and the layout of the encoder- and decoder blocks on each level:
    A list containing tuples results in multiple convolutions on the respective level, e.g.,
    `filters=[(8, 8), 16, 32]` will return a model with a depth of 3, 
    where the first encoder (and last decoder) block has two consecutive convolutions with `filters=8`,
    and the remaining two levels have only a single convolution with `filters=16` and `filters=32`, respectively.

    Downsampling is realized using a strided convolution as proposed by [Springenberger et al.](https://arxiv.org/abs/1412.6806)

    """

    def __init__(
        self,
        filters=[8, 16, 32],
        kernel_size=5,
        strides=1,
        data_format="channels_last",
        dilation_rate=1,
        groups=1,
        activation="relu",
        use_bias=True,
        bottleneck=None,
        merge_layer="concatenate",
        kernel_initializer="he_normal",
        bias_initializer="zeros",
        kernel_regularizer=None,
        bias_regularizer=None,
        kernel_constraint=None,
        bias_constraint=None,
        name=None,
        **kwargs
    ):
        super().__init__(
            rank=3,
            filters=filters,
            kernel_size=kernel_size,
            strides=strides,
            data_format=data_format,
            dilation_rate=dilation_rate,
            groups=groups,
            activation=activation,
            use_bias=use_bias,
            bottleneck=bottleneck,
            merge_layer=merge_layer, 
            kernel_initializer=kernel_initializer,
            bias_initializer=bias_initializer,
            kernel_regularizer=kernel_regularizer,
            bias_regularizer=bias_regularizer,
            kernel_constraint=kernel_constraint,
            bias_constraint=bias_constraint,
            name=name,
            **kwargs
        )


### MODELS THAT USE SMOOTH UPSAMPLING LAYER ###
@saving.register_keras_serializable(package="Kerex.Models.AutoEncoder", name="SmoothUnet1D")
class SmoothUnet1D(BaseSmoothUnet):
    """
    1-D implementation of Unet, cf. [Ronneberger et al.](https://arxiv.org/abs/1505.04597)

    The model is build from a convolutional encoder- and a decoder path,
    and is able to extract features on different scale of the data
    by bisecting the features with each level of the model.
    Additionally, skip connections feed through high-resolution features from the encoder 
    to the decoder on each level.
    Upsampling is performed via a stack of image upsampling and a convolution.

    Parameters
    ----------
    filters : int | list | tuple
        Number of filters. 
        The model will be build symmetrically, meaning that only the number of encoder filters is defined,
        and the decoder will mirror it.
    kernel_size : int | list | tuple, optional
        Kernel size for encoder blocks. 
        An `int` results in a global `kernel_size`, a `list` allows to define the `kernel_size` per layer.
        Decoder blocks will mirror the `kernel_size` of the encoder blocks.
        Defaults to 5.
    strides : int | list | tuple, optional
        Strides for encoder blocks. 
        An `int` results in a global value for `strides`, a `list` allows to define the `strides` per layer.
        Decoder blocks will mirror the `strides` of the encoder blocks.
        Defaults to 1.
    padding : str, optional {`"same"`, `"causal"`}
        Padding for all convolutional layers in the model.
        Defaults to `"same"`.
    data_format : str, optional {`"channels_first"`, `"channels_last"`}
        Data format for the convolution operations.
        Defaults to `"channels_last"`.
    dilation_rate : int | list | tuple, optional
        Dilation rates for encoder blocks. 
        An `int` results in a global value for `dilation_rate`, a `list` allows to define the `dilation_rate` per layer.
        Decoder blocks will mirror the `dilation_rate` of the encoder blocks.
        Defaults to 1.
    groups : int, optional
        Number of convolutional groups for encoder blocks. 
        An `int` results in a global value for `groups`, a `list` allows to define the `groups` per layer.
        Decoder blocks will mirror the `groups` of the encoder blocks.
        Defaults to 1.
    activation : str | keras.activations.Activation | keras.layers.Layer, optional
        Global activation function.
        Can be either a `str`, a `keras.activations.Activation`, or a `keras.layers.Layer`.
        Defaults to `"relu"`.
    use_bias : bool, optional
        If `True`, all layers use a bias.
        Defaults to `True`.
    bottleneck : keras.layers.Layer | keras.models.Model, optional
        An optional `keras.layer.Layer` or `keras.models.Model` that is placed in the bottleneck of the model.
        Defaults to `None`.
    merge_layer : str | keras.layers.Layer, optional {`"concatenate"`, `"average"`, `"maximum"`, `"minimum"`, `"add"`, `"subtract"`, `"multiply"`, `"dot"`}
        Layer to merge the forward information with the information from skip connections.
        Defaults to `"concatenate"`.
    kernel_initializer : str | keras.initializers.Initializer, optional
        Kernel initializer.
        Defaults to `"he_normal"`.
    bias_initializer : str | keras.initializers.Initializer, optional
        Bias initializer.
        Defaults to `"zeros"`.
    kernel_regularizer : str | keras.regularizers.Regularizer, optional
        Kernel regularizer.
        Defaults to `None`.
    bias_regularizer : str | keras.regularizers.Regularizer, optional
        Bias regularizer.
        Defaults to `None`.
    kernel_constraint : str | keras.constraints.Constraint, optional
        Kernel constraint.
        Defaults to `None`.
    bias_constraint : str | keras.constraints.Constraint, optional
        Bias constraint.
        Defaults to `None`.
    name : str, optional
        Name of the model.
        If `None`, `name` is automatically inherited from the class name `"Unet1D"`.
        Defaults to `None`.

    Notes
    -----
    The `filters` argument steers the depth of the model and the layout of the encoder- and decoder blocks on each level:
    A list containing tuples results in multiple convolutions on the respective level, e.g.,
    `filters=[(8, 8), 16, 32]` will return a model with a depth of 3, 
    where the first encoder (and last decoder) block has two consecutive convolutions with `filters=8`,
    and the remaining two levels have only a single convolution with `filters=16` and `filters=32`, respectively.

    Downsampling is realized using a strided convolution as proposed by [Springenberger et al.](https://arxiv.org/abs/1412.6806)

    """

    def __init__(
        self,
        filters=[8, 16, 32],
        kernel_size=5,
        strides=1,
        padding="same",
        data_format="channels_last",
        dilation_rate=1,
        groups=1,
        activation="relu",
        use_bias=True,
        bottleneck=None,
        merge_layer="concatenate",
        kernel_initializer="he_normal",
        bias_initializer="zeros",
        kernel_regularizer=None,
        bias_regularizer=None,
        kernel_constraint=None,
        bias_constraint=None,
        name=None,
        **kwargs
    ):
        super().__init__(
            rank=1,
            filters=filters,
            kernel_size=kernel_size,
            strides=strides,
            padding=padding,
            data_format=data_format,
            dilation_rate=dilation_rate,
            groups=groups,
            activation=activation,
            use_bias=use_bias,
            bottleneck=bottleneck,
            merge_layer=merge_layer, 
            interpolation=None,
            kernel_initializer=kernel_initializer,
            bias_initializer=bias_initializer,
            kernel_regularizer=kernel_regularizer,
            bias_regularizer=bias_regularizer,
            kernel_constraint=kernel_constraint,
            bias_constraint=bias_constraint,
            name=name,
            **kwargs
        )


@saving.register_keras_serializable(package="Kerex.Models.AutoEncoder", name="SmoothUnet2D")
class SmoothUnet2D(BaseSmoothUnet):
    """
    2-D implementation of Unet, cf. [Ronneberger et al.](https://arxiv.org/abs/1505.04597)

    The model is build from a convolutional encoder- and a decoder path,
    and is able to extract features on different scale of the data
    by bisecting the features with each level of the model.
    Additionally, skip connections feed through high-resolution features from the encoder 
    to the decoder on each level.
    Upsampling is performed via a stack of image upsampling and a convolution.

    Parameters
    ----------
    filters : int | list | tuple
        Number of filters. 
        The model will be build symmetrically, meaning that only the number of encoder filters is defined,
        and the decoder will mirror it.
    kernel_size : int | list | tuple, optional
        Kernel size for encoder blocks. 
        An `int` results in a global `kernel_size`, a `list` allows to define the `kernel_size` per layer.
        Decoder blocks will mirror the `kernel_size` of the encoder blocks.
        Defaults to 5.
    strides : int | list | tuple, optional
        Strides for encoder blocks. 
        An `int` results in a global value for `strides`, a `list` allows to define the `strides` per layer.
        Decoder blocks will mirror the `strides` of the encoder blocks.
        Defaults to 1.
    data_format : str, optional {`"channels_first"`, `"channels_last"`}
        Data format for the convolution operations.
        Defaults to `"channels_last"`.
    dilation_rate : int | list | tuple, optional
        Dilation rates for encoder blocks. 
        An `int` results in a global value for `dilation_rate`, a `list` allows to define the `dilation_rate` per layer.
        Decoder blocks will mirror the `dilation_rate` of the encoder blocks.
        Defaults to 1.
    groups : int, optional
        Number of convolutional groups for encoder blocks. 
        An `int` results in a global value for `groups`, a `list` allows to define the `groups` per layer.
        Decoder blocks will mirror the `groups` of the encoder blocks.
        Defaults to 1.
    activation : str | keras.activations.Activation | keras.layers.Layer, optional
        Global activation function.
        Can be either a `str`, a `keras.activations.Activation`, or a `keras.layers.Layer`.
        Defaults to `"relu"`.
    use_bias : bool, optional
        If `True`, all layers use a bias.
        Defaults to `True`.
    bottleneck : keras.layers.Layer | keras.models.Model, optional
        An optional `keras.layer.Layer` or `keras.models.Model` that is placed in the bottleneck of the model.
        Defaults to `None`.
    merge_layer : str | keras.layers.Layer, optional {`"concatenate"`, `"average"`, `"maximum"`, `"minimum"`, `"add"`, `"subtract"`, `"multiply"`, `"dot"`}
        Layer to merge the forward information with the information from skip connections.
        Defaults to `"concatenate"`.
    interpolation : str, optional {`"nearest"`, `"bicubic"`, `"bilinear"`, `"lanczos3"`, `"lanczos5"`}
        Interpolation to use in `SmoothUpSampling2D` layer.
        This option is only valid for `rank=2` and is ignored otherwise.
        Defaults to `"nearest"`.
    kernel_initializer : str | keras.initializers.Initializer, optional
        Kernel initializer.
        Defaults to `"he_normal"`.
    bias_initializer : str | keras.initializers.Initializer, optional
        Bias initializer.
        Defaults to `"zeros"`.
    kernel_regularizer : str | keras.regularizers.Regularizer, optional
        Kernel regularizer.
        Defaults to `None`.
    bias_regularizer : str | keras.regularizers.Regularizer, optional
        Bias regularizer.
        Defaults to `None`.
    kernel_constraint : str | keras.constraints.Constraint, optional
        Kernel constraint.
        Defaults to `None`.
    bias_constraint : str | keras.constraints.Constraint, optional
        Bias constraint.
        Defaults to `None`.
    name : str, optional
        Name of the model.
        If `None`, `name` is automatically inherited from the class name `"Unet2D"`.
        Defaults to `None`.

    Notes
    -----
    The `filters` argument steers the depth of the model and the layout of the encoder- and decoder blocks on each level:
    A list containing tuples results in multiple convolutions on the respective level, e.g.,
    `filters=[(8, 8), 16, 32]` will return a model with a depth of 3, 
    where the first encoder (and last decoder) block has two consecutive convolutions with `filters=8`,
    and the remaining two levels have only a single convolution with `filters=16` and `filters=32`, respectively.

    Downsampling is realized using a strided convolution as proposed by [Springenberger et al.](https://arxiv.org/abs/1412.6806)

    """

    def __init__(
        self,
        filters=[8, 16, 32],
        kernel_size=5,
        data_format="channels_last",
        activation="relu",
        use_bias=True,
        bottleneck=None,
        merge_layer="concatenate",
        interpolation="nearest",
        kernel_initializer="he_normal",
        bias_initializer="zeros",
        kernel_regularizer=None,
        bias_regularizer=None,
        kernel_constraint=None,
        bias_constraint=None,
        name=None,
        **kwargs
    ):
        assert interpolation in ["bicubic", "bilinear", "lanczos3", "lanczos5", "nearest"], f"Unsupported interpolation '{interpolation}'. Supported interpolations are ['bicubic', 'bilinear', 'lanczos3', lanczos5', 'nearest']"
        super().__init__(
            rank=2,
            filters=filters,
            kernel_size=kernel_size,
            data_format=data_format,
            activation=activation,
            use_bias=use_bias,
            bottleneck=bottleneck,
            merge_layer=merge_layer, 
            interpolation=interpolation,
            kernel_initializer=kernel_initializer,
            bias_initializer=bias_initializer,
            kernel_regularizer=kernel_regularizer,
            bias_regularizer=bias_regularizer,
            kernel_constraint=kernel_constraint,
            bias_constraint=bias_constraint,
            name=name,
            **kwargs
        )


@saving.register_keras_serializable(package="Kerex.Models.AutoEncoder", name="SmooothUnet3D")
class SmoothUnet3D(BaseSmoothUnet):
    """
    3-D implementation of Unet, cf. [Ronneberger et al.](https://arxiv.org/abs/1505.04597)

    The model is build from a convolutional encoder- and a decoder path,
    and is able to extract features on different scale of the data
    by bisecting the features with each level of the model.
    Additionally, skip connections feed through high-resolution features from the encoder 
    to the decoder on each level.
    Upsampling is performed via a stack of image upsampling and a convolution.

    Parameters
    ----------
    filters : int | list | tuple
        Number of filters. 
        The model will be build symmetrically, meaning that only the number of encoder filters is defined,
        and the decoder will mirror it.
    kernel_size : int | list | tuple, optional
        Kernel size for encoder blocks. 
        An `int` results in a global `kernel_size`, a `list` allows to define the `kernel_size` per layer.
        Decoder blocks will mirror the `kernel_size` of the encoder blocks.
        Defaults to 5.
    strides : int | list | tuple, optional
        Strides for encoder blocks. 
        An `int` results in a global value for `strides`, a `list` allows to define the `strides` per layer.
        Decoder blocks will mirror the `strides` of the encoder blocks.
        Defaults to 1.
    data_format : str, optional {`"channels_first"`, `"channels_last"`}
        Data format for the convolution operations.
        Defaults to `"channels_last"`.
    dilation_rate : int | list | tuple, optional
        Dilation rates for encoder blocks. 
        An `int` results in a global value for `dilation_rate`, a `list` allows to define the `dilation_rate` per layer.
        Decoder blocks will mirror the `dilation_rate` of the encoder blocks.
        Defaults to 1.
    groups : int, optional
        Number of convolutional groups for encoder blocks. 
        An `int` results in a global value for `groups`, a `list` allows to define the `groups` per layer.
        Decoder blocks will mirror the `groups` of the encoder blocks.
        Defaults to 1.
    activation : str | keras.activations.Activation | keras.layers.Layer, optional
        Global activation function.
        Can be either a `str`, a `keras.activations.Activation`, or a `keras.layers.Layer`.
        Defaults to `"relu"`.
    use_bias : bool, optional
        If `True`, all layers use a bias.
        Defaults to `True`.
    bottleneck : keras.layers.Layer | keras.models.Model, optional
        An optional `keras.layer.Layer` or `keras.models.Model` that is placed in the bottleneck of the model.
        Defaults to `None`.
    merge_layer : str | keras.layers.Layer, optional {`"concatenate"`, `"average"`, `"maximum"`, `"minimum"`, `"add"`, `"subtract"`, `"multiply"`, `"dot"`}
        Layer to merge the forward information with the information from skip connections.
        Defaults to `"concatenate"`.
    kernel_initializer : str | keras.initializers.Initializer, optional
        Kernel initializer.
        Defaults to `"he_normal"`.
    bias_initializer : str | keras.initializers.Initializer, optional
        Bias initializer.
        Defaults to `"zeros"`.
    kernel_regularizer : str | keras.regularizers.Regularizer, optional
        Kernel regularizer.
        Defaults to `None`.
    bias_regularizer : str | keras.regularizers.Regularizer, optional
        Bias regularizer.
        Defaults to `None`.
    kernel_constraint : str | keras.constraints.Constraint, optional
        Kernel constraint.
        Defaults to `None`.
    bias_constraint : str | keras.constraints.Constraint, optional
        Bias constraint.
        Defaults to `None`.
    name : str, optional
        Name of the model.
        If `None`, `name` is automatically inherited from the class name `"Unet3D"`.
        Defaults to `None`.

    Notes
    -----
    The `filters` argument steers the depth of the model and the layout of the encoder- and decoder blocks on each level:
    A list containing tuples results in multiple convolutions on the respective level, e.g.,
    `filters=[(8, 8), 16, 32]` will return a model with a depth of 3, 
    where the first encoder (and last decoder) block has two consecutive convolutions with `filters=8`,
    and the remaining two levels have only a single convolution with `filters=16` and `filters=32`, respectively.

    Downsampling is realized using a strided convolution as proposed by [Springenberger et al.](https://arxiv.org/abs/1412.6806)

    """

    def __init__(
        self,
        filters=[8, 16, 32],
        kernel_size=5,
        strides=1,
        data_format="channels_last",
        dilation_rate=1,
        groups=1,
        activation="relu",
        use_bias=True,
        bottleneck=None,
        merge_layer="concatenate",
        kernel_initializer="he_normal",
        bias_initializer="zeros",
        kernel_regularizer=None,
        bias_regularizer=None,
        kernel_constraint=None,
        bias_constraint=None,
        name=None,
        **kwargs
    ):
        super().__init__(
            rank=3,
            filters=filters,
            kernel_size=kernel_size,
            strides=strides,
            data_format=data_format,
            dilation_rate=dilation_rate,
            groups=groups,
            activation=activation,
            use_bias=use_bias,
            bottleneck=bottleneck,
            merge_layer=merge_layer, 
            interpolation=None,
            kernel_initializer=kernel_initializer,
            bias_initializer=bias_initializer,
            kernel_regularizer=kernel_regularizer,
            bias_regularizer=bias_regularizer,
            kernel_constraint=kernel_constraint,
            bias_constraint=bias_constraint,
            name=name,
            **kwargs
        )