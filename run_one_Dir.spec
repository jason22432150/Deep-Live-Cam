# -*- mode: python ; coding: utf-8 -*-
import os
from PyInstaller.utils.hooks import collect_dynamic_libs

block_cipher = None

# CUDA 相關路徑
cuda_version_11 = "v11.8"  # 根據你的 CUDA 版本調整
cuda_path_11 = f"I:\\NVIDIA GPU Computing Toolkit\\CUDA\\{cuda_version_11}\\bin"  # 使用原始字符串或轉義反斜杠

# 分析部分
a = Analysis(
    ['run.py'],  # 主程式入口
    pathex=[],  # 模組搜索路徑
    binaries=[
        # ONNX Runtime 相關 DLL
        ('Py310_DeepLiveCame\\Lib\\site-packages\\onnxruntime\\capi\\onnxruntime_providers_shared.dll', 'onnxruntime\\capi'),
        ('Py310_DeepLiveCame\\Lib\\site-packages\\onnxruntime\\capi\\onnxruntime_providers_cuda.dll', 'onnxruntime\\capi'),
        ('Py310_DeepLiveCame\\Lib\\site-packages\\onnxruntime\\capi\\onnxruntime_providers_tensorrt.dll', 'onnxruntime\\capi'),
        # CUDA 相關 DLL
        (os.path.join(cuda_path_11, "cudart64_110.dll"), '.'),  # CUDA Runtime
        (os.path.join(cuda_path_11, "cublas64_11.dll"), '.'),  # cuBLAS (如果需要)
    ],
    datas=[        # 資料文件
        ("Py310_DeepLiveCame\\Lib\\site-packages", "."),
        ("package_in_exe\\insightface", "insightface"),
        ("Py310_DeepLiveCame\\Lib\\site-packages\\gfpgan", "gfpgan"),
        ("models", "models"),
        ("modules", "modules"),
        ("locales", "locales"),
    ],
    hiddenimports=['gfpgan','threading','cv2','torch','platform'],  # 隱藏導入的模組
    hookspath=[], # 確保路徑正確
    runtime_hooks=[],  # 運行時鉤子
    excludes=[],  # 排除的模組
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,  # 禁用緩存打包
)

# 設置緩存目錄為當前專案下的 temp 資料夾
a.binaries = a.binaries + collect_dynamic_libs('temp')

# 打包成單一文件
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# 可執行文件配置
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='旺旺換臉',  # 輸出文件名
    debug=False,  # 開啟 debug 模式
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,  # 禁用 UPX 壓縮以加快速度
    console=False,  # 開啟 console
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    jobs=4,  # 启用并行构建，4 是并行任务数
)

# 收集文件
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='旺旺換臉',  # 輸出文件名
)