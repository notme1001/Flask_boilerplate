from .. import fbcrypt

class Encrypt():
    @staticmethod
    def hash_password(password):
        return fbcrypt.generate_password_hash(password).decode('utf-8')

    @staticmethod
    def check_password(dbpassword, password):
        return fbcrypt.check_password_hash(dbpassword, password)
