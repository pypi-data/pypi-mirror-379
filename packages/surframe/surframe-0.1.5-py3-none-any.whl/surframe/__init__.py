# __init__.py — Core estable + PRO lazy
from .io import *  # Core (como ya lo tenías)
from .manifest import *  # si aplica en tu Core
# ... (otros exports Core que ya estuvieran)

# Gating PRO (no fatal)
try:
    from .license import is_pro_enabled
except Exception:
    def is_pro_enabled(*args, **kwargs):  # fallback ultra seguro
        return False

# Exponer wrappers lazy solo si el usuario los llama (evita fallos en import global)
def learn_ucodec(*args, **kwargs):
    if not is_pro_enabled("ucodec"):
        raise RuntimeError("SURFRAME PRO requerido: feature 'ucodec' no habilitada.")
    from .ucodec.learn import learn_ucodec as _impl
    return _impl(*args, **kwargs)

def reencode_ucodec(*args, **kwargs):
    if not is_pro_enabled("ucodec"):
        raise RuntimeError("SURFRAME PRO requerido: feature 'ucodec' no habilitada.")
    from .ucodec.reencode import reencode_ucodec as _impl
    return _impl(*args, **kwargs)

def zorder_optimize(*args, **kwargs):
    if not is_pro_enabled("zopt"):
        raise RuntimeError("SURFRAME PRO requerido: feature 'zopt' no habilitada.")
    from .ucodec.layout import zorder_optimize as _impl
    return _impl(*args, **kwargs)

def tier_plan(*args, **kwargs):
    if not is_pro_enabled("tier"):
        raise RuntimeError("SURFRAME PRO requerido: feature 'tier' no habilitada.")
    from .ucodec.tier import tier_plan as _impl
    return _impl(*args, **kwargs)

__all__ = [
    # core exports ya existentes...
    "learn_ucodec","reencode_ucodec","zorder_optimize","tier_plan","is_pro_enabled"
]
from .ann import ann_build, ann_query
try:
    __all__.extend(["ann_build","ann_query"])
except NameError:
    __all__ = ["ann_build","ann_query"]

# --- PATCH: public alias vsearch (compat con tests) ---
def vsearch(container, *, col="embedding", query_vec=None, k=5, metric="cosine", where=None, id_col="id", columns=None):
    """
    Alias de búsqueda vectorial:
    - Mantiene la firma esperada por tests (query_vec) y la mapea a ann_query(q=...).
    """
    from .ann import ann_query as _ann_query
    q = query_vec
    return _ann_query(container, col=col, q=q, k=int(k), metric=metric, where=where, id_col=id_col, columns=columns)
# --- END PATCH ---

# --- PATCH: exports for ANN ---
try:
    __all__ += ["ann_build", "ann_query", "vsearch"]
except NameError:
    __all__ = ["ann_build", "ann_query", "vsearch"]
# --- END PATCH ---
