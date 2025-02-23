#!/usr/bin/env python3

from modules import core
from pocketbaseCustom import PocketBaseAPI
from pocketbaseCustom import GUI
from pocketbaseCustom.components import encryption

if __name__ == "__main__":
    if not PocketBaseAPI.verify_machine(encryption.get_fingerprint()):
        root = GUI.LicenseInputGUI()
        root.mainloop()
        # print("language:", root.selected_language)
        print("root.result:", root.result)
        if root.result is not None:
            core.run(lang="zh-TW", CpuOrCuda="cuda")
        else:
            pass
    else:
        core.run(lang="zh-TW", CpuOrCuda="cuda")
        pass
