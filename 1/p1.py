with open('data.txt', 'r') as f:
    data = list(map(int, f.readlines()))

last = data[0]
out = 0

for current in data[1:]:
    if current > last:
        out += 1
    last = current

print(out)