size = int(input("Enter number of elements in the list:"))
print("Enter elements one by one:")
li = [int(input()) for _ in range(size)]
etf = int(input("Enter element to find: "))
li.sort()
min = 0
max = size-1
found = False
while (min<=max):
	mid = (min+max)//2
	if (li[mid] == etf):
		print(f"Element found at {str(mid)}")
		found = True
		break
	elif(etf>li[mid]):
		min = mid+1
	else:
		max = mid-1
if(not found):
	print("Element not found")
