n = float(raw_input())
t1 = int(raw_input())
t2 = int(raw_input())

total = n+ n*t1/100 +n*t2/100
print("The total meal cost is {} dollars.".format(int(round(total))))