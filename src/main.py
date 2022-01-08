from TRDb import TRDb

if __name__ == "__main__":
    trdb = TRDb()
    data_path = '../data/'
    print(">>> Training Records <<<")
    print("    Man, work hard every day!")
    print("-----------------------------")
    print("Menu:")
    print("Input 1: Initialize db.\t Input 2: Create new record.")
    print("Input 3: Display all records.\t Input 4: Search records by action.")
    print("Input 5: Get weekly report.\t Input 6: Export records to excel")
    print("Input q: quit.")
    command = ""
    while True:
        command = input("Input your command:").strip()
        print(command)
        if command == '1':
            print("> initializing database.")
            trdb.init_db()
            print("> completed.")
        elif command == '2':
            if trdb.connection is None:
                trdb.connect()
            record = input("> input records, separate value by space."
                           "\n  format: name level num date"
                           "\n  e.g. push-up standard 20 2022-01-01\n")
            record = record.split()
            # print(record)
            trdb.insert_record(record)
        elif command == '3':
            if trdb.connection is None:
                trdb.connect()
            trdb.display_all_records()
        elif command == '4':
            if trdb.connection is None:
                trdb.connect()
            print("> Search records by actions.")
            while True:
                command = input("  input action. (Check existing actions, type '-l' to list all.)\n")
                if command == '-l':
                    trdb.display_all_actions()
                else:
                    break
            # search record table.
            action = command.split()
            trdb.select_records_by_action(action)
        elif command == '5':
            if trdb.connection is None:
                trdb.connect()
            while True:
                command = input("> Input 1: report of this week, Input 2: report of last week.")
                if command == '1':
                    trdb.weekly_report('current')
                    break
                elif command == '2':
                    trdb.weekly_report('last')
                    break
                else:
                    print(" > command couldn't recognize, please type again.")
        elif command == '6':
            if trdb.connection is None:
                trdb.connect()
            file_name = input("> input excel file name: ").strip()
            trdb.export2excel(data_path+file_name)

        elif command == 'q':
            break
        else:
            print(" > command couldn't recognize, please type again.")

