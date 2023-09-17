from pydantic import BaseModel, root_validator
from fastapi.exceptions import HTTPException

from .service import is_empty_string
class ValidationPayload(BaseModel):
    expiry_year: int
    expiry_month: int
    cvv: str
    card_number: int

    @root_validator(pre=True)
    def validate_empty_strings(cls, values):
        if is_empty_string(values.get('expiry_year')):
            raise HTTPException(status_code=400, detail='expiry_year cannot be empty')
        if is_empty_string(values.get('expiry_month')):
            raise HTTPException(status_code=400, detail='expiry_month cannot be empty')
        if is_empty_string(values.get('cvv')):
            raise HTTPException(status_code=400, detail='cvv cannot be empty')
        if is_empty_string(values.get('card_number')):
            raise HTTPException(status_code=400, detail='card_number cannot be empty')
        
        return values