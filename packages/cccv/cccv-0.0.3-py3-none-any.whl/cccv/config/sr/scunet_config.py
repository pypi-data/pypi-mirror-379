from typing import List, Union

from cccv.config import CONFIG_REGISTRY
from cccv.config.base_config import SRBaseConfig
from cccv.type import ArchType, ConfigType, ModelType


class SCUNetConfig(SRBaseConfig):
    arch: Union[ArchType, str] = ArchType.SCUNET
    model: Union[ModelType, str] = ModelType.SRBaseModel
    scale: int = 1
    in_nc: int = 3
    config: List[int] = [4, 4, 4, 4, 4, 4, 4]  # noqa
    dim: int = 64
    drop_path_rate: float = 0.0
    input_resolution: int = 256


SCUNetConfigs = [
    SCUNetConfig(
        name=ConfigType.SCUNet_color_50_1x,
        hash="11f6839726c10dad327a75ce578be661a3e208f01fd7ab6d3eb763a5464bfdfe",
        scale=1,
    ),
    SCUNetConfig(
        name=ConfigType.SCUNet_color_real_psnr_1x,
        hash="fa78899ba2caec9d235a900e91d96c689da71c42029230c2028b00f09f809c2e",
        scale=1,
    ),
    SCUNetConfig(
        name=ConfigType.SCUNet_color_real_gan_1x,
        hash="892c83f812c59173273b74f4f34a14ecaf57a2fdb68df056664589beb55c966e",
        scale=1,
    ),
]

for cfg in SCUNetConfigs:
    CONFIG_REGISTRY.register(cfg)
