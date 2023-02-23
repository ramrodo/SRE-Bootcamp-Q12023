from mysql.connector import connect, Error

HOST = "sre-bootcamp-selection-challenge.cabf3yhjqvmq.us-east-1.rds.amazonaws.com"
DATABASE = "bootcamp_tht"
USER = "secret"
PASSWORD = "jOdznoyH6swQB9sTGdLUeeSrtejWkcw"
ENCRYPT_TOKEN = "my2w7wjd7yXF64FIADfJxNs1oupTGAuW"

class Database():

    def __init__(self):
        try:
            self.conn = connect(host=HOST,
                                database=DATABASE,
                                username=USER,
                                password=PASSWORD,
            )
            self.cursor = self.conn.cursor()
            self.encrypt_token = ENCRYPT_TOKEN
            print("Database connected!")
        except Error as e:
            print("Error connecting to Database:", e)


    def getUser(self, username):
        query = "SELECT * FROM users WHERE username='{}' LIMIT 1".format(username)
        self.cursor.execute(query)
        user = self.cursor.fetchone()
        return user

    def getEncryptToken(self):
        return self.encrypt_token
