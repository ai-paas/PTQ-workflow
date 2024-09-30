from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette import status
from starlette.responses import JSONResponse

from app.api.routers import api_router
from app.core.middlewares import log_and_handle_exceptions
from app.core.settings import get_settings

settings = get_settings()


SWAGGER_TITLE = "Iscream Media Chatbot"
SWAGGER_SUMMARY = "This is RestfulAPI Server for Chatbot"
SWAGGER_DESCRIPTION = """
Iscream Media aitextbook-api [aitextbook-backend Api List Api info]\
(https://docs.google.com/spreadsheets/d/1A0N5jdzmEGhgw-SCUJbNKPY4LqpG_xh0nl2zvurx-5I/edit#gid=0)
[수학 1학기 login](https://stageoauth2.i-screammedia.com/login) <<< || >>> \
[영어 login](https://stageoauth2.i-screammedia.com/login) <<<
[수학 2학기 login](https://stageoauth2.i-screammedia.com/login) <<<
[Iscream docs](https://api-stage.smart-aidt.com/swagger-ui/index.html)

** 교사 비번 동일 123qwe **
- keenedge
- keenedge2
- teacher01 ~ 08

** 학생 비번 동일 123qwe **
- keenedge3 ~ 6
- student01 ~ 32
"""

app = FastAPI(
    title=SWAGGER_TITLE,
    summary=SWAGGER_SUMMARY,
    description=SWAGGER_DESCRIPTION,
    docs_url="/surromind/api/v1/docs",
    redoc_url=None,
)
app.middleware("http")(log_and_handle_exceptions)

# TODO: Production에서 변경 필요.
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/healthz")
def health_check():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status": "ok"})


app.include_router(api_router, prefix=settings.API_STR)
