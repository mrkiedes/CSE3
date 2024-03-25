second = 144229

minutes = int(144229 / 60)

second = 144229 % 60

print(type(minutes))

print("Minutes: " + str(minutes) + " Seconds: " + str(second))

print("Years elapsed: ", 2000000000 / 365.25)
print("Days Left: ", float(2000000000 % 365.25))