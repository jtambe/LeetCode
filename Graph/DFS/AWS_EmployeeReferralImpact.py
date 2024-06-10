from typing import List, Dict
"""
Given a list of employees and their referrals, count the referralImpact for each employee
No cycles exist in adjecency list

Input : [[1,2][2,3][3,4][2,4][4,5]]
Output:
1: 4
2: 3
3: 2
4: 1
5: 0
"""
class solution:

    def referralImpact(self, referrals : List[List[int]]) -> Dict[int, int]:

        d = {} # emp :(referrals)
        ans = {} # emp : referralImpact

        # create adjencency List
        # create ans dictionary marked 0 for all employees
        for x in referrals:
            emp = x[0]
            referred = x[1]
            if emp in d:
                alist = d[emp]
                alist.add(referred)
                d[emp] = alist
            else:
                d[emp] = set()
                d[emp].add(referred)
            if referred not in d:
                d[referred] = set()
            ans[emp] = 0
            ans[referred] = 0

        visitedEmp = set()
        def dfs(emp: int, parents: List[int], visitedReferred: set):
            
            # if there are no further employees to explore return
            if not d[emp]: 
                return
            for referral in d[emp]:
                if referral not in visitedReferred:
                    ans[emp] = ans[emp] +1
                    for x in parents:
                        ans[x] = ans[x] + 1
                    visitedReferred.add(referral)

                if referral not in visitedEmp:
                    visitedEmp.add(referral)
                    parents.append(emp)
                    dfs(referral, parents, visitedReferred)
                    # once chain ends and dfs returns from base condition, 
                    # before we explore next referral in adjecency list, we need to remove last added parent from stack
                    # This will avoid repeating that parent in subsequent dfs stack
                    parents.pop()

        for emp in d:
            if emp not in visitedEmp:
                visitedEmp.add(emp)
                dfs(emp, [], set())
        return ans


sln = solution()
referrals = [[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[6,8]]
# d {1: {2, 3, 4, 5}, 2: {3, 6}, 3: set(), 4: set(), 5: set(), 6: {8}, 8: set()}
# expected output : {1: 6, 2: 3, 3: 0, 4: 0, 5: 0, 6: 1, 8: 0}
ans = sln.referralImpact(referrals)
print(ans)

referrals = [[1,2],[2,3],[3,4],[2,4],[4,5]]
# {1: 4, 2: 3, 3: 2, 4: 1, 5: 0}
ans = sln.referralImpact(referrals)
print(ans)

referrals = [[1,2],[9,3]]
ans = sln.referralImpact(referrals)
print(ans)

