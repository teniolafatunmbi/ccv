from fastapi import status
from fastapi.responses import JSONResponse

class Messages:
    EXPIRED_CREDIT_CARD = "Expired credit card"
    INVALID_AMERICAN_EXPRESS_CARD = "Invalid American Express credit card"
    INVALID_CREDIT_CARD = "Invalid credit card"


messages = Messages()

class ExpiredCreditCard(JSONResponse):
    def __init__(self) -> None:
        super().__init__({'status': 'failed', 'message': messages.EXPIRED_CREDIT_CARD}, status_code=status.HTTP_403_FORBIDDEN)


class InvalidAmericanExpressCard(JSONResponse):
    def __init__(self) -> None:
        super().__init__({'status': 'failed', 'message': messages.INVALID_AMERICAN_EXPRESS_CARD}, status_code=status.HTTP_403_FORBIDDEN)

class InvalidCreditCard(JSONResponse):
    def __init__(self) -> None:
        super().__init__({'status': 'failed', 'message': messages.INVALID_CREDIT_CARD}, status_code=status.HTTP_403_FORBIDDEN)

