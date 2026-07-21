from pydantic import BaseModel


class PredictionResponse(BaseModel):
    prediction: int
    prediction_label: str
    cancellation_probability: float