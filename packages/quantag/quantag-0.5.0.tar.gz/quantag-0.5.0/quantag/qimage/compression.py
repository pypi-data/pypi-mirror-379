import numpy as np
from PIL import Image
from io import BytesIO
import base64
from .utils import (
    load_grayscale_image,
    normalize_to_amplitudes,
    perform_qpca,
    reconstruct_image,
    auto_levels,
    compute_mse
)

class QImageCompressor:
    def __init__(self, energy_threshold: float = 0.95):
        """
        Quantum-inspired image compression based on PCA.
        :param energy_threshold: fraction of total variance to keep
        """
        self.energy_threshold = energy_threshold

    def compress(self, img_path: str) -> dict:
        """Compress an image and return results as numpy arrays and metrics."""
        img_data = load_grayscale_image(img_path)

        amplitudes, shape = normalize_to_amplitudes(img_data)
        eigvals, components = perform_qpca(amplitudes)

        total_energy = np.sum(eigvals)
        cumulative = np.cumsum(eigvals)
        k = np.searchsorted(cumulative, self.energy_threshold * total_energy) + 1

        recon_full = reconstruct_image(components, eigvals, shape)
        recon_compressed = reconstruct_image(components, eigvals, shape, k=k)

        mse = compute_mse(img_data, recon_compressed)

        return {
            "original": img_data,
            "reconstructed": auto_levels(recon_full.astype(float)),
            "compressed": auto_levels(recon_compressed.astype(float)),
            "mse": mse,
            "components": components[:min(6, len(components))].reshape(-1, *shape),
            "k": k
        }

    @staticmethod
    def to_base64(img_array: np.ndarray) -> str:
        """Convert numpy image array to base64 PNG."""
        img = Image.fromarray(img_array.astype(np.uint8))
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        return base64.b64encode(buffer.getvalue()).decode()
