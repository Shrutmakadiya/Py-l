cities = ["surat", "bharuch", "rajkot"]
fruits = ["apple","guava","banana","strawberry","avocado"]
# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(fruits)

# def print_list(list):
#     for i in list:
#         print(i, end=" ")
# print_list(fruits)
# print()


#print factorials
# n = int(input("Enter a number to find factorial : "))
# def cal(num):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)

# cal(n)



# n = int(input("Enter a number to find indian value : "))
# def converter(usd_val):
#     ind_val = usd_val * 83
#     print(usd_val,"USD =",ind_val)

# converter(n)



#=>RECURSION
# n = int(input("Enter a natural number to find sum : "))
# def cal_sum(n):
#     if(n == 0):
#         return 0
#     return cal_sum(n-1) + n
# sum = cal_sum(n)
# print(sum)

# def print_list(list, idx=0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)

# print_list(fruits)