import keyword
from itertools import batched


zaboroneni = keyword.kwlist
# print(f"Заборонені назви змінних: {zaboroneni}")
# Заборонені назви змінних: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', …
# Наступний код розбиває список на маленькі списки по 5 в кожному
# dovzhyna_spysku = len(zaboroneni)
# i = 0
# lol = []
# while i < dovzhyna_spysku:
#     li = []
#     for _ in range(5):
#         li.append(zaboroneni[i])
#         i += 1
#         if i == dovzhyna_spysku:
#             break
#     lol.append(li)
# print(*lol, sep="\n")
for batch in batched(zaboroneni, 5):
    print(batch)
