from pydantic import BaseModel
from enum import Enum
import datetime


class RoleEnum(str, Enum):
    teacher: str = "teacher"
    student: str = "student"


class User(BaseModel):
    role: RoleEnum
    email: str
    password_hash: str


class Lesson(BaseModel):
    title: str
    description: str
    date: datetime


class Slot(BaseModel):
    title: str
    description: str
    task: str


class Music(BaseModel):
    artist: str
    title: str
