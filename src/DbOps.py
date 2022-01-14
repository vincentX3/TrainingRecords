import sqlite3
import traceback
from sqlite3 import Error
import datetime
from utils import Logger


class DbOps:
    db_path = "../db/TRecords_test.db"

    @classmethod
    def execute_sql(cls, sql, values=None):
        try:
            print(">>> executing sql:" + sql)
            con = sqlite3.connect(cls.db_path)
            print('Opened database successfully')
            cur = con.cursor()
            if values is None:
                cur.execute(sql)
            else:
                cur.execute(sql, values)
            print('Execute sql successfully' + '\n')
            data = cur.fetchall()
            con.commit()
            con.close()
            return data
        except:
            log = Logger('./log/logfile.log', level='error')
            log.logger.error("错误:%s", traceback.format_exc())

    @classmethod
    def init_tables(cls):
        cls.init_action_table()
        cls.init_record_table()
        cls.init_todo_table()

    @classmethod
    def init_todo_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS todos(
                Tname text,
                Tlevel text,
                Tnum double,
                PRIMARY KEY (Tname, Tlevel)
                );
              """
        cls.execute_sql(sql)

    @classmethod
    def init_record_table(cls):
        sql = """
                CREATE TABLE IF NOT EXISTS records(
                Rid INTEGER PRIMARY KEY autoincrement,
                RAname text,
                RAlevel text,
                Rnum double,
                Rdate date,
                Rnote text,
                FOREIGN KEY (RAname, RAlevel) REFERENCES actions (Aname, Alevel)
            )
            """
        cls.execute_sql(sql)

    @classmethod
    def init_action_table(cls):
        sql = """
                CREATE TABLE IF NOT EXISTS actions(
                Aname text,
                Alevel text,
                Apart text,
                PRIMARY KEY (Aname, Alevel)
            );    
            """

    @classmethod
    def is_action_exist(cls, action):
        '''
        check whether the action with specified level exist.
        :param action: list [Aname, Alevel]
        :return: bool
        '''
        sql = "SELECT EXISTS(SELECT 1 FROM actions WHERE Aname=\'{name}\' AND Alevel=\'{level}\')" \
            .format(name=action[0], level=action[1])
        # print(sql)
        result = cls.execute_sql(sql)  # result should be [(0,)] or [(1,)]
        result = True if result[0][0] == 1 else False
        # print(result)
        return result

    @classmethod
    def is_todo_exist(cls, todo_item):
        '''
        check whether the action with specified level exist.
        :param todo_item: list [Tname, Tlevel]
        :return: bool
        '''
        sql = "SELECT EXISTS(SELECT 1 FROM todos WHERE Tname=\'{name}\' AND Tlevel=\'{level}\')" \
            .format(name=todo_item[0], level=todo_item[1])
        # print(sql)
        result = cls.execute_sql(sql)  # result should be [(0,)] or [(1,)]
        result = True if result[0][0] == 1 else False
        # print(result)
        return result

    @classmethod
    def insert_action(cls, action):
        sql = "INSERT INTO actions(Aname, Alevel) VALUES (?, ?)"
        cls.execute_sql(sql, action)

    @classmethod
    def insert_record(cls, record):
        action = record[:2]
        if not cls.is_action_exist(action):
            # create new action
            cls.insert_action(action)
        sql = "INSERT INTO records(RAname, RAlevel, Rnum, Rdate) VALUES (?, ?, ?, ?)"
        cls.execute_sql(sql, record)
        # print("> successfully create record:", record)

    @classmethod
    def insert_todo(cls, record):
        if not cls.is_todo_exist(record):
            sql = "INSERT INTO todos(Tname, Tlevel, Tnum) VALUES (?, ?, ?)"
            cls.execute_sql(sql, record)
            print("> successfully create todo-item:", record)
            return True
        else:
            return False  # let GUI raise dialog

    @classmethod
    def fetch_todos(cls):
        todos = cls.execute_sql("SELECT * FROM todos;")
        return todos

    @classmethod
    def fetch_records(cls):
        sql = "select Rid, RAname, RAlevel, Rnum, Rdate from records;"
        return cls.execute_sql(sql)

    @classmethod
    def fetch_week_records(cls, begin, end):
        sql = "select Rid, RAname, RAlevel, Rnum, Rdate from records where rdate>=\'{begin}\' and rdate<=\'{end}\'". \
            format(begin=begin, end=end)
        return cls.execute_sql(sql)

    @classmethod
    def update_record(cls, rid, name, level, num, rdate):
        # TODO: check action exists
        sql = "UPDATE records SET RAname=\'{name}\', RAlevel=\'{name}\', Rnum=\'{num}\', Rdate=\'{rdate}\'" \
              "WHERE Rid={rid}".format(rid=rid, name=name, num=num, rdate=rdate)
        return cls.execute_sql(sql)

    @classmethod
    def delete_todo(cls, todo_item):
        sql = "DELETE FROM todos WHERE Tname=\'{name}\' AND Tlevel=\'{level}\'" \
            .format(name=todo_item[0], level=todo_item[1])
        cls.execute_sql(sql)

    @classmethod
    def delete_record_by_id(cls, rid):
        sql = "DELETE FROM records WHERE Rid=\'{rid}\'".format(rid=rid)
        cls.execute_sql(sql)

    # TODO: 增加导入旧db的功能


if __name__ == '__main__':
    print(len(DbOps.fetch_records()))
