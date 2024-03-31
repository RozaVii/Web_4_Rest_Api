from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse, FileResponse
from sqlalchemy.orm import Session
import models
from database import engine, session_local
import uvicorn


app = FastAPI()

models.base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = session_local()
        yield db
    finally:
        db.close()


class Demon(BaseModel):
    name: str = Field(min_length=1)
    todo: str = Field(min_length=1)


@app.get("/")
def get_api():
    return {"message": "working"}

@app.post("/user")
def create_demon(demon: Demon):
    demon_model = models.Demons()
    demon_model.name = demon.name
    demon_model.todo = demon.todo

    db = session_local()
    db.add(demon_model)
    db.commit()

    return demon

@app.get("/todo")
def get_todo():
    db = session_local()
    res = db.query(models.Demons).all()
    db.close()
    return res

@app.put("/todo/{user_id}")
def edit_demon(user_id: int, demon: Demon):
    db = session_local()

    user = db.query(models.Demons).filter(models.Demons.id == user_id).first()
    if user == None:
        return JSONResponse(status_code=404, content={"message": "User is not found"})

    user.todo = demon.todo
    db.commit()

    db.close()
    return {"message": "Change is complete"}

@app.delete("/user/{user_id}")
def delete_demon(user_id: int):
    db = session_local()

    user = db.query(models.Demons).filter(models.Demons.id == user_id).first()
    if user == None:
        return JSONResponse(status_code=404, content={"message": "User is not found"})

    db.delete(user)
    db.commit()

    db.close()
    return {"message": "The user has been successfully deleted"}