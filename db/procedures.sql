DELIMITER //

CREATE PROCEDURE CountPostalWorkers(IN departmentId INT)
BEGIN
SELECT COUNT(*) AS Количество_почтальонов
FROM Почтальон
WHERE Почтальон.Отделение_связи_id = departmentId;
END //


CREATE PROCEDURE GetSubscribedEditions(IN lastName VARCHAR(255), IN firstName VARCHAR(255), IN surname VARCHAR(255))
BEGIN
SELECT Издание.*
FROM Издание
JOIN Квитанция ON Издание.id = Квитанция.Издание_id
JOIN Подписчик ON Квитанция.Подписчик_id = Подписчик.id
WHERE Подписчик.Фамилия = lastName AND Подписчик.Имя = firstName AND Подписчик.Отчество = surname;
END //


CREATE PROCEDURE GetAverageSubscriptionDuration()
BEGIN
SELECT Издание.id AS Издание_ID, Издание.Название AS Название_Издания, AVG(Квитанция.Срок_подписки) AS Средний_Срок_Подписки
FROM Издание
JOIN Квитанция ON Издание.id = Квитанция.Издание_id
GROUP BY Издание.id, Издание.Название;
END //


CREATE PROCEDURE GetReceiptsForDepartment(IN departmentId INT)
BEGIN
SELECT Квитанция.*
FROM Квитанция
JOIN Подписчик ON Квитанция.Подписчик_id = Подписчик.id
JOIN Дом ON Подписчик.Дом_id = Дом.id
JOIN Участок ON Дом.Участок_id = Участок.id
JOIN Почтальон ON Участок.Почтальон_id = Почтальон.id
JOIN Отделение_связи ON Почтальон.Отделение_связи_id = Отделение_связи.id
WHERE Отделение_связи.id = departmentId;
END //


CREATE PROCEDURE GetPostalWorkersByAddress(IN address VARCHAR(255))
BEGIN
SELECT Почтальон.Фамилия, Почтальон.Имя, Почтальон.Отчество
FROM Почтальон
JOIN Участок ON Почтальон.id = Участок.Почтальон_id
JOIN Дом ON Участок.id = Дом.Участок_id
WHERE Дом.Адрес = address;
END //


CREATE PROCEDURE GetDepartmentNameByCredentials(IN login VARCHAR(255), IN password VARCHAR(255))
BEGIN
SELECT Отделение_связи.Название
FROM Заведующий_почтовым_отделением
JOIN Отделение_связи ON Заведующий_почтовым_отделением.Отделение_связи_id = Отделение_связи.id
WHERE Заведующий_почтовым_отделением.Логин = login AND Заведующий_почтовым_отделением.Пароль = password;
END //


CREATE PROCEDURE GetDepartmentIdByName(IN departmentName VARCHAR(255))
BEGIN
SELECT id
FROM Отделение_связи
WHERE Название = departmentName;
END //


CREATE PROCEDURE GetMaxEditionsCountByPlot()
BEGIN
SELECT Участок.id AS Участок_ID, Участок.Название_Участка AS Название_Участка, COUNT(*) AS Количество_Изданий
FROM Участок
JOIN Почтальон ON Участок.Почтальон_id = Почтальон.id
JOIN Дом ON Участок.id = Дом.Участок_id
JOIN Подписчик ON Дом.id = Подписчик.Дом_id
JOIN Квитанция ON Подписчик.id = Квитанция.Подписчик_id
GROUP BY Участок.id
ORDER BY Количество_Изданий DESC
LIMIT 1;
END //

DELIMITER ;
