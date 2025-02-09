#!/usr/bin/env python3

from modules import core
import wmi
import subprocess


def get_installed_packages():
    """
    獲取已安裝的 Python 包列表。
    """
    try:
        process = subprocess.run(['pip', 'list'], capture_output=True, text=True, check=True)
        output = process.stdout
        packages = []
        # 解析 pip list 的輸出，跳過表頭
        lines = output.strip().split('\n')[2:]
        for line in lines:
            parts = line.split()
            if len(parts) >= 2:
                package_name = parts[0]
                package_version = parts[1] if len(parts) > 1 else "Version N/A"  # 處理沒有版本號的情況 (雖然 pip list 通常會顯示版本)
                packages.append(f"{package_name} ({package_version})")
            elif len(parts) == 1:  # 處理只有包名，沒有版本號的行 (理論上不常見，但為了更健壯)
                package_name = parts[0]
                packages.append(f"{package_name} (Version N/A)")

        return packages
    except subprocess.CalledProcessError as e:
        print(f"執行 'pip list' 命令時出錯: {e}")
        return None
    except FileNotFoundError:
        print("找不到 'pip' 命令。請確保 pip 已安裝並已添加到系統路徑。")
        return None


if __name__ == "__main__":

    installed_packages = get_installed_packages()
    if installed_packages:
        print("已安裝的 Python 包列表:")
        for package_info in installed_packages:
            print(package_info)


    m_wmi = wmi.WMI()
    cpu_info = m_wmi.Win32_Processor()
    if len(cpu_info) > 0:
        serial_number = cpu_info[0].ProcessorId
        print("cpu: ", serial_number)

    core.run(lang="zh-TW", CpuOrCuda="cuda")
