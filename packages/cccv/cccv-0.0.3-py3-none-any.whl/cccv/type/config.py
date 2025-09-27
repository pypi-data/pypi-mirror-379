from enum import Enum


# Enum for config type
# For the Auxiliary Network, {ModelType.model}_{config_name}.pth
# For the Super-Resolution Models, {ModelType.model}_{config_name}_{scale}x.pth
class ConfigType(str, Enum):
    # ------------------------------------- Auxiliary Network ----------------------------------------------------------

    # SpyNet
    SpyNet_spynet_sintel_final = "SpyNet_spynet_sintel_final.pth"

    # ------------------------------------- Single Image Super-Resolution ----------------------------------------------

    # RealESRGAN
    RealESRGAN_RealESRGAN_x4plus_4x = "RealESRGAN_RealESRGAN_x4plus_4x.pth"
    RealESRGAN_RealESRGAN_x4plus_anime_6B_4x = "RealESRGAN_RealESRGAN_x4plus_anime_6B_4x.pth"
    RealESRGAN_RealESRGAN_x2plus_2x = "RealESRGAN_RealESRGAN_x2plus_2x.pth"
    RealESRGAN_realesr_animevideov3_4x = "RealESRGAN_realesr_animevideov3_4x.pth"

    RealESRGAN_AnimeJaNai_HD_V3_Compact_2x = "RealESRGAN_AnimeJaNai_HD_V3_Compact_2x.pth"
    RealESRGAN_AniScale_2_Compact_2x = "RealESRGAN_AniScale_2_Compact_2x.pth"
    RealESRGAN_Ani4Kv2_Compact_2x = "RealESRGAN_Ani4Kv2_Compact_2x.pth"
    RealESRGAN_APISR_RRDB_GAN_generator_2x = "RealESRGAN_APISR_RRDB_GAN_generator_2x.pth"
    RealESRGAN_APISR_RRDB_GAN_generator_4x = "RealESRGAN_APISR_RRDB_GAN_generator_4x.pth"

    # RealCUGAN
    RealCUGAN_Conservative_2x = "RealCUGAN_Conservative_2x.pth"
    RealCUGAN_Denoise1x_2x = "RealCUGAN_Denoise1x_2x.pth"
    RealCUGAN_Denoise2x_2x = "RealCUGAN_Denoise2x_2x.pth"
    RealCUGAN_Denoise3x_2x = "RealCUGAN_Denoise3x_2x.pth"
    RealCUGAN_No_Denoise_2x = "RealCUGAN_No_Denoise_2x.pth"
    RealCUGAN_Conservative_3x = "RealCUGAN_Conservative_3x.pth"
    RealCUGAN_Denoise3x_3x = "RealCUGAN_Denoise3x_3x.pth"
    RealCUGAN_No_Denoise_3x = "RealCUGAN_No_Denoise_3x.pth"
    RealCUGAN_Conservative_4x = "RealCUGAN_Conservative_4x.pth"
    RealCUGAN_Denoise3x_4x = "RealCUGAN_Denoise3x_4x.pth"
    RealCUGAN_No_Denoise_4x = "RealCUGAN_No_Denoise_4x.pth"
    RealCUGAN_Pro_Conservative_2x = "RealCUGAN_Pro_Conservative_2x.pth"
    RealCUGAN_Pro_Denoise3x_2x = "RealCUGAN_Pro_Denoise3x_2x.pth"
    RealCUGAN_Pro_No_Denoise_2x = "RealCUGAN_Pro_No_Denoise_2x.pth"
    RealCUGAN_Pro_Conservative_3x = "RealCUGAN_Pro_Conservative_3x.pth"
    RealCUGAN_Pro_Denoise3x_3x = "RealCUGAN_Pro_Denoise3x_3x.pth"
    RealCUGAN_Pro_No_Denoise_3x = "RealCUGAN_Pro_No_Denoise_3x.pth"

    # EDSR
    EDSR_Mx2_f64b16_DIV2K_official_2x = "EDSR_Mx2_f64b16_DIV2K_official_2x.pth"
    EDSR_Mx3_f64b16_DIV2K_official_3x = "EDSR_Mx3_f64b16_DIV2K_official_3x.pth"
    EDSR_Mx4_f64b16_DIV2K_official_4x = "EDSR_Mx4_f64b16_DIV2K_official_4x.pth"

    # SwinIR
    SwinIR_classicalSR_DF2K_s64w8_SwinIR_M_2x = "SwinIR_classicalSR_DF2K_s64w8_SwinIR_M_2x.pth"
    SwinIR_lightweightSR_DIV2K_s64w8_SwinIR_S_2x = "SwinIR_lightweightSR_DIV2K_s64w8_SwinIR_S_2x.pth"
    SwinIR_realSR_BSRGAN_DFOWMFC_s64w8_SwinIR_L_GAN_4x = "SwinIR_realSR_BSRGAN_DFOWMFC_s64w8_SwinIR_L_GAN_4x.pth"
    SwinIR_realSR_BSRGAN_DFO_s64w8_SwinIR_M_GAN_2x = "SwinIR_realSR_BSRGAN_DFO_s64w8_SwinIR_M_GAN_2x.pth"
    SwinIR_realSR_BSRGAN_DFO_s64w8_SwinIR_M_GAN_4x = "SwinIR_realSR_BSRGAN_DFO_s64w8_SwinIR_M_GAN_4x.pth"

    SwinIR_Bubble_AnimeScale_SwinIR_Small_v1_2x = "SwinIR_Bubble_AnimeScale_SwinIR_Small_v1_2x.pth"

    # SCUNet
    SCUNet_color_50_1x = "SCUNet_color_50_1x.pth"
    SCUNet_color_real_psnr_1x = "SCUNet_color_real_psnr_1x.pth"
    SCUNet_color_real_gan_1x = "SCUNet_color_real_gan_1x.pth"

    # DAT
    DAT_S_2x = "DAT_S_2x.pth"
    DAT_S_3x = "DAT_S_3x.pth"
    DAT_S_4x = "DAT_S_4x.pth"
    DAT_2x = "DAT_2x.pth"
    DAT_3x = "DAT_3x.pth"
    DAT_4x = "DAT_4x.pth"
    DAT_2_2x = "DAT_2_2x.pth"
    DAT_2_3x = "DAT_2_3x.pth"
    DAT_2_4x = "DAT_2_4x.pth"
    DAT_light_2x = "DAT_light_2x.pth"
    DAT_light_3x = "DAT_light_3x.pth"
    DAT_light_4x = "DAT_light_4x.pth"

    DAT_APISR_GAN_generator_4x = "DAT_APISR_GAN_generator_4x.pth"

    # SRCNN
    SRCNN_2x = "SRCNN_2x.pth"
    SRCNN_3x = "SRCNN_3x.pth"
    SRCNN_4x = "SRCNN_4x.pth"

    # HAT
    HAT_S_2x = "HAT_S_2x.pth"
    HAT_S_3x = "HAT_S_3x.pth"
    HAT_S_4x = "HAT_S_4x.pth"
    HAT_2x = "HAT_2x.pth"
    HAT_3x = "HAT_3x.pth"
    HAT_4x = "HAT_4x.pth"
    HAT_Real_GAN_sharper_4x = "HAT_Real_GAN_sharper_4x.pth"
    HAT_Real_GAN_4x = "HAT_Real_GAN_4x.pth"
    HAT_ImageNet_pretrain_2x = "HAT_ImageNet_pretrain_2x.pth"
    HAT_ImageNet_pretrain_3x = "HAT_ImageNet_pretrain_3x.pth"
    HAT_ImageNet_pretrain_4x = "HAT_ImageNet_pretrain_4x.pth"
    HAT_L_ImageNet_pretrain_2x = "HAT_L_ImageNet_pretrain_2x.pth"
    HAT_L_ImageNet_pretrain_3x = "HAT_L_ImageNet_pretrain_3x.pth"
    HAT_L_ImageNet_pretrain_4x = "HAT_L_ImageNet_pretrain_4x.pth"

    # ------------------------------------- Video Super-Resolution -----------------------------------------------------

    # EDVR
    EDVR_M_SR_REDS_official_4x = "EDVR_M_SR_REDS_official_4x.pth"
    EDVR_M_woTSA_SR_REDS_official_4x = "EDVR_M_woTSA_SR_REDS_official_4x.pth"

    # AnimeSR
    AnimeSR_v1_PaperModel_4x = "AnimeSR_v1_PaperModel_4x.pth"
    AnimeSR_v2_4x = "AnimeSR_v2_4x.pth"

    # ------------------------------------- Video Frame Interpolation --------------------------------------------------

    # RIFE
    RIFE_IFNet_v426_heavy = "RIFE_IFNet_v426_heavy.pth"

    # DRBA
    DRBA_IFNet = "DRBA_IFNet.pth"
