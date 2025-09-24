# core/torch_info.py

from torchfetch.model.info import TorchInfo


def get_torch_info() -> TorchInfo:
    try:
        import torch  # type: ignore

        cuda_available = torch.cuda.is_available()
        return TorchInfo(
            version=torch.__version__,
            cuda_version=torch.version.cuda if cuda_available else "N/A",
            cudnn_version=str(torch.backends.cudnn.version())
            if cuda_available
            else "N/A",
            cuda_available=cuda_available,
        )
    except Exception:
        return TorchInfo(
            version="N/A", cuda_version="N/A", cudnn_version="N/A", cuda_available=False
        )
