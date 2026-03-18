"""
Create a function that returns True if ALL of the following conditions are met:
(1) Drug group A, B, C and D overlap by 7 or more days consecutively, for all drugs
(2) The last day of the overlap must be within 30 days look back from 03/31. - 3/01
   Jan                            Feb                         March
                                                        1234567890123456789012345678901234567
   123456789012345678901234567890112345678901234567890123456781234567890123456789012345678901
1: 111111111111111111111111    111111111111111111111111111111 
2:                                                          11111
3:                                                111111111111111111111111111111
4:                                   111111111111111111111111111111
5:                                111111111111111111111111111111   111111111111111111111111111111
"""
"""
MORE HINT
|------------Jan---------------|------------Feb-------------|-----------Mar---------------|
1234567890123456789012345678901123456789012345678901234567891234567890123456789012345678901
0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
1111111111111111111111100000111111111111111111111111111111000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000001111100000000000000000000000000000
0000000000000000000000000000000000000000000000011111111111111111111111111111100000000000000
0000000000000000000000000000000000000000000001111111111111111111111111111110000000000000000
0000000000000000000000000000000111111111111111111111111111111000011111111111111111111111111  


A: 1111111100000000000000000000000000000
B: 1111111111111111111111100000000000000
C: 1111111111111111111110000000000000000
D: 1111111000011111111111111111111111111
S: 4444444322233333333332211111111111111
"""

from datetime import datetime, timedelta

# Util func
def str_to_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d')


def are_drugs_overlapping(meds, target_drug_groups, min_overlap_days, num_days_lookback, end_date):
  
  """
  Overlap days must be consecutive.

  :param meds: List of dict presenting a medication.
  :param target_drug_groups: Set. Containing target drug groups.
  :param min_overlap_days: int. Minimum number of days when all target drug groups overlap
  :param num_days_lookback: int. Number of days from end_date in which the last day of overlap must occurred.
  :param end_date: datetime. Reference date. 
  
    meds array upper limit = 600
    """
    
  # Phase 1: Build {date: set of drug groups active on that day}
  coverage = {}
  for med in meds:
    for group in med["drugGroup"]:
        if group in target_drug_groups:
            for fill in med["fills"]:
                start = str_to_date(fill["fillDate"])
                for i in range(int(fill["daysSupply"])):
                    day = start + timedelta(days=i)
                    coverage.setdefault(day, set()).add(group)

  # Phase 2: Scan sorted dates for consecutive days where ALL groups are covered
  lookback_start = end_date - timedelta(days=num_days_lookback - 1)
  consecutive = 0
  prev_day = None

  for day in sorted(coverage.keys()):
    if coverage[day] >= target_drug_groups:
        # Extend streak if this day immediately follows the previous qualifying day
        if prev_day is not None and day == prev_day + timedelta(days=1):
            consecutive += 1
        else:
            consecutive = 1

        # Check both conditions: streak length and lookback window
        if consecutive >= min_overlap_days and lookback_start <= day <= end_date:
            return True

        prev_day = day
    else:
        # Streak broken — reset
        consecutive = 0
        prev_day = None

    return False


#####################################
# Test
#####################################

meds = [
    {
        "genericName": "drug1",
        "drugGroup": ["A", "E"],
        "fills": [
            {"fillDate": "2021-12-25", "daysSupply": "30"},
            {"fillDate": "2022-01-29", "daysSupply": "30"}
        ]
    },
    {
        "genericName": "drug2",
        "drugGroup": ["A"],
        "fills": [
            {"fillDate": "2022-02-27", "daysSupply": "5"}
        ]
    },
    {
        "genericName": "drug3",
        "drugGroup": ["B", "K"],
        "fills": [
            {"fillDate": "2022-02-17", "daysSupply": "30"}
        ]
    },
    {
        "genericName": "drug4",
        "drugGroup": ["C"],
        "fills": [
            {"fillDate": "2022-02-15", "daysSupply": "30"}
        ]
    },
    {
        "genericName": "drug5",
        "drugGroup": ["D"],
        "fills": [
            {"fillDate": "2022-02-01", "daysSupply": "30"},
            {"fillDate": "2022-03-06", "daysSupply": "30"}
        ]
    }
]


target_drug_groups = {'A', 'B', 'C', 'D'}
min_overlap_days = 7
num_days_lookback = 30
end_date = str_to_date('2022-03-31')
res = are_drugs_overlapping(meds, target_drug_groups, min_overlap_days, num_days_lookback, end_date)
print(res)





# Your last Python3 code is saved below:
# print("Hello")