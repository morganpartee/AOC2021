with open('data.txt', 'r') as f:
    data = list(map(int, f.readlines()))

last = sum(data[0:3])
out = 0

for i in range(1, len(data[1:])):
    current = sum(data[i:i+3])
    if current > last:
        out += 1
    last = current

print(out)