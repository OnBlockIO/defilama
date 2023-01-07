from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.prices import router as price_router
from routes.defillama import router as defillama_router

app = FastAPI(
    version="0.0.1",
    title="GhostMarket API for external apps.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(price_router)
app.include_router(defillama_router)
