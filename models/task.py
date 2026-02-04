from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from models.database import Base

class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, nullable=False)
    status = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    user = relationship("User", back_populates="tasks")
