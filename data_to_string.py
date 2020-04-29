import re


def strConvert(str):
    try:
        return float(str[:str.index(" ")].replace(",", "."))
    except ValueError:
        return str


newDict = {}
newVal = []
array = []
dict_ = {"АО «НКХП»": [["Пшеница 4-го класса", "15,00 р."],
                       ["Пшеница 3-го класса", "16,00 р."],
                       ["Пшеница 4-го класса", "17,00 р."]],
         "АО «КСК»": [["Пшеница 3-го класса", "18,00 р."],
                      ["Пшеница 3-го класса", "19,00 р."],
                      ["Пшеница 4-го класса", "20,00 р."]]}
for (keys, values) in dict_.items():
    for value in values:
        index = value[0].find("4-го")
        if index != -1:
            newVal.append(value[0])
            newVal.append(strConvert(value[1]))
            array.append(newVal)
            newDict.update({keys: array})
        newVal = []
    array = []
final_dict = dict([min(newDict.items(), key=lambda val: val[1])])
# print(newDict)
print(final_dict)
