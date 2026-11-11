
from src.main.api.specs.response_specs import ResponseSpecs

from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requester.validate_crud_requester import ValidateCrudRequester
from src.main.api.requests.create_user_requester import CreateUserRequest
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.steps.base_steps import BaseSteps
from src.main.api.models.deposit_request import DepositRequest
from src.main.api.foundation.requester.crud_requester import CrudRequester
from src.main.api.models.transfer_request import TransferRequest
from src.main.api.models.credit_request import CreditRequest
from src.main.api.models.credit_repay_request import CreditRepayRequest



class UserSteps(BaseSteps):
    def create_account(self, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_created()
        ).post(None)
        return response


    def deposit(self, create_user_request: CreateUserRequest, deposit_request: DepositRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.ACCOUNT_DEPOSIT,
            ResponseSpecs.request_ok()
        ).post(deposit_request)
        return response

    def deposit_invalid(self, create_user_request: CreateUserRequest, deposit_request: DepositRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.ACCOUNT_DEPOSIT,
            ResponseSpecs.request_bad()
        ).post(deposit_request)

    def transfer(self, create_user_request: CreateUserRequest, transfer_request: TransferRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.ACCOUNT_TRANSFER,
            ResponseSpecs.request_ok()
        ).post(transfer_request)
        return response

    def transfer_invalid(self, create_user_request: CreateUserRequest, transfer_request: TransferRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.ACCOUNT_TRANSFER,
            ResponseSpecs.request_bad()
        ).post(transfer_request)

    def request_credit(self, create_user_request: CreateUserRequest, credit_request: CreditRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREDIT_REQUEST,
            ResponseSpecs.request_ok()
        ).post(credit_request)
        return response

    def request_credit_invalid(self, create_user_request: CreateUserRequest, credit_request: CreditRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREDIT_REQUEST,
            ResponseSpecs.request_bad()
        ).post(credit_request)

    def request_credit(self, create_user_request: CreateUserRequest, credit_request: CreditRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREDIT_REQUEST,
            ResponseSpecs.request_created()
        ).post(credit_request)
        return response

    def request_credit_forbidden(self, create_user_request: CreateUserRequest, credit_request: CreditRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREDIT_REQUEST,
            ResponseSpecs.request_forbidden()
        ).post(credit_request)

    def repay_credit(self, create_user_request: CreateUserRequest, repay_request: CreditRepayRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREDIT_REPAY,
            ResponseSpecs.request_ok()   # если придёт 201, замени на request_created()
        ).post(repay_request)
        return response

    def repay_credit_invalid(self, create_user_request: CreateUserRequest, repay_request: CreditRepayRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREDIT_REPAY,
            ResponseSpecs.request_bad()
        ).post(repay_request)

    def repay_credit_forbidden(self, create_user_request: CreateUserRequest, repay_request: CreditRepayRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREDIT_REPAY,
            ResponseSpecs.request_forbidden()
        ).post(repay_request)

