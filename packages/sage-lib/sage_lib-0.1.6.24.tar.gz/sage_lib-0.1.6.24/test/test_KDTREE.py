import numpy as np
from scipy.spatial import cKDTree
import itertools

# --- Paste your PeriodicCKDTree class here ---
import numpy as np
import itertools
from scipy.spatial import cKDTree

class PeriodicCKDTree(cKDTree):
    """
    cKDTree subclass supporting periodic boundary conditions.

    Behaviors:
      - Orthorhombic box (1D bounds) with full periodicity: uses native cKDTree methods.
      - General box (2D bounds matrix): uses query tiling to implement PBC.
    """
    def __init__(self, bounds, data, leafsize=10, pbc=None, force_orth:bool=False):
        data = np.asarray(data, float)
        d    = data.shape[1]

        # Normalize pbc
        if pbc is None:
            pbc = (True,) * d
        elif len(pbc) != d:
            raise ValueError(f"pbc must have length {d}")
        self.pbc = tuple(pbc)

        # Force float-array form
        # Ensure bounds is a float array
        bounds = np.asarray(bounds, float)

        # Determine if we can use the native orthorhombic periodic support
        is_orth = force_orth and ((bounds.ndim==1 and bounds.size==d) \
                  or (bounds.ndim==2 and bounds.shape==(d,d) \
                      and not np.any(np.abs(bounds[~np.eye(d, dtype=bool)])>1e-12)))

        if is_orth and all(self.pbc):
            # Use native cKDTree periodic support for orthorhombic box
            # Orthorhombic periodic box: use native cKDTree periodic support
            box = bounds if bounds.ndim == 1 else np.diag(bounds)
            super().__init__(data, leafsize=leafsize, boxsize=box)
            self._use_native = True
            self.bounds = np.diag(box)
        else:
            # Fallback: plain cKDTree + manual tiling
            # General case: build plain cKDTree on data (no tiling)
            super().__init__(data, leafsize=leafsize)
            self._use_native = False
            if bounds.ndim == 1:
                self.bounds = np.diag(bounds)
            elif bounds.ndim == 2 and bounds.shape == (d, d):
                self.bounds = bounds
            else:
                raise ValueError(f"bounds must be length-{d} or {d}x{d} matrix")

        self._n_orig = data.shape[0]

    def __reduce__(self):
        fn, args, state = super().__reduce__()  
        extra = (self._use_native, self.pbc, self.bounds, self._n_orig)
        return (self.__class__._rebuild, (fn, args, state) + extra)

    @staticmethod
    def _rebuild(fn, args, state, use_native, pbc, bounds, n_orig):
        tree = fn(*args)
        super(PeriodicCKDTree, tree).__setstate__(state)
        tree._use_native = use_native
        tree.pbc          = pbc
        tree.bounds       = bounds
        tree._n_orig      = n_orig
        return tree
    
    @property
    def use_native(self) -> bool:
        """
        Whether this tree is using SciPy’s native periodic-box support
        (True) or the custom tiling implementation (False).
        """
        return self._use_native

    @use_native.setter
    def use_native(self, flag: bool):
        """
        Manually enable or disable native-box support.

        Parameters
        ----------
        flag : bool
            True to force native periodic support; False to force the
            fallback tiling implementation.
        """
        self._use_native = bool(flag)

    def _make_shifts(self, r):
        # Compute integer shifts needed to cover radius r
        lengths = np.linalg.norm(self.bounds, axis=0)
        max_shifts = np.ceil(r / lengths).astype(int)
        axes = [range(-m, m + 1) if p else (0,)
                for m, p in zip(max_shifts, self.pbc)]
        return np.array(list(itertools.product(*axes)), int)

    def query(self, x, k=1, eps=0, p=2, distance_upper_bound=np.inf):
        if self.use_native:
            return super().query(x, k=k, eps=eps, p=p, distance_upper_bound=distance_upper_bound)

        x_arr = np.asarray(x, float)
        single = (x_arr.ndim == 1)
        Q = x_arr.reshape(-1, x_arr.shape[-1])
        d = Q.shape[1]

        # generate shifts for triclinic PBC: {-1,0,1} on periodic axes
        axes = [(-1, 0, 1) if p else (0,) for p in self.pbc]
        shifts_i = np.array(list(itertools.product(*axes)), dtype=int)
        shifts_r = shifts_i.dot(self.bounds)  # shape (S, d), lattice-vector shifts

        # tile queries and run a single kNN on the base tree
        tiledQ = (Q[:, None, :] + shifts_r[None, :, :]).reshape(-1, d)
        dists, idxs = super().query(
            tiledQ, k=k, eps=eps, p=p, distance_upper_bound=distance_upper_bound
        )

        # reshape to (nQ, S*k) and keep best k per original query
        S = shifts_r.shape[0]
        dists = dists.reshape(Q.shape[0], S * k)
        idxs  = idxs.reshape(Q.shape[0], S * k)

        # select top-k along axis=1
        part = np.argpartition(dists, kth=np.minimum(k-1, dists.shape[1]-1), axis=1)[:, :k]
        row_idx = np.arange(Q.shape[0])[:, None]
        d_best = dists[row_idx, part]
        i_best = idxs[row_idx, part]

        # sort those top-k to maintain ascending order
        order = np.argsort(d_best, axis=1)
        d_best = np.take_along_axis(d_best, order, axis=1)
        i_best = np.take_along_axis(i_best, order, axis=1)

        i_best = np.mod(i_best, self._n_orig)

        if single and k == 1:
            return d_best[0, 0], i_best[0, 0]
        if single:
            return d_best[0], i_best[0]
        if k == 1:
            return d_best[:, 0], i_best[:, 0]
        return d_best, i_best

    def query(self, x, k=1, eps=0, p=2, distance_upper_bound=np.inf):
        if self.use_native:
            return super().query(x, k=k, eps=eps, p=p, distance_upper_bound=distance_upper_bound)
        dists, idxs = super().query(x, k=k, eps=eps, p=p, distance_upper_bound=distance_upper_bound)
        return dists, np.mod(idxs, self._n_orig)
        
    def query_ball_point(self, x, r, p=2., eps=0):
        if self.use_native:
            return super().query_ball_point(x, r, p, eps)

        x_arr = np.asarray(x, float)
        single = (x_arr.ndim == 1)
        Q = x_arr.reshape(-1, x_arr.shape[-1])

        shifts_i = self._make_shifts(r)
        shifts_r = shifts_i.dot(self.bounds)
        tiled = (Q[:, None, :] + shifts_r[None, :, :]).reshape(-1, Q.shape[1])
        raw = super().query_ball_point(tiled, r, p, eps)

        raw = np.array(raw, object).reshape(Q.shape[0], -1)
        out = []
        for row in raw:
            idxs = np.concatenate(row) % self._n_orig
            out.append( np.unique(idxs).astype(np.int64) )

        return out[0] if single else out

    def query_ball_tree(self, other, r, p=2., eps=0):
        if self.use_native and getattr(other, 'use_native', False):
            return super().query_ball_tree(other, r, p, eps)
        if not isinstance(other, PeriodicCKDTree):
            raise ValueError("Other tree must be PeriodicCKDTree")
        return other.query_ball_point(self.data, r, p, eps)

    def query_pairs(self, r, p=2., eps=0):
        if self.use_native:
            return super().query_pairs(r, p, eps)
        pairs = set()
        neighbors = self.query_ball_point(self.data, r, p, eps)
        for i, nbrs in enumerate(neighbors):
            for j in nbrs:
                if i < j:
                    pairs.add((i, j))
        return sorted(pairs)

    def count_neighbors(self, other, r, p=2.):
        '''
        if self._use_native and getattr(other, '_use_native', False):
            return super().count_neighbors(other, r, p)
        if not isinstance(other, PeriodicCKDTree):
            raise ValueError("Other tree must be PeriodicCKDTree")
        raw = super().count_neighbors(other, r, p)
        return np.array(raw).reshape(-1, self._n_orig).sum(axis=0)
        '''
        if self.use_native and getattr(other, 'use_native', False):
            return super().count_neighbors(other, r, p)
        if not isinstance(other, PeriodicCKDTree):
            raise ValueError("Other tree must be PeriodicCKDTree")

        counts = np.zeros(other.n, dtype=int)
        for i, point in enumerate(other.data):
            indices = self.query_ball_point(point, r, p)
            counts[i] = len(indices)
            
        return counts

    def sparse_distance_matrix(self, other, max_distance, p=2.):
        if self.use_native and getattr(other, 'use_native', False):
            return super().sparse_distance_matrix(other, max_distance, p)
        if not isinstance(other, PeriodicCKDTree):
            raise ValueError("Other tree must be PeriodicCKDTree")
        raw = super().sparse_distance_matrix(other, max_distance, p)
        result = {}
        for (i_t, j_t), dist in raw.items():
            i, j = i_t % self._n_orig, j_t % other._n_orig
            key = (i, j) if i < j else (j, i)
            if key not in result or dist < result[key]:
                result[key] = dist
        return result

