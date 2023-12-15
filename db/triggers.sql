DELIMITER //

CREATE TRIGGER before_insert_kvitanziya
BEFORE INSERT ON Квитанция FOR EACH ROW
BEGIN
DECLARE total_cost DECIMAL(10, 2);
SET total_cost = NEW.Стоимость_подписки * NEW.Срок_подписки;
UPDATE Издание
SET Количество_изданий = Количество_изданий - 1
WHERE id = NEW.Издание_id;
SET NEW.Стоимость_подписки = total_cost;
END //

DELIMITER ;

DELIMITER //