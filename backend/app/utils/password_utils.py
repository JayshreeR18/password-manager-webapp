from passlib.context import CryptContext

# Set up a hashing context using bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to hash a plain password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Function to verify a plain password against a hashed one
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
