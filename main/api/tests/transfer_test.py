import pytest

from src.main.api.models.deposit_request import DepositRequest
from src.main.api.models.transfer_request import TransferRequest


@pytest.mark.api
class TestTransfer:
    def test_transfer_valid(self, api_manager, create_user_request):
        account_from = api_manager.user_steps.create_account(create_user_request)
        account_to = api_manager.user_steps.create_account(create_user_request)

        deposit_request = DepositRequest(accountId=account_from.id, amount=5000)
        api_manager.user_steps.deposit(create_user_request, deposit_request)

        transfer_request = TransferRequest(
            fromAccountId=account_from.id,
            toAccountId=account_to.id,
            amount=1000
        )
        response = api_manager.user_steps.transfer(create_user_request, transfer_request)

        assert response.fromAccountId == account_from.id

    @pytest.mark.parametrize(
        "amount",
        [0, -100, 999999]
    )
    def test_transfer_invalid_amount(self, api_manager, create_user_request, amount):
        account_from = api_manager.user_steps.create_account(create_user_request)
        account_to = api_manager.user_steps.create_account(create_user_request)

        deposit_request = DepositRequest(accountId=account_from.id, amount=5000)
        api_manager.user_steps.deposit(create_user_request, deposit_request)

        transfer_request = TransferRequest(
            fromAccountId=account_from.id,
            toAccountId=account_to.id,
            amount=amount
        )
        api_manager.user_steps.transfer_invalid(create_user_request, transfer_request)