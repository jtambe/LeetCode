import unittest
import datetime
from company_woven_datetime import monthly_charge

"""
python -m unittest company_woven_datetime_test.py
"""

users = [
  {
    'id': 1,
    'name': 'Employee #1',
    'activated_on': datetime.date(2019, 1, 1),
    'deactivated_on': None,
    'customer_id': 1,
  },
  {
    'id': 2,
    'name': 'Employee #2',
    'activated_on': datetime.date(2019, 1, 1),
    'deactivated_on': None,
    'customer_id': 1,
  },
]

plan = {
  'id': 1,
  'customer_id': 1,
  'monthly_price_in_cents': 5_000
}

no_users = []

# Note: the class must be called Test
class Test(unittest.TestCase):
  def test_works_when_no_users_are_active(self):
    self.assertEqual(monthly_charge('2018-10', plan, users), 0)

  def test_works_when_the_active_users_are_active_the_entire_month(self):
    expected_user_count = 2
    self.assertAlmostEqual(monthly_charge('2020-12', plan, users), expected_user_count * 5_000, delta=1)

  def test_returns_zero_when_subscription_is_none(self):
    """No billing occurs when subscription is None"""
    self.assertEqual(monthly_charge('2020-01', None, users), 0)
  
  def test_returns_zero_when_users_list_is_empty(self):
    """No billing occurs when users list is empty"""
    self.assertEqual(monthly_charge('2020-01', plan, no_users), 0)
  
  # ============= PARTIAL MONTH ACTIVATION =============
  
  def test_user_activated_mid_month(self):
    """User activated mid-month should be prorated for remaining days"""
    # User activated on Jan 15, 2020 (31 days in Jan)
    # Should be billed for 17 days (15, 16, ..., 31 inclusive)
    # Charge: (17/31) * 5000 = 2741.93 cents ≈ 2742 cents
    partial_users = [{
      'id': 1,
      'name': 'Employee #1',
      'activated_on': datetime.date(2020, 1, 15),
      'deactivated_on': None,
      'customer_id': 1,
    }]
    expected = round((17 / 31) * 5000)
    self.assertEqual(monthly_charge('2020-01', plan, partial_users), expected)
  
  def test_user_deactivated_mid_month(self):
    """User deactivated mid-month should be prorated for days active"""
    # User deactivated on Jan 10, 2020 (31 days in Jan)
    # Should be billed for 10 days (1, 2, ..., 10 inclusive)
    # Charge: (10/31) * 5000 = 1612.90 cents ≈ 1613 cents
    partial_users = [{
      'id': 1,
      'name': 'Employee #1',
      'activated_on': datetime.date(2020, 1, 1),
      'deactivated_on': datetime.date(2020, 1, 10),
      'customer_id': 1,
    }]
    expected = round((10 / 31) * 5000)
    self.assertEqual(monthly_charge('2020-01', plan, partial_users), expected)
  
  def test_user_activated_and_deactivated_same_month(self):
    """User active for only part of month (both dates mid-month)"""
    # User activated Jan 10, deactivated Jan 20, 2020 (31 days in Jan)
    # Should be billed for 11 days (10, 11, ..., 20 inclusive)
    # Charge: (11/31) * 5000 = 1774.19 cents ≈ 1774 cents
    partial_users = [{
      'id': 1,
      'name': 'Employee #1',
      'activated_on': datetime.date(2020, 1, 10),
      'deactivated_on': datetime.date(2020, 1, 20),
      'customer_id': 1,
    }]
    expected = round((11 / 31) * 5000)
    self.assertEqual(monthly_charge('2020-01', plan, partial_users), expected)
  
  # ============= EDGE CASES: OUTSIDE MONTH BOUNDARIES =============
  
  def test_user_activated_after_month_ends(self):
    """User activated after requested month should not be billed"""
    # User activated Feb 5, querying Jan
    outside_users = [{
      'id': 1,
      'name': 'Employee #1',
      'activated_on': datetime.date(2020, 2, 5),
      'deactivated_on': None,
      'customer_id': 1,
    }]
    self.assertEqual(monthly_charge('2020-01', plan, outside_users), 0)
  
  def test_user_deactivated_before_month_starts(self):
    """User deactivated before requested month should not be billed"""
    # User deactivated Dec 15, querying Jan
    outside_users = [{
      'id': 1,
      'name': 'Employee #1',
      'activated_on': datetime.date(2019, 11, 1),
      'deactivated_on': datetime.date(2019, 12, 15),
      'customer_id': 1,
    }]
    self.assertEqual(monthly_charge('2020-01', plan, outside_users), 0)
  
  # ============= EDGE CASES: MONTH BOUNDARIES =============
  
  def test_user_activated_on_first_day_deactivated_on_last_day(self):
    """User active entire month (boundary dates)"""
    # 31 days in January, should be full charge
    boundary_users = [{
      'id': 1,
      'name': 'Employee #1',
      'activated_on': datetime.date(2020, 1, 1),
      'deactivated_on': datetime.date(2020, 1, 31),
      'customer_id': 1,
    }]
    self.assertEqual(monthly_charge('2020-01', plan, boundary_users), 5000)
  
  def test_user_activated_on_last_day_of_month(self):
    """User activated on last day should be billed for 1 day"""
    # Activated Jan 31, 2020 (31 days in Jan)
    # Should be billed for 1 day: (1/31) * 5000 = 161.29 cents ≈ 161 cents
    boundary_users = [{
      'id': 1,
      'name': 'Employee #1',
      'activated_on': datetime.date(2020, 1, 31),
      'deactivated_on': None,
      'customer_id': 1,
    }]
    expected = round((1 / 31) * 5000)
    self.assertEqual(monthly_charge('2020-01', plan, boundary_users), expected)
  
  # ============= FEBRUARY EDGE CASE (28 vs 29 days) =============
  
  def test_february_non_leap_year(self):
    """February in non-leap year has 28 days"""
    # 2019 is not a leap year, February has 28 days
    feb_users = [{
      'id': 1,
      'name': 'Employee #1',
      'activated_on': datetime.date(2019, 2, 1),
      'deactivated_on': None,
      'customer_id': 1,
    }]
    self.assertEqual(monthly_charge('2019-02', plan, feb_users), 5000)
  
  def test_february_leap_year(self):
    """February in leap year has 29 days"""
    # 2020 is a leap year, February has 29 days
    # User active entire month
    feb_users = [{
      'id': 1,
      'name': 'Employee #1',
      'activated_on': datetime.date(2020, 2, 1),
      'deactivated_on': None,
      'customer_id': 1,
    }]
    self.assertEqual(monthly_charge('2020-02', plan, feb_users), 5000)
  
  def test_february_leap_year_partial_month(self):
    """Partial month in leap year February"""
    # 2020 is a leap year, February has 29 days
    # User activated Feb 15, deactivated Feb 29
    # Active for 15 days: (15/29) * 5000 = 2586.21 cents ≈ 2586 cents
    feb_users = [{
      'id': 1,
      'name': 'Employee #1',
      'activated_on': datetime.date(2020, 2, 15),
      'deactivated_on': datetime.date(2020, 2, 29),
      'customer_id': 1,
    }]
    expected = round((15 / 29) * 5000)
    self.assertEqual(monthly_charge('2020-02', plan, feb_users), expected)
  
  # ============= MULTIPLE USERS - MIXED SCENARIOS =============
  
  def test_multiple_users_different_activation_dates(self):
    """Multiple users with different activation dates"""
    # User 1: entire month (Jan 1-31) -> 5000
    # User 2: mid-month (Jan 15-31, 17 days) -> (17/31) * 5000 ≈ 2742
    # Total ≈ 7742
    mixed_users = [
      {
        'id': 1,
        'name': 'Employee #1',
        'activated_on': datetime.date(2020, 1, 1),
        'deactivated_on': None,
        'customer_id': 1,
      },
      {
        'id': 2,
        'name': 'Employee #2',
        'activated_on': datetime.date(2020, 1, 15),
        'deactivated_on': None,
        'customer_id': 1,
      }
    ]
    expected = 5000 + round((17 / 31) * 5000)
    self.assertAlmostEqual(monthly_charge('2020-01', plan, mixed_users), expected, delta=1)
  
  def test_multiple_users_some_active_some_inactive(self):
    """Mix of users: some active in month, some not"""
    # User 1: active entire month -> 5000
    # User 2: deactivated before month -> 0
    # User 3: activated after month -> 0
    # Total = 5000
    mixed_users = [
      {
        'id': 1,
        'name': 'Employee #1',
        'activated_on': datetime.date(2020, 1, 1),
        'deactivated_on': None,
        'customer_id': 1,
      },
      {
        'id': 2,
        'name': 'Employee #2',
        'activated_on': datetime.date(2019, 1, 1),
        'deactivated_on': datetime.date(2019, 12, 31),
        'customer_id': 1,
      },
      {
        'id': 3,
        'name': 'Employee #3',
        'activated_on': datetime.date(2020, 2, 1),
        'deactivated_on': None,
        'customer_id': 1,
      }
    ]
    self.assertEqual(monthly_charge('2020-01', plan, mixed_users), 5000)
  
  # ============= SINGLE USER SCENARIOS =============
  
  def test_single_user_full_month(self):
    """Single user active entire month"""
    single_user = [{
      'id': 1,
      'name': 'Employee #1',
      'activated_on': datetime.date(2020, 1, 1),
      'deactivated_on': None,
      'customer_id': 1,
    }]
    self.assertEqual(monthly_charge('2020-01', plan, single_user), 5000)
  
  def test_single_user_one_day(self):
    """Single user active for only 1 day"""
    # Jan 15, 2020 (31 days in Jan)
    # (1/31) * 5000 = 161.29 cents ≈ 161 cents
    single_user = [{
      'id': 1,
      'name': 'Employee #1',
      'activated_on': datetime.date(2020, 1, 15),
      'deactivated_on': datetime.date(2020, 1, 15),
      'customer_id': 1,
    }]
    expected = round((1 / 31) * 5000)
    self.assertEqual(monthly_charge('2020-01', plan, single_user), expected)