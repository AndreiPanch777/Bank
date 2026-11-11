import pytest

from src.main.api.models.credit_request import CreditRequest


@pytest.mark.api
class TestCreditRequest:
    def test_credit_request_forbidden_for_user(self, api_manager, create_user_request):
        account = api_manager.user_steps.create_account(create_user_request)

        credit_request = CreditRequest(accountId=account.id, amount=5000, termMonths=12)
        api_manager.user_steps.request_credit_forbidden(create_user_request, credit_request)

    def test_credit_request_valid(self, api_manager, credit_user_request):
        account = api_manager.user_steps.create_account(credit_user_request)

        credit_request = CreditRequest(accountId=account.id, amount=5000, termMonths=12)
        response = api_manager.user_steps.request_credit(credit_user_request, credit_request)

        assert response.balance == credit_request.amount

    @pytest.mark.parametrize(
        "amount, term_months",
        [
            (4900, 12),
            (15100, 12),
            (0, 12),
            (-100, 12),
            (5000, 0),
            (5000, -1),
        ]
    )
    def test_credit_request_invalid(self, api_manager, credit_user_request, amount, term_months):
        account = api_manager.user_steps.create_account(credit_user_request)

        credit_request = CreditRequest(accountId=account.id, amount=amount, termMonths=term_months)
        api_manager.user_steps.request_credit_invalid(credit_user_request, credit_request)