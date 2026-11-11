from enum import Enum
from src.main.api.models.base_model import BaseModel
from typing import Optional, Type
from dataclasses import dataclass
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.create_user_response import CreateUserResponse, LoginUserResponse
from src.main.api.models.login_user_request import LoginUserRequest
from src.main.api.models.deposit_request import DepositRequest
from src.main.api.models.deposit_response import DepositResponse
from src.main.api.models.transfer_request import TransferRequest
from src.main.api.models.transfer_response import TransferResponse
from src.main.api.models.credit_request import CreditRequest
from src.main.api.models.credit_response import CreditResponse
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.credit_repay_response import CreditRepayResponse


@dataclass
class EndpointConfiguration:
    url: str
    requests_model: Optional[Type[BaseModel]]
    response_model: Optional[Type[BaseModel]]


class Endpoint(Enum):
    ADMIN_CREATE_USER = EndpointConfiguration(
        requests_model=CreateUserRequest,
        url="/admin/create",
        response_model=CreateUserResponse
    )

    ADMIN_DELETE_USER = EndpointConfiguration(
        requests_model=None,
        url="/admin/users",
        response_model=None
    )

    LOGIN_USER = EndpointConfiguration(
        requests_model=LoginUserRequest,
        url="/auth/token/login",
        response_model=LoginUserResponse
    )

    CREATE_ACCOUNT = EndpointConfiguration(
        requests_model=None,
        url="/account/create",
        response_model=CreateAccountResponse
    )

    ACCOUNT_DEPOSIT = EndpointConfiguration(
        requests_model=DepositRequest,
        url="/account/deposit",
        response_model=DepositResponse
    )

    ACCOUNT_TRANSFER = EndpointConfiguration(
        requests_model=TransferRequest,
        url="/account/transfer",
        response_model=TransferResponse
    )

    CREDIT_REQUEST = EndpointConfiguration(
        requests_model=CreditRequest,
        url="/credit/request",
        response_model=CreditResponse
    )

    CREDIT_REPAY = EndpointConfiguration(
        requests_model=CreditRepayRequest,
        url="/credit/repay",
        response_model=CreditRepayResponse
    )





