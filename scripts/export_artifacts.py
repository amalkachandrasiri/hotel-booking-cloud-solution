import json
import pickle
from pathlib import Path

from catboost import CatBoostClassifier

import app.config as config
import data_preprocessing as data_prep

print('Loading dataset...')
df = data_prep.fetch_data(config.RAW_DATA_PATH)

(
    X_train,
    X_test,
    y_train,
    y_test,
    preprocessor
) = data_prep.preprocess_data(df)


print('Training CatBoost model...')

model = CatBoostClassifier(
    iterations=300,
    learning_rate=0.1,
    depth=6,
    random_seed=42,
    verbose=0
)

model.fit(X_train, y_train)


print('Saving model...')

with open(ARTIFACT_DIR / 'catboost_model.pkl', 'wb') as f:
    pickle.dump(model, f)


print('Saving preprocessor...')

with open(ARTIFACT_DIR / 'preprocessor.pkl', 'wb') as f:
    pickle.dump(preprocessor, f)


print('Saving feature columns...')

feature_columns = preprocessor.get_feature_names_out().tolist()

with open(ARTIFACT_DIR / 'feature_columns.pkl', 'wb') as f:
    pickle.dump(feature_columns, f)


print('Saving metadata...')

metadata = {
    'model_name': 'Hotel Booking Cancellation Prediction',
    'algorithm': 'CatBoost',
    'version': '1.0.0',
    'iterations': 300,
    'learning_rate': 0.1,
    'depth': 6,
    'target': 'is_canceled'
}

with open(ARTIFACT_DIR / 'metadata.json', 'w') as f:
    json.dump(metadata, f, indent=4)


print('\nArtifacts exported successfully.')