from pydantic import BaseModel, root_validator
from fastapi.exceptions import HTTPException

class ValidationPayload(BaseModel):
    expiry_year: int
    expiry_month: int
    cvv: str
    card_number: int

    @root_validator(pre=True)
    def validate_values(cls, values):
        def is_empty_string(string: str) -> bool:
            if len(string.strip()) == 0:
                return True
            return False
        card_number = values.get('card_number')
        cvv = values.get('cvv')
        expiry_year = values.get('expiry_year')
        expiry_month = values.get('expiry_month')

        if is_empty_string(expiry_year):
            raise HTTPException(status_code=400, detail='expiry_year cannot be empty')
        if is_empty_string(expiry_month):
            raise HTTPException(status_code=400, detail='expiry_month cannot be empty')
        if is_empty_string(cvv):
            raise HTTPException(status_code=400, detail='cvv cannot be empty')
        if is_empty_string(card_number):
            raise HTTPException(status_code=400, detail='card_number cannot be empty')
        
        if int(expiry_month) > 12:
            raise HTTPException(status_code=400, detail='expiry_month cannot be greater than 12')

        if len(str(expiry_year)) != 4:
            raise HTTPException(status_code=400, detail='expiry_year must be in the YYYY format')
        
        return values
    
class ValidationResponse(BaseModel):
    message: str
    status: str