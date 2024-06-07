#convert the following dictionary into JSON format.
import json
Student_data = {"name": "Samir", "age":13, "marks":87}
data = json.dumps(Student_data)
print(data)
print(type(data))


# Student_data = {"name": "Samir", "age":13, "marks":87}

data = json.load(Student_data)
print(data["age"])