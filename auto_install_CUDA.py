import subprocess
import os
import platform

def check_cuda_installation():
    print("檢查CUDA是否已安裝...")
    try:
        # 檢查CUDA版本
        result = subprocess.run(["nvcc", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if "Cuda compilation tools, release 11.8" in result.stdout:
            print(f"CUDA 11.8 已安裝: {result.stdout.splitlines()[3]}")
            return True
        else:
            print("CUDA 11.8 未安裝或版本不正確。")
            return False
    except FileNotFoundError:
        print("未找到nvcc命令，CUDA可能未安裝。")
        return False


def install_cuda():
    # 檢查操作系統
    system = platform.system()
    if system != "Windows" and system != "Linux":
        print("此腳本僅支持Windows和Linux系統。")
        return

    # 定義CUDA 11.8安裝包的URL
    cuda_version = "11.8.0"
    cuda_package_version = "11.8.0_522.06"
    cuda_url = ""
    if system == "Windows":
        cuda_url = f"https://developer.download.nvidia.com/compute/cuda/{cuda_version}/local_installers/cuda_{cuda_version}_windows.exe"
                        #  https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda_11.8.0_522.06_windows.exe
    elif system == "Linux":
        cuda_url = f"https://developer.download.nvidia.com/compute/cuda/{cuda_version}/local_installers/cuda_{cuda_version}_linux.run"

    # 定義安裝包文件名（包含版本資訊）
    cuda_installer = f"cuda_{cuda_version}_installer.exe" if system == "Windows" else f"cuda_{cuda_version}_installer.run"

    # 檢查是否已經有下載的安裝包
    if os.path.exists(cuda_installer):
        print(f"發現已下載的安裝包: {cuda_installer}，跳過下載步驟。")
    else:
        # 下載CUDA安裝包
        print("正在下載CUDA安裝包...")
        try:
            subprocess.run(["curl", "-o", cuda_installer, cuda_url], check=True)
        except subprocess.CalledProcessError as e:
            print(f"下載CUDA安裝包失敗: {e}")
            return

    # 安裝CUDA
    print("正在安裝CUDA...")
    try:
        if system == "Windows":
            subprocess.run([cuda_installer, "-s"], check=True)
        elif system == "Linux":
            subprocess.run(["sh", cuda_installer, "--silent"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"CUDA安裝失敗: {e}")
        return

    # 清理安裝包（可選）
    print("清理安裝包...")
    if os.path.exists(cuda_installer):
        os.remove(cuda_installer)

    # 檢查CUDA是否安裝成功
    if check_cuda_installation():
        print("CUDA安裝成功！")
    else:
        print("CUDA安裝失敗，請檢查錯誤訊息。")

def check_cuda_installation():
    print("檢查CUDA是否安裝成功...")
    try:
        # 檢查CUDA版本
        result = subprocess.run(["nvcc", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if "Cuda compilation tools, release 11.8" in result.stdout:
            print(f"CUDA版本檢查成功: {result.stdout.splitlines()[3]}")
            return True
        else:
            print("CUDA版本檢查失敗，未找到正確的版本。")
            return False
    except FileNotFoundError:
        print("未找到nvcc命令，CUDA可能未正確安裝。")
        return False

if __name__ == "__main__":
    # 先檢查CUDA是否已經安裝
    if check_cuda_installation():
        print("CUDA 11.8 已經安裝，無需重新安裝。")
    else:
        # 如果未安裝，則執行安裝
        install_cuda()
    # 等待用戶輸入後結束
    input("按 Enter 鍵結束...")