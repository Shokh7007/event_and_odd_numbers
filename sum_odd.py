#A four-digit integer is given. Find the sum of odd digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_odd" and assign it 0.

#Find the sum of the odd digits in the variable "var_int".
x=1233
a=x%10
b=x%100//10
c=x%1000//100
d=x%10000//1000
print(a%2*a+b%2*b+c%2*c+d%2*d)