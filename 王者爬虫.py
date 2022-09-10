'''
https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/548/548-bigskin-1.jpg

https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/502/502-bigskin-1.jpg

https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/540/540-bigskin-1.jpg

https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/106/106-bigskin-6.jpg
'''
import requests
import json
import pprint
url = 'https://pvp.qq.com/web201605/js/herolist.json'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
response = requests.get(url=url, headers=headers)
data_lif = response.json()
for data in data_lif:
    # print(data)
    cname = data['cname']                #英雄名称
    ename = data['ename']                 #英雄编号
    try:
        skin = data['skin_name'].split('|')
    except Exception as e:

        print(e)

    for i in range(len(skin)):
        # print(i+1)

        try:
            hero_url = f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{ename}/{ename}-bigskin-{i+1}.jpg'
        except Exception as e:
            print(e)
        # print(hero_url)
        res_url = requests.get(url=hero_url, headers=headers).content

        with open('hero//' + cname + '-' + skin[i] + '.jpg', 'wb') as f:
            f.write(res_url)

            print('正在下载:' + cname + '-' + skin[i])
