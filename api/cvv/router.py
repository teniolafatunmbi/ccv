from datetime import datetime
from fastapi import APIRouter

from .schema import ValidationPayload
from .service import is_american_express

from .responses import *

router = APIRouter(tags=['Credit Card Validator'])

@router.post('/api/v1/validate')
async def validate_credit_card(payload: ValidationPayload):
    """
        Validates credit card 

        :param expiry_month: The expiry month of the credit card
        :param expiry_year: The expiry month of the credit card
        :param card_number: The card number on the credit card
        :param cvv: The CVV number on the credit card
    """
    current_date = datetime.now()
    current_year = current_date.today().year
    current_month = current_date.today().month

    # if expiry year of credit card less than current date, raise ExpiredCreditCard exception
    if payload.expiry_year < current_year:
        return ExpiredCreditCard()
    
        # elif expiry month is greater than current month, raise ExpiredCreditCard exception
    if (payload.expiry_year < current_year) and (payload.expiry_month < current_month):
        return ExpiredCreditCard()

    if is_american_express(payload.cvv):
        # if cvv is american express, pan card number must start with 34 or 37
        if (str(payload.card_number).startswith('34') or str(payload.card_number).startswith('34')) == False:
            return InvalidAmericanExpressCard()
    
    card_no_is_within_range = len(str(payload.card_number)) >= 16 and len(str(payload.card_number)) <= 19

    if not card_no_is_within_range:
        return InvalidCreditCard()
    
    # validate with luhn's algorithm

    return { 'status': 'success' }
