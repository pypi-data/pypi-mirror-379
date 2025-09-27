__all__ = [
    "ConvBase",
    "BidirectionalConv1d",
    "BidirectionalConv2d",
    "BidirectionalConv3d",
    "calc_max_groups",
    "get_padding_2d",
    "get_conv",
    "remove_norm",
    "is_groups_compatible",
    "is_conv",
]
import math
import torch
from torch import Tensor
from lt_utils.common import *
from lt_utils.misc_utils import filter_kwargs
from torch.nn.utils.parametrize import remove_parametrizations
from torch.nn.utils.parametrizations import weight_norm, spectral_norm
from lt_tensor.common import nn, Model
from typing import TypeGuard
from lt_tensor.tensor_ops import get_padding_conv

TP_SHAPE_1: TypeAlias = Union[int, Tuple[int]]
TP_SHAPE_2: TypeAlias = Union[TP_SHAPE_1, Tuple[int, int]]
TP_SHAPE_3: TypeAlias = Union[TP_SHAPE_2, Tuple[int, int, int]]

TC: TypeAlias = Callable[[Tensor], Tensor]


def _dummy(module: Model, *args, **kwargs):
    return module


def is_groups_compatible(channels_in: int, channels_out: int, groups: int):
    if channels_in < 2 or channels_out < 2:
        return groups == 1
    return groups % channels_in == 0 and groups % channels_out == 0


def calc_max_groups(channels_in: int, channels_out: int):
    return math.gcd(int(channels_in), int(channels_out))


def is_conv(module: nn.Module) -> TypeGuard[nn.modules.conv._ConvNd]:
    return isinstance(
        module,
        (
            nn.Conv1d,
            nn.Conv2d,
            nn.Conv3d,
            nn.ConvTranspose1d,
            nn.ConvTranspose2d,
            nn.ConvTranspose3d,
            nn.LazyConv1d,
            nn.LazyConv2d,
            nn.LazyConv3d,
            nn.LazyConvTranspose1d,
            nn.LazyConvTranspose2d,
            nn.LazyConvTranspose3d,
            nn.modules.conv._ConvNd,
        ),
    )


def get_weight_norm(
    norm_type: Optional[Literal["weight_norm", "spectral_norm"]] = None, **norm_kwargs
) -> Callable[[Union[nn.Module, Model]], Union[nn.Module, Model]]:
    if not norm_type:
        return _dummy
    if norm_type == "weight_norm":
        return lambda x: weight_norm(x, **norm_kwargs)
    return lambda x: spectral_norm(x, **norm_kwargs)


def _init_conv_orthogonal(
    m: Union[nn.Module, Model],
    mean: float = 0.0,
    std: float = 1.0,
    zero_bias: bool = False,
):
    if not hasattr(m, "weight"):
        return False

    nn.init.normal_(m.weight, mean=mean, std=std)

    if zero_bias and hasattr(m, "bias") and m.bias is not None:
        m.bias.zero_()
    return True


def init_conv_orthogonal(
    m: Union[nn.Module, Model], gain: float = 1.0, zero_bias: bool = False
):
    for module in m.modules():
        if not is_conv(module):
            continue
        nn.init.orthogonal_(module.weight, gain)
        if zero_bias and module.bias is not None:
            module.bias.zero_()


def _init_conv_normal(
    m: Union[nn.Module, Model],
    mean: float = 0.0,
    std: float = 1.0,
    zero_bias: bool = False,
):
    if not hasattr(m, "weight"):
        return False

    nn.init.normal_(m.weight, mean=mean, std=std)

    if zero_bias and hasattr(m, "bias") and m.bias is not None:
        m.bias.zero_()
    return True


def init_conv_normal(
    m: Union[nn.Module, Model],
    mean: float = 0.0,
    std: float = 1.0,
    zero_bias: bool = False,
):
    for module in m.modules():
        if not is_conv(module):
            continue
        nn.init.normal_(module.weight, mean=mean, std=std)
        if zero_bias and module.bias is not None:
            module.bias.zero_()


def _init_conv_kaiming(
    m: Union[nn.Module, Model],
    a: Optional[float] = None,
    mode: Literal["fan_in", "fan_out"] = "fan_in",
    nonlinearity: Literal["relu", "leaky_relu"] = "leaky_relu",
    zero_bias: bool = False,
):
    if not hasattr(m, "weight"):
        return False
    if not a:
        a = math.sqrt(5)
    nn.init.kaiming_uniform_(m.weight, a=a, mode=mode, nonlinearity=nonlinearity)
    if zero_bias and hasattr(m, "bias") and m.bias is not None:
        m.bias.zero_()
    return True


