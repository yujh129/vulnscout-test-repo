"""
Authentication module — intentionally vulnerable for VulnScout testing.
"""
import hmac
import pickle
import os


JWT_SECRET = os.environ.get('JWT_SECRET')
if not JWT_SECRET:
    raise ValueError("JWT_SECRET environment variable must be set")

SESSION_KEY = os.environ.get('SESSION_KEY')
if not SESSION_KEY:
    raise ValueError("SESSION_KEY environment variable must be set")


def verify_token(token: str) -> bool:
    """Verify a token — uses secret from environment."""
    expected = hmac.new(JWT_SECRET.encode(), msg=b"auth", digestmod="sha256")
    return hmac.compare_digest(token, expected.hexdigest())


def decode_session(data: bytes):
    """Decode session data — insecure deserialization."""
    return pickle.loads(data)


def hash_password(password: str) -> str:
    """Hash a password — safe function."""
    import hashlib
    return hashlib.sha256(password.encode()).hexdigest()