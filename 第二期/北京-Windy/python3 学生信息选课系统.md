
```
#-*- coding:utf-8 -*-

import sqlite3
# 打开本地数据库用于存储用户数据
cx = sqlite3.connect('student.db')

# 在该数据库中创建学生信息表
cx.execute('''
CREATE TABLE StudentTable(ID INTEGER PRIMARY KEY AUTOINCREMENT,StuId CHAR(11) NOT NULL,
NAME CHAR(11) NOT NULL,
CLASS  TEXT NOT NULL)
''')

print('Table created successfully')

# 在该数据库下创建课程信息表

cx.execute('''CREATE TABLE CourseTable(ID INTEGER PRIMARY KEY AUTOINCREMENT,
 CourseId INT NOT NULL ,
 Name TEXT NOT NULL,
 Teacher TEXT NOT NULL ,
 Classroom TEXT NOT NULL ,
 StartTime CHAR(11) NOT NULL ,
 EndTime CHAR(11) NOT NULL )''')

print('Table created successfully')

# 在该数据库中创建学生选课情况表

cx.execute('''CREATE TABLE ChoseTable(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
 CourseId INT NOT NULL ,
 StuId INT NOT NULL )''')

print('Table created successfully')

# 插入学生信息


def insert_stu():
    conn = sqlite3.connect("student.db")
    stu_id = input('输入学生学号：')
    cursor = cx.execute("SELECT StuId FROM StudentTable WHERE StuId = '%s' " % stu_id)
    conn.commit()
    for row in cursor:
        if stu_id == row[0]:
            print("sorry,该学号已存在,请重新输入")
            break
    else:
        stu_name = input("请输入学生姓名:")
        stu_class = input("请输入学生班级:")
        sql1 = "INSERT INTO StudentTable(StuId,NAME,CLASS) VALUES(%s,'%s',%s);"% (stu_id, stu_name, stu_class)
        conn.execute(sql1)
        conn.commit()
        print("恭喜你,学生录入成功!")

# 学生选课


def choose_cou():
    stu_id = input('输入学生学号：')
    sql2 = "select StuId from StudentTable where StuId = %s;" % stu_id
    cursor1 = cx.execute(sql2)
    for row in cursor1:
        if stu_id == row[0]:
            sql3 = "select CourseId, Name, Teacher,Classroom, StartTime, EndTime from CourseTable"
            cursor2 = cx.execute(sql3)
            for row in cursor2:
                print("CourseId = ", row[0])
                print("Name = ", row[1])
                print("Teacher = ", row[2])
                print("Classroom = ", row[3])
                print("StartTime = ", row[4])
                print("EndTime = ", row[5])
            cou_id = input("请输入要选的课程编号：")
            sql = "select StuId from ChoseTable where CourseId = %d" % cou_id
            cursor3 = cx.execute(sql)
            for row in cursor3:
                if stu_id == row[0]:
                    print("该课程已选，请重新输入要选课程")
                else:
                    sql3 = "insert into ChoseTable (StuId, CourseId) VALUES (%d, %d)" % (stu_id, cou_id)
                    cursor4 = cx.execute(sql3)
                    cx.commit()
                    print("恭喜你，选课成功")
                    break
                break
            break
        else:
            print("该学生不存在")


# 按照学生学号查找学生信息
def stu_id_search():
    stu_id = input("请输入要查询的学生学号：")
    sql5 = "select StuId from StudentTable WHERE StuId = %d" % stu_id
    cursor = cx.execute(sql5)
    for row in cursor:
        if stu_id == row[0]:
            sql6 = "select ID, StuId, NAME, ClASS form StudentTable where StuId = %d" % stu_id
            cursor2 = cx.execute(sql6)
            cx.commit()
            for row in cursor2:
                print()
                print("您要查询的学生信息为：")
                print("ID = ", row[0])
                print("StuId = ", row[1])
                print("NAME = ", row[2])
                print("ClASS = ", row[3])
                break
        else:
            print("该学生不存在")


# 根据学生学号查询该学生选课情况

def stu_id_cou():
    stu_id = input("请输入学生学号：")
    sql5 = "select CourseId from ChoseTable WHERE StuId = %d" % stu_id
    cursor = cx.execute(sql5)
    for row in cursor:
        if stu_id == row[0]:
            sql6 = "select CourseId from ChoseTable WHERE StuId = %d" % stu_id
            cursor = cx.execute(sql6)
            cx.commit()
            for row in cursor:
                print()
                print("该学生所选课程编号为：")
                print(row)
                print()
            break
    else:
        print("该学生还未选课")


def cou_id_search():  #按照课程号查询课程信息
    cou_id = input("请输入要查询的课程号:")
    sql7 = "select CourseId ,Name,Teacher,Classroom,StartTime,EndTime from CourseTable "
    sql7 += "where CourseId = %d;"%(cou_id)
    cursor1 = cx.execute(sql7)
    cx.commit()
    for row in cursor1:
        print("您要查询的课程信息为:")
        print ("CourseId = ",row[0])
        print ("Name = ", row[1])
        print ("Teacher = ", row[2])
        print ("Classroom = ",row[3])
        print ("StartTime = " ,row[4])
        print ("EndTime = ",row[5],"\n")
        break
    else:
        print ("sorry,没有该课程信息!")

# 按照课程号查询选择该课程的学生列表


def cou_id_stu():
    cou_id = input('请输入课程号:')
    sql8 = "select CourseId from XuankeTable where CourseId =%d;"%(cou_id)
    cursor1 = cx.execute(sql8)
    for row in cursor1:
        if cou_id == row[0]:
            sql9 = "select StuId from XuankeTable where CourseId =%d;"%(cou_id)
            cursor2 = cx.execute(sql9)
            cx.commit()
            for row in cursor2:
                print
                print("选择该课程的学生为:")
                print(row, "\n")
            break
        break
    else:
        print("sorry,没有该课程信息!")


def menu():
    print('1.进入学生信息系统(学生信息录入)')
    print('2.进入学生选课系统(学生选课操作)')
    print('3.进入学生选课信息系统(学生信息查询和选课情况查询)')
    print('4.退出程序')


def student():
    print('1.录入学生信息')
    print('2.返回主菜单')
    print('3.退出程序')


def Course():
    print('1.开始选课')
    print('2.返回主菜单')
    print('3.退出程序')


def information():
    print('1.按学号查询学生信息')
    print
    '2.按学号查看学生选课课程列表'
    print
    '3.按课程号查看课程信息'
    print
    '4.按课程号查看选课学生列表'
    print
    '5.返回主菜单'
    print
    '6.退出程序'


while True:
    menu()
    print
    x = input('请输入您的选择菜单号:')
    if x == '1':
        # 进入学生信息系统
        student()
        stu = input('您已进入学生录入系统,请再次输入选择菜单:')
        if stu == '1':
            insert_stu()
            continue
        if stu == '2':
            menu()
            continue
        if stu == '3':
            print
            "谢谢使用！"
            exit()
            continue
        else:
            print
            "输入的选项不存在，请重新输入！"
            continue

    if x == '2':
        # 进入选课信息系统
        Course()
        cou = input('您已进入学生选课系统,请再次输入选择菜单:')
        if cou == '1':
            choose_cou()
            continue
        if cou == '2':
            menu()
            continue
        if cou == '3':
            print
            "谢谢使用！"
            exit()
            continue
        else:
            print
            "输入的选项不存在，请重新输入！"
            continue

    if x == '3':
        # 进入学生选课信息表
        information()
        inf = input('您已进入学生选课信息系统,请再次输入选择菜单:')
        if inf == '1':
            stu_id_search()
            continue
        if inf == '2':
            stu_id_cou()
            continue
        if inf == '3':
            cou_id_search()
            continue
        if inf == '4':
            cou_id_stu()
            continue
        if inf == '5':
            menu()
            continue
        if inf == '6':
            print ("谢谢使用！")
            exit()
            continue
        else:
            print ("输入的选项不存在，请重新输入！")
            continue

    if x == '4':
        print("谢谢使用！")
        exit()
    else:
        print("输入的选项不存在，请重新输入！")
        continue






```