# ----------------------
# Test utilities
# ----------------------
import numpy as np
import itertools
import matplotlib.pyplot as plt

# ---------- Paste your PeriodicCKDTree class definition above this line ----------

# ----------------------
# Helpers
# ----------------------
def triclinic_bounds_2d():
    """
    Simple skewed 2D cell (non-orthogonal). Rows are lattice vectors (a, b).
    """
    a = np.array([1.8, 0.0])
    b = np.array([0.6, 1.4])
    return np.vstack([a, b])  # shape (2,2)

def frac_to_cart(frac, bounds):
    return frac @ bounds

def enumerate_shifts_2d(pbc=(True, True), m=1):
    axes = [range(-m, m+1) if p else (0,) for p in pbc]
    return np.array(list(itertools.product(*axes)), dtype=int)

def min_image_nn(point, data, bounds, pbc=(True,True), m=1):
    """
    Brute-force minimum-image nearest neighbor (index, distance, winning integer shift).
    """
    shifts = enumerate_shifts_2d(pbc, m=m)
    shifts_cart = shifts @ bounds  # (S,2)
    # For each data point, check all images
    best_d = np.inf
    best_i = -1
    best_shift = None
    for i, y in enumerate(data):
        # distances to all images of y
        diffs = point - (y + shifts_cart)
        dists = np.linalg.norm(diffs, axis=1)
        j = np.argmin(dists)
        if dists[j] < best_d:
            best_d = dists[j]
            best_i = i
            best_shift = shifts[j]
    return best_i, best_d, best_shift

