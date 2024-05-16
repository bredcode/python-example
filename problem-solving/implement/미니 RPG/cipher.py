# pip install cryptography
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import base64
import json

class Cipher():
  # 키 생성 함수
  def generate_key(self, password, salt):
      kdf = Scrypt(
          salt=salt,
          length=32,
          n=2**14,
          r=8,
          p=1,
      )
      key = kdf.derive(password.encode())
      return key

  # 암호화 함수
  def encrypt(self, message, password):
      salt = os.urandom(16)
      key = self.generate_key(password, salt)
      aesgcm = AESGCM(key)
      nonce = os.urandom(12)
      
      # 딕셔너리를 JSON 문자열로 변환
      message_str = json.dumps(message)
      
      encrypted_message = aesgcm.encrypt(nonce, message_str.encode(), None)
      return base64.b64encode(salt + nonce + encrypted_message).decode()

  # 복호화 함수
  def decrypt(self, encrypted_message, password):
      decoded_message = base64.b64decode(encrypted_message.encode())
      salt = decoded_message[:16]
      nonce = decoded_message[16:28]
      ciphertext = decoded_message[28:]
      key = self.generate_key(password, salt)
      aesgcm = AESGCM(key)
      decrypted_message = aesgcm.decrypt(nonce, ciphertext, None)
      
      # JSON 문자열을 딕셔너리로 변환
      return json.loads(decrypted_message.decode())
        
"""
# 예제
cipher = Cipher()
password = "your_password"
message = {"name": "John", "age": 30}
message = json.dumps(message)
encrypted_message = cipher.encrypt(message, password)
print(f"Encrypted: {encrypted_message}")

decrypted_message = cipher.decrypt(encrypted_message, password)
print(f"Decrypted: {decrypted_message}")
"""