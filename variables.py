#! /usr/bin/python

#We create a variable by writing the name of the variable we want followed by an equal sign, which is folowed by the value we want to stre in the variable. For example, the following line creates a variabel called hello_str, containing the string Hello World.

hello_str = "Hello World"

hello_bool = True

hello_tuple = (21,32)

hello_list = ["hello," , "this" , "is" , "a" , "list"]
#you can also create the same list in the following way:

hello_list = list()
hello_list.append("Hello,")
hello_list.append("this")
hello_list.append("is")
hello_list.append("a")
hello_list.append("list")

#the first line creates an empty list and the following lines use the append function of the list type to add elements to the list. This way of using a list isnt' really very useful when working with strings ou know of in advance, but it can be useful when working with dynamic data such as a user input. This list will overwrite the first list without any warning as we are using the same variable name as the previous list.

hello_dict = {
    "first_name": "Liam",
    "last_name" : "Fraser",
    "eye_color" : "Blue"
}

#lest access soem elements inside our collections. We'll start by chaingint he value of the last string in our hello_list and add an exclaimation mark to the end. The "list" string is the 5th element in the list. However, indexes in Python are zero-based, which means the first elemnent has an index of 0.

print(hello_list[4])
hello_list[4] += "!"
#the above line is athe same as
hello_list[4] = hello_list[4] + "!"
print(hello_list[4])

print(str(hello_tuple[0]))

print(hello_dict["first_name"] + " " + hello_dict["last_name"] + " has " + hello_dict["eye_color"] + " eyes." )


print("{0} {1} has {2} eyes.".format(hello_dict["first_name"], hello_dict["last_name"], hello_dict["eye_color"]))
