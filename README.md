# Playwright UI & API Restful Booker Project

A comprehensive test automation framework for UI and API testing using **Playwright** and **Pytest**.

## 🚀 Installation

To set up the project and install dependencies:

```bash
git clone https://github.com/yourusername/playwright-ui-api-restful-booker-project.git
cd playwright-ui-api-restful-booker-project
pip install -r requirements.txt
playwright install
```

## 🧪 Usage

1. Open the project in PyCharm or any other IDE
2. Run all tests:
```bash
pytest
```
3. Run tests with specific browser:
```bash
pytest --browser=firefox
pytest --browser=webkit
pytest --browser=chromium
```
4. Run tests by markers:
```bash
pytest -m sanity
pytest -m API
```
5. Generate Allure reports:
```bash
allure serve allure-results
```

## ⚙️ Configuration

The project includes a `pytest.ini` configuration file with the following settings:

```ini
[pytest]
addopts = -v --headed --video=retain-on-failure --alluredir=reports/allure/ ./tests

markers =
    sanity: run test suite of sanity
    regression: run test suite of regression
    production: tests for production environment
    critical: run test suite of critical
    API: run test suite of API
```

### Supported Browsers
- **Chromium** (default)
- **Firefox**
- **WebKit** (Safari)

## 📁 Project structure

```
playwright-ui-api-restful-booker-project/
├── tests/
│   ├── api/
│   │   ├── helpers/
│   │   │   └── booking_requests.py
│   │   ├── test_create_booking_update_delete.py
│   │   ├── conftest.py
│   │   └── base.py
│   ├── ui/
│   │   ├── pages/
│   │   │   └── Edit_page.py
│   │   └── BasePage.py
├── data/
│   └── api_data.py
├── reports/
│   └── allure/
├── requirements.txt
├── pytest.ini
└── README.md
```

#
## 📊 Allure Reports

Allure allows you to generate beautiful and detailed test reports.

### Installation
```bash
pip install allure-pytest
```

### To see the Allure report at the end of the tests run:
```bash

allure serve reports/allure/
```

## 🐞 Known Issues
- Some UI elements may not render correctly depending on the browser version
- API tests may fail if the backend server is unavailable. Check network connectivity and server status
- Video recording is enabled by default and retained only on test failures
