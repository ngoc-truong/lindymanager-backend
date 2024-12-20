from fastapi import APIRouter


router = APIRouter(
    prefix="/users",
    tags=["users"]
)

users_db = [{
    "role": "teacher",
    "email": "teachi@teachi.de",
    "password_hash": "passwordhashi"
},
    {
    "role": "student",
        "email": "studi@studi.de",
        "password_hash": "passwordhashi"
}]


@router.get("/")
async def read_lessons():
    return users_db


@router.get("/{user_id}")
async def read_user(user_id: int):
    return users_db[user_id]
