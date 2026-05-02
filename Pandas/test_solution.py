import pandas as pd
import unittest
from pandas.testing import assert_frame_equal
from tests.helper_functions import build_df, build_incoming_df

class Test(unittest.TestCase):
    def setUp(self):
        self.usage_data = pd.read_csv("data/usage_data.csv")
        self.user_data = pd.read_csv("data/user_data.csv")

    def test_time_spent_by_region(self):
        month='2022-07'

        df = build_df(month=month)
        incoming_df = build_incoming_df(month=month)

        assert_frame_equal(incoming_df, df, check_like=True, check_dtype=False, check_exact=False, atol=1, rtol=0)
