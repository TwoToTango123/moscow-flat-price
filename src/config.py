from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
MODELS_DIR = ROOT / "models"
FIGURES_DIR = ROOT / "reports" / "figures"

# зеркало данных соревнования Sberbank Russian Housing Market (Kaggle, 2017)
RAW_URLS = {
    "train.csv": "https://raw.githubusercontent.com/AdmiralWen/Sberbank-Russian-Housing-Market/master/Data/train.csv",
    "macro.csv": "https://raw.githubusercontent.com/AdmiralWen/Sberbank-Russian-Housing-Market/master/Data/macro.csv",
}

VALID_START = "2014-07-01"
TEST_START = "2015-01-01"

# цены в договоре ровно 1/2/3 млн у инвестиционных сделок - почти наверняка
# занижение суммы в договоре, а не реальная стоимость
FAKE_PRICES = [1_000_000, 2_000_000, 3_000_000]

# признаки самой квартиры - их пользователь вводит в API
FLAT_FEATURES = [
    "full_sq", "life_sq", "kitch_sq", "floor", "max_floor", "build_year",
    "num_room", "material", "state",
]
# расположение: если не передали, берём медиану по району
LOCATION_FEATURES = [
    "kremlin_km", "ttk_km", "sadovoe_km", "mkad_km", "metro_min_walk", "metro_km_avto",
    "park_km", "green_zone_km", "industrial_km", "railroad_km", "water_km",
    "public_transport_station_min_walk", "big_road1_km",
    "cafe_count_1000", "office_count_1000", "sport_count_1000", "trc_count_1000",
]
# характеристики района целиком - всегда из справочника по sub_area
DISTRICT_FEATURES = [
    "raion_popul", "green_zone_part", "indust_part", "school_education_centers_raion",
    "healthcare_centers_raion", "shopping_centers_raion", "office_raion",
]
CAT_FEATURES = ["sub_area", "product_type", "material", "state"]
