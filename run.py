import uvicorn
from fastapi import FastAPI

from apps.database import create_tables

app = FastAPI(
    title="Phantom Mask",
    summary="Server for Pharmacies and Masks Data",
    version="0.0.1"
)

create_tables()

if __name__ == "__run__":
    uvicorn.run("run:app", host="0.0.0.0", port=8000, reload=True)
