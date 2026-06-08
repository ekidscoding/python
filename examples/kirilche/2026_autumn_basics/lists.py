from rich_print import line, print_code, print_error, print_header, print_info, print_warn, print_tip
print_header("1. Create an empty list")

list1 = []
print_code("list1 = []")
print_info(f"List created with `[]`: {list1}")

print_info("or")

list2 = list()
print_code("list2 = list()")
print_info(f"List created with `list()`: {list2}")

print_header("2. Add an element to the list")

my_list = ["Kyiv", "Lviv", "Odesa"]
print_code('my_list = ["Kyiv", "Lviv", "Odesa"]')

my_list.append("Mykolaiv")
print_code('my_list.append("Mykolaiv")')
print_info(my_list)

print_warn("you can't add 2 elements with `append()`")

# my_list.append("Rivne", "Luts'k")
print_error('''    my_list.append("Rivne", "Luts'k")
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
    TypeError: list.append() takes exactly one argument (2 given)''')

print_header("3. to add more than 1 element use `extend()`")

print_info("this works")

my_list.extend(["Rivne", "Luts'k"])
print_code('my_list.extend(["Rivne", "Luts\'k"])')

print_info(my_list)

print_header("4. Get element by Index")

print_info("We can use `[]` after the list name e.g:")

print_tip('''we count from 0
            Index| Order
            ---- | -----
            0    | First
            1    | Second
            2    | Third
            ...  |''')

print_info(my_list)

print_code("first = my_list[0]")
first = my_list[0]
print_code("print(first)")
print_info(first)

print_code("second = my_list[1]")
second = my_list[1]
print_code("print(second)")
print_info(second)

print_header("5. Deleting element from the list")
from contextlib import suppress

print_info('First, add 2 more elements')
my_list.extend(["Warsaw", "Ankara"])
print_code('my_list.extend(["Warsaw", "Ankara"])')
print_info(my_list)

print_warn("you can't remove 2 elements with `remove()`")

# my_list.remove("Warsaw", "Ankara")
print_error('''    my_list.remove("Warsaw", "Ankara")
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
    TypeError: list.remove() takes exactly one argument (2 given)''')

print_info('remove one of them')
with suppress(ValueError):
    my_list.remove('Ankara')

print_code("my_list.remove('Ankara'):")
print_info(my_list)
