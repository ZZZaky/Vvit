list = []
for i in range(50):
    list.append(i+1)

list.sort(reverse=True)
first = list[0]
second = list[1]
s = 0
p = 0
s_max = 0
maxim = []
for i in range(2, len(list)):
    if second + list[i] > first and first + second > list[i] and first + list[i] > second:
        p = (first + second + list[i]) / 2
        s = (p*(p-first)*(p-second)*(p-list[i])) ** 0.5
        maxim = [first, second, list[i]]
        break

print(s, "  ", maxim)
