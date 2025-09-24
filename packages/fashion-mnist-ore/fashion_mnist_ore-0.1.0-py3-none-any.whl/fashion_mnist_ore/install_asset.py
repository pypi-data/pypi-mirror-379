import os, tempfile, hashlib, shutil
from importlib import resources as ir
import zstandard as zstd

ASSET_NAME  = "fashion_mnist.pt"          # 복원될 원본 파일명
ASSET_SHA256 = "f31dda8276fa06b160ec2ec65d5b3e865c7fae9afb0fdf9efceb9cbc1eb809dc"                # 무결성 체크
ZST_NAME     = "fashion_mnist.pt.zst"           # 임시 조립 파일명(.zst)

SHARDS = [('fashion_mnist_ore_shard01', 'shard-01.bin')]

def _default_target_dir():
    return os.getcwd() if os.name == "nt" else "/tmp"

def _assemble_zst(tmp_path):
    with open(tmp_path, "wb") as out:
        for pkg, res in SHARDS:
            with ir.open_binary(pkg, res) as f:
                shutil.copyfileobj(f, out)

def ensure_asset(target_dir=None):
    out_dir = target_dir or os.environ.get("ASSET_TARGET_DIR") or _default_target_dir()
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, ASSET_NAME)
    if not os.path.exists(out_path):
        with tempfile.TemporaryDirectory() as td:
            zst_path = os.path.join(td, ZST_NAME)
            _assemble_zst(zst_path)
            dctx = zstd.ZstdDecompressor()
            with open(zst_path, "rb") as fin, open(out_path, "wb") as fout:
                dctx.copy_stream(fin, fout)

    # 무결성 검증
    h = hashlib.sha256()
    with open(out_path, "rb") as f:
        for chunk in iter(lambda: f.read(1<<20), b""):
            h.update(chunk)
    if h.hexdigest() != ASSET_SHA256:
        try: os.remove(out_path)
        except Exception: pass
        raise RuntimeError("Asset SHA256 mismatch")
    return out_path

def main():
    print(ensure_asset())
