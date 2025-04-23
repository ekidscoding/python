list1 = ["abc", "d", "ef", "ghij", "klmnop", "qrstu", "vwxyz"]
list2 = ["абвгґ", "деєжз", "иіїйклм", "нопр", "стуфх", "цчшщьюя"]

list3 = list((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
list3[4] = 123

# for i in range(len(list3)):
#     print(f"{i=}, {list3[i]=}")

summator = 0
for item in list3:
    summator += item
    print(summator)

# print(len(list1))
# accum = 0
# for word in list2:
#     accum += len(word)

# print(f"Загальна кількість букв = {accum}")