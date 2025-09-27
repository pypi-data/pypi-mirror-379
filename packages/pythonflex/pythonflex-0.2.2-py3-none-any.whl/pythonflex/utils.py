import os
import re  # For sanitization (built-in, minimal regex)
import tempfile
import joblib
import numpy as np
import pandas as pd

# Constants - ADD .parquet to valid extensions
TMP_ROOT = ".tmp"
VALID_EXTS = {".feather", ".parquet", ".npy", ".pkl"}

# Minimal fix - just patch the problematic save
original_to_feather = pd.DataFrame.to_feather
def safe_to_feather(self, path, **kwargs):
    try:
        return original_to_feather(self, path, **kwargs)
    except ValueError as e:
        if "feather does not support serializing" in str(e):
            # FIXED: Better path handling
            parquet_path = os.path.splitext(path)[0] + '.parquet'
            self.to_parquet(parquet_path, **kwargs)
        else:
            raise
pd.DataFrame.to_feather = safe_to_feather

# Helper to sanitize names (make filesystem-safe)
def _sanitize(name):
    if not name:
        return "data"
    # Replace forbidden/problematic chars with '_', collapse multiples, strip edges
    safe = re.sub(r'[<>:"/\\|?*$,\s]+', '_', str(name).strip())
    safe = re.sub(r'_+', '_', safe).strip('_')
    return safe if safe else "data"

# Helper to get safe path
def _safe_path(category, name=None, ext=".pkl"):
    safe_category = _sanitize(category)
    dir_path = os.path.join(TMP_ROOT, safe_category)
    os.makedirs(dir_path, exist_ok=True)
    safe_name = _sanitize(name) if name else "data"
    return os.path.join(dir_path, f"{safe_name}{ext}")

# Save function
def dsave(data, category, name=None, path=None):  # 'path' ignored for compatibility with old code
    # If data is dict and no name, recurse on each item
    if name is None and isinstance(data, dict):
        for k, v in data.items():
            dsave(v, category, k)
        return

    # Choose best extension based on type
    if isinstance(data, pd.DataFrame):
        ext = ".feather"
        save_func = lambda p: data.to_feather(p)
    elif isinstance(data, np.ndarray):
        ext = ".npy"
        save_func = lambda p: np.save(p, data, allow_pickle=False)
    else:
        ext = ".pkl"
        save_func = lambda p: joblib.dump(data, p, compress=0)  # Add compress=3 if needed

    target = _safe_path(category, name, ext)

    # Atomic save: Write to temp file, then rename
    with tempfile.NamedTemporaryFile(dir=os.path.dirname(target), delete=False) as tf:
        tmp_path = tf.name
        tf.close()  # Close so save_func can write
        save_func(tmp_path)
    os.replace(tmp_path, target)  # Atomic move

# Load function - FIXED: Added parquet support
def dload(category, name=None, path=None):  # 'path' ignored for compatibility
    dir_path = os.path.join(TMP_ROOT, _sanitize(category))

    if not os.path.exists(dir_path):
        return {}

    if name is None:
        # Load all in category as dict
        out = {}
        for filename in os.listdir(dir_path):
            if not any(filename.endswith(ext) for ext in VALID_EXTS):
                continue
            k = os.path.splitext(filename)[0]  # Key from filename (without ext)
            full_path = os.path.join(dir_path, filename)
            try:
                if filename.endswith(".feather"):
                    out[k] = pd.read_feather(full_path)
                elif filename.endswith(".parquet"):  # ADDED
                    out[k] = pd.read_parquet(full_path)
                elif filename.endswith(".npy"):
                    out[k] = np.load(full_path, mmap_mode="r")  # MMap for perf
                elif filename.endswith(".pkl"):
                    out[k] = joblib.load(full_path, mmap_mode="r")  # MMap for perf
            except (EOFError, ValueError, OSError):
                print(f"Warning: '{full_path}' is corrupted. Skipping...")
                os.remove(full_path)  # Delete corrupted file
        return out

    # Load specific name (try extensions in order - PREFER PARQUET over FEATHER)
    # Check parquet first since it's more reliable for complex data
    preferred_order = [".parquet", ".feather", ".npy", ".pkl"]
    
    for ext in preferred_order:
        if ext not in VALID_EXTS:
            continue
        target = _safe_path(category, name, ext)
        if os.path.exists(target):
            try:
                if ext == ".feather":
                    return pd.read_feather(target)
                elif ext == ".parquet":
                    return pd.read_parquet(target)
                elif ext == ".npy":
                    return np.load(target, mmap_mode="r")  # MMap for perf
                elif ext == ".pkl":
                    return joblib.load(target, mmap_mode="r")  # MMap for perf
            except (EOFError, ValueError, OSError) as e:
                print(f"Warning: '{target}' is corrupted ({e}). Trying next format...")
                os.remove(target)  # Delete corrupted file
                continue  # Try next format instead of returning {}
    
    print(f"Warning: No valid file found for {category}/{name}")
    return {}