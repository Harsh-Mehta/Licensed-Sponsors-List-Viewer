from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Annotated
from contextlib import asynccontextmanager

import logging
from utils import read_data, download_latest_data


@asynccontextmanager
async def lifespan(app: FastAPI):
    download_latest_data()
    yield


app = FastAPI(lifespan=lifespan)
templates = Jinja2Templates(directory="templates")
logger = logging.getLogger("sponsor_app")


@app.get("/", response_class=HTMLResponse)
@app.post("/", response_class=HTMLResponse)
def home(request: Request, name: Annotated[str, Form()] = None):
    count, columns, data = read_data(name)

    return templates.TemplateResponse(
        name="homepage.html",
        request=request,
        context={"count": count, "columns": columns, "rows": data},
    )



