import pymysql


try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="osdeliex",
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Подключено. для работы с базой данных необходимо отредактировать файл (main.py) /Dbpy/main.py")
    print("#" * 122)

    # try:
        # cursor = connection.cursor()

        # create table
        # with connection.cursor() as cursor:
        #     create_table_query = "CREATE TABLE `osdel_tb`(id int AUTO_INCREMENT," \
        #                          " login varchar(32)," \
        #                          " passwd varchar(32), PRIMARY KEY (id));"
        #     cursor.execute(create_table_query)
        #     print("Table norm")

        # insert data
        # with connection.cursor() as cursor:
            # insert_query = "INSERT INTO `osdel_tb` (login, passwd) VALUES ('', '');"
            # cursor.execute(insert_query)
            # connection.commit()

        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Victor', '123456', 'victor@gmail.com');"
        #     cursor.execute(insert_query)
        #     connection.commit()
        #
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Oleg', '112233', 'olegan@mail.ru');"
        #     cursor.execute(insert_query)
        #     connection.commit()

        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Oleg', 'kjlsdhfjsd', 'ole2gan@mail.ru');"
        #     cursor.execute(insert_query)
        #     connection.commit()
        #
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Oleg', '889922', 'olegan3@mail.ru');"
        #     cursor.execute(insert_query)
        #     connection.commit()

        # update data
        # with connection.cursor() as cursor:
        #     update_query = "UPDATE `users` SET password = 'xxxXXX' WHERE name = 'Oleg';"
        #     cursor.execute(update_query)
        #     connection.commit()

        # delete data
        # with connection.cursor() as cursor:
        #     delete_query = "DELETE FROM `users` WHERE id = 5;"
        #     cursor.execute(delete_query)
        #     connection.commit()

        # drop table
        # with connection.cursor() as cursor:
        #     drop_table_query = "DROP TABLE `users`;"
        #     cursor.execute(drop_table_query)

        # select all data from table
        # with connection.cursor() as cursor:
        #     select_all_rows = "SELECT * FROM `users`"
        #     cursor.execute(select_all_rows)
            # cursor.execute("SELECT * FROM `users`")
        #     rows = cursor.fetchall()
        #     for row in rows:
        #         print(row)
        #     print("#" * 20)

    # finally:
        # connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)
