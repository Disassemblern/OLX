import bisect

def solution(juice, capacity):
    N = len(juice)
    
    sorted_juice = sorted(juice)
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + sorted_juice[i]
    
    max_flavors = 1
    
    for i in range(N):
        space = capacity[i] - juice[i]
        
        pos_i = bisect.bisect_left(sorted_juice, juice[i])
        
        low, high = 0, pos_i
        max_fit_before = 0
        while low <= high:
            mid = (low + high) // 2
            if prefix[mid] <= space:
                max_fit_before = mid
                low = mid + 1
            else:
                high = mid - 1
        candidate1 = 1 + max_fit_before
        
        low, high = pos_i + 1, N
        max_fit_after = 0
        while low <= high:
            mid = (low + high) // 2
            if mid > N:
                break
            if prefix[mid] - juice[i] <= space:
                max_fit_after = mid
                low = mid + 1
            else:
                high = mid - 1
        candidate2 = max_fit_after  
        
        current_max = max(candidate1, candidate2)
        max_flavors = max(max_flavors, current_max)
    
    return max_flavors