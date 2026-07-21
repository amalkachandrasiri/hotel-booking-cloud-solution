from pathlib import Path

import joblib
from catboost import CatBoostClassifier

import sys
from pathlib import Path

# Add the parent folder (project root) to Python's import search path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils.logger import logger  # or import utils.logger
import app.config as config

logger.info('Loading CatBoost model...')

model = CatBoostClassifier()
model.load_model(config.MODEL_PATH)

logger.info('CatBoost model loaded successfully.')

logger.info('Loading preprocessor...')

preprocessor = joblib.load(config.PREPROCESSOR_PATH)

logger.info('Preprocessor loaded successfully.')