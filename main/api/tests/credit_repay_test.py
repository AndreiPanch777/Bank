import pytest

from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.credit_request import CreditRequest


@pytest.mark.api
class TestCreditRepay:
    def test_credit_repay_forbidden_for_user(self, api_manager, create_user_request):
        account = api_manager.user_steps.create_account(create_user_request)

        repay_request = CreditRepayRequest(creditId=1, accountId=account.id, amount=1000)
        api_manager.user_steps.repay_credit_forbidden(create_user_request, repay_request)

    def test_credit_repay_valid(self, api_manager, credit_user_request):
        account = api_manager.user_steps.create_account(credit_user_request)
        credit = api_manager.user_steps.request_credit(
            credit_user_request,
            CreditRequest(accountId=account.id, amount=5000, termMonths=12),
        )

        repay_request = CreditRepayRequest(creditId=credit.creditId, accountId=account.id, amount=5000)
        response = api_manager.user_steps.repay_credit(credit_user_request, repay_request)


        assert response.creditId == credit.creditId
        assert response.amountDeposited == repay_request.amount

        assert response.creditId == credit.creditId

    @pytest.mark.parametrize("amount", [0, -100])
    def test_credit_repay_invalid_amount(self, api_manager, credit_user_request, amount):
        account = api_manager.user_steps.create_account(credit_user_request)
        credit = api_manager.user_steps.request_credit(
            credit_user_request,
            CreditRequest(accountId=account.id, amount=5000, termMonths=12),
        )

        repay_request = CreditRepayRequest(creditId=credit.creditId, accountId=account.id, amount=amount)
        api_manager.user_steps.repay_credit_invalid(credit_user_request, repay_request)

