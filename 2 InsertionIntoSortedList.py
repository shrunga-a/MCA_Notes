n=int(input("How many elements: \n"))
arr=[]
print("Enter ",n,"  array elements :")
for i in range(n):
    arr.append(int(input()))
arr.sort()
print(arr)
ele=int(input("Enter element to be inserted: "))
for i in arr:
    if i>ele:
        arr.insert(arr.index(i),ele)
        break
else:
  arr.append(ele)
print("Elements in the list after insertion: \n",arr)
