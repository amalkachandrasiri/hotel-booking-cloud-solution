import joblib
import pandas as pd
from catboost import CatBoostClassifier

from app import config
from utils.logger import logger

class PredictionService:

    def __init__(self):
        logger.info('Loading model and preprocessor...')

        self.model = CatBoostClassifier()
        self.model.load_model(config.MODEL_PATH)

        self.preprocessor = joblib.load(config.PREPROCESSOR_PATH)

        logger.info('Prediction service initialized successfully.')

    def predict(self, booking_data: dict) -> dict:
        try:
            logger.info('Preparing booking data for prediction.')

            input_df = pd.DataFrame([booking_data])
            processed_input = self.preprocessor.transform(input_df)

            prediction = int(self.model.predict(processed_input)[0])

            cancellation_probability = float(
                self.model.predict_proba(processed_input)[0][1]
            )

            prediction_label = (
                'Cancelled'
                if prediction == 1
                else 'Not Cancelled'
            )

            logger.info(
                'Prediction completed. Class: %s, Probability: %.4f',
                prediction,
                cancellation_probability
            )

            return {
                'prediction': prediction,
                'prediction_label': prediction_label,
                'cancellation_probability': round(
                    cancellation_probability,
                    4
                )
            }

        except Exception:
            logger.exception('Prediction failed.')
            raise