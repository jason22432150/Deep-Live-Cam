from pocketbase import PocketBase  # Client also works the same
from pocketbaseCustom.components import PC_detail
from pocketbaseCustom.components import encryption
import os
from dotenv import load_dotenv

# 載入 .env 檔案
load_dotenv()

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'  # orange on some systems
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
LIGHT_GRAY = '\033[37m'
DARK_GRAY = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
WHITE = '\033[97m'

RESET = '\033[0m'  # called to return to standard terminal text color

BASE_URL = os.environ.get("BASE_URL")
USER_TOKEN = os.environ.get("USER_TOKEN")


def get_token():
    # authenticate as regular user
    client = PocketBase(BASE_URL)
    user_data = client.collection("users").auth_with_password(
        "user@example.com", "4ZQ50ZFoABO-nNR")
    return user_data.token


def license_verify(license_value):
    client = PocketBase(BASE_URL)
    client.auth_store.save(USER_TOKEN, None)
    license_verify_res = client.collection("License").get_list(1, 1, {
        "filter": f"License = '{license_value}'"})
    if license_verify_res.items:
        print(license_verify_res.items)
        license_id = str(license_verify_res.items).split(": ")[1]
        license_id = license_id.split(">")[0]
        return True, license_id
    else:
        return False


def create_machine(license_id):
    client = PocketBase(BASE_URL)
    client.auth_store.save(USER_TOKEN, None)
    license_verify_res = client.collection("Machines").get_list(1, 1, {
        "filter": f"Fingerprint = '{encryption.get_fingerprint()}'"})
    if license_verify_res.items:
        print("Machine already exists")
        return
    else:
        # 設置請求主體
        body = {
            "Licence": f"{license_id}",
            "Fingerprint": f"{encryption.get_fingerprint()}",
            "IP": f"{PC_detail.get_ip_address()}",
        }
        try:
            # 創建記錄
            print(body)
            record = client.collection("Machines").create(body_params=body)
            record_id = str(record).split(": ")[1]
            record_id = record_id.split(">")[0]
            print("創建成功:", record_id)
            return record
        except Exception as e:
            print("創建失敗:", e)
            return None


def verify_machine(machine_Fingerprint):
    client = PocketBase(BASE_URL)
    client.auth_store.save(USER_TOKEN, None)
    license_verify_res = client.collection("Machines").get_list(1, 1, {
        "filter": f"Fingerprint = '{machine_Fingerprint}'"})
    if license_verify_res.items:
        print(license_verify_res.items)
        return True
    else:
        return False


def change_license_false(license_id):
    client = PocketBase(BASE_URL)
    # Update a record in the "users" collection with the given record ID
    updated_record = client.collection("License").update(license_id, {
        "Use_Status": False
    })
    print(updated_record)


if __name__ == "__main__":
    change_license_false("b753029wj8926zm")
    # client = PocketBase('https://pocketbase.miku-izayoi.uk')
    # license_verify, license_id = license_verify(client, "123456")
    # if license_verify:
    #     create_machine(client, encryption.get_fingerprint(), PC_detail.get_ip_address(), license_id)
    pass
    # print(license_verify(client, ""))
