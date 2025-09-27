# pawtorch/_patch.py
from __future__ import annotations
import sys
import types

def activate() -> None:
    """
    Import-time activator. After `import pawtorch`, the following are available:
      - Module aliases: paw, paw.nyanya, paw.cuda, paw.autoscratch, paw.scatter_treats, paw.optimeowzer
      - Extra module: zoomies with zoomies.nyavailable()
      - Methods/properties patched onto torch.nn.Module and torch.Tensor
    """
    try:
        import torch as _torch
        import torch.nn as _nn
    except Exception as e:
        raise RuntimeError(
            "pawtorch requires PyTorch. Please install torch first, e.g. `pip install torch`."
        ) from e

    # --- Create the 'paw' module shim ---
    paw = types.ModuleType("paw")
    paw.__doc__ = "Cat-themed alias facade over torch."

    # Core module aliases
    # torch → paw
    # torch.nn → paw.nyanya
    # torch.cuda → paw.cuda
    # torch.autograd → paw.autoscratch
    sys.modules["paw"] = paw
    sys.modules["paw.nyanya"] = _nn
    sys.modules["paw.cuda"] = _torch.cuda
    sys.modules["paw.autoscratch"] = _torch.autograd
    sys.modules["paw.scatter_treats"] = _torch.distributions
    sys.modules["paw.optimeowzer"] = _torch.optim

    # zoomies.nyavailable() (maps to cuda.is_available())
    zoomies = types.ModuleType("zoomies")
    def nyavailable() -> bool:
        return _torch.cuda.is_available()
    zoomies.nyavailable = nyavailable  # type: ignore[attr-defined]
    sys.modules["zoomies"] = zoomies

    # "cpu" → "nap_spot" (string constant)
    paw.nap_spot = "cpu"  # type: ignore[attr-defined]

    # torch.device() → paw.spot()
    paw.spot = _torch.device  # type: ignore[attr-defined]

    # Tensors
    paw.Yarn = _torch.Tensor            # torch.Tensor → paw.Yarn
    paw.yarn = _torch.tensor            # torch.tensor(...) → paw.yarn(...)

    # Utilities
    paw.bury   = _torch.save            # torch.save() → paw.bury()
    paw.dig_up = _torch.load            # torch.load() → paw.dig_up()
    paw.no_scritches = _torch.no_grad   # with torch.no_grad(): → with paw.no_scritches():
    paw.meownual_seed = _torch.manual_seed  # manual_seed() → meownual_seed()
    paw.cat = _torch.cat                # keep cat as cat
    paw.meowtmul = _torch.matmul        # matmul → meowtmul

    # stack() → paw.catpile()
    # NOTE: name collision with torch.multiprocessing → paw.catpile (module).
    # We must choose one. By default we expose the *module* at paw.catpile (per your spec),
    # and provide the stack alias as paw.catpile_stack().
    paw.catpile_stack = _torch.stack    # stack → catpile_stack()
    # torch.multiprocessing → paw.catpile (module alias)
    sys.modules["paw.catpile"] = _torch.multiprocessing

    # expand() → stretchies()
    def _stretchies(x: _torch.Tensor, *sizes):
        return x.expand(*sizes)
    paw.stretchies = _stretchies  # type: ignore[attr-defined]

    # --------- Patch nn.Module methods ---------
    def _mod_sniff(self):               # .eval() → .sniff()
        return self.eval()
    def _mod_whiskers(self):            # .parameters() → .whiskers()
        return self.parameters()
    def _mod_treats(self):              # .state_dict() → .treats()
        return self.state_dict()
    def _mod_nom_treats(self, *a, **kw):  # .load_state_dict() → .nom_treats()
        return self.load_state_dict(*a, **kw)
    def _mod_clean_paws(self):          # .zero_grad() → .clean_paws()
        return self.zero_grad()

    _nn.Module.sniff = _mod_sniff               # type: ignore[attr-defined]
    _nn.Module.whiskers = _mod_whiskers         # type: ignore[attr-defined]
    _nn.Module.treats = _mod_treats             # type: ignore[attr-defined]
    _nn.Module.nom_treats = _mod_nom_treats     # type: ignore[attr-defined]
    _nn.Module.clean_paws = _mod_clean_paws     # type: ignore[attr-defined]
    # .train() stays .train()

    # --------- Patch optim.Optimizer methods ---------
    # optimizer → optimeowzer (module alias already); methods:
    import torch.optim as _optim
    def _opt_pounce(self, *a, **kw):            # optimizer.step() → optimeowzer.pounce()
        return self.step(*a, **kw)
    def _opt_clean_paws(self):                   # optimizer.zero_grad() → optimeowzer.clean_paws()
        return self.zero_grad()
    _optim.Optimizer.pounce = _opt_pounce        # type: ignore[attr-defined]
    _optim.Optimizer.clean_paws = _opt_clean_paws  # type: ignore[attr-defined]

    # --------- Patch torch.autograd (module alias is paw.autoscratch) ---------
    # autograd.backward() → autoscratch.backward() (covered by alias)

    # --------- Patch Tensor methods/properties ---------
    T = _torch.Tensor

    # .detach() → .slink_away()
    T.slink_away = T.detach  # type: ignore[attr-defined]
    # .clone() → .litter_copy()
    T.litter_copy = T.clone  # type: ignore[attr-defined]
    # loss.backward() → loss.hissback()
    def _ten_hissback(self, *a, **kw):
        return self.backward(*a, **kw)
    T.hissback = _ten_hissback  # type: ignore[attr-defined]

    # .grad_fn → .scratch_fn (property alias)
    try:
        scratch_fn = property(fget=lambda self: self.grad_fn)
        setattr(T, "scratch_fn", scratch_fn)
    except Exception:
        pass

    # .requires_grad → .needs_scritchies (property alias)
    try:
        needs_scritchies = property(
            fget=lambda self: self.requires_grad,
            fset=lambda self, v: setattr(self, "requires_grad", v),
        )
        setattr(T, "needs_scritchies", needs_scritchies)
    except Exception:
        pass

    # --------- Layers in paw.nyanya ---------
    ny = sys.modules["paw.nyanya"]
    # nn.Linear → nyanya.linear
    setattr(ny, "linear", _nn.Linear)
    # nn.Conv2d → nyanya.PawPrint2d
    setattr(ny, "PawPrint2d", _nn.Conv2d)
    # nn.ReLU → nyanya.ReLuv
    setattr(ny, "ReLuv", _nn.ReLU)
    # nn.Dropout → nyanya.HideNSeek
    setattr(ny, "HideNSeek", _nn.Dropout)
    # nn.Softmax → nyanya.Softmax
    setattr(ny, "Softmax", _nn.Softmax)
    # nn.LayerNorm → nyanya.Grooming
    setattr(ny, "Grooming", _nn.LayerNorm)

    # final: bind convenience names onto 'paw' for discoverability
    paw.nyanya = ny                     # type: ignore[attr-defined]
    paw.cuda = _torch.cuda              # type: ignore[attr-defined]
    paw.autoscratch = _torch.autograd   # type: ignore[attr-defined]
    paw.scatter_treats = _torch.distributions  # type: ignore[attr-defined]
    paw.optimeowzer = _torch.optim      # type: ignore[attr-defined]