def plot_cell_and_images(ax, bounds, m=1, **kw):
    # draw central cell as a polygon and its neighbors
    a, b = bounds[0], bounds[1]
    cell = np.array([[0,0], a, a+b, b, [0,0]])
    for i in range(-m, m+1):
        for j in range(-m, m+1):
            T = i*a + j*b
            poly = cell + T
            ax.plot(poly[:,0], poly[:,1], **kw)

def visualize_mismatch(tree, bounds, data, q, naive_idx, true_idx, true_shift):
    fig, ax = plt.subplots(figsize=(6.0, 6.0))
    ax.set_aspect('equal', adjustable='box')

    # draw unit cell + neighbors
    plot_cell_and_images(ax, bounds, m=1, color='0.8', linewidth=1.0)

    # plot data and query
    ax.scatter(data[:,0], data[:,1], s=20, label='Data', zorder=3)
    ax.scatter([q[0]],[q[1]], marker='*', s=180, color='red', label='Query', zorder=4)

    # naive neighbor (no PBC tiling in query)
    y_naive = data[naive_idx]
    ax.scatter([y_naive[0]],[y_naive[1]], s=80, facecolors='none', edgecolors='orange', linewidths=2.0,
               label='naive query() NN', zorder=4)
    ax.plot([q[0], y_naive[0]], [q[1], y_naive[1]], linestyle='--', linewidth=1.5, color='orange')

    # true min-image neighbor (may require shifting the data point)
    a, b = bounds[0], bounds[1]
    y_true_img = data[true_idx] + true_shift[0]*a + true_shift[1]*b
    ax.scatter([y_true_img[0]],[y_true_img[1]], s=80, marker='s', facecolors='none',
               edgecolors='green', linewidths=2.0, label='true min-image NN', zorder=5)
    ax.plot([q[0], y_true_img[0]], [q[1], y_true_img[1]], linewidth=2.0, color='green')

    ax.legend(loc='upper right', frameon=True)
    ax.set_title('Nearest neighbor under triclinic PBC:\nnaive query() vs. true minimum-image')
    plt.tight_layout()
    plt.show()

# ----------------------
# Main demo
# ----------------------
if __name__ == "__main__":
    rng = np.random.default_rng(72)
    bounds = triclinic_bounds_2d()
    pbc = (True, True)

    # random data in [0,1)^2 then mapped to triclinic
    n = 200
    frac = rng.random((n, 2))
    data = frac_to_cart(frac, bounds)

    # Build your tree (ensure non-native path)
    tree = PeriodicCKDTree(bounds=bounds, data=data, pbc=pbc, force_orth=False)
    assert not tree.use_native, "Expecting non-native path for triclinic cell."

    # Hunt for a mismatch between naive query() and brute-force min-image
    found = False
    for _ in range(500):
        q_frac = rng.random(2)
        q = frac_to_cart(q_frac, bounds)

        # naive (current implementation)
        d_naive, i_naive = tree.query(q, k=1, p=2)

        # brute-force min-image (reference)
        i_true, d_true, shift = min_image_nn(q, data, bounds, pbc, m=1)

        # Consider a mismatch if indices differ or distances differ notably
        if (int(i_naive) != int(i_true)) or (abs(float(d_naive) - float(d_true)) > 1e-10):
            print("Mismatch found!")
            print(f" naive: idx={i_naive}, dist={d_naive:.6f}")
            print(f" true : idx={i_true}, dist={d_true:.6f}, shift={tuple(shift)}")
            visualize_mismatch(tree, bounds, data, q, int(i_naive), int(i_true), shift)
            found = True
            break

    if not found:
        print("No mismatch found in this run. (Common after applying the tiled query() fix.)")
        # Optionally, still visualize a random query to see geometry
        q_frac = rng.random(2); q = frac_to_cart(q_frac, bounds)
        i_true, d_true, shift = min_image_nn(q, data, bounds, pbc, m=1)
        visualize_mismatch(tree, bounds, data, q, int(i_true), int(i_true), shift)
