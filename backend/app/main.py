from fastapi import FastAPI
from app.routes import user,vault # you'll connect user routes here

app = FastAPI()

# Root route to test the API
@app.get("/")
def home():
    return {"message": "🔐 Password Manager API is live!"}

# Include user-related routes
app.include_router(user.router, prefix="/user")
app.include_router(user.router)
app.include_router(vault.router) 