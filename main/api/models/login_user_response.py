from src.main.api.models.base_model import BaseModel
from src.main.api.models.create_user_response import CreateUserResponse
from src.main.api.models.login_user_response import LoginUserResponse

class User(BaseModel):
    username: str
    role: str



class LoginUserResponse(BaseModel):
    token: str
    user: User