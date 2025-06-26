from fastapi import APIRouter, HTTPException
from app.models.schema import VaultEntryRequest
from app.utils.crypto import derive_key, encrypt_data
from app.utils.storage import save_password
from app.models.schema import VaultViewRequest
from app.utils.storage import load_passwords
from app.utils.crypto import derive_key, decrypt_data
router = APIRouter(prefix="/vault", tags=["Vault"])

@router.post("/add")
def add_entry(entry: VaultEntryRequest):
    try:
        # Use static salt for now (can be replaced with user-specific salt from file later)
        salt = b"static_salt_123456"
        
        key = derive_key(entry.master_password, salt)
        encrypted_password = encrypt_data(entry.password, key)

        # Save the entry under the user
        save_password(
            username=entry.username,
            website=entry.website,
            login=entry.username,
            encrypted_password=encrypted_password
        )
        return {"message": "✅ Password saved securely."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/view")
def view_passwords(request: VaultViewRequest):
    try:
        # Derive decryption key
        salt = b"static_salt_123456"  # same salt used for encryption
        key = derive_key(request.master_password, salt)

        # Load all saved data
        data = load_passwords()
        user_data = data.get(request.username)

        if not user_data:
            raise HTTPException(status_code=404, detail="No saved passwords found for this user.")

        decrypted_entries = []
        for entry in user_data:
            try:
                decrypted_pwd = decrypt_data(entry["password"], key)
            except Exception:
                decrypted_pwd = "🔐 DECRYPTION_FAILED"
            decrypted_entries.append({
                "website": entry["website"],
                "login": entry["username"],
                "password": decrypted_pwd
            })

        return {"entries": decrypted_entries}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))