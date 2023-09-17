from datetime import datetime
from .schema import ValidationPayload
from .responses import *

def is_american_express(cvv: str):
    if len(cvv) == 4:
        return True
    return False


def luhn_checksum(card_number: str):
    card_number = [int(d) for d in str(card_number)]
    
    # get all odd numbers
    oddly_placed_numbers = card_number[-1::-2]

    # get all even numbers
    evenly_placed_numbers = card_number[-2::-2]

    # sum all odd numbers
    odd_nos_sum = sum(oddly_placed_numbers)
    even_nos_sum = 0

    for num in evenly_placed_numbers:
        num_double = num * 2 #double even number

        # if the len of the double is two digits, sum the individual digits, and add the sum to the even_nos_sum
        if len(str(num_double)) == 2:
            num_double = sum([int(d) for d in str(num_double)])
            even_nos_sum += num_double 
        else:
            even_nos_sum += num_double

    checksum = odd_nos_sum + even_nos_sum
    print(checksum)

    if (checksum % 10) != 0:
        return False
    return True


def validate_credit_card(payload: ValidationPayload):
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
    

    if not luhn_checksum(payload.card_number):
        return InvalidCreditCard()
    
    return { 'status' : 'success' }