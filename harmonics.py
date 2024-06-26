amplitude = 10
total_mw = 0

for x in range(1, 13, 2):
    total_mw += ((2 * amplitude) / (x * 3.14 * (3 ** 0.5))) ** 2

print(total_mw)