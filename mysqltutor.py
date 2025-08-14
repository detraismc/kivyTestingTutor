from kivy.lang import Builder
from kivymd.app import MDApp
import mysql.connector
from mysqltutorBuilder import *

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Dark"

        # Set Koneksi Mysql
        mydb = mysql.connector.connect(
            host="mysql-179b3d4e-detraismc-b8de.h.aivencloud.com",
            user="avnadmin",
            passwd="AVNS_Sz-HAXbcvrCVGn92E6H",
            port="13492"
        )
        c = mydb.cursor()
        c.execute("CREATE DATABASE IF NOT EXISTS second_db")
        #c.execute("SHOW DATABASES")
        #for db in c:
        #    print(db)
        c.execute("USE second_db")

        c.execute("""
            CREATE TABLE IF NOT EXISTS customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name text
            )
        """)

        mydb.commit()
        mydb.close()

        return Builder.load_string(mysqltutor_helper)
    def submit(self):
        mydb = mysql.connector.connect(
            host="mysql-179b3d4e-detraismc-b8de.h.aivencloud.com",
            user="avnadmin",
            passwd="AVNS_Sz-HAXbcvrCVGn92E6H",
            port="13492"
        )
        c = mydb.cursor()
        c.execute("USE second_db")
        c.execute("INSERT INTO customers (name) VALUES (%s)", (self.root.ids.word_input.text,))

        self.root.ids.word_label.text = f'{self.root.ids.word_input.text} Added'
        self.root.ids.word_input.text = ''

        mydb.commit()
        mydb.close()

    def show_record(self):
        mydb = mysql.connector.connect(
            host="mysql-179b3d4e-detraismc-b8de.h.aivencloud.com",
            user="avnadmin",
            passwd="AVNS_Sz-HAXbcvrCVGn92E6H",
            port="13492"
        )
        c = mydb.cursor()
        c.execute("USE second_db")
        c.execute("SELECT * FROM customers")
        records = c.fetchall()

        word = ''

        for record in records:
            word = f'{word}\n{record[1]}'
            self.root.ids.word_label.text = f'{word}'

        mydb.commit()
        mydb.close()

MyApp().run()