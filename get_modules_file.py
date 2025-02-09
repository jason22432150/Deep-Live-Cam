import os


def list_files_in_directory(directory):
    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_paths.append(f"'{os.path.abspath(os.path.join(root, file))}',")
    return file_paths


def replace_backslashes(file_paths):
    return [file_path.replace("\\", "\\") for file_path in file_paths]


if __name__ == "__main__":
    directory = "media"
    files = list_files_in_directory(directory)
    replaced_files = replace_backslashes(files)
    for file in files:
        # print(replace_backslashes(file))
        print(file)




#  --add-binary
# venv/Lib/site-packages/onnxruntime/capi/onnxruntime_providers_cuda.dll;
# ./onnxruntime/capi/
#
# --add-binary
# venv/Lib/site-packages/onnxruntime/capi/onnxruntime_providers_tensorrt.dll;
# ./onnxruntime/capi/