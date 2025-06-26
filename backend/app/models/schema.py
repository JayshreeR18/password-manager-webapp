from pydantic import BaseModel

class SignupRequest(BaseModel):
    username: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str

class MasterPasswordRequest(BaseModel):
    master_password: str


class VaultEntryRequest(BaseModel):
    username: str          # user identifier
    website: str           # e.g. "gmail.com"
    login: str             # e.g. "jay123@gmail.com"
    password: str          # to be encrypted
    master_password: str   # used for encryption


class VaultViewRequest(BaseModel):
    username: str
    master_password: str
