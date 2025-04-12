#Data loading & saving 
import pandas as pd
from config import DATASET_PATH, PAST_PRED_PATH

def load_historical_data():
    df = pd.read_csv(DATASET_PATH)
    df['date'] = pd.to_datetime(df['date'])
    return df

def load_past_predictions():
    try:
        return pd.read_csv(PAST_PRED_PATH)
    except FileNotFoundError:
        return pd.DataFrame(columns=['date', 'region', 'precipitation', 'temp_max', 'temp_min', 'wind', 'prediction'])

def save_prediction(new_row, past_df):
    new_df = pd.concat([past_df, pd.DataFrame([new_row])], ignore_index=True)
    new_df.to_csv(PAST_PRED_PATH, index=False)
    return new_df