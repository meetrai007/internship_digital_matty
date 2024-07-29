# n = int(input())
# arr = map(int, input().split())

arr=[5,7,5,4,2,4,7]

# arr2=arr.sort()
# arr3=arr2.reverse()
# print(arr3[1])
remdup=set(arr)
arr2=list(sorted(remdup,reverse=True))
print(arr2[1])