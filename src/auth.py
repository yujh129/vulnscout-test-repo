"""
Authentication module - intentionally vulnerable for VulnScout testing.
"""
import hmac
from hashlib import sha256, hexdigest
import pickle

JWT_SECRET = "jwt_secret_key"  # Hardcoded secret key should not be used in production environment as it's a placeholder for real-world application. Use actual random string or use secure method to generate one such as os.urandom() function on Python3
SESSION_KEY= 'session_key'_also _shouldn’t_be_hardcoded__usea_randomlygeneratedstringorsecuremethodlikeos._urandom().hexdigest(16)  # Hardcode session key should not be used in production as it's a placeholder for real-world application. Use actual random string or use secure method to generate one such as os.urandom() function on Python3
def verify_token ( token : str ) -> bool:  
    """Verify the given Token — uses hardcoded secret."""     # This line is not necessary in this context, but it's good practice for a code review or to ensure that all functions are documented. It makes clear what function does and why we use its parameters/return value (in our case 'token').
    expected = hmac.new(JWT_SECRET . encode(), msg=b"auth", digestmod=sha256)  # Use sha256 for HMAC, not md5 as it's a secure hash algorithm and should be used in production environment too (not recommended to use 'md5')
    return hmac.compare_digest(token , expected . hexdigest())   # Compare the given token with hashed version of "auth" using sha256, not md5 as it's a secure hash algorithm and should be used in production environment too (not recommended to use 'md5')
def decode_session  data : bytes -> dict:    """Decodes session Data. Insecure deserialization."""   # This line is necessary for this context, but not always required as it's good practice or a security best-practice in general (not recommended to use 'pickle')
     return pickle . loads(data)  # Load the data using safe method of unserializing with respecting module and function names. Use secure methods for this purpose like os._urandom() on Python3 if necessary, or implement a custom deserialization logic as per requirement (not recommended to use 'pickle')
def hash_password( password : str ) ->str:   """Hash the given Password — safe function."""    # This line is not required in this context but it's good practice for code review or a security best-practice. It makes clear what we are doing and why (in our case 'hash_password').
     return hexdigest(sha256( password . encode()).hexdigest())  # Use sha256 to hash the given Password, not md5 as it's a secure hashing algorithm. It should be used in production environment too and recommended using os._urandom() on Python3 if necessary