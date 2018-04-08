# __author__ ='wuwa'
# -*- coding:utf-8 -*-
import csv


def write_csv(filename):
    """
    打开文件，写入内容,并以逗号分隔，关闭文件
    :param filename:
    :return:
    """
    with open(filename, 'w', newline='') as f:
        spamwriter = csv.writer(f, delimiter=',')
        spamwriter.writerow(['csv_demo'] * 5 + ['DeepTest'])
        spamwriter.writerow(['hello', 'Study Python3', 'Auto Testing'])
        f.close()


def read_csv(filename):
    """
    读取文件
    :param filename:
    :return:
    """
    with open(filename, 'r') as f:
        render = csv.reader(f, delimiter=',')
        for row in render:
            for data in row:
                print(data, "  ")


def write_dict_csv(filename):
    """
    将字典格式的数据写入到csv中
    :param filename:
    :return:
    """
    with open(filename, 'w', newline="") as f:
        # 写csv头
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        # 写入数据
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
        writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
        f.close()


def read_dict_csv(filename):
    """
    以字典格式将数据从csv中读取
    :param filename:
    :return:
    """
    with open(filename, 'r') as f:
        render = csv.DictReader(f)
        for row in render:
            print(row['first_name'], row['last_name'])


if __name__ == "__main__":
    # write_csv('csvdemo.csv')
    # read_csv("csvdemo.csv")
    write_dict_csv("csvdemo1.csv")
    read_dict_csv("csvdemo1.csv")
