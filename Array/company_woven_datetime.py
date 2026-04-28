"""
Prorating Subscriptions
Background
Our company has started selling to larger customers, so we are creating subscription tiers with different feature sets to cater to our customers’ unique needs. We previously charged every customer a flat fee per month, but now we plan on charging for the number of users active on the customer's subscription plan. As a result, we're changing our billing system.

Instructions
You’ve picked up the work item to implement the logic to compute the monthly charge:

Prorating Subscriptions (#8675309)
We'd like you to implement a monthly_charge function to calculate the total monthly bill for a customer.

Customers are billed based on their subscription tier. We charge them a prorated amount for the portion of the month each user’s subscription was active. For example, if a user was activated or deactivated part way through the month, then we charge them only for the days their subscription was active.

We want to bill customers for all days users were active in the month (including any activation and deactivation dates, since the user had some access on those days).

We do need to support historical calculations (previous dates)
We only charge whole cents
Notes
We recommend spending some time designing your algorithm before jumping into writing code, since some ways of handling this might end up being harder to build than others.

Testing
The provided unit tests only cover a few cases that one of your colleagues shared, so you should plan to add your own tests to ensure that your solution handles any edge cases.

Notes
It’s more important for the return value to be correct than it is for the algorithm to be highly optimized.
You should not change function names or return types of the provided functions since our test cases depend on those not changing.
"""


import datetime
import calendar

def monthly_charge_old(month, subscription, users):
  """ Computes the monthly charge for a given subscription.
 
  @rtype: int
  @returns: the total monthly bill for the customer in cents, rounded
    to the nearest cent. For example, a bill of $20.00 should return 2000.
    If there are no active users or the subscription is None, returns 0.
 
  @type month: str
  @param month - Always present
    Has the following structure:
    "2022-04"  # April 2022 in YYYY-MM format

  @type subscription: dict
  @param subscription - May be None
    If present, has the following structure:
    {
      'id': 763,
      'customer_id': 328,
      'monthly_price_in_cents': 359  # price per active user per month
    }
 
  @type users: list
  @param users - May be empty, but not None
    Has the following structure:
    [
      {
        'id': 1,
        'name': "Employee #1",
        'customer_id': 1,
    
        # when this user started
        'activated_on': datetime.date(2021, 11, 4),
    
        # last day to bill for user
        # should bill up to and including this date
        # since user had some access on this date
        'deactivated_on': datetime.date(2022, 4, 10)
      },
      {
        'id': 2,
        'name': "Employee #2",
        'customer_id': 1,
    
        # when this user started
        'activated_on': datetime.date(2021, 12, 4),
    
        # hasn't been deactivated yet
        'deactivated_on': None
      },
    ]
  """
  # your code here!
  pass

def monthly_charge(month, subscription, users):
  """ Computes the monthly charge for a given subscription.
 
  @rtype: int
  @returns: the total monthly bill for the customer in cents, rounded
    to the nearest cent. For example, a bill of $20.00 should return 2000.
    If there are no active users or the subscription is None, returns 0.
 
  @type month: str
  @param month - Always present
    Has the following structure:
    "2022-04"  # April 2022 in YYYY-MM format

  @type subscription: dict
  @param subscription - May be None
    If present, has the following structure:
    {
      'id': 763,
      'customer_id': 328,
      'monthly_price_in_cents': 359  # price per active user per month
    }
 
  @type users: list
  @param users - May be empty, but not None
    Has the following structure:
    [
      {
        'id': 1,
        'name': "Employee #1",
        'customer_id': 1,
    
        # when this user started
        'activated_on': datetime.date(2021, 11, 4),
    
        # last day to bill for user
        # should bill up to and including this date
        # since user had some access on this date
        'deactivated_on': datetime.date(2022, 4, 10)
      },
      {
        'id': 2,
        'name': "Employee #2",
        'customer_id': 1,
    
        # when this user started
        'activated_on': datetime.date(2021, 12, 4),
    
        # hasn't been deactivated yet
        'deactivated_on': None
      },
    ]
  """
  
  # Handle null subscription or no users
  if subscription is None or not users:
    return 0
  
  # Parse the month string "YYYY-MM"
  year, month_num = map(int, month.split('-'))
  
  # Get first and last day of the month
  first_day = datetime.date(year, month_num, 1)
  last_day = last_day_of_month(first_day)
  
  # Total days in the month
  total_days_in_month = (last_day - first_day).days + 1
  
  # Price per active user per month
  monthly_price = subscription['monthly_price_in_cents']
  
  total_charge = 0.0
  
  for user in users:
    activated_on = user['activated_on']
    deactivated_on = user['deactivated_on']
    
    # Calculate the active period for this user in this month
    # Start: the later of (user activation date, month start)
    period_start = max(activated_on, first_day)
    
    # End: the earlier of (user deactivation date or month end, month end)
    if deactivated_on is None:
      period_end = last_day  # User still active, bill until end of month
    else:
      period_end = min(deactivated_on, last_day)
    
    # If period_start > period_end, user was not active in this month
    if period_start > period_end:
      continue
    
    # Calculate days active (inclusive of both start and end dates)
    days_active = (period_end - period_start).days + 1
    
    # Prorate the monthly charge
    prorated_charge = (days_active / total_days_in_month) * monthly_price
    total_charge += prorated_charge
  
  # Round to nearest cent
  return round(total_charge)

####################
# Helper functions #
####################

def first_day_of_month(date):
  """
  Takes a datetime.date object and returns a datetime.date object
  which is the first day of that month. For example:

  >>> first_day_of_month(datetime.date(2022, 3, 17))  # Mar 17
  datetime.date(2022, 3, 1)                           # Mar  1

  Input type: datetime.date
  Output type: datetime.date
  """
  return date.replace(day=1)

def last_day_of_month(date):
  """
  Takes a datetime.date object and returns a datetime.date object
  which is the last day of that month. For example:

  >>> last_day_of_month(datetime.date(2022, 3, 17))  # Mar 17
  datetime.date(2022, 3, 31)                         # Mar 31

  Input type: datetime.date
  Output type: datetime.date
  """
  last_day = calendar.monthrange(date.year, date.month)[1]
  return date.replace(day=last_day)

def next_day(date):
  """
  Takes a datetime.date object and returns a datetime.date object
  which is the next day. For example:

  >>> next_day(datetime.date(2022, 3, 17))   # Mar 17
  datetime.date(2022, 3, 18)                 # Mar 18

  >>> next_day(datetime.date(2022, 3, 31))  # Mar 31
  datetime.date(2022, 4, 1)                 # Apr  1

  Input type: datetime.date
  Output type: datetime.date
  """
  return date + datetime.timedelta(days=1)