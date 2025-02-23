from pocketbase import PocketBase  # Client also works the same
from pocketbaseCustom.components import PC_detail
from pocketbaseCustom.components import encryption

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

BASE_URL = 'https://pocketbase.miku-izayoi.uk'


# client = PocketBase('https://pocketbase.miku-izayoi.uk')


def get_token():
    # authenticate as regular user
    client = PocketBase(BASE_URL)
    user_data = client.collection("users").auth_with_password(
        "user@example.com", "4ZQ50ZFoABO-nNR")
    # check if user token is valid
    # user_data.is_valid
    return user_data.token


def license_verify(license_value):
    client = PocketBase(BASE_URL)
    token_admin = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2xsZWN0aW9uSWQiOiJwYmNfMzE0MjYzNTgyMyIsImV4cCI6MTc0MDEzMjMwMCwiaWQiOiI3MDc0OWJsMDBvaXk3MjgiLCJyZWZyZXNoYWJsZSI6ZmFsc2UsInR5cGUiOiJhdXRoIn0.VdViLF_zghXa9vCy4za8cvyxkhEXPLl_9gl2oyXe_0k"
    token_user = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2xsZWN0aW9uSWQiOiJfcGJfdXNlcnNfYXV0aF8iLCJleHAiOjE3NDA2NTA4MDgsImlkIjoicHltMmo1ZXE0MzRyN3Q2IiwicmVmcmVzaGFibGUiOmZhbHNlLCJ0eXBlIjoiYXV0aCJ9.BEPVqvNHo-zzvtyV9yjcTKiu0Z7t6XSHEclDEro74Uk'
    client.auth_store.save(token_user, None)
    license_verify_res = client.collection("License").get_list(1, 1, {
        "filter": f"License = '{license_value}'"})
    if license_verify_res.items:
        print(license_verify_res.items)
        return True
    else:
        # print(license_verify_res.items[0]["id"])
        return False


def create_machine(license_id):
    client = PocketBase(BASE_URL)
    # token_admin = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2xsZWN0aW9uSWQiOiJwYmNfMzE0MjYzNTgyMyIsImV4cCI6MTc0MDEzMjMwMCwiaWQiOiI3MDc0OWJsMDBvaXk3MjgiLCJyZWZyZXNoYWJsZSI6ZmFsc2UsInR5cGUiOiJhdXRoIn0.VdViLF_zghXa9vCy4za8cvyxkhEXPLl_9gl2oyXe_0k"
    token_user = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2xsZWN0aW9uSWQiOiJfcGJfdXNlcnNfYXV0aF8iLCJleHAiOjE3NDA2NTA4MDgsImlkIjoicHltMmo1ZXE0MzRyN3Q2IiwicmVmcmVzaGFibGUiOmZhbHNlLCJ0eXBlIjoiYXV0aCJ9.BEPVqvNHo-zzvtyV9yjcTKiu0Z7t6XSHEclDEro74Uk'
    client.auth_store.save(token_user, None)
    license_verify_res = client.collection("Machines").get_list(1, 1, {
        "filter": f"Fingerprint = '{encryption.get_fingerprint()}'"})
    if license_verify_res.items:
        print("Machine already exists")
        # print(license_verify_res.items)
        return
    else:
        # print(license_verify_res.items[0]["id"])
        # 設置請求主體
        body = {
            "Licence": f"{license_id}",
            "Fingerprint": f"{encryption.get_fingerprint()}",
            "IP": f"{PC_detail.get_ip_address()}",
        }
        try:
            # 創建記錄
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
    token_admin = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2xsZWN0aW9uSWQiOiJwYmNfMzE0MjYzNTgyMyIsImV4cCI6MTc0MDEzMjMwMCwiaWQiOiI3MDc0OWJsMDBvaXk3MjgiLCJyZWZyZXNoYWJsZSI6ZmFsc2UsInR5cGUiOiJhdXRoIn0.VdViLF_zghXa9vCy4za8cvyxkhEXPLl_9gl2oyXe_0k"
    token_user = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2xsZWN0aW9uSWQiOiJfcGJfdXNlcnNfYXV0aF8iLCJleHAiOjE3NDA2NTA4MDgsImlkIjoicHltMmo1ZXE0MzRyN3Q2IiwicmVmcmVzaGFibGUiOmZhbHNlLCJ0eXBlIjoiYXV0aCJ9.BEPVqvNHo-zzvtyV9yjcTKiu0Z7t6XSHEclDEro74Uk'
    client.auth_store.save(token_user, None)
    license_verify_res = client.collection("Machines").get_list(1, 1, {
        "filter": f"Fingerprint = '{machine_Fingerprint}'"})
    if license_verify_res.items:
        print(license_verify_res.items)
        return True
    else:
        # print(license_verify_res.items[0]["id"])
        return False


if __name__ == "__main__":
    # client = PocketBase('https://pocketbase.miku-izayoi.uk')
    # license_verify, license_id = license_verify(client, "I3848-7D07X-0881B-XGAC1")
    # if license_verify:
    #     create_machine(client, encryption.get_fingerprint(), PC_detail.get_ip_address(), license_id)
    pass
    # print(license_verify(client, "9D0W1-7MRV9-W0B9M-JRJ0Q"))
    # print(license_verify(client, "I3848-7D07X-0881B-XGAC"))
    # print(license_verify(client, "9D0W1-7MRV9-W0B9M-JRJ0"))
