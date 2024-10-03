#Python program to perform Linear search
list1=[]
ele=int(input("How many elements"))
for i in range(ele):
  list1.append(int(input()))
print(list1)
ele=int(input("Enter the search element :"))
for i in list1:
  if ele==i:
    print("Element ",ele," is found at position ",list1.index(ele)+1)
    break
else:
  print("Element ",ele," not found in the list")