def init_conv_kaiming(
    m: Union[nn.Module, Model],
    a: Optional[float] = None,
    mode: Literal["fan_in", "fan_out"] = "fan_in",
    nonlinearity: Literal["relu", "leaky_relu"] = "leaky_relu",
    zero_bias: bool = False,
):

    if is_conv(m):
        _init_conv_kaiming(m)
    else:
        for module in m.modules():
            if not is_conv(module):
                continue
            _init_conv_kaiming(module, a, mode, nonlinearity, zero_bias)


def remove_norm(module, name: str = "weight"):
    try:
        try:
            remove_parametrizations(module, name, leave_parametrized=False)
        except:
            try:
                remove_parametrizations(module, name, leave_parametrized=True)
            except:
                pass
    except ValueError:
        pass  # not parametrized


def get_conv(
    in_channels: int = 1,
    out_channels: Optional[int] = None,
    kernel_size: TP_SHAPE_3 = 1,
    stride: TP_SHAPE_3 = 1,
    padding: TP_SHAPE_3 = 0,
    output_padding: TP_SHAPE_3 = 0,
    dilation: TP_SHAPE_3 = 1,
    groups: TP_SHAPE_3 = 1,
    bias: bool = True,
    padding_mode: str = "zeros",
    *,
    dim: Literal["1d", "2d", "3d"] = "1d",
    transposed: bool = False,
    norm: Optional[Literal["weight_norm", "spectral_norm"]] = None,
    norm_kwargs: Dict[str, Any] = {},
    lazy: bool = False,
) -> Union[
    nn.Conv1d,
    nn.LazyConv1d,
    nn.ConvTranspose1d,
    nn.LazyConvTranspose1d,
    nn.Conv2d,
    nn.LazyConv2d,
    nn.ConvTranspose2d,
    nn.LazyConvTranspose2d,
    nn.Conv3d,
    nn.LazyConv3d,
    nn.ConvTranspose3d,
    nn.LazyConvTranspose3d,
    TC,
]:
    dim = dim.lower().strip()
    assert dim in [
        "1d",
        "2d",
        "3d",
    ], f"Invalid conv dim '{dim}'. It must be either '1d', '2d' or '3d'."
    if norm is not None:
        norm = norm.strip().lower()
        if norm and norm not in ["weight_norm", "spectral_norm"]:
            if norm == "weight":
                norm = "weight_norm"
            elif norm == "spectral":
                norm == "spectral_norm"
            elif norm == "none":
                norm = None
            else:
                raise ValueError(
                    f"Invalid norm '{norm}'. "
                    'It must be either "weight_norm" or "spectral_norm" or None.'
                )
    out_ch = out_channels if out_channels is not None else in_channels
    kwargs = dict(
        in_channels=max(in_channels, 1),
        out_channels=max(out_ch, 1),
        kernel_size=kernel_size,
        padding=padding,
        stride=stride,
        dilation=dilation,
        bias=bias,
        groups=groups,
        padding_mode=padding_mode,
        output_padding=output_padding,
    )

    match dim:
        case "1d":
            if transposed:
                if lazy:
                    md = nn.LazyConvTranspose1d
                else:
                    md = nn.ConvTranspose1d
            else:
                if lazy:
                    md = nn.LazyConv1d
                else:
                    md = nn.Conv1d
        case "2d":
            if transposed:
                if lazy:
                    md = nn.LazyConvTranspose2d
                else:
                    md = nn.ConvTranspose2d
            else:
                if lazy:
                    md = nn.LazyConv2d
                else:
                    md = nn.Conv2d
        case _:
            if transposed:
                if lazy:
                    md = nn.LazyConvTranspose3d
                else:
                    md = nn.ConvTranspose3d

            else:
                if lazy:
                    md = nn.LazyConv3d
                else:
                    md = nn.Conv3d

    kwargs = filter_kwargs(md, False, [], **kwargs)
    if norm:
        norm_fn = get_weight_norm(norm, **norm_kwargs)
        return norm_fn(md(**kwargs))
    return md(**kwargs)


