def binary_search(data, n):
    bot = 0
    top = len(data) - 1
    mid = (top - bot) // 2
    print(bot,mid,top)
    print('mid',data[mid],'n',n)
    if data[mid] == n:
        #print('n', n)
        print(str(n) + '은 있습니다.')
    elif  bot==top:
        print(str(n) + '은 없습니다.')
    elif data[mid] < n:
        binary_search(data[mid+1 :top+1], n)

    elif data[mid] > n:
        binary_search(data[bot:mid], n)




data = [1, 7, 11, 12, 14, 23, 33, 47, 51, 64, 67, 77, 130, 672, 871]
for i in data:
    binary_search(data,i-1)
