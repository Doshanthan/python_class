# #condition  if
# # 1.if 

# a=30
# b=20
# if(a>b):
#     print("a is greater")
    

# # 2.if else
# if(a>b):
#     print("a is gerater b")
# else:
#     print("b is gerater a")


# # 3.if elif
# age = 25

# if age < 18:
#     print("You are a minor.")
# elif age >= 18 and age < 65:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")
    
    
# # 4.Nested if

# # Nested If
# # You can have if statements inside if statements, 
# # this is called nested if statements.


# x = 11

# if x > 10:
#     print("Above ten,")
#     if x > 20:
#         print("and also above 20!")
#     else:
#         print("but not above 20.")
        
        

#02.condition while

# Example of a while loop

# count = 0

# while count <5:
#     print("Count is:",count)
#     count += 1

# # Example of a nested while loop
# row = 0
# while row < 3:
#     col = 0
#     while col < 3:
#         # print(f"Row {row}, Col {col}")
#         print("row and col:",row,col)
#         col += 1
#     row += 1
    
    

#03.condition forloop
# Example of inserting a for loop into an existing context

# numbers = [1, 2, 3, 4, 5]
# sum = 0   
# # 0 1 2 3 4 (index)

# for num in numbers:
#     sum += num  #sum=sum+1    0+1
#     # 1+2
#     # 3+3
#     # 6+4
#     # 10+5
    
# print("The sum of numbers:", sum)


# Example of for loop with range() specifying start and end
print("Numbers from 2 to 6:")

for i in range(2, 7, 2): 
    # start=2 end=7(6) step=2 2 4 6      
    print(i)

# Example of for loop with range() specifying start, end, and step
print("Numbers from 1 to 10, skipping every other number:")
for i in range(1, 11, 2):
    print(i)
    
    

# # homework
# '''



# * * * * *

# * * * * *
# * * * * *
# * * * * *
# * * * * *

# *
# * * 
# * * *
# * * * *
# * * * * *

# 1 1 1 1 1
# 1 1 1 1
# 1 1 1
# 1 1
# 1 

# '''
