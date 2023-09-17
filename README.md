# A simple credit card validator
A simple service for validate credit cards enhanced with [Luhn's algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm).

# Requirements
- Python v3.9+
- Pip v20+
- Unix-based OS.

# Setup
1. Clone this Github Repo to your computer.
```sh 
    git clone https://github.com/teniolafatunmbi/cvv.git
```

2. Install [Python]('https://www.python.org/downloads/'), if you don't have it installed on your PC. An installation comes with Pip.

3. Create a virtual environment for the project.
```sh
    python3 -m venv .venv 
```

4. Activate the virtual environment.
```sh
    source .venv/bin/activate
```

4. Install project dependencies.
```sh
    pip install -r requirements.txt
```

5. Run `python main.py` to start the app.

6. Visit `http://localhost:7001` to verify that the server is running.

# Usage
Ensure you have an internet connection to load the minimal styles on the frontend from Tailwind CDN.
- The API documentation is at `http://localhost:7001/docs`
- The validate endpoint is at `http://localhost:7001/api/v1/validate`.
- The UI for credit card validation is at `http://localhost:7001/app`.