def get_1d_conv(
    in_channels: int,
    out_channels: Optional[int] = None,
    kernel_size: int = 1,
    stride: int = 1,
    padding: int = 0,
    output_padding: int = 0,
    dilation: int = 1,
    groups: int = 1,
    bias: bool = True,
    padding_mode: str = "zeros",
    *,
    transposed: bool = False,
    norm: Optional[Literal["weight_norm", "spectral_norm"]] = None,
    norm_kwargs: Dict[str, Any] = {},
    lazy: bool = False,
) -> Union[nn.Conv1d, nn.ConvTranspose1d, TC]:
    return get_conv(
        in_channels=in_channels,
        out_channels=out_channels,
        kernel_size=kernel_size,
        padding=padding,
        stride=stride,
        dilation=dilation,
        bias=bias,
        groups=groups,
        padding_mode=padding_mode,
        output_padding=output_padding,
        transposed=transposed,
        norm=norm,
        norm_kwargs=norm_kwargs,
        dim="1d",
        lazy=lazy,
    )


def get_2d_conv(
    in_channels: int,
    out_channels: Optional[int] = None,
    kernel_size: TP_SHAPE_2 = 1,
    stride: TP_SHAPE_2 = 1,
    padding: TP_SHAPE_2 = 0,
    output_padding: TP_SHAPE_2 = 0,
    dilation: TP_SHAPE_2 = 1,
    groups: int = 1,
    bias: bool = True,
    padding_mode: str = "zeros",
    *,
    transposed: bool = False,
    norm: Optional[Literal["weight_norm", "spectral_norm"]] = None,
    norm_kwargs: Dict[str, Any] = {},
    lazy: bool = False,
) -> Union[nn.Conv2d, nn.ConvTranspose2d, TC]:
    return get_conv(
        in_channels=in_channels,
        out_channels=out_channels,
        kernel_size=kernel_size,
        padding=padding,
        stride=stride,
        dilation=dilation,
        bias=bias,
        groups=groups,
        padding_mode=padding_mode,
        output_padding=output_padding,
        transposed=transposed,
        norm=norm,
        norm_kwargs=norm_kwargs,
        dim="2d",
        lazy=lazy,
    )


def get_3d_conv(
    in_channels: int,
    out_channels: Optional[int] = None,
    kernel_size: TP_SHAPE_3 = 1,
    stride: TP_SHAPE_3 = 1,
    padding: TP_SHAPE_3 = 0,
    output_padding: TP_SHAPE_3 = 0,
    dilation: TP_SHAPE_3 = 1,
    groups: int = 1,
    bias: bool = True,
    padding_mode: str = "zeros",
    *,
    transposed: bool = False,
    norm: Optional[Literal["weight_norm", "spectral_norm"]] = None,
    norm_kwargs: Dict[str, Any] = {},
    lazy: bool = False,
) -> Union[nn.Conv3d, nn.ConvTranspose3d, TC]:
    return get_conv(
        in_channels=in_channels,
        out_channels=out_channels,
        kernel_size=kernel_size,
        padding=padding,
        stride=stride,
        dilation=dilation,
        bias=bias,
        groups=groups,
        padding_mode=padding_mode,
        output_padding=output_padding,
        transposed=transposed,
        norm=norm,
        norm_kwargs=norm_kwargs,
        dim="3d",
        lazy=lazy,
    )


