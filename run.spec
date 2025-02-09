# run.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

cuda_version_11 = "v11.8"  # Adjust to your CUDA version
cuda_path_11 = f"C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\{cuda_version_11}\\bin" # Use raw string or escaped backslashes

a = Analysis(
    [
        'run.py'
    ],
    pathex=[],
    binaries=[
        ('venv\\Lib\\site-packages\\onnxruntime\\capi\\onnxruntime_providers_shared.dll', 'onnxruntime\\capi'),
        ('venv\\Lib\\site-packages\\onnxruntime\\capi\\onnxruntime_providers_cuda.dll', 'onnxruntime\\capi'),
        ('venv\\Lib\\site-packages\\onnxruntime\\capi\\onnxruntime_providers_tensorrt.dll', 'onnxruntime\\capi'),
        (os.path.join(cuda_path_11, "cudart64_110.dll"), '.'),  # CUDA Runtime
        (os.path.join(cuda_path_11, "cublas64_11.dll"), '.'),  # cuBLAS (if needed)
    ],
    datas=[
        ("models","models"),
        ("modules", "modules"),
        ("locales", "locales"),
    ],
    hiddenimports=[
        'absl',  # 注意: absl-py 的 package 名稱是 absl
        'addict',
        'albumentations',
        'altgraph',
        'astunparse',
        'basicsr',
        'bs4',      # beautifulsoup4 的 package 名稱是 bs4
        'cachetools',
        'certifi',
        'charset_normalizer', # charset-normalizer 的 package 名稱
        'colorama',
        'coloredlogs',
        'comtypes',
        'contourpy',
        'customtkinter',
        'cv2_enumerate_cameras',
        'cycler',
        'Cython',
        'darkdetect',
        'easydict',
        'facexlib',
        'filelock',
        'filterpy',
        'flatbuffers',
        'fonttools',
        'future',
        'gast',
        'gdown',
        'gfpgan',
        'google.auth', # google-auth 的 package 名稱
        'google_auth_oauthlib', # google-auth-oauthlib 的 package 名稱
        'google_pasta', # google-pasta 的 package 名稱
        'grpc',      # grpcio 的 package 名稱是 grpc
        'h5py',
        'humanfriendly',
        'idna',
        'imageio',
        'insightface',
        'jax',
        'jaxlib',
        'jinja2', # Jinja2 的 package 名稱
        'joblib',
        'keras',
        'kiwisolver',
        'lazy_loader',
        'libclang',
        'llvmlite',
        'lmdb',
        'markdown', # Markdown 的 package 名稱
        'markupsafe', # MarkupSafe 的 package 名稱
        'matplotlib',
        'ml_dtypes',
        'mpmath',
        'networkx',
        'numba',
        'numpy',
        'oauthlib',
        'onnx',
        'onnxruntime', # onnxruntime-gpu 的 package 名稱是 onnxruntime (PyInstaller 通常會處理 GPU 版本)
        'cv2',      # opencv-python 或 opencv-python-headless 的 package 名稱是 cv2
        'opennsfw2',
        'opt_einsum',
        'packaging',
        'pefile',
        'PIL',      # Pillow 的 package 名稱是 PIL
        'pip',
        'platformdirs',
        'prettytable',
        'protobuf',
        'psutil',
        'pyasn1',
        'pyasn1_modules',
        'pygrabber',
        'pyinstaller',
        'pyinstaller_hooks_contrib', # pyinstaller-hooks-contrib 的 package 名稱
        'pyparsing',
        'pyreadline3',
        'socks',    # PySocks 的 package 名稱是 socks
        'dateutil', # python-dateutil 的 package 名稱是 dateutil
        'win32',    # pywin32 的 package 名稱 (可能需要更精確，例如 'win32api', 'win32con' 等，視乎你的程式碼實際使用情況)
        'win32ctypes', # pywin32-ctypes 的 package 名稱
        'yaml',     # PyYAML 的 package 名稱是 yaml
        'qudida',
        'requests',
        'requests_oauthlib',
        'rsa',
        'skimage',  # scikit-image 的 package 名稱是 skimage
        'sklearn',  # scikit-learn 的 package 名稱是 sklearn
        'scipy',
        'setuptools',
        'six',
        'soupsieve',
        'sympy',
        'tb_nightly', # tb-nightly 的 package 名稱
        'tensorboard',
        'tensorboard_data_server', # tensorboard-data-server 的 package 名稱
        'tensorflow',
        'tensorflow_estimator', # tensorflow-estimator 的 package 名稱
        'tensorflow_intel', # tensorflow-intel 的 package 名稱
        'tensorflow_io_gcs_filesystem', # tensorflow-io-gcs-filesystem 的 package 名稱
        'termcolor',
        'threadpoolctl',
        'tifffile',
        'tkinter',  # tk 的 package 名稱是 tkinter
        'tkinterdnd2',
        'tomli',
        'torch',
        'torchvision',
        'tqdm',
        'typing_extensions',
        'urllib3',
        'wcwidth',
        'werkzeug',
        'wheel',
        'wmi',
        'wrapt',
        'yapf',
    ],
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
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='run',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # 如果是 GUI 程式，改為 False
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)