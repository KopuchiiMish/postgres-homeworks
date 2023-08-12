-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar,
-- birthday date, phone varchar
CREATE TABLE student
(
	student_id serial,
	first_name varchar(50),
	last_name varchar(50),
	birthday_date date,
	phone varchar(30)
)

-- 2. Добавить в таблицу student колонку middle_name varchar
ALTER TABLE student ADD COLUMN middle_name varchar(50)

-- 3. Удалить колонку middle_name
ALTER TABLE student DROP COLUMN middle_name

-- 4. Переименовать колонку birthday в birth_date
ALTER TABLE student RENAME birthday_date TO birth_date

-- 5. Изменить тип данных колонки phone на varchar(32)
ALTER TABLE student ALTER COLUMN phone SET DATA TYPE varchar(32)

-- 6. Вставить три любых записи с автогенерацией идентификатора
INSERT INTO student (first_name, last_name, birth_date, phone) VALUES
('Ivan', 'Ivanov', '1984-03-06', '+79165341278'),
('Maria', 'Ivanova-Petrova', '1980-05-07', '+79161234758'),
('Petr', 'Petrov', '1996-03-09', '+79154892345')

-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние
TRUNCATE TABLE student RESTART IDENTITY
