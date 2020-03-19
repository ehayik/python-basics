""""
Write a program that extracts the last three items in the list sports and assigns it to the
variable last. Make sure to write your code so that it works no matter how many items are in the list.
"""
sports = ['curling', 'ping pong', 'hockey']
last = sports[-3:]
print(last)

by = "You are"
az = "doing a great "
io = "job"
qy = "keep it up!"

words = by.split() + az.split() + [io + ","] + qy.split()
message = " ".join(words)

print(message)


rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
rainfall_mi = rainfall_mi.split(", ")
num_rainy_months = 0

for elm in rainfall_mi:
    if float(elm) > 3:
        num_rainy_months += 1