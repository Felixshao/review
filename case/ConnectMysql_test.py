# *-- coding:utf-8 --*
import pymysql


def connect_mysql():
    # pymysql.cooect(ip，账户，密码，库名)连接数据库方法
    db = pymysql.connect("localhost", 'root', '13691916244shaos', 'study')

    # cursor()方法，获取操作游标，用来执行sql或其他
    currot = db.cursor()

    sele = "select * from study"     # 查询语句
    inst = "insert into study values(%s,%s,%s,%s)"  # 插入语句
    inst_value = [[5, '一', 49.5, '加油，你行的!'], [6, '二', 80, '很好']]
    dele = 'delete from study where ID in(5,6)'     # 删除语句
    upda = 'update study set Grade = "40" where id in(3,4)'  # 修改语句

    currot.callproc()     # callproc()方法，执行存储过程，返回行数
    print(currot.executemany(inst, inst_value))   # executemay(),执行单挑sql，根据值得个数循环执行，返回行数
    # print(currot.execute(upda))  # execute()方法，执行单挑sql语句，返回受影响的行数（即条数）
    currot.execute(sele)      # execute()方法，执行单挑sql语句，返回受影响的行数（即条数）
    # db.commit()                 # 增、删、改执行多条语句，需使用commit()方法
    # data_one = currot.fetchone()    # fetchone()返回一条结果
    data_all = currot.fetchall()      # fetchall()返回所有结果
    print(data_all)
    while True:
        data_many = currot.fetchmany(2)
        print('1')
        if not data_many:
            print(3)
            break
        for i in data_many:
            print(2)
            print(i)

    currot.close()      # 关闭游标
    db.close()          # 关闭数据库

    return data_all

def connect_mysql2():

    # 连接数据库，传入ip、账号、密码、库名(可不传入)
    db = pymysql.connect('localhost', 'root', '13691916244shaos', 'study')
    # 获取数据库操作游标对象
    cursor = db.cursor()
    # sql语句
    sql = 'select * from study.study'
    # 执行单挑sql语句
    cursor.execute(sql)
    # 返回sql语句所有结果并打印
    data = cursor.fetchone()
    print(data, '\n', type(data))
    # 关闭游标和数据库
    cursor.close()
    db.close()
    # data = {}
    # data.update()


if __name__ == '__main__':
    connect_mysql2()

    # data_all = connect_Mysql()
    # print(type(data_all))
    # for name in range(len(data_all)):
    #     # print('名字:{}'.format(data_all[name][1]))
    #     print('成绩:{}'.format(data_all[name][2]))
