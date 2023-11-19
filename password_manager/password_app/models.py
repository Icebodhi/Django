from django.db import models
from cryptography.fernet import Fernet

class Password(models.Model):
    username = models.CharField(max_length=255)
    encrypted_password = models.BinaryField()
    key = models.BinaryField()

    def set_password(self, password):
        key = Fernet.generate_key()
        cipher = Fernet(key)
        encrypted_password = cipher.encrypt(password.encode())
        self.encrypted_password = encrypted_password
        self.key = key

    def get_password(self):
        cipher = Fernet(self.key)
        decrypted_password = cipher.decrypt(self.encrypted_password).decode()
        return decrypted_password