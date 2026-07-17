class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, cols = len(matrix), len(matrix[0])

        # early reject if target is out of bounds    
        if target < matrix[0][0] or target > matrix[rows-1][cols-1]:
            return False

        # find the row where number could be
        def find_the_row_index() -> int:
            arr = [matrix[row][0] for row in range(rows)]
            print(f"arr:{arr}")
            if target >= matrix[rows-1][0]:
                return rows-1

            l, r = 0, rows-1
            while l <= r:
                mid = (l+r)//2
                if arr[mid] == target:
                    return mid
                if target > arr[mid]:
                    if mid+1 < rows and target < arr[mid+1]:
                        return mid
                    else:
                        l = mid+1
                if target < arr[mid]:
                    if mid-1 >= 0 and target > arr[mid-1]:
                        return mid-1
                    else:
                        r = mid-1

        # check if the row has the number with basic binary search
        def exist_in_row(row) -> bool:
            arr = matrix[row][:]
            print(f"arr:{arr}")
            l, r = 0, len(arr)-1
            while l <= r:
                mid = (l+r)//2
                if arr[mid] == target:
                    return True
                if target > arr[mid]:
                    l = mid+1
                if target < arr[mid]:
                    r = mid-1
            return False

                    

        row_idx = find_the_row_index()
        return exist_in_row(row_idx)