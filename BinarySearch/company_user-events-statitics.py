"""
You have a sequence of queries, ordered in time.

There are two types of queries:

1. The user with user_id generated an event (pressed the red button)

2. Count the number of users who generated >= 1,000 events (pressed the red button >= 1,000 times) over the last 5 minutes.

Implement a data structure that can efficiently process such queries.

[(user_id:int, time:int)]

{user_id : [int, int, int]}

{int: set(user_id)}

"""



class UserStatistics_old:

    def __init__(self, window: int, limit: int):
        self.userEvents = {}
        self.window = window
        self.limit = limit #1000 events in window minutes.
        
    def event(self, now: int, user_id: int):
        if user_id in self.userEvents:
            self.userEvents[user_id].append(now)
        else:
            self.userEvents[user_id] = [now]
    

    def get_robot_count(self, now: int):
        
        answer = 0
        
        def get_count(event_times:list[int], now:int) -> int:
            """
            get event count against this user
            """
            index = len(event_times) - 1
            counter = 0 
                    
            while index >= 0 and event_times[index] >= (now - self.window):
                counter += 1
                index -= 1
                
            return counter
                
        for user, event_times in self.userEvents.items():
            if get_count(event_times, now) >= 1000:
                answer += 1
                
        
        return answer
    

class UserStatistics:

    def __init__(self, window: int, limit: int):
        self.userEvents = {} # {user_id: {timestamp: cumulative_event_count}}
        self.window = window
        self.limit = limit # 1000 events in window minutes.
        
    def event(self, now: int, user_id: int):
        if user_id in self.userEvents:
            if now in self.userEvents[user_id]:
                self.userEvents[user_id][now] += 1
            else:
                self.userEvents[user_id][now] = 1
        else:
            self.userEvents[user_id] = {now: 1}


    def get_robot_count(self, now: int):
        
        answer = 0
        
        def get_count(event_time_count_map:dict[int, int], now:int) -> int:
            """
            get event count against this user
            """
            counter = 0
            timestamps = list(event_time_count_map.keys())
            last_valid_timestamp_for_window = now - self.window

            # if no valid timestamp present for the given window, 0 events happened for that user
            if timestamps[-1] < last_valid_timestamp_for_window:
                return counter
            
            # 1. If there is only 1 entry in timestamps and it is valid, simply return event count of that timestamp
            # 2. We do this here because finding closest number using binary search checks with mid-1 >= 0 
            # As such, mid-1 >= 0 will not work out for single element which is greater than last_valid_timestamp_for_window
            if len(timestamps) == 1:
                return event_time_count_map[timestamps[-1]]
            

            # Do a binary search to find closest_valid_timestamp index in timestamps array
            l, r = 0, len(timestamps) - 1
            closest_valid_timestamp_index = -1
            while l <= r:
                mid = (l + r)// 2
                if timestamps[mid] == last_valid_timestamp_for_window:
                    closest_valid_timestamp_index = mid
                    break
                elif timestamps[mid] < last_valid_timestamp_for_window:
                    l = mid + 1
                elif timestamps[mid] > last_valid_timestamp_for_window:
                    if mid - 1 >= 0 and timestamps[mid-1] < last_valid_timestamp_for_window:
                        closest_valid_timestamp_index = mid
                        break
                    r = mid - 1

            
            closest_valid_timestamp_count = event_time_count_map[timestamps[closest_valid_timestamp_index]]
            last_valid_timestamp_count = event_time_count_map[timestamps[-1]]
            total_events = last_valid_timestamp_count - closest_valid_timestamp_count
            return total_events    

                
        for user, event_time_count_map in self.userEvents.items():
            if get_count(event_time_count_map, now) >= self.limit:
                answer += 1
                
        
        return answer