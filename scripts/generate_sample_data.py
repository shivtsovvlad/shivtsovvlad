import pandas as pd
import random
import string
from datetime import datetime, timedelta

def generate_sales_data(n_rows: int = 1000):
    """Генерирует тестовые данные продаж."""
    data = []
    start_date = datetime(2025, 1, 1)
    
    for i in range(n_rows):
        data.append({
            "order_id": i + 1,
            "customer_id": random.randint(1000, 9999),
            "amount": round(random.uniform(10, 1000), 2),
            "order_date": (start_date + timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d"),
            "product_category": random.choice(["Electronics", "Clothing", "Books", "Home"]),
            "region": random.choice(["North", "South", "East", "West"])
        })
    
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = generate_sales_data(5000)
    df.to_csv("sample_data/sales_sample.csv", index=False)
    print(f"Сгенерировано {len(df)} записей в sample_data/sales_sample.csv")