class ConvBase(Model):

    @staticmethod
    def get_1d_conv(
        in_channels: int,
        out_channels: Optional[int] = None,
        kernel_size: int = 1,
        stride: int = 1,
        padding: int = 0,
        output_padding: int = 0,
        dilation: int = 1,
        groups: int = 1,
        bias: bool = True,
        padding_mode: str = "zeros",
        *,
        transposed: bool = False,
        norm: Optional[Literal["weight_norm", "spectral_norm"]] = None,
        norm_kwargs: Dict[str, Any] = {},
        lazy: bool = False,
    ) -> Union[nn.Conv1d, nn.ConvTranspose1d, TC]:
        return get_conv(
            in_channels=in_channels,
            out_channels=out_channels,
            kernel_size=kernel_size,
            padding=padding,
            stride=stride,
            dilation=dilation,
            bias=bias,
            groups=groups,
            padding_mode=padding_mode,
            output_padding=output_padding,
            transposed=transposed,
            norm=norm,
            norm_kwargs=norm_kwargs,
            dim="1d",
            lazy=lazy,
        )

    @staticmethod
    def get_2d_conv(
        in_channels: int,
        out_channels: Optional[int] = None,
        kernel_size: TP_SHAPE_2 = 1,
        stride: TP_SHAPE_2 = 1,
        padding: TP_SHAPE_2 = 0,
        output_padding: TP_SHAPE_2 = 0,
        dilation: TP_SHAPE_2 = 1,
        groups: int = 1,
        bias: bool = True,
        padding_mode: str = "zeros",
        *,
        transposed: bool = False,
        norm: Optional[Literal["weight_norm", "spectral_norm"]] = None,
        norm_kwargs: Dict[str, Any] = {},
    ) -> Union[nn.Conv2d, nn.ConvTranspose2d, TC]:
        return get_conv(
            in_channels=in_channels,
            out_channels=out_channels,
            kernel_size=kernel_size,
            padding=padding,
            stride=stride,
            dilation=dilation,
            bias=bias,
            groups=groups,
            padding_mode=padding_mode,
            output_padding=output_padding,
            transposed=transposed,
            norm=norm,
            norm_kwargs=norm_kwargs,
            dim="2d",
        )

    @staticmethod
    def get_3d_conv(
        in_channels: int,
        out_channels: Optional[int] = None,
        kernel_size: TP_SHAPE_3 = 1,
        stride: TP_SHAPE_3 = 1,
        padding: TP_SHAPE_3 = 0,
        output_padding: TP_SHAPE_3 = 0,
        dilation: TP_SHAPE_3 = 1,
        groups: int = 1,
        bias: bool = True,
        padding_mode: str = "zeros",
        *,
        transposed: bool = False,
        norm: Optional[Literal["weight_norm", "spectral_norm"]] = None,
        norm_kwargs: Dict[str, Any] = {},
    ) -> Union[nn.Conv3d, nn.ConvTranspose3d, TC]:
        return get_conv(
            in_channels=in_channels,
            out_channels=out_channels,
            kernel_size=kernel_size,
            padding=padding,
            stride=stride,
            dilation=dilation,
            bias=bias,
            groups=groups,
            padding_mode=padding_mode,
            output_padding=output_padding,
            transposed=transposed,
            norm=norm,
            norm_kwargs=norm_kwargs,
            dim="3d",
        )

    @staticmethod
    def get_max_groups(in_channels: int, out_channels: int):
        return calc_max_groups(in_channels, out_channels)

    @staticmethod
    def get_padding(kernel_size: int, dilation: int, mode: Literal["a", "b"] = "a"):
        return get_padding_conv(kernel_size, dilation, mode.lower())

    def remove_norms(self, name: str = "weight"):
        for module in self.modules():
            try:
                if is_conv(module):
                    remove_norm(module, name)
            except:
                pass

    @staticmethod
    def _normal_init_default(m: nn.Module, mean=0.0, std=0.01, zero_bias: bool = False):
        if is_conv(m):
            nn.init.normal_(m.weight, mean=mean, std=std)
            if zero_bias and m.bias is not None:
                nn.init.zeros_(m.bias)


class BidirectionalConv1d(ConvBase):
    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        kernel_size: int = 1,
        stride: int = 1,
        dilation: int = 1,
        padding: int = 0,
        groups_fwd: int = 1,
        groups_bwd: int = 1,
        output_padding: int = 0,
        bias_fwd: bool = True,
        bias_bwd: bool = True,
        transposed: bool = False,
        *,
        return_tuple: bool = False,
        norm: Optional[Literal["weight", "spectral"]] = None,
        flip_back: bool = True,
        flip_dims: List[int] = [-1],
        **kwargs,
    ):
        super().__init__()
        assert (
            isinstance(flip_dims, list)
            and flip_dims
            and all([isinstance(x, int) for x in flip_dims])
        )
        self.fwd = self.get_1d_conv(
            in_channels=in_channels,
            out_channels=out_channels,
            kernel_size=kernel_size,
            groups=groups_fwd,
            dilation=dilation,
            padding=padding,
            stride=stride,
            norm=norm,
            output_padding=output_padding,
            transposed=transposed,
            bias=bias_fwd,
        )
        self.bwd = self.get_1d_conv(
            in_channels=in_channels,
            out_channels=out_channels,
            kernel_size=kernel_size,
            groups=groups_bwd,
            dilation=dilation,
            padding=padding,
            norm=norm,
            output_padding=output_padding,
            transposed=transposed,
            bias=bias_bwd,
        )
        self.flip_back = flip_back
        self.return_tuple = return_tuple
        self.flip_dims = flip_dims

    def __call__(self, *args, **kwds) -> Union[Tuple[Tensor, Tensor], Tensor]:
        return super().__call__(*args, **kwds)

    def forward(self, x: Tensor) -> Union[Tuple[Tensor, Tensor], Tensor]:
        # forward path
        y_fwd = self.fwd(x)
        # backward path: flip, convolve, flip back if needed
        y_bwd = self.bwd(x.flip(dims=self.flip_dims))
        if self.flip_back:
            y_bwd = y_bwd.flip(dims=self.flip_dims)
        if self.return_tuple:
            return y_fwd, y_bwd
        return torch.cat((y_fwd, y_bwd), dim=1)


