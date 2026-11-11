from src.main.api.models.base_model import BaseModel


class CreditResponse(BaseModel):
    creditId: int
    balance: float