from sqlalchemy.orm import Session
from models.user import User
from models.token import Token
from token_fun import generate_token, get_expiry_time
from datetime import datetime

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
    
    def create_token(self, session: Session, user_id: int):
        token_str = generate_token()
        expires_at = get_expiry_time()
        
        new_token = Token(
            user_id=user_id,
            token=token_str,
            expires_at=expires_at
        )
        
        session.add(new_token)
        session.commit()
        
        return token_str
    
    def get_user_id_by_token(self, session: Session, token: str):
        token_obj = session.query(Token).filter(Token.token == token).first()
        
        if not token_obj:
            return None
        
        if token_obj.expires_at < datetime.now():
            return None
        
        return token_obj.user_id
    
    def get_user_by_id(self, session: Session, user_id: int):
        return session.query(User).filter(User.id == user_id).first()
