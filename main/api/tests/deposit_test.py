import pytest

from src.main.api.models.deposit_request import DepositRequest


@pytest.mark.api
class TestDeposit:
    def test_deposit_valid(self, api_manager, create_user_request):
        account = api_manager.user_steps.create_account(create_user_request)

        deposit_request = DepositRequest(accountId=account.id, amount=5000)
        response = api_manager.user_steps.deposit(create_user_request, deposit_request)

        assert response.id == account.id
        assert response.balance == deposit_request.amount

    @pytest.mark.parametrize(
        "amount",
        [0, -100, 999, 9001]
    )
    def test_deposit_invalid_amount(self, api_manager, create_user_request, amount):
        account = api_manager.user_steps.create_account(create_user_request)

        deposit_request = DepositRequest(accountId=account.id, amount=amount)
        api_manager.user_steps.deposit_invalid(create_user_request, deposit_request)