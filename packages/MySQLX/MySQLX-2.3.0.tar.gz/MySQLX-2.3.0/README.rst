Mapper file
'''''''''''

Create a mapper file in 'mapper' folder, you can named
'user_mapper.xml', like follow:

.. code:: xml

       <?xml version="1.0" encoding="UTF-8"?>
       <!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "https://gitee.com/summry/mysqlx/blob/master/dtd/mapper.dtd">
       <mapper namespace="user">
           <select id="select_all">
               select id, name, age from user
            </select>

            <select id="select_by_name">
               select id, name, age from user where name = ?
            </select>

            <select id="select_by_name2">
               select id, name, age from user where name = :name
            </select>

            <select id="select_include" include="select_all">
               {{ select_all }}
                 {% if name -%}
                  where name = :name
                 {%- endif -%}
            </select>
       </mapper>

Usage Sample
''''''''''''

.. code:: python

    from mysqlx.orm import Model
    from typing import List, Tuple, Mapping
    from mysqlx import mapper, sql, db, dbx, init_db

    @mapper(namespace='user')
    def select_all(): List

    @mapper(namespace='user')
    def select_by_name(name: str): List

    @mapper(namespace='user')
    def select_by_name2(name: str): List

    @mapper(namespace='user')
    def select_include(name: str): List

    @sql('select id, name, age from user where name = ?')
    def query_by_name(name: str): List(Mapping)

    @sql('select id, name, age from user where name = :name')
    def query_by_name2(name: str): List(Mapping)

    if __name__ == '__main__':
        init_db(host='127.0.0.1', port='3306', user='xxx', password='xxx', database='test', pool_size=5, show_sql=True, mapper_path='./mapper')

        users = select_all()
        # result:
        # (3, 'zhangsan', 15)
        # (4, 'lisi', 26)
        # (5, 'wangwu', 38)

        users = select_by_name('zhangsan')
        # result:
        # (3, 'zhangsan', 15)

        users = select_by_name2(name='zhangsan')
        # result:
        # (3, 'zhangsan', 15)

        users = select_include(name='zhangsan')
        # result:
        # (3, 'zhangsan', 15)

        users = query_by_name('zhangsan')
        # result:
        # {'id': 3, 'name': 'zhangsan', 'age': 15}

        users = query_by_name2(name='zhangsan')
        # result:
        # {'id': 3, 'name': 'zhangsan', 'age': 15}
       
        # you can use dbx execte mapper sql with full sql id: namespace join sql id
        users = dbx.select('user.select_all')  # 'user' is namespace, 'select_all' is sql id
        # result:
        # (3, 'zhangsan', 15)
        # (4, 'lisi', 26)
        # (5, 'wangwu', 38)

        users = dbx.select('user.select_by_name', name='zhangsan')
        # result:
        # (3, 'zhangsan', 15)

        users = dbx.sql('user.select_by_name').select(name='zhangsan')
        # result:
        # (3, 'zhangsan', 15)

        # you can direct execute sql with db
        effected_rowcount = db.table('user').insert(name='zhangsan', age=15)
        # 1

        primary_key = db.table('user').save(name='lisi', age=26)
        # 4

        effected_rowcount = db.insert(table='user', name='wangwu', age=38)
        # 1

        users = db.table('user').columns('id, name, age').select()
        # result:
        # (3, 'zhangsan', 15)
        # (4, 'lisi', 26)
        # (5, 'wangwu', 38)

        users = db.table('user').columns('id, name, age').where(name='zhangsan').query()
        # result:
        # [{'id': 3, 'name': 'zhangsan', 'age': 15}]

        users = db.table('user').columns('id, name, age').where(name__eq='zhangsan').query()
        # result:
        # [{'id': 3, 'name': 'zhangsan', 'age': 15}]

        users = db.select('select id, name, age from user')
        # result:
        # (3, 'zhangsan', 15)
        # (4, 'lisi', 26)
        # (5, 'wangwu', 38)

        users = db.query('select id, name, age from user name = :name', name='zhangsan')
        # result:
        # [{'id': 3, 'name': 'zhangsan', 'age': 15}]

        users = db.sql('select id, name, age from user name = :name').query(name='zhangsan')
        # result:
        # [{'id': 3, 'name': 'zhangsan', 'age': 15}]

Transaction
'''''''''''

.. code:: python

       from mysqlx import trans

       @trans
       def test_transaction():
           insert_func(....)
           update_func(....)


       def test_transaction2():
           with trans():
               insert_func(....)
               update_func(....)

If you want to use ORM, may be you need SQLORMX: https://pypi.org/project/sqlormx

If you want to operate PostgreSQL database, may be you need PgSQLX: https://pypi.org/project/pgsqlx

If you just wanted a simple sql executor, may be you need SQLExecX: https://pypi.org/project/sqlexecx

If you wanted simultaneously support MySQL and PostgreSQL, may be you need BatisX: https://pypi.org/project/batisx
