import sqlite3
from sqlite3 import Error
from pprint import pprint
from pandas import read_sql_query
import datetime

class TRDb:
    def __init__(self):
        self.db_path = "../db/TRecords.db"
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.cursor = self.connection.cursor()
            print("> connect to ", self.db_path)
        except Error as e:
            print(e)

    def create_table(self):
        action_table = """
            CREATE TABLE IF NOT EXISTS actions(
                Aname text,
                Alevel text,
                Apart text,
                PRIMARY KEY (Aname, Alevel)
            );
        """
        record_table = """
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
        self.cursor.execute(action_table)
        self.cursor.execute(record_table)

    def init_db(self):
        self.connect()
        self.create_table()

    def is_action_exist(self, action):
        '''
        check whether the action with specified level exist.
        :param action: list [Aname, Alevel]
        :return: bool
        '''
        sql = "SELECT EXISTS(SELECT 1 FROM actions WHERE Aname=\'{name}\' AND Alevel=\'{level}\')"\
            .format(name=action[0], level=action[1])
        # print(sql)
        result = self.cursor.execute(sql).fetchall() # result should be [(0,)] or [(1,)]
        result = True if result[0][0] == 1 else False
        # print(result)
        return result

    def insert_action(self, action):
        sql = "INSERT INTO actions(Aname, Alevel) VALUES (?, ?)"
        self.cursor.execute(sql, action)
        self.connection.commit()

    def insert_record(self, record):
        # 日期可选，不填写时默认当天，填写则对应日期
        action = record[:2]
        if not self.is_action_exist(action):
            # create new action
            self.insert_action(action)
        sql = "INSERT INTO records(RAname, RAlevel, Rnum, Rdate) VALUES (?, ?, ?, ?)"
        if len(record)<4:
            # input without date
            today = str(datetime.date.today())
            record.append(today)
        self.cursor.execute(sql, record)
        self.connection.commit()
        print("> successfully create record:", record)

    def select_records_by_action(self, action):
        base_sql = "SELECT Rdate, RAname, RAlevel, Rnum, Rnote FROM records "
        if len(action) == 1:
            sql = base_sql + "WHERE RAname=\'{name}\'".format(name=action[0])
        elif len(action) == 2:
            sql = base_sql + "WHERE RAname=\'{name}\' AND RAlevel=\'{level}\'".format(name=action[0], level=action[1])
        print(read_sql_query(sql, self.connection))

    def display_all_actions(self):
        sql = "SELECT * FROM actions"
        print(read_sql_query(sql, self.connection))

    def display_all_records(self):
        sql = "SELECT Rdate, RAname, RAlevel, Rnum, Rnote FROM records"
        # result = self.cursor.execute(sql).fetchall()
        # pprint(result)
        print(read_sql_query(sql, self.connection))

    def weekly_report(self, week):
        if week == 'current':
            # this week
            sql = "select RAname, RAlevel, SUM(Rnum) as num from records where " \
                  "Rdate >= date('now','start of day', '-6 day','weekday 1') and " \
                  "Rdate < date('now','start of day', '+6 day','weekday 1')" \
                  "GROUP BY RAname, RAlevel;"
        elif week == 'last':
            # last week
            sql = "select RAname, RAlevel, SUM(Rnum) as num from records where " \
                  "Rdate >= date('now','start of day', '-13 day','weekday 1') and " \
                  "Rdate < `date('now','start of day', '-6 day','weekday 1')`" \
                  "GROUP BY RAname, RAlevel;"
        else:
            pass
        print(read_sql_query(sql, self.connection))

    def export2excel(self,file_name):
        try:
            sql = "select Rdate, Apart, RAname, RAlevel, Rnum, Rnote from records join actions" \
                  " on records.RAname = actions.Aname and records.RAlevel= actions.Alevel;"
            # write excel
            read_sql_query(sql, self.connection).to_excel(file_name+".xlsx")
        except Exception as e:
            print(e)
        print(" Successfully export to ",file_name+".xlsx")



# trdb = TRDb()
# trdb.connect()
# trdb.is_action_exist(['push-up', 'diamond'])