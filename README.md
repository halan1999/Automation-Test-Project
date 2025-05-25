# Automation-Test-Project

This repository demonstrates automated UI testing using Playwright with Pytest, integrated with GitHub Actions for CI/CD.


## 🛠 Tools & Technologies

- [Playwright](https://playwright.dev/)
- Pytest
- GitHub Actions
- HTML Test Report
- Python 3.10+

## 📁 Project Structure
Automation-Test-Project/
│
├── tests/ #Test cases folder
│ └── test_demo.py # Main demo test file
├── .github/workflows/ci.yml # GitHub Actions CI pipeline
├── README.md # This file
└── requirements.txt # Python dependencies


##  How to Run Locally

**Clone this repository**
```bash
git clone https://github.com/halan1999/Automation-Test-Project.git
cd Automation-Test-Project
Create and activate a virtual environment

python3 -m venv venv
source venv/bin/activate
Install dependencies

pip install -r requirements.txt
playwright install
Run tests (headless or with UI)

# With UI and slow steps
pytest tests/ --headed --slowmo=1000 --html=report.html --self-contained-html

#Test Report
After running, a file named report.html will be generated in the project root.
You can open it in your browser to see detailed results, including pass/fail and screenshots on failure.

# CI/CD - GitHub Actions
This repository includes a GitHub Actions pipeline that runs tests automatically on every push.

See: .github/workflows/ci.yml

#Screenshots
Screenshots will be automatically saved if a test fails (see pytest-playwright feature).
View the HTML report for embedded screenshots.
