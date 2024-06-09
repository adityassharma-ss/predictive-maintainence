import unittest
from src.data_preprocessing import preprocess_data

class TestDataPreprocessing(unittest.TestCase):
    def test_preprocess_data(self):
        data, scaler = preprocess_data('data/sensor_data.csv')
        self.assertIsInstance(data, pd.DataFrame)
        self.assertIsInstance(scaler, MinMaxScaler)
        self.assertEqual(data.isnull().sum().sum(), 0)
        self.assertTrue(all(data[['temp', 'vibration', 'pressure', 'rpm', 'load']].max() <= 1))
        self.assertTrue(all(data[['temp', 'vibration', 'pressure', 'rpm', 'load']].min() >= 0))

if __name__ == '__main__':
    unittest.main()