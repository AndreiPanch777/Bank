from src.main.api.db.models.account_table import Account
from sqlalchemy.orm import Session


class AccountCrudDb:
    @staticmethod
    def get_account_by_id(db: Session, account_id: int) -> None:
        return db.query(Account).filter_by(id=account_id).first()

