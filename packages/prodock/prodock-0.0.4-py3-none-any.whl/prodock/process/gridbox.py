"""
prodock.process.gridbox.py

Utilities to compute docking grid boxes from ligand coordinates.

This module provides the GridBox class which supports loading ligands
(from file-path or pasted block), building grid boxes (padding, scaling,
isotropic/cubic), snapping/rounding, presets, Vina config import/export,
and simple summaries.

Dependencies
------------
- numpy
- rdkit

Example
-------
A minimal usage example:

.. code-block:: python

    from gridbox import GridBox
    gb = (
        GridBox()
        .load_ligand("lig.sdf", fmt="sdf")
        .from_ligand_pad(pad=4.0, isotropic=True)
    )
    print(gb.vina_dict)
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional, Tuple, Union, Dict, Iterable
import numpy as np
from rdkit import Chem
from prodock.io.parser import (
    _parse_sdf_text,
    _parse_pdb_text,
    _parse_mol2_text,
    _parse_xyz_text,
)


# -------------------------
# Helpers
# -------------------------
def _is_pathlike(x: Union[str, Path]) -> bool:
    """
    Return True if x refers to an existing path.

    :param x: candidate path-like object or string
    :type x: str or pathlib.Path
    :return: True if path exists on filesystem, False otherwise
    :rtype: bool
    """
    try:
        return Path(str(x)).exists()
    except Exception:
        return False


def _coords_from_mol(mol: Chem.Mol) -> np.ndarray:
    """
    Return (N,3) numpy array of atom coordinates for an RDKit mol.

    :param mol: RDKit molecule containing at least one conformer
    :type mol: rdkit.Chem.rdchem.Mol
    :return: array of shape (n_atoms, 3) with x,y,z coordinates
    :rtype: numpy.ndarray
    :raises ValueError: if the molecule has no conformers
    """
    conf = mol.GetConformer()
    n = mol.GetNumAtoms()
    return np.array(
        [
            [
                conf.GetAtomPosition(i).x,
                conf.GetAtomPosition(i).y,
                conf.GetAtomPosition(i).z,
            ]
            for i in range(n)
        ],
        dtype=float,
    )


def _gb_coords_from_mol(mol: Chem.Mol, heavy_only: bool = False) -> np.ndarray:
    """
    Return coordinates as an (M,3) array optionally considering heavy atoms only.

    If no atoms remain after filtering (e.g., all H and heavy_only=True),
    falls back to returning coordinates for all atoms.

    :param mol: RDKit molecule with conformer
    :type mol: rdkit.Chem.rdchem.Mol
    :param heavy_only: if True, exclude hydrogen atoms (atomic number 1)
    :type heavy_only: bool
    :return: numpy array of coordinates used for bounding calculations
    :rtype: numpy.ndarray
    """
    conf = mol.GetConformer()
    out = []
    for i in range(mol.GetNumAtoms()):
        if heavy_only and mol.GetAtomWithIdx(i).GetAtomicNum() == 1:
            continue
        p = conf.GetAtomPosition(i)
        out.append((p.x, p.y, p.z))
    if not out:
        # fallback to all atoms
        for i in range(mol.GetNumAtoms()):
            p = conf.GetAtomPosition(i)
            out.append((p.x, p.y, p.z))
    return np.asarray(out, dtype=float)


def _round_tuple(t: Iterable[float], nd: int) -> Tuple[float, float, float]:
    """
    Round a 3-tuple to nd decimals.

    :param t: iterable of three float-like values
    :type t: Iterable[float]
    :param nd: number of decimal places
    :type nd: int
    :return: rounded 3-tuple
    :rtype: tuple
    """
    a, b, c = t
    return float(round(a, nd)), float(round(b, nd)), float(round(c, nd))


def _snap_val(v: float, step: float) -> float:
    """
    Snap a scalar to nearest multiple of step.

    :param v: input value
    :type v: float
    :param step: snapping step
    :type step: float
    :return: snapped value
    :rtype: float
    """
    return float(round(v / step) * step)


def _snap_tuple(t: Iterable[float], step: float) -> Tuple[float, float, float]:
    """
    Snap a 3-tuple to nearest multiples of step.

    :param t: iterable of three values
    :type t: Iterable[float]
    :param step: snap step
    :type step: float
    :return: snapped tuple
    :rtype: tuple
    """
    a, b, c = t
    return _snap_val(a, step), _snap_val(b, step), _snap_val(c, step)


def _ensure_pos_size(size: Iterable[float]) -> Tuple[float, float, float]:
    """
    Validate and cast size components to positive floats.

    :param size: iterable of three numeric values
    :type size: Iterable[float]
    :return: validated positive size tuple
    :rtype: tuple
    :raises ValueError: if any component is <= 0
    """
    sx, sy, sz = tuple(float(x) for x in size)
    if sx <= 0 or sy <= 0 or sz <= 0:
        raise ValueError("All size components must be positive.")
    return sx, sy, sz


# -------------------------
# GridBox
# -------------------------
class GridBox:
    """
    Compute and represent a docking grid box.

    Builders return ``self`` so calls can be chained. Use properties to
    retrieve computed values.

    :param mol: optional RDKit Mol object to initialize with.
    :type mol: rdkit.Chem.Mol or None

    Example
    -------

    .. code-block:: python

        from gridbox import GridBox
        gb = GridBox().load_ligand("ligand.sdf", fmt="sdf").from_ligand_pad(pad=4.0)
        print(gb.summary())
    """

    def __init__(self, mol: Optional[Chem.Mol] = None) -> None:
        self._mol: Optional[Chem.Mol] = mol
        self._center: Optional[Tuple[float, float, float]] = None
        self._size: Optional[Tuple[float, float, float]] = None

    # -------------------------
    # Loading
    # -------------------------
    def load_ligand(
        self, data: Union[str, Path], fmt: Optional[str] = None
    ) -> "GridBox":
        """
        Load ligand from a path or raw text block.

        Supported formats: 'sdf', 'pdb', 'mol2', 'xyz'.

        :param data: Path or raw text containing molecule data.
        :type data: str or pathlib.Path
        :param fmt: Optional format hint. If None and `data` is a path, infer from suffix.
        :type fmt: str or None
        :return: self (builder)
        :rtype: GridBox
        :raises ValueError: if parsing fails or unsupported format supplied
        """
        # obtain text (from file path or raw string)
        if _is_pathlike(data):
            text = Path(str(data)).read_text()
            if fmt is None and Path(str(data)).suffix:
                fmt = Path(str(data)).suffix.lstrip(".").lower()
        else:
            text = str(data)

        fmt = (fmt or "sdf").lower()

        # dispatch to small parser helpers
        parsers = {
            "sdf": _parse_sdf_text,
            "pdb": _parse_pdb_text,
            "mol2": _parse_mol2_text,
            "xyz": _parse_xyz_text,
        }

        parser = parsers.get(fmt)
        if parser is None:
            raise ValueError(f"Unsupported ligand format: {fmt}")

        mol = parser(text)
        if mol is None:
            # format-specific error messages roughly match prior behavior
            if fmt == "sdf":
                raise ValueError("No valid molecule found in SDF content.")
            elif fmt == "pdb":
                raise ValueError("Failed to parse PDB content for ligand.")
            elif fmt == "mol2":
                raise ValueError(
                    "Failed to parse MOL2 content (RDKit build may lack MOL2 support)."
                )
            else:  # xyz or unknown fallback
                raise ValueError(f"Failed to parse {fmt.upper()} content.")

        self._mol = mol
        return self

    # -------------------------
    # Builders
    # -------------------------
    def from_ligand_pad(
        self,
        pad: Union[float, Tuple[float, float, float]] = 4.0,
        isotropic: bool = False,
        min_size: Union[float, Tuple[float, float, float]] = 0.0,
    ) -> "GridBox":
        """
        Center on ligand bounding-box center and expand by padding.

        :param pad: padding in Å (scalar or (x,y,z)).
        :type pad: float or tuple
        :param isotropic: if True, use the maximum span and make cubic box.
        :type isotropic: bool
        :param min_size: enforce minimum edge lengths (scalar or triple).
        :type min_size: float or tuple
        :return: self
        :rtype: GridBox
        :raises ValueError: if no ligand loaded
        """
        if self._mol is None:
            raise ValueError("No ligand loaded. Call load_ligand() first.")

        xyz = _coords_from_mol(self._mol)
        xyz_min = xyz.min(axis=0)
        xyz_max = xyz.max(axis=0)
        center = (xyz_min + xyz_max) / 2.0
        span = xyz_max - xyz_min

        if isotropic:
            base = float(np.max(span))
            size = np.array([base, base, base], dtype=float)
        else:
            size = span.astype(float)

        pad_vec = (
            np.array([pad, pad, pad], dtype=float)
            if isinstance(pad, (int, float))
            else np.array(pad, dtype=float)
        )
        size = size + 2.0 * pad_vec

        min_vec = (
            np.array([min_size, min_size, min_size], dtype=float)
            if isinstance(min_size, (int, float))
            else np.array(min_size, dtype=float)
        )
        size = np.maximum(size, min_vec)

        self._center = (
            float(np.round(center[0], 3)),
            float(np.round(center[1], 3)),
            float(np.round(center[2], 3)),
        )
        self._size = (
            float(np.round(size[0], 3)),
            float(np.round(size[1], 3)),
            float(np.round(size[2], 3)),
        )
        return self

    def from_ligand_scale(
        self, scale: float = 1.5, isotropic: bool = False
    ) -> "GridBox":
        """
        Center on ligand bounding-box center and scale the span by factor.

        :param scale: multiplier applied to ligand bounding span.
        :type scale: float
        :param isotropic: if True use cubic box with max-axis * scale.
        :type isotropic: bool
        :return: self
        :rtype: GridBox
        :raises ValueError: if no ligand loaded
        """
        if self._mol is None:
            raise ValueError("No ligand loaded. Call load_ligand() first.")
        xyz = _coords_from_mol(self._mol)
        xyz_min = xyz.min(axis=0)
        xyz_max = xyz.max(axis=0)
        center = (xyz_min + xyz_max) / 2.0
        span = xyz_max - xyz_min

        if isotropic:
            base = float(np.max(span)) * scale
            size = np.array([base, base, base], dtype=float)
        else:
            size = span * float(scale)

        self._center = (
            float(np.round(center[0], 3)),
            float(np.round(center[1], 3)),
            float(np.round(center[2], 3)),
        )
        self._size = (
            float(np.round(size[0], 3)),
            float(np.round(size[1], 3)),
            float(np.round(size[2], 3)),
        )
        return self

    def from_center_size(
        self, center: Tuple[float, float, float], size: Tuple[float, float, float]
    ) -> "GridBox":
        """
        Set the box explicitly from numeric center and size.

        :param center: (x,y,z) center in Å.
        :type center: tuple
        :param size: (w,h,d) size in Å.
        :type size: tuple
        :return: self
        :rtype: GridBox
        :raises ValueError: if any size component <= 0
        """
        if any(s <= 0 for s in size):
            raise ValueError("All size components must be positive.")
        self._center = (float(center[0]), float(center[1]), float(center[2]))
        self._size = (float(size[0]), float(size[1]), float(size[2]))
        return self

    def from_ligand_pad_adv(
        self,
        pad: Union[float, tuple[float, float, float]] = 4.0,
        isotropic: bool = False,
        min_size: Union[float, tuple[float, float, float]] = 0.0,
        *,
        heavy_only: bool = False,
        snap_step: Optional[float] = None,
        round_ndigits: int = 3,
    ) -> "GridBox":
        """
        Advanced builder with additional options.

        :param pad: padding in Å (scalar or triple).
        :type pad: float or tuple
        :param isotropic: cubic box if True.
        :type isotropic: bool
        :param min_size: minimal edge length (scalar or triple).
        :type min_size: float or tuple
        :param heavy_only: compute spans using heavy atoms only (exclude H).
        :type heavy_only: bool
        :param snap_step: if provided, snap center/size to multiples of this step.
        :type snap_step: float or None
        :param round_ndigits: decimals to round to for final numbers.
        :type round_ndigits: int
        :return: self
        :rtype: GridBox
        :raises ValueError: if no ligand loaded
        """
        if self._mol is None:
            raise ValueError("No ligand loaded. Call load_ligand() first.")
        xyz = _gb_coords_from_mol(self._mol, heavy_only=heavy_only)
        xyz_min = xyz.min(axis=0)
        xyz_max = xyz.max(axis=0)
        center = (xyz_min + xyz_max) / 2.0
        span = xyz_max - xyz_min

        if isotropic:
            base = float(np.max(span))
            size = np.array([base, base, base], dtype=float)
        else:
            size = span.astype(float)

        pad_vec = (
            np.array([pad, pad, pad], dtype=float)
            if isinstance(pad, (int, float))
            else np.array(pad, dtype=float)
        )
        size = size + 2.0 * pad_vec

        min_vec = (
            np.array([min_size, min_size, min_size], dtype=float)
            if isinstance(min_size, (int, float))
            else np.array(min_size, dtype=float)
        )
        size = np.maximum(size, min_vec)

        center_t = (float(center[0]), float(center[1]), float(center[2]))
        size_t = (float(size[0]), float(size[1]), float(size[2]))

        if snap_step:
            center_t = _snap_tuple(center_t, snap_step)
            size_t = _snap_tuple(size_t, snap_step)

        self._center = _round_tuple(center_t, round_ndigits)
        self._size = _ensure_pos_size(_round_tuple(size_t, round_ndigits))
        return self

    def preset(
        self,
        mode: str = "safe",
        *,
        heavy_only: bool = False,
        snap_step: Optional[float] = 0.25,
        round_ndigits: int = 3,
    ) -> "GridBox":
        """
        Convenience presets for common workflows.

        :param mode: one of 'tight', 'safe', 'vina24'
        :type mode: str
        :param heavy_only: use heavy atoms only for span computation.
        :type heavy_only: bool
        :param snap_step: snap step for center/size rounding.
        :type snap_step: float or None
        :param round_ndigits: decimal places to round result to.
        :type round_ndigits: int
        :return: self
        :rtype: GridBox
        :raises ValueError: if unknown preset requested
        """
        mode = mode.lower()
        if mode == "tight":
            kwargs = dict(pad=3.0, isotropic=False, min_size=0.0)
        elif mode == "safe":
            kwargs = dict(pad=4.0, isotropic=True, min_size=22.5)
        elif mode in ("vina24", "cube24", "vina"):
            kwargs = dict(pad=2.0, isotropic=True, min_size=24.0)
        else:
            raise ValueError(f"Unknown preset: {mode}")
        return self.from_ligand_pad_adv(
            **kwargs,
            heavy_only=heavy_only,
            snap_step=snap_step,
            round_ndigits=round_ndigits,
        )

    def snap(self, step: float = 0.25, round_ndigits: int = 3) -> "GridBox":
        """
        Snap current center/size to a grid and round.

        :param step: grid step to snap to (Å).
        :type step: float
        :param round_ndigits: decimals to round to after snapping.
        :type round_ndigits: int
        :return: self
        :rtype: GridBox
        :raises ValueError: if center/size not computed yet
        """
        cx, cy, cz = self.center
        sx, sy, sz = self.size
        self._center = _round_tuple(_snap_tuple((cx, cy, cz), step), round_ndigits)
        self._size = _ensure_pos_size(
            _round_tuple(_snap_tuple((sx, sy, sz), step), round_ndigits)
        )
        return self

    # -------------------------
    # Properties / Export
    # -------------------------
    @property
    def center(self) -> Tuple[float, float, float]:
        """
        Get computed center.

        :return: (x, y, z) center in Å.
        :rtype: tuple
        :raises ValueError: if center not computed yet
        """
        if self._center is None:
            raise ValueError(
                "Center not computed yet. Use a builder (e.g., from_ligand_pad())."
            )
        return self._center

    @property
    def size(self) -> Tuple[float, float, float]:
        """
        Get computed size.

        :return: (w, h, d) in Å.
        :rtype: tuple
        :raises ValueError: if size not computed yet
        """
        if self._size is None:
            raise ValueError(
                "Size not computed yet. Use a builder (e.g., from_ligand_pad())."
            )
        return self._size

    @property
    def vina_dict(self) -> Dict[str, float]:
        """
        Return a dictionary ready to be written into a Vina config.

        :return: dict with keys center_x/.. and size_x/..
        :rtype: dict
        :raises ValueError: if center/size not computed yet
        """
        cx, cy, cz = self.center
        sx, sy, sz = self.size
        return {
            "center_x": float(cx),
            "center_y": float(cy),
            "center_z": float(cz),
            "size_x": float(sx),
            "size_y": float(sy),
            "size_z": float(sz),
        }

    def to_vina_lines(self, fmt: str = "{k} = {v:.3f}") -> str:
        """
        Compose Vina config snippet.

        :param fmt: per-line format string (receives k and v).
        :type fmt: str
        :return: multiline string
        :rtype: str
        """
        d = self.vina_dict
        return "\n".join(fmt.format(k=k, v=v) for k, v in d.items())

    def to_vina_file(self, path: Union[str, Path]) -> Path:
        """
        Write Vina snippet to a file.

        :param path: destination path.
        :type path: str or pathlib.Path
        :return: path written
        :rtype: pathlib.Path
        """
        p = Path(path)
        p.write_text(self.to_vina_lines() + "\n")
        return p

    @property
    def volume(self) -> float:
        """
        Return the box volume in Å^3.

        :return: volume
        :rtype: float
        """
        sx, sy, sz = self.size
        return float(sx * sy * sz)

    def summary(self) -> str:
        """
        Return a short human-readable summary.

        :return: summary string
        :rtype: str
        """
        cx, cy, cz = self.center
        sx, sy, sz = self.size
        return (
            f"center=({cx:.3f}, {cy:.3f}, {cz:.3f}) | "
            f"size=({sx:.3f}, {sy:.3f}, {sz:.3f}) | "
            f"volume={self.volume:.1f} Å^3"
        )

    # -------------------------
    # Vina config parsing
    # -------------------------
    @staticmethod
    def parse_vina_cfg(text: str) -> Dict[str, float]:
        """
        Parse a Vina-style config text into a dict.

        Accepts lines like:
            center_x = 10.5
            size_x  20

        :param text: config text
        :type text: str
        :return: dict with 6 keys: center_x/y/z and size_x/y/z
        :rtype: dict
        :raises ValueError: if keys are missing from parsed content
        """
        out: Dict[str, float] = {}
        keys = {"center_x", "center_y", "center_z", "size_x", "size_y", "size_z"}
        for raw in text.splitlines():
            line = raw.split("#", 1)[0].strip()
            if not line:
                continue
            parts = [p.strip() for p in line.replace("=", " ").split()]
            if len(parts) != 2:
                continue
            k, v = parts
            if k in keys:
                try:
                    out[k] = float(v)
                except ValueError:
                    pass
        missing = keys - set(out)
        if missing:
            raise ValueError(f"Missing keys in cfg: {sorted(missing)}")
        return out

    @staticmethod
    def from_vina_cfg(text: str) -> "GridBox":
        """
        Construct GridBox from a Vina config snippet.

        :param text: Vina config text
        :type text: str
        :return: GridBox with center/size set
        :rtype: GridBox
        :raises ValueError: if parsing fails or keys are missing
        """
        d = GridBox.parse_vina_cfg(text)
        gb = GridBox().from_center_size(
            (d["center_x"], d["center_y"], d["center_z"]),
            (d["size_x"], d["size_y"], d["size_z"]),
        )
        return gb

    def as_tuple(self) -> Tuple[Tuple[float, float, float], Tuple[float, float, float]]:
        """
        Return (center, size) as tuples.

        :return: (center, size)
        :rtype: tuple
        """
        return self.center, self.size

    def __repr__(self) -> str:
        return f"<GridBox center={getattr(self,'_center',None)} size={getattr(self,'_size',None)}>"
