#1.Write to find odd or even number and take the input from user.

n=int(input('enter number:'))
if n%2==0:
    print('even')
else :
    print("odd")

#2.Write a program to find the person is eligible for votes or not and take the age as input ?

n=int(input('enter age'))
 
if n>18:
    print('person is eligiable for vote')

else:
    print('person not eligiable for vote')
#3.write a python program to calculate the area of a rectangle .ask the user for length and width of the rectangle as input?

length=int(input('Enter a length of rectangle:'))
width=int(input('Enter a width of rectangle:'))
Area=length*width
print('Area of rectangle:',Area)

#4.Create a python program to that takes a number from user and check if it is positive,negative,zero?

n=int(input('Enter a number:'))
if n>0 :
    print('it is positive')
elif n<0 :
    print('it is negative')
else : 
    print('it is zero')

#5.Develop a python programto convert a temperature form faherenheit to celsius.promot the user to enter the temperature in fehrenheit?

fehrenheit=int(input('Enter the temperature in fehrenheit:'))

celsius= (fehrenheit-32)*5/9
print('The temperature in celsius:',celsius)

#6.create a python program that checks whether a given year is leap year or not .Ask the user to input the year?

year=int(input('Enter a year:'))
if (year %4 == 0 and year %100 != 0)or(year %400 == 0):
    print('it is leap year',year)
else :
    print('it is not leap year',year)

#7.Develop a python program to find the largest among three numbers .prompt the user to input three numbers?

number1=int(input('Enter the first number:'))
number2=int(input('Enter the Second number:'))
number3=int(input('Enter the Third number:'))

largest=max(number1,number2,number3)
print('the largest numbers is:',largest)

#8.Develop a python program to find the smallest among three numbers .prompt the user to input three numbers?

num1=int(input('Enter a  first number:'))
num2=int(input('Enter a second  number:'))
num3=int(input('Enter the third number:'))

smallest=min(num1,num2,num3)
print('the smallest numbers is:',smallest)

