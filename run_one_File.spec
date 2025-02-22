# -*- mode: python ; coding: utf-8 -*-

import os
from PyInstaller.utils.hooks import collect_dynamic_libs

block_cipher = None

# CUDA 相關路徑
cuda_version_11 = "v11.8"  # 根據你的 CUDA 版本調整
cuda_path_11 = f"C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\{cuda_version_11}\\bin"  # 使用原始字符串或轉義反斜杠

# 分析部分
a = Analysis(
    ['run.py'],  # 主程式入口
    pathex=[],  # 模組搜索路徑
    binaries=[
        # ONNX Runtime 相關 DLL
        ('venv\\Lib\\site-packages\\onnxruntime\\capi\\onnxruntime_providers_shared.dll', 'onnxruntime\\capi'),
        ('venv\\Lib\\site-packages\\onnxruntime\\capi\\onnxruntime_providers_cuda.dll', 'onnxruntime\\capi'),
        ('venv\\Lib\\site-packages\\onnxruntime\\capi\\onnxruntime_providers_tensorrt.dll', 'onnxruntime\\capi'),
        # CUDA 相關 DLL
        (os.path.join(cuda_path_11, "cudart64_110.dll"), '.'),  # CUDA Runtime
        (os.path.join(cuda_path_11, "cublas64_11.dll"), '.'),  # cuBLAS (如果需要)
    ],
    datas=[        # 資料文件
        ("venv\\Lib\\site-packages", "."),
        ("package_in_exe\\insightface", "insightface"),
        ("venv\\Lib\\site-packages\\gfpgan", "gfpgan"),
        ("models", "models"),
        ("modules", "modules"),
        ("locales", "locales"),
    ],
    hiddenimports=['gfpgan','frame_processor_module','threading','cv2','torch','platform'],  # 隱藏導入的模組
    hookspath=[],  # 自定義鉤子路徑
    runtime_hooks=[],  # 運行時鉤子
    excludes=[],  # 排除的模組
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,  # 禁用緩存打包
)

# 設置緩存目錄為當前專案下的 temp 資料夾
# 移除不必要的行
# a.binaries = a.binaries + collect_dynamic_libs('temp')

# 打包成單一文件
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# 可執行文件配置
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,  # 這裡應該填 a.binaries 而不是 []
    a.zipfiles,
    a.datas,
    [],
    name='旺旺換臉',  # 設定輸出文件名
    debug=False,  # 關閉 debug 模式
    bootloader_ignore_signals=False,  # 不忽略啟動加載器信號
    strip=False,  # 不移除符號表
    upx=False,  # 啟用 UPX 壓縮以減小文件大小
    console=False,  # GUI 應用關閉 console
    disable_windowed_traceback=False,  # 允許 GUI 回溯顯示
    target_arch=None,  # 不指定目標架構
    codesign_identity=None,  # 不使用代碼簽名身份
    entitlements_file=None  # 不使用權限文件
)


# 移除 COLLECT 部分，因為我們要單一 EXE
# coll = COLLECT(
#     exe,
#     a.binaries,
#     a.zipfiles,
#     a.datas,
#     strip=False,
#     upx=False,
#     upx_exclude=[],
#     name='run',  # 輸出文件名
# )