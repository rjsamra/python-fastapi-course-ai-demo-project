from fastapi import FastAPI, HTTPException
from starlette.responses import Response

from app.db.models import UserAnswer
from app.api import api

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Fast API in Python"}


@app.get("/user")
def read_user():
    """
    Return a list of users registered in the system.

    Returns:
        list: list of users
    """
    return api.read_user()


@app.get("/question/{position}", status_code=200)
def read_questions(position: int, response: Response):
    """
    Return a question object from the database given its position.

    Args:
        position (int): the position of the question in the database
        response (Response): the response object

    Returns:
        dict: the question object
    """
    # Read the question by its position
    question = api.read_questions(position)

    # If the question does not exist, return an error
    if not question:
        raise HTTPException(status_code=400, detail="Error")

    # Return the question
    return question


@app.get("/alternatives/{question_id}")
def read_alternatives(question_id: int):
    return api.read_alternatives(question_id)


@app.post("/answer", status_code=201)
def create_answer(payload: UserAnswer):
    payload = payload.dict()

    return api.create_answer(payload)


@app.get("/result/{user_id}")
def read_result(user_id: int):
    return api.read_result(user_id)
