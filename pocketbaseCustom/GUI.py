import tkinter as tk
from tkinter import ttk, messagebox
from pocketbaseCustom.components import encryption
from pocketbaseCustom import PocketBaseAPI


class LicenseInputGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("License 輸入")
        self.geometry("300x200")
        self.result = None

        # 主框架，統一管理所有元件
        self.main_frame = ttk.Frame(self, padding=20)
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        # License 輸入標籤與輸入框
        ttk.Label(self.main_frame, text="請輸入 License:").pack(pady=(0, 5))
        self.license_entry = ttk.Entry(self.main_frame, width=30)
        self.license_entry.pack(pady=(0, 10))

        # 語言選擇標籤與下拉選單
        # ttk.Label(self.main_frame, text="請選擇語言:").pack(pady=(0, 5))
        # self.options = ["繁體中文", "简体中文", "English"]
        # self.selected_option = tk.StringVar(self)
        # self.selected_option.set(self.options[0])
        # self.option_menu = ttk.OptionMenu(self.main_frame, self.selected_option, self.options[0], *self.options)
        # self.option_menu.config(width=10)
        # self.option_menu.pack(pady=(0, 10))
        # self.selected_language = tk.StringVar(self, value=self.options[0])

        # 提交按鈕
        ttk.Button(self.main_frame, text="提交", command=self.submit_license).pack(pady=(0, 10))

    def submit_license(self):
        license_key = self.license_entry.get().strip()
        if not license_key:
            messagebox.showwarning("警告", "請注意：'授權碼' 欄位不能為空。請輸入您的有效 License 碼。")
            return

        try:
            license_state, license_id = PocketBaseAPI.license_verify(license_key)
            if license_state:
                messagebox.showinfo("成功", "License 驗證成功！請稍後，正在啟動程式。\n第一次執行換臉時會需要一些時間，請耐心等候")
                PocketBaseAPI.create_machine(license_id)
                PocketBaseAPI.change_license_false(license_id)
                self.result = license_id
                self.destroy()
            else:
                messagebox.showerror("錯誤", "License 驗證失敗！請檢查您的 License 碼是否正確。")
        except Exception as e:
            print("License 驗證發生例外:", e)
            messagebox.showerror("錯誤", "License 驗證失敗！請檢查您的 License 碼是否正確。")


if __name__ == "__main__":
    # 若機器驗證未通過，則要求輸入 License
    app = LicenseInputGUI()
    app.mainloop()
    print("language:", app.selected_option)
    print("result:", app.result)
    # if not PocketBaseAPI.verify_machine(encryption.get_fingerprint()):
    #     app = LicenseInputGUI()
    #     app.mainloop()
    #     print("result:", app.result)
    # else:
    #     # 驗證通過後，可進一步執行其他程式邏輯
    pass
