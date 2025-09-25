Usage Sample
''''''''''''

.. code:: python

       import sqlexecx as db

       if __name__ == '__main__':
           db.init('test.db', driver='sqlite3', show_sql=True, debug=True)

           # or
           db.init("postgres://user:password@127.0.0.1:5432/testdb", driver='psycopg2', pool_size=5, show_sql=True, debug=True)

           # or
           db.init(host='127.0.0.1', port='5432', user='xxx', password='xxx', database='testdb', show_sql=True, driver='psycopg2')

           effected_rowcount = db.insert(table='person', name='zhangsan', age=15)

           # if driver is 'pymysql' or 'mysql.connector' of MySQL, the select_key is 'SELECT LAST_INSERT_ID()'
           select_key = "SELECT currval('person_id_seq')"

           id = db.save(select_key=select_key, table='person', name='lisi', age=26)

           id = db.save_sql(select_key, 'INSERT INTO person(name, age) VALUES(?,?)', 'wangwu', 38)

           id = db.save_sql(select_key, 'INSERT INTO person(name, age) VALUES(:name, :age)', name='zhaoliu', age=45)

           count = db.get('select count(1) from person')
           # result: 4

           count = db.sql('select count(1) from person').get()
           # result: 4

           persons = db.select('select id, name, age from person')
           # result:
           # (3, 'zhangsan', 15)
           # (4, 'lisi', 26)
           # (5, 'wangwu', 38)
           # (6, 'zhaoliu', 45)

           persons = db.sql('select id, name, age from person').select()
           # result:
           # (3, 'zhangsan', 15)
           # (4, 'lisi', 26)
           # (5, 'wangwu', 38)
           # (6, 'zhaoliu', 45)

           persons = db.table('person').select('id', 'name', 'age')
           # result:
           # (3, 'zhangsan', 15)
           # (4, 'lisi', 26)
           # (5, 'wangwu', 38)
           # (6, 'zhaoliu', 45)

           persons = db.select_one('select id, name, age from person where name = ?', 'zhangsan')
           # result:
           # (3, 'zhangsan', 15)

           persons = db.sql('select id, name, age from person where name = ?').select_one('zhangsan')
           # result:
           # (3, 'zhangsan', 15)

           persons = db.select('select id, name, age from person where name = :name', name='zhangsan')
           # result:
           # [(3, 'zhangsan', 15)]

           persons = db.sql('select id, name, age from person where name = :name').select(name='zhangsan')
           # result:
           # [(3, 'zhangsan', 15)]

           persons = db.sql('select id, name, age from person where name = :name').param(name='zhangsan').select()
           # result:
           # [(3, 'zhangsan', 15)]

           persons = db.table('person').where(name__eq='zhangsan').select('id', 'name', 'age')
           # result:
           # [(3, 'zhangsan', 15)]

           persons = db.query('select id, name, age from person')
           # result:
           # {'id': 3, 'name': 'zhangsan', 'age': 15}
           # {'id': 4, 'name': 'lisi', 'age': 26}
           # {'id': 5, 'name': 'wangwu', 'age': 38}
           # {'id': 6, 'name': 'zhaoliu', 'age': 45}

           persons = db.sql('select id, name, age from person').query()
           # result:
           # {'id': 3, 'name': 'zhangsan', 'age': 15}
           # {'id': 4, 'name': 'lisi', 'age': 26}
           # {'id': 5, 'name': 'wangwu', 'age': 38}
           # {'id': 6, 'name': 'zhaoliu', 'age': 45}

           persons = db.query_one('select id, name, age from person where name = ?', 'zhangsan')
           # result:
           # {'id': 3, 'name': 'zhangsan', 'age': 15}

           persons = db.sql('select id, name, age from person where name = ?').query_one('zhangsan')
           # result:
           # {'id': 3, 'name': 'zhangsan', 'age': 15}

           persons = db.query('select id, name, age from person where name = :name', name='zhangsan')
           # result:
           # [{'id': 3, 'name': 'zhangsan', 'age': 15}]

           persons = db.sql('select id, name, age from person where name = :name').query(name='zhangsan')
           # result:
           # [{'id': 3, 'name': 'zhangsan', 'age': 15}]

           persons = db.sql('select id, name, age from person where name = :name').param(name='zhangsan').query()
           # result:
           # [{'id': 3, 'name': 'zhangsan', 'age': 15}]

           persons = db.table('person').columns('id', 'name', 'age').where(name='zhangsan').query()
           # result:
           # [{'id': 3, 'name': 'zhangsan', 'age': 15}]

           effected_rowcount = db.table('person').where(name='zhangsan').update(name='xxx', age=45)

           effected_rowcount = db.table('person').where(id=6).delete()
           count = db.table('person').count())
           # result: 3

           effected_rowcount = db.execute('delete from person where id = :id', id=5)
           count = db.get('select count(1) from person')
           # result: 2

           effected_rowcount = db.sql('delete from person where id = ?').execute(4)
           count = db.sql('select count(1) from person').get()
           # result: 1

           effected_rowcount = db.sql('delete from person where id = :id').execute(id=3)
           count = db.sql('select count(1) from person').get()
           # result: 0

           # select data save as csv
           db.sql('select name, age from person WHERE name = ?').load('张三').to_csv('test.csv')

           db.sql('select name, age from person WHERE name = ?').param('张三').to_csv('test.csv')

           # insert from csv
           db.table('person').insert_from_csv('test.csv')

           # select data transform to DataFrame of pandas
           df = db.sql('select name, age from person WHERE name = :name').load(name='张三').to_df()

           df = db.sql('select name, age from person WHERE name = :name').param(name='张三').to_df()

           # insert from DataFrame of pandas
           db.table('person').insert_from_df(dataframe)

           # select data save as json
           db.sql('select name, age from person WHERE name = ?').load('张三').to_json('test.json')

           db.sql('select name, age from person WHERE name = ?').param('张三').to_json('test.json')

           # insert from json
           db.table('person').insert_from_json('test.json')

           db.close()

Transaction
'''''''''''

.. code:: python

       from sqlexecx import trans

       @trans
       def test_transaction():
           insert_func(....)
           update_func(....)


       def test_transaction2():
           with trans():
               insert_func(....)
               update_func(....)

If you want to use ORM, may be you need SQLORMX: https://pypi.org/project/sqlormx

If you want to operate MySQL database like Mybatis, may be you need MySQLX: https://pypi.org/project/mysqlx

If you want to operate PostgreSQL databaselike Mybatis, may be you need PgSQLX: https://pypi.org/project/pgsqlx

If you wanted simultaneously support MySQL and PostgreSQL, may be you need BatisX: https://pypi.org/project/batisx
