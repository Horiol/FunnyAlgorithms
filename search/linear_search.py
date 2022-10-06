l = int(input("Enter number of elements in the list:"))
print("Enter elements one by one:")
li = [int(input()) for _ in range(l)]
etf = int(input("Enter element to find: "))
found = False
location = -1
counter = 0
for x in li:
	if(x==etf):
		found = True
		location = counter
		break
	counter+=1
if found:
	print(f"Element {etf} found at {str(location)}")
else:
	print("Element not found")
