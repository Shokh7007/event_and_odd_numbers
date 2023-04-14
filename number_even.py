#A four-digit integer is given. Find the number of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of even digits in the variable "var_int".
x=1244
a=x%10
b=x%100//10
c=x%1000//100
d=x%10000//1000
print((a-1)%2+(b-1)%2+(c-1)%2+(d-1)%2)