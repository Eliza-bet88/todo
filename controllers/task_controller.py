from sqlalchemy.orm import Session
from models.task import Task

class TaskController:
    
    def create_task(self, session: Session, task_text: str, user_id: int):
        new_task = Task(
            task=task_text,
            status=False,
            user_id=user_id
        )
        
        session.add(new_task)
        session.commit()
        session.refresh(new_task)
        
        return new_task
    
    def get_all_tasks(self, session: Session):
        return session.query(Task).all()
    
    def get_user_tasks(self, session: Session, user_id: int):
        return session.query(Task).filter(Task.user_id == user_id).all()
    
    def get_incomplete_tasks(self, session: Session):
        return session.query(Task).filter(Task.status == False).all()
    
    def get_completed_tasks(self, session: Session):
        return session.query(Task).filter(Task.status == True).all()
    
    def mark_task_done(self, session: Session, task_id: int):
        task = session.query(Task).filter(Task.id == task_id).first()
        
        if not task:
            return None
        
        task.status = True
        session.commit()
        session.refresh(task)
        
        return task
    
    def delete_task(self, session: Session, task_id: int):
        task = session.query(Task).filter(Task.id == task_id).first()
        
        if not task:
            return None
        
        session.delete(task)
        session.commit()
        
        return {"message": "Task deleted"}
