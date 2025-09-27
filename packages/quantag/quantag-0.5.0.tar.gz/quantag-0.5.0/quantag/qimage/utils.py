import numpy as np
from PIL import Image


def load_grayscale_image(path: str) -> np.ndarray:
    """Load image as grayscale numpy array."""
    return np.array(Image.open(path).convert("L"))


def normalize_to_amplitudes(img: np.ndarray):
    """
    Flatten image to a normalized vector (like quantum state amplitudes).
    Returns normalized vector and original shape.
    """
    vec = img.flatten().astype(float)
    norm = np.linalg.norm(vec)
    if norm == 0:
        return vec, img.shape
    return vec / norm, img.shape


def perform_qpca(amplitudes: np.ndarray):
    """
    Quantum-inspired PCA using eigen-decomposition of outer product.
    Returns eigenvalues and eigenvectors (components).
    """
    cov = np.outer(amplitudes, amplitudes)
    eigvals, eigvecs = np.linalg.eigh(cov)
    idx = np.argsort(eigvals)[::-1]  # sort descending
    return eigvals[idx], eigvecs[:, idx].T


def reconstruct_image(components, eigvals, shape, k=None):
    """
    Reconstruct image from eigencomponents.
    The result will have the same size as the original image.
    """
    if k is None:
        k = len(eigvals)

    comps = components[:k]   # shape (k, N)
    vals = eigvals[:k]       # shape (k,)

    recon = np.zeros(comps.shape[1])
    for i in range(k):
        recon += vals[i] * comps[i]

    return recon.reshape(shape)


def auto_levels(img: np.ndarray):
    """Scale image values to 0 - 255 range."""
    img = (img - img.min()) / (img.max() - img.min() + 1e-9) * 255
    return img.astype(np.uint8)


def compute_mse(original: np.ndarray, compressed: np.ndarray):
    """Mean Squared Error between two images."""
    return float(np.mean((original - compressed) ** 2))

