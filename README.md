# 🕵️ LabsQAharbor Website Automation Testing Project

## Project Description

This automation testing project is developed to ensure the quality and performance of the **LabsQAharbor Limited** website using modern and robust testing tools such as **Playwright**, **pytest**, and the **Page Object Model (POM)** design pattern. 

The main goal of this project is to validate the core functionalities of the web platform, starting with login flows and easily extendable to cover additional areas like form submissions, dashboard verifications, data-driven testing, and visual validations. It enables QA engineers, developers, and CI/CD pipelines to automatically run comprehensive test suites with minimal setup. 

By using Playwright, which supports modern browser automation, this project ensures cross-browser compatibility, accurate DOM inspection, and reliable headless execution support. The use of `pytest` provides powerful test execution, reporting, and scalability for large test suites.

Whether you are a beginner or a seasoned QA engineer, this project offers a clean, reusable structure and a hands-on learning opportunity to adopt industry-standard automation practices.

---

## 🚀 Getting Started

Follow the steps below to install the necessary dependencies, set up the folder structure, and run your test cases successfully.

---

### ✅ Step 1: Install Python and Check Versions

Make sure Python and pip are installed on your system.

```bash
python --version
pip --version
```

---

### ✅ Step 2: Install Required Packages

```bash
pip install pytest
pip install pytest-playwright
pip install playwright
```

---

### ✅ Step 3: Install Browsers for Playwright

```bash
python -m playwright install
```

---

### ✅ Step 4: Project Folder Structure

Your project should be organized as follows:

```
QAHarbor_PageObjectModel_Project/
|-- pytest_cache/
|-- pages/            # Page Object classes
|   |-- _pycache_/
|   |-- acc_page.py
|   |-- account_page.py
|   |-- bookmark_jobpage.py
|   |-- candidate_registration_pa...
|   |-- change_password.py
|   |-- findjobs_page.py
|   |-- home_page.py
|   |-- job_details_page.py
|   |-- login_page.py
|   |-- logout_page.py
|   |-- registration_page.py
|   |-- remove_job.py
|   |-- single_bookmark_jobpage.py
|   |-- single_findjobs_page.py
|   |-- single_job_details_page.py
|   |-- social_pages.py
|   |-- subscribe_page.py
|   |-- update_profile_page.py
|-- tests/            # Test cases using Page Objects
|   |-- _pycache_/
|   |-- information/
|   |-- test_account_creation.py
|   |-- test_apply_jobs.py
|   |-- test_bookmarked_jobs_details.py
|   |-- test_change_acc_pass.py
|   |-- test_home_page.py
|   |-- test_login.py
|   |-- test_logout.py
|   |-- test_profile_completion.py
|   |-- test_qa_social_pages.py
|   |-- test_remove_job.py
|   |-- test_search_jobs.py
|   |-- test_show_applied_jobs.py
|   |-- test_subscribe.py
|-- confest.py
|-- requirements.txt

---
```

### ✅ Step 5: Run the Tests

Navigate to your project directory:

```bash
cd _:\_your_directory where the project stored
```

Run the login test file with browser window:

```bash
python -m pytest tests/test_login.py --headed
```

Run the login test file without browser window (headless):

```bash
python -m pytest tests/test_login.py
```

---

### ✅ Step 6: You will see the expected Output Example:

```text
================================================= test session starts =================================================
platform win32 -- Python 3.12.6, pytest-8.3.5, pluggy-1.5.0 -- C:\Python312\python.exe
cachedir: .pytest_cache
rootdir: ___:\_your_directory
configfile: pytest.ini
collected 2 items

tests/test_login.py::test_login_valid_credentials PASSED

================================================== 2 passed in 5.75s ==================================================
```

---

### ✅ Step 7: Run the Tests with More Detailed Commands

Run all tests together:

```bash
python -m pytest tests/
```

Run all tests with detailed output:

```bash
python -m pytest -v tests/
```

Run specific test file:

```bash
python -m pytest tests/test_example.py
```

Run specific test function inside a test file:

```bash
python -m pytest tests/test_example.py::test_example
```

---

### ✅ Step 8: Exit

Once testing is complete, you're all set. You can expand the framework for new test cases and components.

---

### 🙏 Thank You for Downloading & Using This Automation Project!

Feel free to contribute or customize it for your team or projects.

Automation_Testing_Project_LabsQAharbor_Limited
