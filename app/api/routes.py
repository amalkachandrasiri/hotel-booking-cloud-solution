from fastapi import APIRouter, HTTPException

from app.models.booking_request import BookingRequest
from app.services.prediction_service import PredictionService
from utils.logger import logger

from app.models.prediction_response import PredictionResponse

router = APIRouter()

prediction_service = PredictionService()

@router.get('/')
def root():
    logger.info('Root endpoint accessed.')

    return {
        'message': 'Hotel Booking Cancellation API is running.'
    }

@router.get('/health')
def health_check():
    logger.info('Health endpoint accessed.')

    return {
        'status': 'healthy'
    }

@router.post(
    '/predict',
    response_model=PredictionResponse
)
def predict_booking(booking: BookingRequest):
    logger.info('Prediction endpoint accessed.')

    try:
        return prediction_service.predict(
            booking.model_dump()
        )

    except Exception:
        logger.exception('Prediction request failed.')

        raise HTTPException(
            status_code=500,
            detail='Prediction could not be completed.'
        )