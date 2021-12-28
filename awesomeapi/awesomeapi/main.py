""" An awesome API built with FastAPI. """

from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    """root: Root endpoint. Returns "Hello".

    Returns:
        dict: A dictionary containing the string "Hello".
    """
    return JSONResponse({"message": "Hello"})

@app.get("/path/{path_param}")
def echo_path_param(path_param: str):
    """echo_path_param: Echo path parameter endpoint. Returns the path parameter.

    Args:
        path_param (str): The path parameter.

    Returns:
        dict: A dictionary containing the path parameter.
    """
    return JSONResponse({"message": path_param})

@app.get("/query")
def echo_query_param(query_param: str):
    """echo_query_param: Echo query parameter endpoint. Returns the query parameter.

    Args:
        query_param (str): The query parameter.

    Returns:
        dict: A dictionary containing the query parameter.
    """
    return JSONResponse({"message": query_param})
