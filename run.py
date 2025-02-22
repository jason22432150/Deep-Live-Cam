#!/usr/bin/env python3

from modules import core
import wmi

if __name__ == "__main__":

    m_wmi = wmi.WMI()
    cpu_info = m_wmi.Win32_Processor()
    if len(cpu_info) > 0:
        serial_number = cpu_info[0].ProcessorId
        print("cpu: ", serial_number)

    try:
        core.run(lang="zh-TW", CpuOrCuda="cuda")
    except Exception as e:
        print(e)
        input("Press Enter to exit...")
    # core.run(lang="zh-TW", CpuOrCuda="cuda")
