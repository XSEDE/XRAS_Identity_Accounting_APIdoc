To install the dependencies:
1. Start from a Python>=3.8 environment. 
2. Install fastpi: ```pip install fastapi```
3. Install ASGI Server: ```pip install "uvicorn[standard]"``` 

I recommend using PyCharm to run the service. Once you installed the dependencies, add the env created above to the
project's interpreter and run main.py. If not, navigate to the parent directory of main.py and run 
`uvicorn app.main:app --reload`

Once it's running, navigate to `http://0.0.0.0:8000/docs` to run the examples.