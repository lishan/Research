import requests
import fake_useragent
from lxml import html

headers = {'User-Agent': fake_useragent.UserAgent().random}
# response = requests.get("http://zfyxdj.xa.gov.cn/zfrgdjpt/jggs.aspx?qy=70&yxbh=0000001006&page=100", headers=headers)
# print(response.text)
r1 = 0
r2 = 0
r1pass = 0
r2pass = 0


def output():
    print("r1=" + str(r1) + ", r1pass=" + str(r1pass))
    print("r2=" + str(r2) + ", r2pass=" + str(r2pass))


for i in range(1, 100):
    response = requests.get("http://zfyxdj.xa.gov.cn/zfrgdjpt/jggs.aspx?qy=70&yxbh=0000001006&page=" + str(i),
                            headers=headers)
    if response.text.find("暂未查到意向登记！") != -1:
        print("find it")
        break
    tree = html.fromstring(response.text)
    records = tree.xpath('//table[@class="yxdjmdTable"]//tr')
    for record in records:
        if record[4].text == "普通家庭":
            r2 += 1
            if record[7].text == "核验通过":
                r2pass += 1
        elif record[4].text == "刚需家庭":
            r1 += 1
            if record[7].text == "核验通过":
                r1pass += 1
        output()
print("--------------------------------------")
output()
