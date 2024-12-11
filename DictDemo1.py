# empset={"QA":"Mukesh","Dev":"Akash","Devops":"John","Security":98, 50:"Python"}

# print(type(empset))

# print(empset["Dev"]) #o/p is Akash

# print(empset.get("Dev")) #o/p is Akash

# print(empset.get(50))  #o/p is Python


# list in dictionary


# empset={"QA":["Mukesh","Rahul","David"],"Dev":"Akash","Devops":"John"}

# print(empset["QA"])

# print(empset["QA"][2])


# empset1=empset["QA"]

# print(empset1)

# print(empset1[1])


# Dictionary in dictionary

# emp={"QA":"Mukesh","Dev":{"Frontend":"Rajeev","backend":"Neha"}}

# print(emp.get("Dev"))

# print(emp.get("Dev").get("Frontend"))


# print(emp["Dev"])

# print(emp["Dev"]["Frontend"])


# emp1=emp["Dev"]

# print(emp1)

# emp_name=emp1["Frontend"]

# print(emp_name)


# adding/add some key and value in the dictionary


# emp={"QA":"Mukesh","Dev":{"Frontend":"Rajeev","backend":"Neha"}}

# emp["Manager"]="XYZ" #adding the name in the above dictionary

# print(emp)


# updating/update existing value"XYZ" with "Sathya" in the dictionary

# emp={"QA":"Mukesh","Dev":{"Frontend":"Rajeev","backend":"Neha"}}

# emp["Manager"]="Sathya"

# print(emp)


# remove the key and value from the dictionary

# emp={"QA":"Mukesh","Dev":{"Frontend":"Rajeev","backend":"Neha"}}

# emp.pop("QA") #at least one argument require in the pop

# print(emp)


# emp={"QA":"Mukesh","Dev":{"Frontend":"Rajeev","backend":"Neha"}}

# emp["Manager"]="XYZ" #adding the name in the above dictionary

# emp["Manager"]="Sathya" #updating the value in the dictionary

# print(emp.popitem()) #it will remove the last added key and value --interview question

# print(emp)