from pathlib import Path

# Project Root
BASE_DIR = Path(__file__).resolve().parent.parent

# Artifact Directory
ARTIFACT_DIR = BASE_DIR / 'artifacts'

# Artifact Files
MODEL_PATH        = ARTIFACT_DIR / 'catboost_model.cbm'
PREPROCESSOR_PATH = ARTIFACT_DIR / 'preprocessor.pkl'


FEATURE_COLUMNS_PATH = ARTIFACT_DIR / 'feature_columns.pkl'
METADATA_PATH = ARTIFACT_DIR / 'metadata.json'