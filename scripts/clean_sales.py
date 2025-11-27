"""
Очистка данных продаж: удаление дублей, заполнение пропусков, нормализация.
"""
import pandas as pd
import logging

def clean_sales_data(input_df: pd.DataFrame) -> pd.DataFrame:
    """
    Основные шаги:
    1. Удаление дубликатов по order_id
    2. Замена пропусков в amount на 0
    3. Приведение дат к формату ISO
    """
    logging.info("Начало очистки данных...")

    # Удаление дублей
    df = input_df.drop_duplicates(subset=["order_id"])

    # Обработка пропусков
    df["amount"] = df["amount"].fillna(0)

    # Нормализация дат
    df["order_date"] = pd.to_datetime(df["order_date"]).dt.strftime("%Y-%m-%d")

    logging.info(f"Очищено {len(df)} записей")
    return df

if __name__ == "__main__":
    # Для тестирования
    test_df = pd.DataFrame({
        "order_id": [1, 2, 2],
        "customer_id": [101, 102, 102],
        "amount": [100.5, None, 200.0],
        "order_date": ["2025-01-01", "2025-01-02", "2025-01-02"]
    })
    cleaned = clean_sales_data(test_df)
    print(cleaned)
