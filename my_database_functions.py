import pymysql.cursors

#to connect to the database 
connection = pymysql.connect(host = "localhost",
                             user = "root",
                             password = "",
                             db = "riddey_academy",
                             charset = "utf8mb4",
                             cursorclass = pymysql.cursors.DictCursor)


def create_tables():
    with connection.cursor() as Cursor:
        create_table_riddey_info = """CREATE TABLE IF NOT EXISTS riddey_info(
                                    id INT(10) AUTO_INCREMENT NOT NULL PRIMARY KEY,
                                    name VARCHAR(100),
                                    gender VARCHAR(10),
                                    age INT(4) 
                                    );
                                    """
        Cursor.execute(create_table_riddey_info)



        create_table_riddey_records = """CREATE TABLE IF NOT EXISTS riddey_records(
                                        id INT(10) AUTO_INCREMENT NOT NULL PRIMARY KEY,
                                        student_id INT(10), FOREIGN KEY riddey_records(student_id) REFERENCES riddey_info(id),
                                        subject VARCHAR(100),
                                        score INT(4)
                                    );
                                    """
        Cursor.execute(create_table_riddey_records)
        
        connection.commit()


def write_info_data(name, gender, age):
    with connection.cursor() as Cursor:
        add_info = f"INSERT INTO riddey_info (name, gender, age) VALUES ('{name}', '{gender}', {age});"

        Cursor.execute(add_info)

        connection.commit()



def write_records_data(student_id, subject, score):
    with connection.cursor() as Cursor:
        add_records = f"INSERT INTO riddey_records (student_id, subject, score) VALUES ({student_id}, '{subject}', {score});"


        Cursor.execute(add_records)

        connection.commit()




create_tables()






































        


