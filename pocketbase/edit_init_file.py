import os
import configparser


def file_exists(filename):
    if os.path.exists(filename):
        return ini_to_dict(filename)
    else:
        return False


def create_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)  # 創建一個空文件
    print(f"文件 '{filename}' 已創建！")


# def read_file(filename):
#     try:
#         with open(filename, "r", encoding="utf-8") as file:
#             content = file.read()
#         return content
#     except FileNotFoundError:
#         return f"文件 '{filename}' 不存在！"


def ini_to_dict(file_path):
    """
    读取 INI 文件并转换为字典。

    Args:
        file_path (str): INI 文件的路径。

    Returns:
        dict: 从 INI 文件读取的数据字典。
              如果文件读取失败或 DEFAULT section 不存在，则返回空字典。
    """
    config = configparser.ConfigParser()
    data_dict = {}

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            config.read_file(file) # config.read_file() 需要檔案物件
        if 'DEFAULT' in config:  # 检查是否存在 DEFAULT section
            for key in config['DEFAULT']:
                data_dict[key] = config['DEFAULT'][key]
        else:
            print(f"警告: 文件 '{file_path}' 中沒有 DEFAULT section。")
    except FileNotFoundError:
        print(f"錯誤: 文件 '{file_path}' 未找到。")
        return "No_File"
    except Exception as e:
        print(f"讀取文件 '{file_path}' 時發生錯誤: {e}")

    return data_dict


def dict_to_ini(data_dict, file_path):
    """
    將字典資料寫入 INI 檔案。

    Args:
        data_dict (dict): 要寫入 INI 檔案的字典資料。
        file_path (str): 要寫入的 INI 檔案路徑。
    """
    config = configparser.ConfigParser()

    # 將字典中的鍵值對寫入 DEFAULT 區段
    for key, value in data_dict.items():
        config.set('DEFAULT', key, str(value))  # 確保值是字串

    try:
        with open(file_path, 'w', encoding='utf-8') as configfile:  # 使用 utf-8 編碼避免中文問題
            config.write(configfile)
        print(f"資料已成功寫入到 INI 檔案: '{file_path}'")
    except Exception as e:
        print(f"寫入 INI 檔案 '{file_path}' 時發生錯誤: {e}")


if __name__ == "__main__":
    # data_to_write = {
    #     'id': '987654321',
    #     'language': 'zh-TW',
    #     'name': '範例名稱',
    #     'setting': '開啟'
    # }
    # dict_to_ini(data_to_write, 'information.ini')

    # file_state = file_exists('information.ini')
    result_dict = ini_to_dict('information.ini')
    print(result_dict)
    if 'id' in result_dict:
        id_value = result_dict['id']
        print(f"字典中的 id 值是: {id_value}")
    else:
        print("字典中找不到 'id' 這個鍵。")
    # print(file_state)
    pass