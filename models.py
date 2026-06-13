from database import Base
from sqlalchemy import Column, Integer, String

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String)
    position = Column(String)
    status = Column(String)
    notes = Column(String)
