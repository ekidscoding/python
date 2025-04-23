import copy
original_library = []

original_library.append({"назва": "Маленький принц", "автор": "Антуан де Сент-Екзюпері", "рік_видання": 1943})
original_library.append({"назва": "Гаррі Поттер і філософський камінь", "автор": "Дж. К. Ролінг", "рік_видання": 1997})
original_library.append({"назва": "1984", "автор": "Джордж Орвелл", "рік_видання": 1949})

copy_library = copy.deepcopy(original_library)
copy_library[0]["назва"] = "Le Petit Prince"

print("Перша книга (копія):", copy_library[0])
print("Перша книга (Оригінал):", original_library[0])