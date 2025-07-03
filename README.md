# 🧪 Playwright + Pytest Automation Project (UI & API)

This project is a complete automation testing framework using:

- ✅ **Playwright** for Web UI testing
- ✅ **Requests + Pytest** for API testing
- ✅ **Allure** for rich HTML test reports

It includes modular structure, markers for test categorization, and parallel test execution.

---

## 🌐 Tested Websites

- **UI Testing**: [https://automationintesting.online](https://automationintesting.online)
- **API Testing**: [https://restful-booker.herokuapp.com/apidoc/index.html](https://restful-booker.herokuapp.com/apidoc/index.html)

---

## 📁 Project Structure

```
Playwright-restful-booker-project/
│
├── api_tests/               # API automation
│   ├── core/                # API request logic (CRUD)
│   ├── data/                # Request payloads and test data
│   └── tests/               # API test cases
│
├── gui_tests/               # Web UI automation
│   ├── pages/               # Page Object Model (POM)
│   ├── test/                # UI test cases
│   └── utils/               # Base page and utilities
│
├── reports/                 # Allure report output
├── conftest.py              # Global fixtures
├── requirements.txt         # Python dependencies
├── pytest.ini               # Markers & config
└── README.md                # Project documentation
```

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run All Tests

```bash
pytest
```

### 3. Run Tests by Marker

```bash
pytest -m sanity
pytest -m API
pytest -m regression
```

### 4. Run Tests in Parallel (Example: 2 workers)

```bash
pytest -m sanity -n 2
```

---

## 🧪 Markers

Custom markers are defined in `pytest.ini`:

```ini
[pytest]
markers =
    sanity: run test suite of sanity
    regression: run test suite of regression
    production: tests for production environment
    critical: run test suite of critical
    API: run test suite of API
```

Use them like:

```bash
pytest -m critical
```

---

## 📊 Allure Reports

### Generate Report

```bash
pytest --alluredir=reports/allure
```

### View Report

```bash
allure serve reports/allure
```

---

## 🧰 Tech Stack

- **Python 3.11**
- **Playwright**
- **Pytest**
- **Requests**
- **Allure**

---

## 📌 Notes

- You can combine markers and run them in parallel to optimize execution time.
- The project follows **Page Object Model (POM)** for UI tests.
- Test data is separated for better maintainability.