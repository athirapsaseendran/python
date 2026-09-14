numbers = input("Enter numbers separated by comma: ")

my_list = numbers.split(",")
my_tuple = tuple(my_list)

print("List:", my_list)
print("Tuple:", my_tuple)