from PyInstaller.utils.hooks import collect_dynamic_libs

hiddenimports = ['onnxruntime', 'onnxruntime.capi', 'onnxruntime.capi.onnxruntime_pybind11_state']

binaries = collect_dynamic_libs('onnxruntime')