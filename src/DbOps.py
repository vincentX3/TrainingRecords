import sqlite3
import re
import subprocess
import traceback
from sqlite3 import Error
import datetime
from utils import Logger
from ui_macro import DB_PATH


class DbOps:
    db_path = DB_PATH

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
            log = Logger('../log/logfile.log', level='error')
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
                ON UPDATE CASCADE ON DELETE CASCADE
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
        cls.execute_sql(sql)

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
        sql = "select Rid, RAname, RAlevel, Rnum, Rdate from records ORDER BY Rdate;"
        return cls.execute_sql(sql)

    @classmethod
    def fetch_week_records(cls, begin, end):
        sql = "select Rid, RAname, RAlevel, Rnum, Rdate from records " \
              "where rdate>=\'{begin}\' and rdate<=\'{end}\' ORDER BY Rdate". \
            format(begin=begin, end=end)
        return cls.execute_sql(sql)

    @classmethod
    def fetch_records_by_action(cls, name, level=''):
        if len(level) == 0:
            sql = "SELECT Rid, RAname, RAlevel, Rnum, Rdate FROM records WHERE RAname=\'{name}\' ORDER BY Rdate". \
                format(name=name)
        else:
            sql = "SELECT Rid, RAname, RAlevel, Rnum, Rdate FROM records " \
                  "WHERE RAname=\'{name}\' AND RAlevel=\'{level}\' ORDER BY Rdate". \
                format(name=name, level=level)
        return cls.execute_sql(sql)

    @classmethod
    def fetch_parts(cls):
        sql = "SELECT DISTINCT Apart FROM actions;"
        return cls.execute_sql(sql)

    @classmethod
    def fetch_actions(cls):
        sql = "SELECT * FROM actions ORDER BY Aname;"
        return cls.execute_sql(sql)

    @classmethod
    def fetch_names(cls, part=''):
        if len(part) == 0:
            sql = "SELECT DISTINCT Aname FROM actions;"
        else:
            sql = "SELECT DISTINCT Aname FROM actions WHERE Apart=\'{part}\'".format(part=part)
        return cls.execute_sql(sql)

    @classmethod
    def fetch_levels(cls, name):
        sql = "SELECT DISTINCT Alevel FROM actions WHERE Aname=\'{name}\'".format(name=name)
        return cls.execute_sql(sql)

    @classmethod
    def update_record(cls, rid, name, level, num, rdate):
        action = [name, level]
        if not cls.is_action_exist(action):
            # create new action
            cls.insert_action(action)
        sql = "UPDATE records SET RAname=\'{name}\', RAlevel=\'{level}\', Rnum=\'{num}\', Rdate=\'{rdate}\'" \
              "WHERE Rid={rid}".format(rid=rid, name=name, level=level, num=num, rdate=rdate)
        return cls.execute_sql(sql)

    @classmethod
    def update_action(cls, ori_name, ori_level, name, level, part):
        sql = "UPDATE actions SET Aname=\'{name}\', Alevel=\'{level}\', Apart=\'{part}\' " \
              "WHERE Aname=\'{ori_name}\' AND Alevel=\'{ori_level}\'".format(name=name, level=level, ori_name=ori_name,
                                                                             ori_level=ori_level, part=part)
        return cls.execute_sql(sql)

    @classmethod
    def delete_todo(cls, todo_item):
        sql = "DELETE FROM todos WHERE Tname=\'{name}\' AND Tlevel=\'{level}\'" \
            .format(name=todo_item[0], level=todo_item[1])
        cls.execute_sql(sql)

    # TODO: check why the cascade setting isn't work

    @classmethod
    def delete_record_by_id(cls, rid):
        sql = "DELETE FROM records WHERE Rid=\'{rid}\'".format(rid=rid)
        cls.execute_sql(sql)

    @classmethod
    def delete_action(cls, aname, alevel):
        sql = "DELETE FROM actions WHERE Aname=\'{name}\' AND Alevel=\'{level}\'" \
            .format(name=aname, level=alevel)
        cls.execute_sql(sql)

    @classmethod
    def import_old_db(cls, db_path):
        # dump previous db
        cmd = 'sqlite3 {path} .dump'.format(path=db_path)
        result = subprocess.run(cmd.split(), stdout=subprocess.PIPE).stdout.decode('utf-8')
        result = result.split("\n")
        # execute every INSERT sql
        for sql in result:
            sql = sql.strip()
            if sql.startswith("INSERT"):
                if sql.split()[2] == 'records':
                    # for records INSERTION, omit rid
                    temp = "INSERT INTO records(RAname, RAlevel, Rnum, Rdate, Rnote) VALUES"
                    values = re.findall(r'[(](.*?)[)]', sql)[0]  # Extract content in parentheses
                    values = values.split(",", 1)[1]  # omit rid
                    sql = temp + '(' + values + ');'
                cls.execute_sql(sql)


if __name__ == '__main__':
    print(len(DbOps.fetch_records()))
