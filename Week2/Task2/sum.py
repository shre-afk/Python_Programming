# Task 2. Given a string s1, write a program to return the sum and average of the digits that
# appear in the string, ignoring all other characters.

s1 = input("Enter a string:")

total=0
cnt=0
average=0

for i in s1:
    if  i.isdigit():
        total=total+int(i)
        cnt=cnt+1

print("Sum is ",total)

if cnt>0:
    print("Average is ",(total/cnt))
else :
    print("No numbers in the string :|")