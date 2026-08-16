from fastapi import FastAPI
from app.routes import router as tasks_router

app = FastAPI(title="Task API")
app.include_router(tasks_router)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def root():
    return {"message": "L'API  est opérationnel, voir les routes /docs "}
