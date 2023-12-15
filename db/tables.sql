CREATE TABLE Отделение_связи (
id INT AUTO_INCREMENT PRIMARY KEY,
Название VARCHAR(255)
);

CREATE TABLE Издание (
id INT AUTO_INCREMENT PRIMARY KEY,
Индекс INT,
Название VARCHAR(255),
Подписная_цена DECIMAL(10, 2),
Количество_изданий INT,
Отделение_связи_id INT,
FOREIGN KEY (Отделение_связи_id) REFERENCES Отделение_связи(id)
);

CREATE TABLE Почтальон (
id INT AUTO_INCREMENT PRIMARY KEY,
Фамилия VARCHAR(255),
Имя VARCHAR(255),
Отчество VARCHAR(255),
Отделение_связи_id INT,
FOREIGN KEY (Отделение_связи_id) REFERENCES Отделение_связи(id)
);

CREATE TABLE Участок (
id INT AUTO_INCREMENT PRIMARY KEY,
Название VARCHAR(255),
Почтальон_id INT,
FOREIGN KEY (Почтальон_id) REFERENCES Почтальон(id)
);

CREATE TABLE Дом (
id INT AUTO_INCREMENT PRIMARY KEY,
Адрес VARCHAR(255),
Участок_id INT,
FOREIGN KEY (Участок_id) REFERENCES Участок(id)
);

CREATE TABLE Подписчик (
id INT AUTO_INCREMENT PRIMARY KEY,
Фамилия VARCHAR(255),
Имя VARCHAR(255),
Отчество VARCHAR(255),
Дом_id INT,
FOREIGN KEY (Дом_id) REFERENCES Дом(id)
);

CREATE TABLE Квитанция (
id INT AUTO_INCREMENT PRIMARY KEY,
Стоимость_подписки DECIMAL(10, 2),
Срок_подписки INT,
Дата_начала_подписки DATE,
Подписчик_id INT,
Издание_id INT,
FOREIGN KEY (Подписчик_id) REFERENCES Подписчик(id),
FOREIGN KEY (Издание_id) REFERENCES Издание(id)
);

CREATE TABLE Заведующий_почтовым_отделением (
id INT AUTO_INCREMENT PRIMARY KEY,
Логин VARCHAR(255),
Пароль VARCHAR(255),
Отделение_связи_id INT,
FOREIGN KEY (Отделение_связи_id) REFERENCES Отделение_связи(id)
);