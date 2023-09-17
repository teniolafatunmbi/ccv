def is_american_express(cvv: str):
    if len(cvv) == 4:
        return True
    return False

def validate_with_luhn_algo(card_number: list[int]):
    check_digit = 0
    pass

def is_empty_string(string: str) -> bool:
    if len(string.strip()) == 0:
        return True
    return False