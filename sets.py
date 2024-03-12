A = {}
B = {}

A = {(input("Enter Set A elements: "))
     for _ in range(int(input("How many elements in set A? ")))}
B = {(input("Enter Set B elementS: "))
     for _ in range(int(input("How many elements in this set B? ")))}

print("Each Set and Elements:", A, B)

common_elements = A.intersection(B)

print("Common elements in both sets:", common_elements)
