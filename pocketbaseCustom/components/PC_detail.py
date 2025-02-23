import psutil
import requests
import wmi
import socket

m_wmi = wmi.WMI()


def get_cpu_logical_count():
    return psutil.cpu_count()


def get_cpu_nological_count():
    return psutil.cpu_count(logical=False)


def get_cpu_serial():
    cpu_info = m_wmi.Win32_Processor()
    if len(cpu_info) > 0:
        serial_number = cpu_info[0].ProcessorId
        return serial_number
    else:
        return None  # 或者返回空字符串 ""


def get_mac_address():
    mac_addresses = [addrs[0].address for iface, addrs in psutil.net_if_addrs().items() if
                     addrs[0].family == psutil.AF_LINK and addrs]  # 确保 addrs 不为空
    return mac_addresses  # 返回列表


def get_user_name():
    return [user.name for user in psutil.users()]


def get_pc_name():
    return socket.gethostname()


def get_disk_serial():
    disk_info = m_wmi.Win32_PhysicalMedia()
    if len(disk_info) > 0:
        serial_number = disk_info[0].SerialNumber.strip()
        return serial_number
    else:
        return None  # 或者返回空字符串 ""


def get_board_serial():
    board_info = m_wmi.Win32_BaseBoard()
    if len(board_info) > 0:
        board_id = board_info[0].SerialNumber.strip().strip('.')
        return board_id
    else:
        return None  # 或者返回空字符串 ""


def get_ip_address():
    ip = requests.get('https://api.ipify.org').text
    return ip

def get_bios_serial_wmi():
    try:
        c = wmi.WMI()
        bios_serial = c.Win32_BIOS()[0].SerialNumber
        return bios_serial
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":  # 添加 main 代码块，只在直接运行 PC_detail.py 时执行
    print("--- PC_detail.py 模块 ---")
    print("CPU 邏輯數量: ", get_cpu_logical_count())
    print("實際物理 CPU 數量: ", get_cpu_nological_count())
    print("CPU 序列號: ", get_cpu_serial())
    print("MAC 位址: ", get_mac_address())
    print("登陸的使用者名稱: ", get_user_name())
    print("獲取硬碟序列號: ", get_disk_serial())
    print("獲取主機板序列號: ", get_board_serial())
    print("IP 位址: ", get_ip_address())
    print("BIOS 序列號: ", get_bios_serial_wmi())

# 這些值存儲於硬體內部，不受 Windows 重新安裝影響：
# BIOS 序號（BIOS Serial Number） ✅ 不會變
# 主機板序號（Motherboard Serial Number） ✅ 不會變
# CPU 序號（Processor ID） ✅ 不會變
# 硬碟序號（Disk Serial Number） ✅ 不會變（但格式化不影響，更換硬碟會變）
# MAC 地址（MAC Address） ✅ 不會變（但更換網卡會變）