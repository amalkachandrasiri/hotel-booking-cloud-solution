import pandas as pd
import joblib
from catboost import CatBoostClassifier

import sys
from pathlib import Path

# Add the parent folder (project root) to Python's import search path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils.logger import logger
from app import config

from app.services.prediction_service import PredictionService


logger.info('Loading model and preprocessor...')

model = CatBoostClassifier()
model.load_model(config.MODEL_PATH)

preprocessor = joblib.load(config.PREPROCESSOR_PATH)

logger.info('Artifacts loaded successfully.')


sample_booking = {
    'hotel': 'Resort Hotel',
    'lead_time': 120,
    'arrival_date_year': 2017,
    'arrival_date_month': 'July',
    'arrival_date_week_number': 27,
    'arrival_date_day_of_month': 1,
    'stays_in_weekend_nights': 2,
    'stays_in_week_nights': 3,
    'adults': 2,
    'children': 0,
    'babies': 0,
    'meal': 'BB',
    'country': 'PRT',
    'market_segment': 'Online TA',
    'distribution_channel': 'TA/TO',
    'is_repeated_guest': 0,
    'previous_cancellations': 0,
    'previous_bookings_not_canceled': 0,
    'reserved_room_type': 'A',
    'assigned_room_type': 'A',
    'booking_changes': 0,
    'deposit_type': 'No Deposit',
    'agent': 240,
    'days_in_waiting_list': 0,
    'customer_type': 'Transient',
    'adr': 95.0,
    'required_car_parking_spaces': 0,
    'total_of_special_requests': 1
}
'''
input_df = pd.DataFrame([sample_booking])

logger.info('Transforming input data...')

processed_input = preprocessor.transform(input_df)

logger.info('Generating prediction...')

prediction = model.predict(processed_input)
prediction_probability = model.predict_proba(processed_input)

logger.info('Prediction completed successfully.')

logger.info('Predicted class: %s', int(prediction[0]))
logger.info(
    'Cancellation probability: %.4f',
    prediction_probability[0][1]
)
'''
# test prediction service 
prediction_service = PredictionService()
result = prediction_service.predict(sample_booking)
logger.info('Prediction result: %s', result)

