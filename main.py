import requests
import json


def listToString(s):
    # initialize an empty string
    str1 = " "

    # return string
    return str1.join(s)


url = "https://app.fakejson.com/q/1P7FQdFq?token=CVuc-35tnqfJ1eARz2OWYg"

r = requests.get(url)
# print(r.content.decode("utf8"))
j = json.loads(r.content.decode("utf8"))
print(j['homeworks'])
data = json.dumps(j['homeworks'])
data = json.loads(data)

SearchDate = input('Get homework on date : ')
HomeworkOnDate = json.loads(json.dumps(list(filter(lambda x: x['date'] == SearchDate, data))))

work = list(i['works'] for i in HomeworkOnDate)
work = work.__str__().replace("[", "").replace("]", "").replace("'", "").replace(", ", "\n")

print(work)
