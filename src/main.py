from fastapi import FastAPI

app = FastAPI(title="ZenOfLearning Fellowship API")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
