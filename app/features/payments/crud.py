from app.core.base_crud import BaseCRUD
from .models import Payment
from .schemas import PaymentCreate, PaymentUpdate

class CRUDPayment(BaseCRUD[Payment, PaymentCreate, PaymentUpdate]):
    pass

payment = CRUDPayment(Payment)
