from __future__ import annotations
from dataclasses import dataclass
from typing import Literal, Optional, Tuple
import numpy as np

point_dtype = np.dtype([
    ("x", np.float32),
    ("y", np.float32),
    ("energy", np.float32),
])

@dataclass
class PatternSettings:
    point_distance: float
    type: Literal["square", "triangular", "contour"] = "square"
    offset: float = 0.0
    start_rotation: float = 0.0
    layer_rotation: float = 0.0
    lattice_3d: Optional[Literal["bcc", "fcc", "hcp"]] = None
    layers: int = 1

@dataclass
class PatternData:
    grid: np.ndarray                  # 2D structured array: (total_rows, cols)
    shape: Tuple[int, int]            # (total_rows, cols)  <-- BACKWARD COMPATIBLE
    spacing: float

    @classmethod
    def create_empty(
        cls,
        xmin: float,
        ymin: float,
        xmax: float,
        ymax: float,
        point_distance: float,
        pattern_type: Literal["square", "triangular"] = "square",
        rotation_deg: float = 0.0,
        *,
        lattice_3d: Optional[Literal["bcc", "fcc", "hcp"]] = None,
        layers: int = 1,
        layer_rotation: float = 0.0,
    ) -> "PatternData":

        cx = np.float32((xmin + xmax) / 2.0)
        cy = np.float32((ymin + ymax) / 2.0)

        def rotmat32(deg: float) -> np.ndarray:
            th = np.deg2rad(deg).astype(np.float32)
            c = np.cos(th, dtype=np.float32)
            s = np.sin(th, dtype=np.float32)
            return np.array([[c, -s],[s, c]], dtype=np.float32)

        base_R = rotmat32(rotation_deg)

        # Rotate bbox to compute extents in rotated frame (float32)
        corners = np.array([[xmin, ymin],
                            [xmin, ymax],
                            [xmax, ymin],
                            [xmax, ymax]], dtype=np.float32).T
        centered = corners - np.array([[cx],[cy]], dtype=np.float32)
        rot_corners = base_R @ centered + np.array([[cx],[cy]], dtype=np.float32)
        rxmin, rxmax = rot_corners[0].min(), rot_corners[0].max()
        rymin, rymax = rot_corners[1].min(), rot_corners[1].max()
        width, height = rxmax - rxmin, rymax - rymin

        a = np.float32(point_distance)

        # --- build base layer in rotated frame (vectorized) ---
        def make_square_layer32(pitch: np.float32):
            cols = int(np.floor(width  / pitch)) + 1
            rows = int(np.floor(height / pitch)) + 1
            xs = rxmin + np.arange(cols, dtype=np.float32) * pitch
            ys = rymin + np.arange(rows, dtype=np.float32) * pitch
            X, Y = np.meshgrid(xs, ys, indexing="xy")
            return X, Y

        def make_triangular_layer32(pitch: np.float32):
            cols = int(np.floor(width / pitch)) + 1
            row_h = np.float32(pitch * np.sqrt(3.0) / 2.0)
            rows = int(np.floor(height / row_h)) + 1
            c = np.arange(cols, dtype=np.float32)[None, :]                  # (1, cols)
            r = np.arange(rows, dtype=np.float32)[:, None]                  # (rows, 1)
            offsets = ((r % 2.0) * (pitch * 0.5)).astype(np.float32)        # (rows,1)
            X = rxmin + offsets + c * pitch                                 # (rows, cols)
            Y = rymin + r * row_h                                           # (rows, cols)
            return X, Y

        if (lattice_3d in {"fcc", "hcp"}) or (lattice_3d is None and pattern_type == "triangular"):
            X0, Y0 = make_triangular_layer32(a)
        else:
            X0, Y0 = make_square_layer32(a)

        rows, cols = X0.shape

        # --- stacking offsets defined in *rotated* frame ---
        a1 = np.array([a, 0.0], dtype=np.float32)
        a2 = np.array([a*0.5, a*np.float32(np.sqrt(3.0)/2.0)], dtype=np.float32)
        def tri_offset(u: float, v: float) -> np.ndarray:
            return (u * a1 + v * a2).astype(np.float32)

        if lattice_3d == "hcp":      # ABAB
            seq = [np.array([0.0, 0.0], dtype=np.float32), tri_offset(1/3, 2/3)]
        elif lattice_3d == "fcc":    # ABC
            seq = [np.array([0.0, 0.0], dtype=np.float32),
                tri_offset(1/3, 2/3),
                tri_offset(2/3, 1/3)]
        elif lattice_3d == "bcc":    # square, half-cell
            seq = [np.array([0.0, 0.0], dtype=np.float32), np.array([a*0.5, a*0.5], dtype=np.float32)]
        else:
            seq = [np.array([0.0, 0.0], dtype=np.float32)]
        period = len(seq)

        L = max(1, int(layers))

        # Precompute base global coords once (layer 0, no per-layer rotation)
        pts0 = np.vstack((X0.ravel(), Y0.ravel())).astype(np.float32)             # (2, N)
        centered0 = pts0 - np.array([[cx],[cy]], dtype=np.float32)
        inv_base = base_R.T                                                        # orthonormal inverse
        base_global = inv_base @ centered0 + np.array([[cx],[cy]], dtype=np.float32)
        Xg0 = base_global[0].reshape(rows, cols)
        Yg0 = base_global[1].reshape(rows, cols)

        # Allocate final grid (stack layers along row axis)
        grid = np.zeros((rows * L, cols), dtype=point_dtype)

        if layer_rotation == 0.0:
            # ---- FAST PATH ----
            # Convert each rotated-frame offset to global frame once, then just add constants.
            seq_global = []
            for off in seq:
                off_global = inv_base @ off.reshape(2,1)  # (2,1)
                seq_global.append(off_global.ravel().astype(np.float32))

            for li in range(L):
                dx, dy = seq_global[li % period]
                r0 = li * rows
                r1 = r0 + rows
                grid[r0:r1, :]["x"] = (Xg0 + dx).astype(np.float32)
                grid[r0:r1, :]["y"] = (Yg0 + dy).astype(np.float32)
                grid[r0:r1, :]["energy"] = 0.0
        else:
            # ---- GENERAL PATH (still vectorized, but per-layer rotation needed) ----
            for li in range(L):
                R_layer = rotmat32(rotation_deg + np.float32(li * layer_rotation))
                off = seq[li % period].reshape(2,1).astype(np.float32)
                pts = (np.vstack((X0.ravel(), Y0.ravel())).astype(np.float32) + off)
                centered_pts = pts - np.array([[cx],[cy]], dtype=np.float32)
                XY = R_layer.T @ centered_pts + np.array([[cx],[cy]], dtype=np.float32)
                Xg = XY[0].reshape(rows, cols)
                Yg = XY[1].reshape(rows, cols)
                r0 = li * rows
                r1 = r0 + rows
                grid[r0:r1, :]["x"] = Xg
                grid[r0:r1, :]["y"] = Yg
                grid[r0:r1, :]["energy"] = 0.0

        return cls(grid=grid, shape=grid.shape, spacing=float(a))
