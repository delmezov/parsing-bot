from bs4 import BeautifulSoup
import requests
import csv
import ssl


def get_html(url):
    r = requests.get(url, verify=False)
    r.encoding = 'utf8'
    return r.text


def getDataByURL(url):
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

    return dataToString(newDict)

# print(list(getDataByURL("https://rif-rostov.ru/price/?arCrops%5B%5D=127").keys())[0])


def dataToString(dict):
    data = []
    temp_str = ""
    for (keys, values) in dict.items():
        for value in values:
            temp_str = "<b>" + keys + " - " + \
                value[0] + " - " + value[2] + "</b>" + "\n"
            temp_str += value[1]
            data.append(temp_str)

    return data
