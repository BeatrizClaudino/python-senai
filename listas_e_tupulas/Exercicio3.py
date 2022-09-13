list = [2, 5, 9, 1, 3]
num = set(list)

while True:
    if (len(list) > 0 and len(list)<6):
        list.pop()
        list.sort(reverse=True)
        print(list)