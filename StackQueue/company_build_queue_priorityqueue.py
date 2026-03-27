# # Welcome!

# In this coding challenge, you'll implement a Queue data structure step-by-step, building on your implementation as we introduce new requirements along the way.

# ___

# __Feel free to use whatever programming language you're most comfortable with. You can select your preferred language/environment from the tabs on the left:__
# - Click on: "Question" > "Language"
# - Select your preferred programming language


# **A few guidelines:**

# - Please don't use AI or LLM assistance during this challenge
# - If you need to look something up online, just let us know what you're searching for and why
# - Think out loud! We're interested in understanding your problem-solving approach, so sharing your thought process as you work is really helpful to us

# Looking forward to seeing how you approach this!



class Queue:

    def __init__(self, upper_limit:int):
        self.mylist = []
        self.upper_limit = upper_limit
        self.length = 0
    
    def push(self, item):
        if self.length < self.upper_limit:
            self.mylist.append(item)
            self.length += 1
        else:
            raise Exception("Queue upper limit reached")

    def popleft(self):
        if self.length == 0:
            raise Exception("Queue is empty")
        popped_element = self.mylist[0]
        self.mylist = self.mylist[1:]
        self.length -= 1
        return popped_element

    def first_element(self):
        if self.length == 0:
            raise Exception("Queue is empty")
        return self.mylist[0]

    def remove_all(self):
        self.mylist = []

    def is_empty(self):
        return self.length == 0


# q = Queue(5)
# q.push(20)
# q.push(21)
# q.push(22)
# q.push(23)
# q.push(24)
# # q.push(25)
# print(f"{q.popleft()}")
# print(f"{q.popleft()}")
# print(f"{q.popleft()}")
# print(f"{q.popleft()}")
# print(f"{q.popleft()}")
# print(f"{q.popleft()}")


class PriorityQueue:

    def __init__(self):
        self.mylist = {}
        self.length = 0
    
    def push(self, item, priority):
        if priority in self.mylist:
            self.mylist[priority].append(item)
        else:
            self.mylist[priority] = [item]
        self.length += 1

    def pop(self):
        if self.length <= 0:
            raise Exception("Queue is empty")
        priorities_sorted = sorted(self.mylist.keys())
        max_priority = priorities_sorted[0]
        result = self.mylist[max_priority][0]
        if len(self.mylist[max_priority]) > 1:
            self.mylist[max_priority] = self.mylist[max_priority][1:]
        else:
            del self.mylist[max_priority]
        self.length -= 1
        return result

    def peek(self):
        if self.length <= 0:
            raise Exception("Queue is empty")
        priorities_sorted = list(sorted(self.mylist.keys()))
        max_priority = priorities_sorted[0]
        return self.mylist[max_priority][0]
        
    def is_empty(self):
        return self.length == 0


q = PriorityQueue()
q.push(20,6)
q.push(21,0)
q.push(22,4)
q.push(23,4)
q.push(24,5)
print(q.peek())
print(q.pop())
print(q.peek())