@echo off
:: Create and activate virtual environment
echo Creating virtual environment...
python -m venv venv

:: Activate virtual environment
echo Activating virtual environment...
call .\venv\Scripts\activate

:: Install requirements
echo Installing requirements...
pip install -r requirements.txt

:: Upgrade pip
echo Upgrading pip...
pip install --upgrade pip

:: Run Django server
echo Starting Django server...
python manage.py runserver

pause
