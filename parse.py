from bs4 import BeautifulSoup
import requests
import csv
import ssl
import re


def get_html(url):
    r = requests.get(url, verify=False)
    r.encoding = 'utf8'
    return r.text


def getDataByURL(url, product_name):
    text = get_html(url)
    soup = BeautifulSoup(text, 'lxml')

    newDict = {}

    for tags in soup.find_all("div", "main-price-elevator-item"):
        if "Новороссийск" in tags.find("p").text:
            nameOrg = tags.find("h3").text.strip().replace(u'\xa0', u' ')

            classes = []
            dopInfo = []
            prices = []

            if "»" in nameOrg:
                nameOrg = nameOrg[:nameOrg.rfind("»")+1]
            if "\"" in nameOrg:
                nameOrg = nameOrg[:nameOrg.rfind("\"")+1]
            newDict[nameOrg] = []
            for tag in (tags.tbody.find_all("div", "name")):
                classes.append(tag.text.strip())
            for tag in (tags.tbody.find_all("tr", {"class", "price-data"})):
                prices.append(tag.td.text.strip())
            for tag in (tags.tbody.find_all("div", "props")):
                dopInfo.append(tag.text.strip())
            for i in range(len(classes)):
                newDict[nameOrg].append([classes[i].replace(u'\xa0', u' '), dopInfo[i].replace(
                    u'\xa0', u' '), prices[i].replace(u'\xa0', u' ')])
            if (newDict[nameOrg] == []):
                newDict.pop(nameOrg, None)
<<<<<<< HEAD
=======
            
    return newDict
>>>>>>> algorithm

    return dataToString(newDict, product_name)

def dataToString(dict, product_name):
    temp_str = ""
    for (keys, values) in dict.items():
        for value in values:
            temp_str += "<b>" + keys + " - " + \
                value[0] + " - " + value[2] + "</b>" + "\n"
            if product_name == "Пшеница":
                buf = re.findall(r'[п][р][о][т][е][и][н][ ][≥][ ][ ][0-9]{2}[,][0-9]', value[1])
                temp_str += "".join(buf) + "\n\n"
            else:
                temp_str += value[1] + "\n\n"
    return temp_str
<<<<<<< HEAD
=======

def strConvert(str):
    try: 
        return float(str[:str.index(" ")].replace(",","."))
    except ValueError:
        return 0

def getMaxPrice(dict):

    returnStr = ""
    finalString = []
    newDict = {}
    classes = []
    ports = []
    prices = []
    
    for (key,values) in dict.items():
        for value in values:
            ports.append(key)
            classes.append(value[0])
            prices.append(strConvert(value[2]))
            if strConvert(value[2]) != 0:
                try:
                    newDict[value[0]].append(strConvert(value[2]))
                except KeyError:
                    newDict[value[0]] = [strConvert(value[2])]
            
    for key in newDict.keys():
        newDict[key] = [max(newDict[key]),min(newDict[key])]

    for i in range(len(classes)):
        for (keys, values) in newDict.items():
            if (keys == classes[i]) and (values[0] == prices[i]):
                finalString.append("{CLASS}, Максимальная цена - {MAX} р, {PORT}\n".format(
                    PORT = ports[i],
                    CLASS = keys,
                    MAX = values[1]
                ))
            if (keys == classes[i]) and (values[1] == prices[i]):
                finalString.append("{CLASS}, Минимальная цена - {MIN} р, {PORT}\n".format(
                    PORT = ports[i],
                    CLASS = keys,
                    MIN = values[1]
                ))

    for el in sorted(finalString):
        returnStr += el + "\n"

    return returnStr



#print(getMaxPrice(getDataByURL("https://rif-rostov.ru/price/?arCrops%5B%5D=127")))

'''
print("ququ")
text = get_html("https://zerno-trade.biz")
soup = BeautifulSoup(text, 'lxml')

newDict = {}
table = soup.find("table", { "class" : "p1-table" })

for el in table.find_all("th"):
    newDict[el.text.strip()] = []

#for row in table.find_all("tr"):
    


print(mas)
'''
>>>>>>> algorithm
