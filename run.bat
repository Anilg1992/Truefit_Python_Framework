cd /d %~dp0
pip install selenium
pip install behave
pip install allure-behave
pip install pytest
behave -f allure_behave.formatter:AllureFormatter -o ./reports/ ./features
pause