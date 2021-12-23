#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)
my_pets = ["dog", "cat"]
print(my_pets)
my_pets.append("bird")
print(my_pets)
zoo_animals = ["lion", "tiger", "bear"]
my_pets.extend(zoo_animals)
print(my_pets)
