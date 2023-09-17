from datetime import datetime
from fastapi import APIRouter

from .schema import ValidationPayload
import api.cvv.service as service

from .responses import *

router = APIRouter(tags=['Credit Card Validator'])

@router.post('/api/v1/validate')
def validate_credit_card(payload: ValidationPayload):
    """
        Validates credit card 

        :param expiry_month: The expiry month of the credit card
        :param expiry_year: The expiry month of the credit card
        :param card_number: The card number on the credit card
        :param cvv: The CVV number on the credit card
    """
    response = service.validate_credit_card(payload)
    
    # validate with luhn's algorithm

    return response
