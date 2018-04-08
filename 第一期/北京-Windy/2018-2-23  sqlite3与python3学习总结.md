## 2018-2-23  sqlite3

---
1、sqlite3模块提供了SQL接口，使用时不需要安装，python2.5以上的版本均默认自带了该模块。

---

2、该模块提供的API

```
① sqlite3.connect（database[,timeout, other optinonal arguments]）
实际操作：
cx = sqlite.connect('test.db')

```
- 该API打开一个到 SQLite 数据库文件 database 的链接。如果数据库成功打开，则返回一个连接对象connection
- 当一个数据库被多个连接访问，且其中一个修改了数据库，此时SQLite数据库被锁定，直到事物提交。timeout参数表示连接等待锁定的持续时间，直到发生异常断开连接。timeout参数默认是5s(这段话是抄来的，具体应用还没接触到)
- 如果给定的数据库名称不存在，则该调用会创建一个数据库。

```
② connection.cursor([cursorClass])
实际操作：
cu = cx.cursor()
```
- 该例程会创建一个cursor，用于后续执行sql语句

```
③ connection.execute(sql, [, optional paramet])
④ cursor.execute(sql, [, optional paramet])
实际操作：
cu.execute('create table user(id varchar(20) primary key, name varchar(20))')
cu.execute('insert into user(id, name) values(\'1\',\'Mark\')')
```
- 初步了解到这两个方法执行的效果都是一样的

---
执行完sql语句后，可以通过rowcount获取插入的行数
```
cu.rowconut
```
关闭游标

```
cu.close()
```

提交事务

```
cx.commit()
```

关闭connection

```
cx.close()
```
