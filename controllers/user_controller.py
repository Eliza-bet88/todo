from sqlalchemy.orm import Session
from models.user import User

class UserController:
    
    def register_user(self, session: Session, email: str, password: str):
        existing_user = session.query(User).filter(User.email == email).first()
        if existing_user:
            return None

        new_user = User(email=email, password=password)

        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        
        return new_user
    
    def login_user(self, session: Session, email: str, password: str):
        user = session.query(User).filter(User.email == email).first()
        
        if not user:
            return None
        if user.password != password:
            return None

        return user
    
    def get_user_by_id(self, session: Session, user_id: int):
        return session.query(User).filter(User.id == user_id).first()
