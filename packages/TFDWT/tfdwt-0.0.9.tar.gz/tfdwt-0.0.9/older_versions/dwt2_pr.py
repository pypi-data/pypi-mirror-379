import os
import sys
from pathlib import Path
import tensorflow as tf
from TFDWT.DWT2DFB import DWT2D, IDWT2D


def dwt2_ml(x: tf.Tensor, level: int = 3, wave: str = 'haar'):
    """Multilevel 2D DWT (analysis) using TFDWT layers.

    Returns a list of subbands ordered as: [H1, H2, ..., Hn, Ln],
    where each Hi is the concatenated highpass subbands at level i and Ln is the final lowpass.

    Perfect reconstruction is achieved by passing the returned list into idwt2_ml.
    """
    subbands = []
    current = x
    channels_in = x.shape[-1]

    for _ in range(level):
        w = DWT2D(wave=wave)(current)
        lowpass = w[:, :, :, :channels_in]
        highpass = w[:, :, :, channels_in:]
        subbands.append(highpass)
        current = lowpass
    subbands.append(current)
    return subbands


def idwt2_ml(subbands, wave: str = 'haar') -> tf.Tensor:
    """Multilevel 2D IDWT (synthesis) for the companion dwt2_ml output.

    Input subbands should be ordered as returned by dwt2_ml: [H1, H2, ..., Hn, Ln].
    """
    *highpasses, lowpass = subbands  # unpack: [H1, H2, ..., Hn, Ln]

    current = lowpass
    for H in reversed(highpasses):
        current = IDWT2D(wave=wave)(tf.concat([current, H], axis=-1))
    return current


def _self_test_pr(batch: int = 1, N: int = 256, C: int = 1, level: int = 3, wave: str = 'haar'):
    """Run a quick perfect-reconstruction check and print diagnostics."""
    # Optional: force CPU to avoid GPU nondeterminism in CI
    os.environ.setdefault("CUDA_VISIBLE_DEVICES", "-1")

    x = tf.random.normal((batch, N, N, C))
    subs = dwt2_ml(x, level=level, wave=wave)
    x_rec = idwt2_ml(subs, wave=wave)

    max_err = float(tf.reduce_max(tf.abs(x - x_rec)).numpy())
    pr_ok = bool(max_err <= 1e-5)

    print("levels:", level, "wave:", wave)
    print("subbands shapes:", [tuple(s.shape) for s in subs])
    print("max abs error:", max_err)
    print("PR ok (atol=1e-5):", pr_ok)

    return max_err, pr_ok


if __name__ == '__main__':
    # Allow running directly: ensure package root (TFDWT.pypi) is on sys.path
    here = Path(__file__).resolve()
    pkg_root = here.parents[2]  # .../TFDWT.pypi
    if str(pkg_root) not in sys.path:
        sys.path.insert(0, str(pkg_root))

    # Example run
    err, ok = _self_test_pr(batch=1, N=256, C=2, level=3, wave='haar')
    if not ok:
        raise SystemExit(f"Perfect reconstruction check failed (max error {err})")
