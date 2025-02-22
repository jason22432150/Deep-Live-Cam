from components import PC_detail
import base64
import hashlib
from pyDes import *


def encrypted(plain_text):
  """
    Encrypts the given text using DES, Base32 encoding, and MD5 hashing.

    Args:
        plain_text (str): The text to be encrypted.

    Returns:
        str: The final MD5 hash of the Base32 encoded and DES encrypted text, in uppercase.
             Returns None if encryption process fails.
    """
  try:
    des_key = "posdvsgt"  # DES encryption key
    des_iv = "\x11\x02\x2a\x03\x01\x27\x02\x00"  # DES initialization vector
    k = des(des_key, CBC, des_iv, pad=None, padmode=PAD_PKCS5)
    
    des_encrypted_bytes = k.encrypt(plain_text.encode('utf-8'))  # Ensure plain_text is encoded to bytes
    
    base64_encoded_bytes = base64.b32encode(des_encrypted_bytes)
    
    md5_hash = hashlib.md5(base64_encoded_bytes)
    final_encrypted_code = md5_hash.hexdigest().upper()
    return final_encrypted_code
  except Exception as e:
    print(f"Encryption failed: {e}")  # Consider more robust error handling or logging
    return None


def get_fingerprint():
  """
    Generates a machine fingerprint based on CPU, Disk, and Board serial numbers.

    Returns:
        str: An MD5 hash of the combined serial numbers, in uppercase.
             Returns None if any serial number retrieval fails.
    """
  cpu_serial = PC_detail.get_cpu_serial()
  disk_serial = PC_detail.get_disk_serial()
  board_serial = PC_detail.get_board_serial()
  
  cpu_serial_str = str(cpu_serial) if cpu_serial else ""
  disk_serial_str = str(disk_serial) if disk_serial else ""
  board_serial_str = str(board_serial) if board_serial else ""
  
  hardware_identifiers_str = cpu_serial_str + disk_serial_str + board_serial_str
  hardware_identifiers_bytes = hardware_identifiers_str.encode("utf-8")
  
  fingerprint_hash = hashlib.md5(hardware_identifiers_bytes)
  hardware_fingerprint_md5 = fingerprint_hash.hexdigest().upper()
  return hardware_fingerprint_md5


if __name__ == "__main__":
  machine_fingerprint = get_fingerprint()
  if machine_fingerprint:
    print("Machine Fingerprint:", machine_fingerprint)
    encrypted_fingerprint = encrypted(machine_fingerprint)
    if encrypted_fingerprint:
      print("Encrypted Fingerprint:", encrypted_fingerprint)
    else:
      print("Failed to encrypt the machine fingerprint.")
  else:
    print("Failed to generate machine fingerprint.")
