# run.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

cuda_version_11 = "v11.8"  # Adjust to your CUDA version
cuda_version_12 = "v12.1"  # Adjust to your CUDA version
cuda_path_11 = f"C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\{cuda_version_11}\\bin" # Use raw string or escaped backslashes
cuda_path_12 = f"C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\{cuda_version_12}\\bin" # Use raw string or escaped backslashes

a = Analysis(
    [
        'run.py'
    ],
    pathex=[],
    binaries=[
        (os.path.join(cuda_path_11, "cudart64_110.dll"), '.'),  # CUDA Runtime
        (os.path.join(cuda_path_12, "cudart64_12.dll"), '.'),  # CUDA Runtime
        (os.path.join(cuda_path_11, "cublas64_11.dll"), '.'),  # cuBLAS (if needed)
        (os.path.join(cuda_path_12, "cublas64_12.dll"), '.'),  # cuBLAS (if needed)
    ],
    datas=[
        ("models","models"),
        ("modules", "modules"),
        ("locales", "locales"),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='run',
    debug=all,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,  # 如果是 GUI 應用程式，設置為 False
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    log_level='TRACE',  # Add log level
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='run',
    onefile=True,  # Set to False to enable --onedir
)