# Конспект: Основы SQL для маркетологов

По статье [HubSpot SQL Tutorial](https://blog.hubspot.com/marketing/sql-tutorial-introduction)

[Полный текст статьи на русском языке с интерактивными примерами в Jupyter Notebook](How_to_Write_Simple_Queries.ipynb)

## 1. Что такое SQL

* SQL (Structured Query Language) — язык для работы с реляционными БД.
* Основные возможности: **получение данных (SELECT)**, **добавление (INSERT)**, **обновление (UPDATE)**, **удаление (DELETE)**.
* Позволяет работать с большими массивами данных быстрее и безопаснее, чем Excel.

---

## 2. Зачем маркетологу SQL

* Безопаснее, чем Excel (меньше риск удалить/испортить данные).
* Работа с **тысячами и миллионами записей**.
* Поддержка многопользовательского доступа.
* Гибкое разграничение прав доступа.
* Легкая интеграция с инструментами визуализации.
* Обеспечивает **целостность и консистентность** данных.

---

## 3. Иерархия SQL-базы

1. **Instance (сервер)** → включает несколько баз данных.
2. **Database (БД)** → хранит данные по крупным областям.
3. **Tables (таблицы)** → аналог Excel-листов.
4. **Fields (поля)** → столбцы таблицы.
5. **Rows (строки)** → записи с конкретными значениями.

Пример:

* БД `NewEngland`
* Таблицы: `people_massachusetts`, `people_maine`, …
* Поля: `first_name`, `last_name`, `hair_color`, `birth_date`, …

---

## 4. Основные SQL-запросы

### SELECT — выборка данных

```sql
SELECT first_name, last_name
FROM people_massachusetts;
```

### WHERE — фильтрация

```sql
SELECT first_name, last_name
FROM people_massachusetts
WHERE hair_color = 'red';
```

### BETWEEN — диапазон

```sql
SELECT first_name, last_name
FROM people_massachusetts
WHERE birth_date BETWEEN '2003-01-01' AND '2003-12-31';
```

### AND / OR / NOT

```sql
-- И
WHERE hair_color = 'red' AND birth_date BETWEEN '2003-01-01' AND '2003-12-31';

-- Или
WHERE hair_color = 'red' OR birth_date BETWEEN '2003-01-01' AND '2003-12-31';

-- Не
WHERE NOT hair_color = 'red';
```

### ORDER BY — сортировка

```sql
... ORDER BY last_name;
```

### GROUP BY — группировка

```sql
SELECT hair_color, COUNT(*)
FROM people_massachusetts
GROUP BY hair_color;
```

### LIMIT — ограничение выборки

```sql
... LIMIT 100;
```

---

## 5. Модификация данных

### INSERT INTO

```sql
INSERT INTO people_massachusetts (first_name, last_name, address_state)
VALUES ('Jane', 'Doe', 'Massachusetts');
```

### UPDATE

```sql
UPDATE people_massachusetts
SET hair_color = 'brown'
WHERE first_name = 'Jane' AND last_name = 'Doe';
```

### DELETE

```sql
DELETE FROM people_massachusetts
WHERE address_state = 'maine';
```

---

## 6. Дополнительные возможности

* `*` — выбрать все поля.
* `LIKE` + `%` — поиск по шаблону.

```sql
WHERE address_zip LIKE '02%';
```

* `DATE_SUB` — динамический диапазон (последние 30 дней).
* Агрегации: `COUNT`, `AVG`, `SUM`, `MIN`, `MAX`.
* `JOIN` — объединение данных из разных таблиц по ключу.

```sql
SELECT b.first_name, b.last_name
FROM birthdate_massachusetts b
JOIN haircolor_massachusetts h USING (user_id)
WHERE h.hair_color = 'red';
```

* `CASE` — условия внутри запроса.

```sql
SELECT first_name,
       last_name,
       CASE
         WHEN hair_color = 'brown' THEN 'This person has brown hair.'
         WHEN hair_color = 'blonde' THEN 'This person has blonde hair.'
         ELSE 'Hair color not known.'
       END AS hair_info
FROM people_massachusetts;
```

---

## 7. Базовые запросы для маркетолога

* **Выборка клиентов по признаку** (WHERE).
* **Фильтрация по дате** (BETWEEN / DATE\_SUB).
* **Аналитика по сегментам** (GROUP BY + COUNT/AVG).
* **Обновление/чистка данных** (UPDATE, DELETE).
* **Объединение данных из разных таблиц** (JOIN).

---

📌 У тебя уже есть `How_to_Write_Simple_Queries.ipynb` с интерактивными примерами — этот конспект идеально ложится как теоретическая шпаргалка к нему.

Хочешь, я тебе его сразу переведу в markdown-оглавление + готовый блок в `.ipynb`, чтобы в начале ноутбука был компактный «содержание» с кликабельными ссылками на все главы (как мы обсуждали про TOC)?
