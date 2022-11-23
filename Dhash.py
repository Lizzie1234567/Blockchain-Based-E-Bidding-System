import hashlib

class Dhash:

    def sha256(self, pattern) -> str:
        if not isinstance(pattern, (bytes, bytearray, str)):
            raise TypeError("pattern should be bytes, bytearray or string")
        if isinstance(pattern, str):
            pattern = pattern.encode("utf-8")
        return hashlib.sha256(pattern).hexdigest()

    def Dhash(self, str1):
        return self.sha256(self.sha256(str1))
