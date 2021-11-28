arr = input('Type numbers: ')
arr = list(arr.split(' '))
arr = [int(x) for x in arr]
arr.sort(reverse = True)

maxim = {'1': 0, '2': 0, '3': 0}

a = 0 #area
p = 0 #perimeter

for i in range(2, len(arr)):
    if arr[i - 1] + arr[i] > arr[i - 2] and arr[i - 2] + arr[i] > arr[i - 1] and arr[i - 2] + arr[i - 1] > arr[i]:
        p = (arr[i] + arr[i - 1] + arr[i - 2]) / 2
        a = (p * (p - arr[i]) * (p - arr[i - 1]) * (p - arr[i - 2])) ** 0.5
        
        maxim['1'] = arr[i]
        maxim['2'] = arr[i - 1]
        maxim['3'] = arr[i - 2]
        break

if a > 0:
    print("Maximum area: ", a)
    print("Sides: ", maxim)
else:
    print("No way to create a triangle")
