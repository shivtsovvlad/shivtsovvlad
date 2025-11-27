import unittest
import pandas as pd
from scripts.clean_sales import clean_sales_data

class TestCleanSales(unittest.TestCase):
    def setUp(self):
        self.sample_data = pd.DataFrame({
            "order_id": [1, 2, 2, 3],
            "customer_id": [101, 102, 102, 103],
            "amount": [100.5, None, 200.0, 150.0],
            "order_date": ["2025-01-01", "2025-01-02", "2025-01-02", "invalid-date"]
        })

    def test_remove_duplicates(self):
        result = clean_sales_data(self.sample_data)
        self.assertEqual(len(result), 3)  # Дубликат order_id=2 удалён

    def test_fill_na_amount(self):
        result = clean_sales_data(self.sample_data)
        self.assertFalse(result["amount"].isna().any())

    def test_date_format(self):
        result = clean_sales_data(self.sample_data)
        # Невалидная дата должна быть обработана (например, установлена в NaT)
        self.assertIn("2025-01-01", result["order_date"].tolist())

if __name__ == "__main__":
    unittest.main()
