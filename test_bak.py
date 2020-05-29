a12, a13, a14, a15, a16, a17, a18, a19, a20 = 0,0,0,0,0,0,0,0,0

# Get the first input
str_input = input().split(",")

start = int(str_input[0])
end = int(str_input[1])
while start != -1 and end != -1:
	if 12.5 > start and 12.5 < end:
		a12 += 1
	if 13.5 > start and 13.5 < end:
		a13 += 1
	if 14.5 > start and 14.5 < end:
		a14 += 1
	if 15.5 > start and 15.5 < end:
		a15 += 1
	if 16.5 > start and 16.5 < end:
		a16 += 1
	if 17.5 > start and 17.5 < end:
		a17 += 1
	if 18.5 > start and 18.5 < end:
		a18 += 1
	if 19.5 > start and 19.5 < end:
		a19 += 1
	str_input = input().split(",")

	start = int(str_input[0])
	end = int(str_input[1])
for i in range(12, 20):
	print("[" + str(i) + "," + str(i+1) + "):" + str(eval('a' + str(i))))