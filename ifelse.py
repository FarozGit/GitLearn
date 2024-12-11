a = 80

if a > 50:
    print("hello")

'''



#if 100>10:print("Yes")



#if 10>100:print("Yes")

#print("10 is lesser than 100")



#print("Yes") if 50>10 else print("no")



#mark=85

#print("A+") if mark>90 else print("A")



'''

a = 100

if a > 100:

    print(" a is greather than 100")

else:

    print("a is equal to 100")

'''



'''

name = "Python"

if name == 'Python':

    print("Python found")

else:

    print("Python not found")

'''



'''

language = "Python"

if language == "Seleninum":

    print("Selenium is declared")

elif language == "Java":

    print("Java is declared")

elif language == "Python":

    print("Python is declared")

'''



'''

language = "Python"

if language == "Seleninum":

    print("Selenium is declared")

elif language == "Java":

    print("Java is declared")

elif language == "SQL":

    print("SQL is declared")

else:

    print("Sorry could not found anything")

'''



'''

language = input("Enter the programming language: ")

if language == "selenium":

    print("Selenium found")

elif language == "Java":

    print("Java found")

elif language == "Python":

    print("Python found")

else:

    print("Sorry we couldn't find ")

'''



'''

# nestedif condition


sal = 50000

if sal > 40000:

    print("Eligible for car loan")

    if sal > 60000:

        print("Eligible for bike loan")

        if sal > 30000:
            print("Eligible for home loan")



else:

    print("Sorry you are not eligible")

'''



'''

salary = input("please enter the salary: ")

sal = int(salary)

print(sal)

print(type(sal))

if sal > 50000:

    print("Salary is greater than 50000")

    if sal > 10000:

        print("Salary is 10000")

        if sal < 20000:
            print("Salary is less than 20000")

else:

    print("Given Salary is not matching with above Salary")

'''



'''

status = False

names = ["Python", "Java", "JS", "CSharp"]

for name in names:

    if name == "JS":

        status = True

        break

    else:

        print("Still searching")

if status:

    print("we found the JS in the third iteration")

else:

    print("Sorry we couldn't find")

'''





'''  # below program is not working, because num will hold a single value, so it is not iterable

status = False

number = input("Enter the number: ")

num = int(number)

for x in num:

    if x == 15:

        status = True

        break

    else:

        print("Still we are searching")

if status:

    print("You entered " + x)

else:

    print("We couldn't found")


status = False

lang = input("Please enter the language : ")

for x in lang:

    print(x)

    if x == "Java":

        status = True

        break

    else:

        print("Still we are searching")

if status:

    print("You entered: " + lang)

else:

    print("We couldn't found")

