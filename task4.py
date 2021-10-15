my_list = input().split()
for i in range(len(my_list)):
    if len(my_list[i]) > 10:
        my_list[i] = my_list[i][:10]
    print(i + 1, my_list[i])
