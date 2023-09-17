from datetime import datetime
from fastapi.testclient import TestClient
from main import app

test_client = TestClient(app)

def test_expired_credit_card():
    card_details = {
        "card_number": "82309240293382",
        "expiry_year": datetime.now().year - 2,
        "expiry_month": datetime.now().month + 5,
        "cvv": "232",
    }
    response = test_client.post('/api/v1/validate', json=card_details)

    assert response.status_code == 403
    data = response.json()
    assert data['status'] == "failed"

def test_american_express_credit_card():
    card_details = {
        "card_number": "3482093029049203942",
        "expiry_year": datetime.now().year - 2,
        "expiry_month": datetime.now().month + 5,
        "cvv": "232",
    }
    pass

def test_invalid_credit_card():
    card_details = {
        "card_number": "823382",
        "expiry_year": datetime.now().year - 2,
        "expiry_month": datetime.now().month + 5,
        "cvv": "232",
    }
    pass

def test_luhn_algo_validator():
    pass

def test_correct_credit_card():
    card_details = {
        "card_number": "82983023892840923",
        "expiry_year": datetime.now().year +1,
        "expiry_month": datetime.now().month + 5,
        "cvv": "232",
    }
    pass

def test_correct_american_express_credit_card():
    pass