#!/usr/bin/env python3

from modules import core
from pocketbaseCustom import PocketBaseAPI
from pocketbaseCustom import GUI
from pocketbaseCustom.components import encryption


if __name__ == "__main__":
    if not PocketBaseAPI.verify_machine(encryption.get_fingerprint()):
        root = GUI.create_gui()
        root.mainloop()
        print(root)
    else:
        pass

    try:
        core.run(lang="zh-TW", CpuOrCuda="cuda")
    except Exception as e:
        print(e)
        input("Press Enter to exit...")

