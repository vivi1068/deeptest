#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

import asyncio, logging

import aiomysql
#args=()在调用log函数时，可传入参数如log(1,(5,6))
def log(sql, args=()):
    logging.info('SQL: %s' % sql)
#创建连接池
async def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    #定义全局变量，保存数据库连接信息
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )
#select类
async def select(sql, args, size=None):
    #调用log函数
    log(sql, args)
    #global __pool
    #使用get()方法连接数据库
    async with __pool.get() as conn:
        # 获取游标,默认游标返回的结果为元组,每一项是另一个元组,通过aiomysql.DictCursor指定元组的元素为字典
        async with conn.cursor(aiomysql.DictCursor) as cur:
            # 调用游标的execute()方法来执行sql语句,execute()接收两个参数,第一个为sql语句可以包含占位符,第二个为占位符对应的值,使用该形式可以避免直接使用字符串拼接出来的sql的注入攻击
            #SQL语句的占位符是?，而MySQL的占位符是%s，自动替换
            # args or ()表示参数可以是tuple类型
            await cur.execute(sql.replace('?', '%s'), args or ())
            # size有值就获取对应数量的数据
            if size:
                rs = await cur.fetchmany(size)
            else:
                # 获取所有数据库中的所有数据,此处返回的是一个数组,数组元素为字典
                rs = await cur.fetchall()
        logging.info('rows returned: %s' % len(rs))
        return rs

#增删改类
async def execute(sql, args, autocommit=True):
    log(sql)
    async with __pool.get() as conn:
        #非自动提交事物，手动提交
        if not autocommit:
            await conn.begin()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute(sql.replace('?', '%s'), args)
                #cur.rowcount()获得影响的行数
                affected = cur.rowcount
            if not autocommit:
                # 提交事务
                await conn.commit()
        #如果报错，回滚
        except BaseException as e:
            if not autocommit:
                #rollback() 回滚
                await conn.rollback()
            raise
        return affected

#创建拥有几个占位符的字符串
#传入一个数字，在L中增加相应个数的？
def create_args_string(num):
    L = []
    for n in range(num):
        L.append('?')
    return ', '.join(L)

#ORM的思路就是把一个表映射成python中的类，行数据映射成类的实例
#该类是为了保存数据库列名和类型的基类
class Field(object):
    def __init__(self, name, column_type, primary_key, default):
        self.name = name #列名
        self.column_type = column_type #数据类型
        self.primary_key = primary_key #是否为主键
        self.default = default #默认值

#self.__class__.__name__ 表示类名Field
    def __str__(self):
        return '<%s, %s:%s>' % (self.__class__.__name__, self.column_type, self.name)

# 不同类型的字段类型，供不同类型的列调用，均继承自Field基类
# 字段信息均有默认值，可缺省定义也可定制
# 字符串类型
class StringField(Field):
    def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
        #super().__init__调用父类Field的__init__方法
        super().__init__(name, ddl, primary_key, default)
# 布尔值类型
class BooleanField(Field):
    def __init__(self, name=None, default=False):
        super().__init__(name, 'boolean', False, default)
# 整数类型
class IntegerField(Field):
    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, 'bigint', primary_key, default)
# 浮点数类型
class FloatField(Field):
    def __init__(self, name=None, primary_key=False, default=0.0):
        super().__init__(name, 'real', primary_key, default)
# 文本类型
class TextField(Field):
    def __init__(self, name=None, default=None):
        super().__init__(name, 'text', False, default)

