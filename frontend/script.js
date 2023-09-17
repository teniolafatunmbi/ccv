const inputValues = {
    card_number: '',
    cvv: '',
    expiry_date: ''
};

const cardNumber = document.getElementById('card_number');
const cvv = document.getElementById('cvv');
const expiryDate = document.getElementById('expiry_date');
const submitBtn = document.getElementById('submit');
const response = document.getElementById('response');

let formHasErrors = false;

function handleInputChange(element) {
    element.addEventListener("blur", (e) => {
        let value = e.target.value;
        let valueIsEmpty = value.length == 0;
        let errorElem = document.getElementById(`${e.target.name}_error`);

        if (valueIsEmpty) {
            //  notify errors
            errorElem.innerText = `${e.target.name} cannot be empty`;
            errorElem.classList.add('text-rose-900');
            errorElem.classList.add('text-xs');

            // disable button
            submitBtn.disabled = true;
            submitBtn.classList.add('opacity-70');
        }
        runInputChecks();
    });

    element.addEventListener("change", (e) => {
        inputValues[e.target.name] = e.target.value;
    });
};

function runInputChecks() {
    Object.keys(inputValues).forEach((el, _) => { 
        let errorElem = document.getElementById(`${el}_error`);
        let invalidFields = [];
        const inputIsEmpty = inputValues[el].length == 0;

        if (inputIsEmpty) {
            // notify errors
            errorElem.innerText = `${el} cannot be empty`;
            errorElem.classList.add('text-rose-900');
            errorElem.classList.add('text-xs');

            // disable button
            submitBtn.disabled = true;
            submitBtn.classList.add('opacity-70');
            formHasErrors = true;
            invalidFields.push(el)
        } else {
            errorElem.innerText = '';
            errorElem.classList.add('text-rose-900');
            errorElem.classList.add('text-xs');
            
        }

        if (invalidFields.length != 0) {
            formHasErrors = true
        } else {
            formHasErrors = false;
            submitBtn.disabled = false;
            submitBtn.classList.remove('opacity-70')
        }
    })
}

handleInputChange(cardNumber);
handleInputChange(cvv);
handleInputChange(expiryDate);


submitBtn.addEventListener("click", () => {
    // if any of the fields are empty
    runInputChecks();
    if (!formHasErrors) {
        const [month, year] = expiryDate.value.split('/');


        // confirm that card_number is a valid number
        if (isNaN(inputValues.card_number)) {
            formHasErrors = true;
            document.getElementById('card_number_error').innerText = 'Card number is not a valid number';
            return;
        }

        // confirm that month and year have valid values
        if (!month || !year) {
            formHasErrors = true;
            document.getElementById('expiry_date_error').innerText = 'Expiry date is not in the MM/YYYY format';
            return;
        }

        // confirm that month in in the correct format
        if (isNaN(month)) {
            formHasErrors = true;
            document.getElementById('expiry_date_error').innerText = 'Month is not a number';
            return;
        }

        // confirm that month in in the correct format
        if (+month > 12) {
            formHasErrors = true;
            document.getElementById('expiry_date_error').innerText = 'Month cannot be greater than 12';
            return;
        }

        // confirm that month in in the correct format
        if (isNaN(year)) {
            formHasErrors = true;
            document.getElementById('expiry_date_error').innerText = 'Year not a number';
            return;
        }

        // confirm that year in in the correct format
        if (year.length != 4) {
            formHasErrors = true;
            document.getElementById('expiry_date_error').innerText = 'Year is not in the YYYY format';
            return;
        }

        // confirm that cvv is a valid number
        if (isNaN(inputValues.cvv)) {
            formHasErrors = true;
            document.getElementById('cvv_error').innerText = 'CVV is not a valid number';
            return;
        }

        submitBtn.innerText = "Validating ..."
        submitBtn.disabled = true;
        submitBtn.classList.add('opacity-70');

        let payload = {...inputValues};

        payload['expiry_year'] = year
        payload['expiry_month'] = month;

        fetch('/api/v1/validate', {
            method: 'POST',
            headers: { "content-type": "application/json"},
            body: JSON.stringify(payload)
        }).then((res) => {
            let data = res.json();
            if (!res.ok) {
                submitBtn.innerText = "Submit"
                submitBtn.disabled = false; 
                submitBtn.classList.remove('opacity-70')
                return data;
            }
            return data;
            
        }).then((data) => {
            response.innerText = `${data.status}`;

            if (['failed', 'success'].includes(data.status)) {
                response.className = data.status;
            }

            submitBtn.innerText = "Submit";
            submitBtn.disabled = false; 
            submitBtn.classList.remove('opacity-70');
        })
    }
});
