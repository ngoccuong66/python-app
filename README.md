## install env
python -m venv venv

Windows:
    - Cmd: .\venv\Scripts\activate

## environment with ``PIP``

pip install -r requirements.txt

## run project 

uvicorn app.main:app --port 8000 --reload