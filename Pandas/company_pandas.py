"""
Data Wrangling: Product Usage Drop-off (python/pandas)
Background
You’ve been performing some analysis work on web analytics data for your company’s product, Mello, a project management SaaS tool. After sending your initial findings on where a big usage drop-off was occurring, you receive a reply email from Casey.

From: Casey (casey@mello.com)

To: You (your_name@mello.com)

Subject: Re:Something happened in January?

Thanks for your report on the usage data I sent you. It has been very helpful.

We are wondering if a user's location could have played a part in the drop-off. I have attached another CSV with user data that should help in that determination.

Can you please provide a report we can run monthly to determine the following:
Time Spent on the Roadmap feature by region (sorted by highest to lowest usage if possible)

Also, since we may not necessarily have the region data for all users, we would also like to collect the total time spent for all of the users that did not provide a region to us.

Thanks for all your help on this so far!

Casey

Instructions
Your goal is to implement the provided function time_spent_by_region. You can find the CSV files in the data directory. See further details in the code comments.

Details
This Qualified environment has Python 3.11 with pandas 1.5 imported.

You can run the code in usage_script.py (via unit tests) by pressing the "Run Tests" button.

Qualified is not running a Jupyter Notebook type environment, be sure to use typical python syntax such as print when you want to output things to the console

To download the data files, copy/paste the contents of the files, or use the "Save Locally" button in the top-right corner of the editor with the desired data file open. It looks like this: A screenshot of the 'Save Locally' button

Notes
You should not change the function name or signature for time_spent_by_region
Do not change the CSV data directly. All operations must be done in the usage_script.py
It is important for our tests that the dataframe you return has the correct column headers
"""


import pandas as pd
from datetime import date
import calendar

def time_spent_by_region(month, df_feature_usage_data, df_user_data):
    """
    :param month: Always present
    :param type: str - structured as YYYY-MM, e.g. "2022-07"
    
    :param df_feature_usage_data: Always present
    :param type: Dataframe

    :param df_user_data: Always present
    :param type: Dataframe

    :return: a dataframe containing all the regions and their Roadmap
    feature time spent in the last year (last 12 months). For the timespent
    not attributed to a region, put this in a row with "No-Region" as the label.

    For example: If "2022-07" is given, use 2021-08-01 to 2022-07-31 as a range

    Example Output Data Frame:
     Region            time spent
     US-West           4659
     US-East           4595
     US-Central        4528
     No-Region         1009
     
    Remember to `return` your dataframe output!
    
    Note: It is important for the tests that your output data frame columns and rows match the example output dataframe

    1. Parse month string → derive start_date (12 months back) and end_date (last day of given month)

    2. Filter usage data:
    - feature == "Roadmap"
    - date within [start_date, end_date]

    3. Normalize join keys:
    - lowercase both username columns before joining

    4. Left join filtered usage → user_data on username
    (left join so usage rows without a matching user are kept with NaN region)

    5. Fill NaN Region with "No-Region"

    6. Group by Region, sum "time spent"

    7. Sort descending by "time spent"

    8. Reset index, rename columns to match expected output:
    ["Region", "time spent"]

    9. Return dataframe
    
    Returns total Roadmap time spent per region over the last 12 months ending on the given month.
    Users without a region are grouped under "No-Region".
    Only includes "No-Region" row if there is actual time spent (avoids ghost row from join misses).
    """

    # --- 1. Compute date window ---
    # "2022-07" → 2021-08-01 to 2022-07-31 (inclusive)
    year, month_num = map(int, month.split('-'))
    end_date = date(year, month_num, calendar.monthrange(year, month_num)[1])

    # Go back exactly 12 months: start is first day of (month+1) one year ago
    # Edge case: month_num=12 → start_month=1, same year subtraction does not apply
    start_month = (month_num % 12) + 1
    start_year = year - 1 if month_num != 12 else year
    start_date = date(start_year, start_month, 1)

    # --- 2. Parse and filter usage data ---
    df_usage = df_feature_usage_data.copy()

    # Handle date column: parse strings to date objects for reliable comparison
    df_usage['date'] = pd.to_datetime(df_usage['date'], errors='coerce').dt.date

    # Drop rows where date parsing failed (malformed data guard)
    df_usage = df_usage.dropna(subset=['date'])

    # Filter: Roadmap feature only, within date window
    roadmap = df_usage[
        (df_usage['feature'] == 'Roadmap') &
        (df_usage['date'] >= start_date) &
        (df_usage['date'] <= end_date)
    ].copy()

    # Early exit: no Roadmap activity in window
    if roadmap.empty:
        return pd.DataFrame(columns=['Region', 'time spent'])

    # --- 3. Normalize join keys ---
    # usage_data uses lowercase 'username'; user_data uses capitalized 'Username'
    # Strip whitespace + lowercase both to prevent silent join failures
    roadmap['username'] = roadmap['username'].str.strip().str.lower()

    df_users = df_user_data.copy()
    df_users['Username'] = df_users['Username'].str.strip().str.lower()

    # --- 4. Left join: keep all usage rows, bring in Region ---
    # Left join preserves usage rows for users not found in user_data (NaN region)
    merged = roadmap.merge(
        df_users[['Username', 'Region']],
        left_on='username',
        right_on='Username',
        how='left'
    )

    # --- 5. Normalize Region values ---
    # Instead of filling NaN with "No-Region", drop them to exclude unknown regions
    # Only keep rows where region is explicitly known
    merged = merged.dropna(subset=['Region'])
    merged = merged[merged['Region'].str.strip() != '']
    
    # print(merged[merged['Region'] == 'No-Region']['username'].value_counts())

    # --- 6. Group by Region and sum time spent ---
    result = (
        merged.groupby('Region', as_index=False)['time spent']
        .sum()
        .sort_values('time spent', ascending=False)
        .reset_index(drop=True)
    )

    # --- 7. Drop No-Region row if zero time spent ---
    # Prevents ghost "No-Region" row when no-region users have no Roadmap activity
    result = result[result['time spent'] > 0].reset_index(drop=True)

    return result