def grid_traveler(m,n):
    if m or n == 0: return 0
    if m and n == 1: return 1
    
    return grid_traveler(m-1,n) + grid_traveler(m,n-1)
    
    
    
    
print(grid_traveler(9,3)) # 3