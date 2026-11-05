# Hudl Playwright Test Automation Project

This project is a Playwright test automation framework built with Python and pytest to automate and validate login and authentication workflows on the Hudl website.

The goal of this project was to practice UI automation, Page Object Model design, test case development, and validating different user scenarios across login, credential validation, password visibility, and account navigation.

## Tech Stack

- Python
- Playwright
- pytest
- pytest-repeat
- python-dotenv

## Test Coverage

The test suite covers:

### Authentication

- Verify the Hudl welcome page loads successfully
- Login page loads successfully
- Successful login with valid credentials
- Uppercase email login
- Invalid email format validation
- Invalid credentials validation
- Empty email validation
- Empty password validation

### Password Recovery

- Forgot password navigation
- Forgot password submission and confirmation
- Verify the password visibility toggle
- Navigate back to the email input
- Navigate back to the email input and change email address

## Project Structure

```text
hudl_playwright_login_project/
├── pages/
│   └── login_page.py
├── tests/
│   └── test_login.py
├── utils/
│   └── config.py
├── .env.example
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Setup Instructions

Clone the repository:

```bash
git clone https://github.com/BrooklenBlack/hudl_playwright_login_project.git
cd hudl_playwright_login_project
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

Mac/Linux:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Install Playwright browsers:

```bash
python -m playwright install
```

## Environment Variables

Create a `.env` file in the root of the project using `.env.example` as a guide.

Example:

```env
HUDL_EMAIL=
HUDL_PASSWORD=
BASE_URL=https://www.hudl.com
```

Credentials are stored using environment variables and should not be committed to GitHub.

## Running Tests

Run all tests:

```bash
python -m pytest
```

Run tests with the browser visible:

```bash
python -m pytest --headed --slowmo 1000
```

Run tests five times using pytest-repeat:

```bash
python -m pytest --count=5
```

## Running in Visual Studio Code (Optional)

1. Open the project folder in Visual Studio Code.
2. Install the Python extension.
3. Select the project virtual environment:

```text
Ctrl + Shift + P
Python: Select Interpreter
```

4. Choose the `.venv` interpreter.
5. Run tests from the terminal:

```bash
python -m pytest
```

## Notes

- This project uses the Page Object Model (POM) to separate page interactions from test logic.
- Credentials are handled through environment variables and excluded from version control.
- The tests use Playwright locators based on roles and Hudl's `data-qa-id` attributes.
- The project uses pytest-repeat to run tests multiple times and evaluate test repeatability.
- The tests interact with Hudl's live website
- Some authentication tests interact with real login and password recovery workflows. Repeated login attempts may trigger Hudl's security restrictions such as temporarily blocking your account.
