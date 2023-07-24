import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api.v1 import menu, submenu, dish
from core.config import get_settings as settings

app = FastAPI(
    title="APP Restaurant",
    version="1.0.0",
    description="REST API по работе с меню ресторана, все CRUD операции",
    docs_url=settings.BASE_URL + "/swagger",
    openapi_url=settings.BASE_URL + "/openapi.json",
    default_response_class=ORJSONResponse,
    redoc_url=None,
    debug=settings.DEBUG
)


@app.on_event('startup')
async def startup():
    pass


@app.on_event('shutdown')
async def shutdown():
    pass


app.include_router(router=menu.router, prefix="/api/v1/menus", tags=["menus"])
app.include_router(router=submenu.router, prefix="/api/v1/menus", tags=["submenus"])
app.include_router(router=dish.router, prefix="/api/v1/menus", tags=["dishes"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=6000, reload=True)
