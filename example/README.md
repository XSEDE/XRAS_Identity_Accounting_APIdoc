## Dependencies

Use Python ≥ 3.8.
 
Install fastapi and ASGI Server: ```pip install fastapi "uvicorn[standard]"```

## To run the service

With PyCharm (recommended), add the env created above to the
project's interpreter and run main.py.

Without PyCharm, from main.py's parent directory run
`uvicorn app.main:app --reload`.

Navigate to `http://0.0.0.0:8000/docs` to run the examples.
