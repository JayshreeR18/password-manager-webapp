
from fastapi import APIRouter, HTTPException
from app.models.schema import SignupRequest
from app.utils.storage import save_user
from app.utils.password_utils import hash_password
from app.models.schema import LoginRequest
from app.utils.storage import load_users
from app.utils.password_utils import verify_password
router = APIRouter()

@router.get("/test")
def test_user():
    return {"message": "👤 User route working"}




router = APIRouter()

@router.post("/signup")
def signup(user: SignupRequest):
    hashed_pwd = hash_password(user.password)

    success = save_user(user.username, hashed_pwd)
    if not success:
        raise HTTPException(status_code=400, detail="Username already exists.")
    
    return {"message": "✅ User registered successfully"}


@router.post("/login")
def login(user: LoginRequest):
    users = load_users()

    if user.username not in users:
        raise HTTPException(status_code=401, detail="❌ Invalid username or password")

    hashed_pwd = users[user.username]
    is_valid = verify_password(user.password, hashed_pwd)

    if not is_valid:
        raise HTTPException(status_code=401, detail="❌ Invalid username or password")

    return {"message": "✅ Login successful", "username": user.username}