from app.core.base_crud import CRUDBase
from .models import Payment
from .schemas import PaymentCreate

class CRUDPayment(CRUDBase[Payment, PaymentCreate, PaymentCreate]):
    pass

payment = CRUDPayment(Payment)
