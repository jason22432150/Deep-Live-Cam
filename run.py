#!/usr/bin/env python3

from modules import core
import wmi

if __name__ == "__main__":

    try:
        core.run(lang="zh-TW", CpuOrCuda="cuda")
    except Exception as e:
        print(e)
        input("Press Enter to exit...")

