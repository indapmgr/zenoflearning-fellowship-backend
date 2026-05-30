from fastapi import FastAPI

from src.routes import students

app = FastAPI(title="ZenOfLearning Fellowship API")


app.include_router(students.router)
@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}