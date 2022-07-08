numbers="Manish"
# use new_list=["new_item" for "item" in "list" if test]
new_list=[n for n in numbers]
print(new_list)
# xyz=''.join(new_list)
# print(xyz)

double_num=[n*2 for n in range(1,11) if n%2==0]
print(double_num)

# squared numbers:
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers=[n**2 for n in numbers]
even_numbers=[n for n in numbers if n%2==0]
print(even_numbers)
print(squared_numbers)