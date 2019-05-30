import json
import requests
import time
from fake_useragent import UserAgent
import random, os
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
import numpy as np


# 获取存储职位信息的json对象，遍历获得公司名、福利待遇、工作地点、学历要求、工作类型、发布时间、职位名称、薪资、工作年限
def get_json(url, datas):
    ua = UserAgent()
    my_headers = {
        "User-Agent": ua.random,
        "Referer": "https://www.lagou.com/jobs/list_Python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=",
        "Content-Type": "application/x-www-form-urlencoded;charset = UTF-8"
    }
    time.sleep(random.random() * 5)
    with requests.Session() as ses:  # 获取session
        ses.headers.update(my_headers)  # 更新
        ses.get(
            "https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=")
        response = ses.post(url=url, data=datas, )
        result = response.json()
        info = result['content']['positionResult']['result']

        positionid = [job['positionId'] for job in info]
        # print(positionid)
        city = [job['city'] for job in info]
        companyFullName = [job['companyFullName'] for job in info]
        companyLabelList = [job['companyLabelList'] for job in info]
        district = [job['district'] for job in info]
        education = [job['education'] for job in info]
        firstType = [job['firstType'] for job in info]
        formatCreateTime = [job['formatCreateTime'] for job in info]
        positionName = [job['positionName'] for job in info]
        salary = [job['salary'] for job in info]
        workYear = [job['workYear'] for job in info]

        df = pd.DataFrame(
            {'positionid': positionid,
             'city': city,
             'companyFullName': companyFullName,
             'companyLabelList': companyLabelList,
             'district': district,
             'education': education,
             'firstType': firstType,
             'formatCreateTime': formatCreateTime,
             'positionName': positionName,
             'salary': salary,
             'workYear': workYear,
             }
        )
        if not os.path.exists('python_position.csv'):
            df.to_csv('python_position.csv', index=False, header=True, mode='a', encoding='utf-8-sig')
        else:
            df.to_csv('python_position.csv', index=False, header=None, mode='a', encoding='utf-8-sig')


def mk_plot():
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    data = pd.read_csv('python_position.csv', sep=',', header=0, encoding='utf-8')
    position_cnt = data.groupby(by=['city']).size()  # 每个城市有多少职位
    plt.title('各个城市Python职位数目')
    plt.xlabel('城市名称')
    plt.ylabel('职位数目')
    # position_cnt.plot.bar()
    x = position_cnt.index
    y = position_cnt.values
    plt.bar(x, y)
    plt.show()
    salary_city = data.groupby(['city', 'education'])[
        'salary'].value_counts()  # 这时, 组内操作的结果不是单个值, 是一个序列, 我们可以用.unstack()将它展开
    # salary_mean = data.groupby('city')['salary'].value_counts().unstack()
    shanghai_salary = data[data['city'] == '上海']['salary'].value_counts(normalize=True)  # normalize=True 显示百分比
    education = data['education'].value_counts(normalize=True)
    # salary_city.plot.bar()
    # plt.show()

    # 添加数据标签
    for a, b in zip(x, y):
        plt.text(a, b + 0.05, r'{}'.format(b), ha='center', va='bottom', fontsize=11)
    plt.ylim(0, 3700)
    plt.show()
    # x = len(position_cnt.index)
    # for a, b in zip(position_cnt.index, position_cnt['column0']):
    #     plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=7)
    # position_cnt.plot.bar()
    # plt.show()
    # # print(test)
    # position_cnt_df = position_cnt.reset_index(name='cnt')  # 重置索引
    # position_cnt_df.set_index(['city'], inplace=True)
    # position_cnt_df.index.name = None
    # position_cnt_df.plot.bar()
    # plt.show()


def main():
    page = int(input('请输入你要抓取的页码总数：'))
    # kd = input('请输入你要抓取的职位关键字：')
    # city = input('请输入你要抓取的城市：')
    # info_result = []
    # title = ['岗位id', '城市', '公司全名', '福利待遇', '工作地点', '学历要求', '工作类型', '发布时间', '职位名称', '薪资', '工作年限']
    # info_result.append(title)
    for x in range(1, page + 1):
        url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
        datas = {
            'first': 'true',
            'pn': x,
            'kd': 'python',
        }
        try:
            get_json(url, datas)
            print("第%s页正常采集" % x)
        except Exception as msg:
            print("第%s页出现问题" % x)
        while x == page:
            print('crawl done')


if __name__ == '__main__':
    # main()
    mk_plot()
