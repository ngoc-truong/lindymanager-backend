# Lindyhop Manager

The backend for the platform to create and plan lindy hop courses.

# Functionalities (as user stories)

- As a teacher I want to create slots for a lindy hop lesson so that I can plan a lesson in detail.
- As a teacher I want to see whether students will come to my class to plan the lesson accordingly (e.g. are they enough leaders/followers, how many will participate).
- As a teacher and as a student I want to have a calender so that I know exactly when the lessons will take place and what we have practiced on which day.
- As a student I want to view summaries of a lesson so that I can decide whether I want to participate or not.

## Nice-to-have

- As a teacher I want to have the summaries of a lesson created automatically based on my slots (A.I.).
- As a student I want to have more additional information (e.g. videos, blog articles, pictures) for the content of the lesson so that I can deep dive into the course material.
- As a student I want to comment on classes to ask questions so that I can improve my dancing.
- As a teacher I want to answer these comments to get immediate feedback and imporve my classes.

# Models

User

- id: str
- role: str, Values can be teacher or student
- email: str
- password_hash: str
- picture_url
- teacher has_many: lessons
- teacher has_many: comments
- student has_many: lessons
- student has_many: comments

Lesson

- id: str
- title: str
- description: str
- date: datetime
- has_many: teachers
- has_many: students
- has_many: comments

Slot

- id: str
- title: str
- description: str
- task: str
- has_many lessons (can belong to several lessons)
- has_many musics

Music

- id: str
- artist: str
- title: str
- has_many slots

## Nice-to-have models

Comment

- id: str
- description: str
- belongs_to: teacher/student
- belongs_to: lesson