class BidirectionalConv2d(ConvBase):
    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        kernel_size: int = 1,
        stride: int = 1,
        dilation: int = 1,
        padding: int = 0,
        groups_fwd: int = 1,
        groups_bwd: int = 1,
        output_padding: int = 0,
        bias_fwd: bool = True,
        bias_bwd: bool = True,
        transposed: bool = False,
        *,
        return_tuple: bool = False,
        norm: Optional[Literal["weight", "spectral"]] = None,
        flip_back: bool = True,
        flip_dims: List[int] = [-2, -1],
        **kwargs,
    ):
        super().__init__()
        assert (
            isinstance(flip_dims, list)
            and flip_dims
            and all([isinstance(x, int) for x in flip_dims])
        )
        self.fwd = self.get_2d_conv(
            in_channels=in_channels,
            out_channels=out_channels,
            kernel_size=kernel_size,
            groups=groups_fwd,
            dilation=dilation,
            padding=padding,
            stride=stride,
            norm=norm,
            output_padding=output_padding,
            transposed=transposed,
            bias=bias_fwd,
        )
        self.bwd = self.get_2d_conv(
            in_channels=in_channels,
            out_channels=out_channels,
            kernel_size=kernel_size,
            groups=groups_bwd,
            dilation=dilation,
            padding=padding,
            norm=norm,
            output_padding=output_padding,
            transposed=transposed,
            bias=bias_bwd,
        )
        self.return_tuple = return_tuple
        self.flip_back = flip_back
        self.flip_dims = flip_dims

    def __call__(self, *args, **kwds) -> Union[Tuple[Tensor, Tensor], Tensor]:
        return super().__call__(*args, **kwds)

    def forward(self, x: Tensor) -> Union[Tuple[Tensor, Tensor], Tensor]:
        y_fwd = self.fwd(x)
        y_bwd = self.bwd(x.flip(dims=self.flip_dims))
        if self.flip_back:
            y_bwd = y_bwd.flip(dims=self.flip_dims)
        if self.return_tuple:
            return y_fwd, y_bwd
        return torch.cat((y_fwd, y_bwd), dim=1)


class BidirectionalConv3d(ConvBase):
    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        kernel_size: int = 1,
        stride: int = 1,
        dilation: int = 1,
        padding: int = 0,
        groups_fwd: int = 1,
        groups_bwd: int = 1,
        output_padding: int = 0,
        bias_fwd: bool = True,
        bias_bwd: bool = True,
        transposed: bool = False,
        *,
        return_tuple: bool = False,
        norm: Optional[Literal["weight", "spectral"]] = None,
        flip_back: bool = True,
        flip_dims: List[int] = [-3, -2, -1],
        **kwargs,
    ):
        super().__init__()
        assert (
            isinstance(flip_dims, list)
            and flip_dims
            and all([isinstance(x, int) for x in flip_dims])
        )
        self.fwd = self.get_3d_conv(
            in_channels=in_channels,
            out_channels=out_channels,
            kernel_size=kernel_size,
            groups=groups_fwd,
            dilation=dilation,
            padding=padding,
            stride=stride,
            norm=norm,
            output_padding=output_padding,
            transposed=transposed,
            bias=bias_fwd,
        )
        self.bwd = self.get_3d_conv(
            in_channels=in_channels,
            out_channels=out_channels,
            kernel_size=kernel_size,
            groups=groups_bwd,
            dilation=dilation,
            padding=padding,
            norm=norm,
            output_padding=output_padding,
            transposed=transposed,
            bias=bias_bwd,
        )
        self.return_tuple = return_tuple
        self.flip_back = flip_back
        self.flip_dims = flip_dims

    def __call__(self, *args, **kwds) -> Union[Tuple[Tensor, Tensor], Tensor]:
        return super().__call__(*args, **kwds)

    def forward(self, x: Tensor) -> Union[Tuple[Tensor, Tensor], Tensor]:
        y_fwd = self.fwd(x)
        y_bwd = self.bwd(x.flip(dims=self.flip_dims))
        if self.flip_back:
            y_bwd = y_bwd.flip(dims=self.flip_dims)
        if self.return_tuple:
            return y_fwd, y_bwd
        return torch.cat((y_fwd, y_bwd), dim=1)
