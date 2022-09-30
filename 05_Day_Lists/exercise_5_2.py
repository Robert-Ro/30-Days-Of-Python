ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min = ages[0]
print("min of ages: ", ages[0])
ages.sort(reverse=True)
max = ages[0]
print("max of ages: ", ages[0])
ages.append(min)
ages.append(max)
print("ages after append min and max: ", ages)