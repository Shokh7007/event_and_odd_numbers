#A four-digit integer is given. Find the number of odd digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of odd digits in the variable "var_int".
x=1234
a=x%10
b=x%100//10
c=x%1000//100
d=x%10000//1000
print(b+d)