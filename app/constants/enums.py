from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"
    MODERATOR = "moderator"

class BookingStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
    COMPLETED = "completed"

class PaymentStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    FAILED = "failed"
    REFUNDED = "refunded"
