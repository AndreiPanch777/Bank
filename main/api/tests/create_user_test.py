from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.create_user_request import CreateUserRequest
import pytest
from sqlalchemy.orm import Session

from src.main.api.models.create_user_response import CreateUserResponse
from src.main.api.db.crud.user_crud import UserCrudDb as User



@pytest.mark.api
class TestCreateUser:
    def test_create_user_valid(self, api_manager: ApiManager, create_user_request:CreateUserRequest, db_session: Session):
        create_user_request = CreateUserRequest(username="Max32421", password="Pas!sw0rd", role="ROLE_USER")

        response = api_manager.admin_steps.create_user(create_user_request)

        assert create_user_request.username == response.username
        assert create_user_request.role == response.role

        user_from_db = User.get_user_by_username(db_session, create_user_request.username)
        assert user_from_db.username == create_user_request.username, 'Созданного пользователя нет в БД'


    @pytest.mark.parametrize(
        "username, password,",
        [
            ("абв", "Pas!swOrd"),
            ("ab","Pas!swOrd"),
            ("abv!", "Pas!swOrd"),
            ("Maxx1", "Pas!swOrд"),
            ("Maxx2", "Pas!swO"),
            ("Maxx3", "pas!s0rd"),
            ("Maxx4", "PAS!SWORD"),
            ("Maxx5", "PASSWORD"),
            ("Maxx6", "PAS!SWRRD"),



        ]
    )
    def test_creat_user_invalide(self, db_session: Session, username: str, password: str, api_manager: ApiManager):
        create_user_request = CreateUserRequest(username=username, password=password, role="ROLE_USER")
        api_manager.admin_steps.create_invalid_user(create_user_request)

        username_from_db = User.get_user_by_username(db_session, create_user_request.username)

        assert username_from_db is None, 'Пользователь создан, ошибка'

