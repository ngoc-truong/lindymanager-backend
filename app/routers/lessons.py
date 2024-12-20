from fastapi import APIRouter
import datetime

router = APIRouter(
    prefix="/lessons",
    tags=["lessons"]
)

lessons_db = [{
    "title": "Rock Steps",
    "description": "We practice rock steps",
    "date": datetime.datetime(2020, 4, 25, 18, 23)
},
    {
        "title": "Triple Steps",
        "description": "A triple step",
        "date": datetime.datetime(2020, 4, 25, 18, 23)
}]


@router.get("/")
async def read_lessons():
    return lessons_db


@router.get("/{lesson_id}")
async def read_lessons(lesson_id: int):
    return lessons_db[lesson_id]
