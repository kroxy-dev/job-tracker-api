from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from models import Application
from fastapi import FastAPI, Depends, HTTPException


Base.metadata.create_all(bind=engine)

app = FastAPI()

class ApplicationSchema(BaseModel):
    company: str
    position: str
    status: str
    notes: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/applications")
def add_application(data: ApplicationSchema, db: Session = Depends(get_db)):
    new_app = Application(**data.model_dump())
    db.add(new_app)
    db.commit()
    db.refresh(new_app)
    return new_app

@app.get("/applications")
def get_applications(db: Session = Depends(get_db)):
    return db.query(Application).all()


@app.delete("/applications/{id}")
def delete_application(id: int, db: Session = Depends(get_db)):
    app = db.query(Application).filter(Application.id == id).first()
    if app is None:
        raise HTTPException(status_code=404, detail="Application not found")
    db.delete(app)
    db.commit()
    return {"status": "deleted"}

@app.put("/application/{id}")
def update_application(data:ApplicationSchema ,id:int,db:Session =Depends(get_db)):
    app=db.query(Application).filter(Application.id==id).first()
    if app is None:
        raise HTTPException(status_code=404,detail="Application not found")
    app.company = data.company
    app.position = data.position
    app.status = data.status
    app.notes = data.notes
    db.commit()
    db.refresh(app)
    return app