from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel

from ml.mlsentiment.models import load_model


model = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global model
    model = load_model()
    try:
        yield
    finally:
        model = None


app = FastAPI(
    lifespan=lifespan,
    openapi_url="/openapi.json",
)


class SentimentPrediction(BaseModel):
    text: str
    sentiment_label: str
    sentiment_score: float


@app.get("/predict_sentiment", tags=["AI анализатор текста"])
async def sentiment_prediction(text: str) -> dict:
    """
    Определяет настроение сообщения.
    """
    sentiment = model(text)
    response = {
        "Настроение": sentiment.label,
        "Текст": text,
        "Точность": round(sentiment.score, 2),
    }
    return response


# To generate OpenAPI schema
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="AI анализатор текста.",
        version="1.0.0",
        summary="Анализатор текста. Использует модель Hugging Face.",
        description="Это простое приложение для AI анализа текста.",
        routes=app.routes,
        contact={
            "name": "Nikita Nesterenko",
            "url": "https://github.com/nikitairl",
            "email": "nikita.n.irl@gmail.com",
        },
    )
    return openapi_schema


app.openapi = custom_openapi
