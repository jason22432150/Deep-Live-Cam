import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pocketbaseCustom.components import encryption
from pocketbaseCustom import PocketBaseAPI


def create_gui():
    """
    建立 License 輸入 GUI 介面。
    """
    root = tk.Tk()
    root.title("License 輸入")
    root.geometry("300x200")

    # 使用 Frame 組織元件，方便佈局和管理
    main_frame = ttk.Frame(root, padding=20)  # 增加 padding 使元件與邊框有間距
    main_frame.pack(expand=True, fill=tk.BOTH)  # expand 和 fill 讓 Frame 填滿視窗

    # License 輸入標籤
    license_label = ttk.Label(main_frame, text="請輸入 License:")
    license_label.pack(pady=(0, 5))  # pady 上方間距為 0, 下方間距為 5，更精細的控制

    # License 輸入框
    license_entry = ttk.Entry(main_frame, width=30)
    license_entry.pack(pady=(0, 10))  # pady 上方間距為 0, 下方間距為 10

    # 選單文字標籤
    license_label = ttk.Label(main_frame, text="請選擇語言:")
    license_label.pack(pady=(0, 5))  # pady 上方間距為 0, 下方間距為 5，更精細的控制

    # 選項選單樣式 (使用 ttk.Style 統一風格)
    style = ttk.Style(root)  # Style 需以 root 為父元件
    style.configure("TMenubutton", font=("Arial", 12), padding=10, relief="raised")

    # 選項選單
    options = ["繁體中文", "简体中文", "English"]
    selected_option = tk.StringVar(root)
    selected_option.set(options[0])  # 設置默認值
    option_menu = ttk.OptionMenu(main_frame, selected_option, *options)  # 使用 ttk.OptionMenu
    option_menu.config(width=10)  # 設定樣式 (config 可以直接用 ttk 元件)
    option_menu.pack(pady=(0, 10))

    # 提交按鈕
    submit_button = ttk.Button(main_frame, text="提交",
                               command=lambda: submit_license(root, license_entry.get()))  # 獲取 Entry 的值
    submit_button.pack(pady=(0, 10))

    return root  # 返回 root 方便後續操作 (例如在其他地方啟動 GUI)


def submit_license(root, license_key):
    """
    提交 License 的處理函數 (此處為範例，您可以根據需求修改)。
    """
    if license_key == "":
        print("License 不能為空！")
        warning_message_license_empty = "請注意：'授權碼' 欄位不能為空。請輸入您的有效 License 碼。"
        tk.messagebox.showwarning("警告", warning_message_license_empty)
    else:
        license_state, license_id = PocketBaseAPI.license_verify(license_key)
        if license_state:
            print("License 驗證成功！")
            success_message_license_verified = "License 驗證成功！"
            tk.messagebox.showinfo("成功", success_message_license_verified)
            PocketBaseAPI.create_machine(license_id)
            root.destroy()  # 關閉視窗

        else:
            print("License 驗證失敗！")
            error_message_license_invalid = "License 驗證失敗！請檢查您的 License 碼是否正確。"
            tk.messagebox.showerror("錯誤", error_message_license_invalid)
    print(f"License: {license_key}")
    return


if __name__ == "__main__":
    if not PocketBaseAPI.verify_machine(encryption.get_fingerprint()):
        root = create_gui()
        root.mainloop()
        print(root)
    else:
        pass
