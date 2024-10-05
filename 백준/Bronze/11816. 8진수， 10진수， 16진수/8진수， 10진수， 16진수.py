num = input()

if num[0] == '0':
    if num[1] == 'x':
        print(int(num, 16))
    else:
        print(int(num, 8))
else:
    print(int(num))