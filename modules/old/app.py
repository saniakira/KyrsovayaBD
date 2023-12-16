import hashlib
from copy import copy
from json import dump

from PyQt5.QtWidgets import QMessageBox
from icecream import ic

from modules.constants import cursor, link, JSON, HTML
from modules.old.main_window_old import Ui_MainWindow


# Сначала создается Отделение связи.К нему создается издание и зав. отделением.
# TODO:Создать запрос на создание почтальона.
# TODO:Во время создания записи в таблицу "квитанция" должны быть указаны:
#     Подписчик, отделение связи и издание должны уже существовать.
#     Стоимость подписки должна считаться на стороне сервера процедурой и триггером на sql.
#     Нужно указать дату начала подписки(будет браться либо автоматически текущая при создании либо указывать вручную)
# TODO: Во время создания записи в таблицу "подписчик" должны быть указаны:
#     Дом.
# TODO: Во время создания записи в таблицу "Дом" должен быть участок.
# TODO: Во время создания записи в таблицу "участок" должен быть почтальон.
#
# Заведующий почтовым отделением регестрируется отдельно.Пароль хешируется.


class App(Ui_MainWindow):
    def __init__(self):
        self.department_id = None
        self.subscribers = []
        self.releases = []
        self.postmen = []
        self.locations = []
        self.receipts = []
        self.homes = []

    def fill_receipts(self):
        cursor.execute(
            f""""CALL GetReceiptsForDepartment(1); -- Замените 1 на фактический идентификатор вашего отделения связи{self.department_id}""")
        for receipt in cursor.fetchall():
            self.receipts.append(
                {"id": receipt[0],
                 "price": float(receipt[1]),
                 "time": receipt[2],
                 "date": str(receipt[3]),
                 "subscriber_id": receipt[4],
                 "release_id": receipt[5]
                 })
        ic(self.receipts)
        for receipt in self.receipts:
            self.listWidgetTabReceipts.addItem(
                f"Квитанция номер {receipt['id']} была выдана в {receipt['date']} на срок {receipt['time']} месяцев  на сумму {receipt['price']} рублей ")

    def fill_locations(self):
        cursor.execute(f"SELECT * FROM Участок WHERE Почтальон_id = {self.department_id}")
        for location in cursor.fetchall():
            self.locations.append(
                {
                    "id": location[0],
                    "name": location[1],
                    "postman_id": location[2]
                })
        ic(self.locations)
        [self.listWidgetLocations.addItem(i['name']) for i in self.locations]

    def fill_subscribers(self):
        cursor.execute("select * from подписчик;")
        for subscriber in cursor.fetchall():
            self.subscribers.append(
                {
                    "id": subscriber[0],
                    "last_name": subscriber[1],
                    "first_name": subscriber[2],
                    "surname": subscriber[3],
                    "home_id": subscriber[4],
                })
        for i in self.subscribers:
            self.Subscribers_view.addItem(f"{i['first_name']} {i['surname']} {i['last_name']}")
        ic(self.subscribers)

    def fill_releases(self):
        cursor.execute(f"select * from издание where Отделение_связи_id='{self.department_id}'")
        releases = list(cursor.fetchall())
        for release in releases:
            self.releases.append(
                {
                    "id": release[0],
                    "index": release[1],
                    "name": release[2],
                    "price": float(release[3]),
                    "amount": float(release[4]),
                    "location": release[5]
                })
        for release in self.releases:
            string = f"Индекс издания = {release['index']}, Название = {release['name']}, Цена = {float(release['price'])}, Количество изданий = {release['amount']}"
            self.listWidgetTabReleases.addItem(string)
            self.listWidgetReleases.addItem(string)

    def enable_buttons(self):
        self.AddReceiptButton.setEnabled(True)
        self.pushButtonAddRelease.setEnabled(True)
        self.pushButtonTabPostmen_3.setEnabled(True)
        self.pushButtonTabSubscribers_3.setEnabled(True)
        self.pushButtonForRequest.setEnabled(True)

    def fill_postmen(self):
        cursor.execute(f"select * from почтальон where Отделение_связи_id='{self.department_id}'")
        for postman in cursor.fetchall():
            self.postmen.append({"id": postman[0],
                                 "last_name": postman[1],
                                 "first_name": postman[2],
                                 "surname": postman[3],
                                 "home_id": postman[4]
                                 })
        ic(self.postmen)
        for postman in self.postmen:
            self.listWidget_TabPostmen.addItem(
                f"Почтальон {postman['first_name']} {postman['surname']} {postman['last_name']}")

    def fill_locations_for_request(self):
        cursor.execute("SELECT * from дом")
        for home in cursor.fetchall():
            self.homes.append(
                {
                    "id": home[0],
                    "adress": home[1],
                    "location_id": home[2]
                })
            self.viewLocationsForRequest.addItem(self.homes[-1]['adress'])

    def update_lists(self):
        self.listWidget_TabPostmen.clear()
        self.postmen = []
        self.fill_postmen()
        self.listWidgetTabReleases.clear()
        self.listWidgetReleases.clear()
        self.releases = []
        self.fill_releases()
        self.listWidgetLocations.clear()
        self.locations = []
        self.fill_locations()
        self.subscribers = []
        self.fill_subscribers()
        self.receipts = []
        self.fill_receipts()
        self.fill_locations_for_request()
        for subscriber in self.subscribers:
            self.listWidgetFioSubscriber.addItem(
                f"{subscriber['first_name']} {subscriber['last_name']} {subscriber['surname']}")

    def find_postman(self):
        cursor.execute(f"""SELECT Почтальон.Фамилия, Почтальон.Имя, Почтальон.Отчество
            FROM Почтальон
            JOIN Участок ON Почтальон.id = Участок.Почтальон_id
            JOIN Дом ON Участок.id = Дом.Участок_id
            WHERE Дом.Адрес = '{self.viewLocationsForRequest.selectedItems()[0].text()}';
        """)
        result = cursor.fetchone()
        self.labelResultForRequest.setText(f"{result[0]} {result[1]} {result[2]}")

    def verify(self):
        if not self.department_id:
            cursor.execute(f"""
            SELECT Отделение_связи.Название
            FROM Заведующий_почтовым_отделением
            JOIN Отделение_связи ON Заведующий_почтовым_отделением.Отделение_связи_id = Отделение_связи.id
            WHERE Заведующий_почтовым_отделением.Логин = '{self.LoginEdit.text()}' AND Заведующий_почтовым_отделением.Пароль = '{hashlib.sha256(self.PasswordEdit.text().encode('utf8')).hexdigest()}';
                """)
            name = cursor.fetchone()
            if name:
                name = name[0]
                self.enable_buttons()
                cursor.execute(f"select id from Отделение_связи where название='{name}'")
                self.department_id = cursor.fetchone()[0]
                self.update_lists()
                msg = QMessageBox()
                msg.setWindowTitle("Удачная авторизация")
                msg.setText(f"Администратор отделения {name} успешно вошёл")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Неудачная авторизация")
                msg.setText(f"Неверный логин или пароль")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()

    def set_releases(self):
        self.stackedWidget.setCurrentWidget(self.pageReleases)

    def set_receipts(self):
        self.stackedWidget.setCurrentWidget(self.pageReceipts)

    def set_subscribers(self):
        self.stackedWidget.setCurrentWidget(self.pageSubscribers)

    def set_postmen(self):
        self.stackedWidget.setCurrentWidget(self.pagePostmen)

    def make_new_receipt(self):
        last_name = self.LastNamelineEdit.text()
        first_name = self.LastNamelineEdit.text()
        surname = self.SectionLineEdit.text()
        location = self.lineEdit.text()
        subscribe_time = self.spinBox.text()
        date = "-".join(self.dateEdit.text().split(".")[::-1])
        ic(self.locations)
        id_location = 0
        for l in self.locations:
            if l['name'] == self.listWidgetLocations.selectedItems()[0].text():
                id_location = l['id']
        cursor.execute(f"INSERT INTO Дом (Адрес, Участок_id) VALUES ('{location}', {id_location});")
        link.commit()
        cursor.execute(f"select id from Дом where Адрес='{location}';")
        home_id = cursor.fetchone()[0]
        cursor.execute(
            f"INSERT INTO Подписчик(Фамилия, Имя, Отчество, Дом_id) VALUES('{last_name}', '{first_name}', '{surname}', {home_id});")
        link.commit()
        cursor.execute(f"select id from подписчик where фамилия='{last_name}';")
        subscriber_id = cursor.fetchone()[0]
        index = self.listWidgetReleases.selectedItems()[0].text().split(",")[0].split(" ")[-1]
        cursor.execute(f"select id from издание where индекс = '{index}';")
        release_id = cursor.fetchone()[0]
        cursor.execute(
            f"INSERT INTO Квитанция (Срок_подписки, Дата_начала_подписки, Подписчик_id, Издание_id) VALUES({subscribe_time}, '{date}', {subscriber_id}, {release_id});")
        link.commit()
        self.update_lists()

    def find_max(self):
        (cursor.execute
         (f"""
        SELECT Участок.id AS Участок_ID, Участок.Название_Участка AS Название_Участка, COUNT(*) AS Количество_Изданий
        FROM Участок
        JOIN Почтальон ON Участок.Почтальон_id = Почтальон.id
        JOIN Дом ON Участок.id = Дом.Участок_id
        JOIN Подписчик ON Дом.id = Подписчик.Дом_id
        JOIN Квитанция ON Подписчик.id = Квитанция.Подписчик_id
        GROUP BY Участок.id
        ORDER BY Количество_Изданий DESC
        LIMIT 1;
            """
          ))
        self.labelResultForRequest.setText(
            f"Количесто изданий максимально на участке под названием '{cursor.fetchone()[1]}'")

    def find_average(self, id=None):
        (cursor.execute
         (f"""
            SELECT Издание.id AS Издание_ID, Издание.Название AS Название_Издания, AVG(Квитанция.Срок_подписки) AS Средний_Срок_Подписки
            FROM Издание
            JOIN Квитанция ON Издание.id = Квитанция.Издание_id
            GROUP BY Издание.id, Издание.Название;
         """))
        results = cursor.fetchall()
        ic(results)
        final_text = ""
        for result in results:
            final_text += f"Средний срок подписки на издание под названием {result[1]} равен {result[-1]}.\n"
        self.labelResultForRequest.setText(final_text)
        if id:
            for result in results:
                if int(result[0]) == int(id):
                    return result[-1]

    def find_magazines(self):
        for subscriber in self.subscribers:
            if (subscriber['first_name'] == self.listWidgetFioSubscriber.selectedItems()[0].text().split(" ")[0]
                    and subscriber['last_name'] == self.listWidgetFioSubscriber.selectedItems()[0].text().split(" ")[1]
                    and subscriber['surname'] == self.listWidgetFioSubscriber.selectedItems()[0].text().split(" ")[2]):
                cursor.execute(f"""SELECT Издание.*
                        FROM Издание
                        JOIN Квитанция ON Издание.id = Квитанция.Издание_id
                        JOIN Подписчик ON Квитанция.Подписчик_id = Подписчик.id
                        WHERE Подписчик.Фамилия = '{subscriber['last_name']}' AND 
                        Подписчик.Имя = '{subscriber['first_name']}' AND Подписчик.Отчество = '{subscriber['surname']}';
                        """)
                for result in cursor.fetchall():
                    index = result[1]
                    name = result[2]
                    price = float(result[3])
                    count = result[4]
                    self.labelResultForRequest.setText(
                        f"Индекс={index}, Название={name}, Цена={price}, Количество доступно={count}")

    def count_postmen(self):
        (cursor.execute
         (f"""
                SELECT COUNT(*) AS Количество_почтальонов
                FROM Почтальон
                WHERE Почтальон.Отделение_связи_id = {self.department_id};
                """
          ))
        result = cursor.fetchone()[0]
        self.labelResultForRequest.setText(f"Количество почтальонов, работающих в отделении ={result}")
        return result

    def make_new_release(self):
        pass

    def make_report(self):
        if self.listWidgetReport.item(0):
            self.listWidgetReport.clear()
        main_info = f"""
        Отчет о доставке почтой газет и журналов

        Общая информация:

        Количество почтальонов в почтовом отделении: [{len(self.postmen)}]
        Общее количество обслуживаемых участков: [{len(self.locations)}]
        Общее количество различных изданий, доставляемых подписчикам: [{len(self.releases)}]
        """
        postmen = copy(self.postmen)
        releases = copy(self.releases)
        locations = []
        for location in self.locations:
            for i, p in enumerate(postmen):
                if location['postman_id'] == p['id']:
                    postman = postmen.pop(i)
            for i, r in enumerate(releases):
                if r['location'] == self.department_id:
                    release = releases.pop(i)
            locations.append(f"""
        Участок {location['id']}:
            Фамилия и инициалы почтальона: [{postman['first_name']} {postman['surname']} {postman['last_name']}]
            Перечень доставляемых изданий:
                Название издания [{release['name']}], Индекс: [{release['index']}], Адрес доставки: [{location['name']}],
                 Средний срок подписки: [{int(self.find_average(location['id']))}] месяцев, Количество экземпляров: [{release['amount']}]
        """)
        for location in locations:
            main_info += location

        self.listWidgetReport.addItem(main_info)
        with open(JSON, "w") as f:
            dump([self.subscribers, self.postmen, self.locations, self.releases, self.homes, self.receipts], f)
        with open(HTML, "w") as f:
            f.write(main_info)

    def choose(self):
        if self.radioButtonFioPostman.isChecked():
            self.find_postman()
        elif self.radioButtonMagazines.isChecked():
            self.find_magazines()
        elif self.radioButtonCountPostman.isChecked():
            self.count_postmen()
        elif self.radioButtonMax.isChecked():
            self.find_max()
        elif self.radioButtonAverage.isChecked():
            self.find_average()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Неудачная попытка")
            msg.setText("Вы не выбрали ни один вариант")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

    def setupUi(self, MainWindow):
        super(App, self).setupUi(MainWindow)
        self.LoginButton.clicked.connect(self.verify)
        self.AddReceiptButton.setEnabled(False)
        self.pushButtonAddRelease.setEnabled(False)
        self.pushButtonTabPostmen_3.setEnabled(False)
        self.pushButtonTabSubscribers_3.setEnabled(False)
        self.pushButtonForRequest.setEnabled(False)
        self.pushButtonTabReleases.clicked.connect(self.set_releases)
        self.pushButtonTabReleases_2.clicked.connect(self.set_releases)
        self.pushButtonTabPostmen.clicked.connect(self.set_postmen)
        self.pushButtonTabPostmen_3.clicked.connect(self.set_postmen)
        self.pushButtonTabReceipts.clicked.connect(self.set_receipts)
        self.pushButtonTabReceipts_2.clicked.connect(self.set_receipts)
        self.pushButtonTabSubscribers.clicked.connect(self.set_subscribers)
        self.pushButtonTabSubscribers_3.clicked.connect(self.set_subscribers)
        self.AddReceiptButton.clicked.connect(self.make_new_receipt)
        self.pushButtonAddRelease.clicked.connect(self.make_new_release)
        self.pushButtonForRequest.clicked.connect(self.choose)
        self.pushButtonReport.clicked.connect(self.make_report)
