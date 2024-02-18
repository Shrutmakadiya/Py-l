'''Create a new file “practice.txt” using python. Add the following data in it:
Hi everyone
we are learning File I/O
using Java.
I like programming in Java.'''
# '''ans'''
# with open("practice.txt", "w") as f:
    # f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")



'''WAF that replace all occurrences of “java” with “python” in above file.'''
# with open("practice.txt",'r') as f:
#     data = f.read()

# new_data = data.replace("Java","Python")
# print(new_data)

# # write new data in file
# with open("practice.txt", "w") as f:
#     f.write(new_data)




'''Search if the word “learning” exists in the file or not.'''
# def check_word(file_name, word_forFind):
#     with open(file_name,"r") as f:
#         data = f.read()
#         if(data.find(word_forFind) != -1):
        #   if(word_forFind in data):
#             print("found")
#         else:
#             print("not found")

# fileName = input("enter file Name : ")
# word = input("Enter a word which found : ")

# check_word(fileName,word)



'''WAF to find in which line of the file does the word “learning”occur first.
Print -1 if word not found'''



'''From a file containing numbers separated by comma, print the count of even numbers.'''
count = 0
# with open("practice2.txt","r") as f:
#     data = f.read()
#     print(data)

#     nums = data.split(",")
#     for i in nums:
#         if(int(i) % 2 == 0):
#             print(i)
#             count += 1

# print(count)