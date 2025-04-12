#Config and constants
MODEL_PATH = "weather_model.pkl"
DATASET_PATH = "seattle-weather.csv"
PAST_PRED_PATH = "past_predictions.csv"

REGIONS = ["India", "USA", "Australia", "Canada", "Brazil"]
WEATHER_LABELS = {
    1: ("Rainy / Cloudy", "🌧️"),
    0: ("Clear / Sunny", "☀️")
}