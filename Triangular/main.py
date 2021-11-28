arr = input('Type numbers: ')
arr = list(arr.split(','))
arr = [int(x) for x in arr]
arr.sort(reverse = True)

maxim = {'1': 0, '2': 0, '3': 0}

area = 0
perimeter= 0

for i in range(2, len(arr)):
    if arr[i - 1] + arr[i] > arr[i - 2] and arr[i - 2] + arr[i - 1] > arr[i] and arr[i - 2] + arr[i] > arr[i - 1]:
        perimeter = (arr[i - 2] + arr[i - 1] + arr[i]) / 2
        area = (perimeter * (perimeter - arr[i - 2]) * (perimeter - arr[i - 1]) * (perimeter - arr[i])) ** 0.5
        
        maxim['1'] = arr[i - 2]
        maxim['2'] = arr[i - 1]
        maxim['3'] = arr[i]
        break

if area > 0:
    print("Maximum area: ", area)
    print("Sides: ", maxim)
else:
    print("No way to create a triangle")