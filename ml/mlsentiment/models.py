from dataclasses import dataclass

from transformers import pipeline

from .ml_settings import Ml_settings


@dataclass
class SentimentPrediction:
    """ Dataclass for sentiment prediction. """
    label: str
    score: float


def load_model():
    hf_model = pipeline(
        Ml_settings.task,
        model=Ml_settings.model,
        device=-1,
    )

    def model(text: str) -> SentimentPrediction:
        prediction = hf_model(text)
        prediction_best = prediction[0]
        return SentimentPrediction(
            prediction_best["label"],
            prediction_best["score"]
        )
    return model
