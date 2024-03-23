n_len = int(input())

num_list = list(map(int, input().split()))

print(num_list)
search_num = int(input())

sum = 0

for j in num_list:
    if j == search_num:
        sum+=1

print(sum)

    
    
