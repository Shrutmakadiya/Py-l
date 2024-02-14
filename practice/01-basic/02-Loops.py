# Print numbers from 1 to 100.
# i=1
# while i <= 100:
#     print(i)
#     i += 1

#Print numbers from 100 to 1.
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# Print the multiplication table of a number n.
# num1 = int(input("Enter number for tabel : "))
# i = 1
# while i <= 10:
#     print(num1*i)
#     i+=1

# Print the elements of the following list using a loop: [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx+=1

# Search for a number x in this tuple using loop:
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
# x = 25
# i=0
# while i < len(nums):
#     if(nums[i] == x):
#         print("found at idx", i)
#     i += 1


# Print the elements of the following list using a loop:
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# for num in nums:
#     print(num)

# Search for a number x in this tuple using loop:
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# x = 36
# idx = 0 
# for num in nums:
#     if(num == x):
#         print("founs 36 at index:",idx)
#         break #for only one time
#     idx += 1



# using for & range( )

#Print numbers from 1 to 100
# for num in range(1,101):
#     print(num)

# Print numbers from 100 to 1.
# for num in range(100,0,-1):
#     print(num)

# Print the multiplication table of a number n.
# num1 = int(input("Enter number for tabel : "))
# for i in range (1,11):
#     print(num1*i)

# WAP to find the sum of first n numbers. (using while)
# n = 6
# sum = 0
# i = 1
# while i <= n:
#     sum+=i
# print("Total is :", sum)
# for i in range(1, n+1):
#     sum += i
# print("Total is :", sum) 

# WAP to find the factorial of first n numbers. (using for)
# n=5
# fact = 1
# for i in range(1, n+1):
#     fact*=i
# print("factorial is : ", fact)
# i = 1
# while i <= n:
#     fact*=i
#     i += 1
# print("factorial is : ", fact)