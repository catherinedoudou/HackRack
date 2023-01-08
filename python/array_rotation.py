### brief
## rotate an array by shifting K places
## input ([1,2,3], 2)
## output ([2,3,1])


# def solution(arr, k):
#     if len(arr) == k:
#         return arr
#     if sum(arr) == 0:
#         return arr
#     rotation = []
#     for i in range(k-1, len(arr)):
        
#         rotation.append(arr[i])
#     for i in range(len(arr)-k):
#         rotation.append(arr[i])
#     return rotation







def solution(arr, k):
    arr = list(reversed(arr))
    new_arr = arr[:k]
    new = arr[k:]
    print(list(reversed(new_arr))+list(reversed(new)))
    
    

tests = [([3, 8, 9, 7, 6],3),
         ([0,0,0],1),
         ([1,2,3,4],4)]

for test in tests:
    solution(*test)