#元类
#metaclass是类的模板，所以必须从`type`类型派生
class ModelMetaclass(type):
    #attrs传入一个未命名的变量参数，*attrs所有未命名的变量参数
    #类方法的第一个参数是类对象cls，那么通过cls引用的必定是类对象的属性和方法
    #不理解__new__()
    def __new__(cls, name, bases, attrs):
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        # 保存表名,如果获取不到,则把类名当做表名,完美利用了or短路原理
        tableName = attrs.get('__table__', None) or name
        logging.info('found model: %s (table: %s)' % (name, tableName))
        # 保存列类型的对象
        mappings = dict()
        fields = []
        primaryKey = None
        for k, v in attrs.items():
            if isinstance(v, Field):
                logging.info('  found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
                if v.primary_key:
                    # 找到主键:
                    if primaryKey:
                        raise StandardError('Duplicate primary key for field: %s' % k)
                    primaryKey = k
                else:
                    fields.append(k)
        if not primaryKey:
            raise StandardError('Primary key not found.')
        for k in mappings.keys():
            attrs.pop(k)
        escaped_fields = list(map(lambda f: '`%s`' % f, fields))
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = tableName
        attrs['__primary_key__'] = primaryKey # 主键属性名
        attrs['__fields__'] = fields # 除主键外的属性名
        attrs['__select__'] = 'select `%s`, %s from `%s`' % (primaryKey, ', '.join(escaped_fields), tableName)
        attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (tableName, ', '.join(escaped_fields), primaryKey, create_args_string(len(escaped_fields) + 1))
        attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (tableName, ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primaryKey)
        attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (tableName, primaryKey)
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def getValue(self, key):
        return getattr(self, key, None)

    def getValueOrDefault(self, key):
        value = getattr(self, key, None)
        if value is None:
            field = self.__mappings__[key]
            if field.default is not None:
                value = field.default() if callable(field.default) else field.default
                logging.debug('using default value for %s: %s' % (key, str(value)))
                setattr(self, key, value)
        return value

    @classmethod
    async def findAll(cls, where=None, args=None, **kw):
        ' find objects by where clause. '
        sql = [cls.__select__]
        if where:
            sql.append('where')
            sql.append(where)
        if args is None:
            args = []
        orderBy = kw.get('orderBy', None)
        if orderBy:
            sql.append('order by')
            sql.append(orderBy)
        limit = kw.get('limit', None)
        if limit is not None:
            sql.append('limit')
            if isinstance(limit, int):
                sql.append('?')
                args.append(limit)
            elif isinstance(limit, tuple) and len(limit) == 2:
                sql.append('?, ?')
                args.extend(limit)
            else:
                raise ValueError('Invalid limit value: %s' % str(limit))
        rs = await select(' '.join(sql), args)
        return [cls(**r) for r in rs]

    @classmethod
    async def findNumber(cls, selectField, where=None, args=None):
        ' find number by select and where. '
        sql = ['select %s _num_ from `%s`' % (selectField, cls.__table__)]
        if where:
            sql.append('where')
            sql.append(where)
        rs = await select(' '.join(sql), args, 1)
        if len(rs) == 0:
            return None
        return rs[0]['_num_']

    @classmethod
    async def find(cls, pk):
        ' find object by primary key. '
        rs = await select('%s where `%s`=?' % (cls.__select__, cls.__primary_key__), [pk], 1)
        if len(rs) == 0:
            return None
        return cls(**rs[0])

    # 保存实例到数据库
    async def save(self):
        args = list(map(self.getValueOrDefault, self.__fields__))
        args.append(self.getValueOrDefault(self.__primary_key__))
        rows = await execute(self.__insert__, args)
        if rows != 1:
            logging.warn('failed to insert record: affected rows: %s' % rows)

    # 更新数据库数据
    async def update(self):
        args = list(map(self.getValue, self.__fields__))
        args.append(self.getValue(self.__primary_key__))
        rows = await execute(self.__update__, args)
        if rows != 1:
            logging.warn('failed to update by primary key: affected rows: %s' % rows)

    # 删除数据
    async def remove(self):
        args = [self.getValue(self.__primary_key__)]
        rows =await execute(self.__delete__, args)
        if rows != 1:
            logging.warn('failed to remove by primary key: affected rows: %s' % rows)


