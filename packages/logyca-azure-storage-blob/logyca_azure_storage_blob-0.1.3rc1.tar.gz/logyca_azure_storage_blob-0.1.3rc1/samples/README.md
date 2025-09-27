## Python

    - Version 3.11+

## Python Virtual environment
```Powershell
C:\python\python311\python.exe --version
C:\python\python311\python.exe -m pip install --upgrade pip
C:\python\python311\python.exe -m pip install virtualenv --upgrade
```

## Install virtual environment
```Powershell
C:\python\python311\python.exe -m virtualenv venv
```

## Activate
```Powershell
.\venv\Scripts\activate
python --version
python -m pip install --upgrade pip
```

## Install packages
```Powershell
# for each microservice
pip install -r .\AzFuncSqlScriptsRunner\requirements.txt
pip install -r .\AzFuncReportExecutorBySteps\requirements.txt
pip install -r .\commonlib\requirements.txt
# for debug
pip install -r .\requirements-debug.txt
```

