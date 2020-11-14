import os
import sys
from typing import Optional

from fastapi import FastAPI, Request, Body

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
if ROOT_PATH not in sys.path:
    sys.path.append(ROOT_PATH)


from runner import run_spider


app = FastAPI()


@app.get("/ping", response_model=str)
async def ping_pong():
    """
    Respond with a dummy message
    """

    return "pong"


@app.get("/run", response_model=dict)
async def handler():
    """
    Parse request payload and run Scrapy spider.
    """

    result = run_spider()
    return {
        "status": result["status"],
        "data": result.get("results"),
        "message": result.get("message"),
    }
