# SQL Data Types — Конспект

[Полная статья](https://www.digitalocean.com/community/tutorials/sql-data-types)  
[Видео по теме](https://www.youtube.com/watch?v=vAiBa69YCnk)

---

## Зачем важно правильно выбирать типы данных
- **Эффективность хранения** — используем минимальный подходящий размер.
- **Производительность** — меньше размер → быстрее запросы.
- **Целостность данных** — типы предотвращают некорректные значения.

---

## Основные категории типов данных
1. **Числовые**: `TINYINT`, `SMALLINT`, `INT`, `BIGINT`, `DECIMAL`, `NUMERIC`, `FLOAT`, `REAL`.  
2. **Дата и время**: `DATE`, `TIME`, `DATETIME`, `TIMESTAMP`, `YEAR`.  
3. **Строковые**: `CHAR`, `VARCHAR`, `TEXT`.  
4. **Unicode строки**: `NCHAR`, `NVARCHAR`, `NTEXT`.  
5. **Бинарные**: `BINARY`, `VARBINARY`, `BLOB`.  
6. **Прочие**: `BOOLEAN`, `UUID`, `JSON`, `XML`, `CLOB`.

---

## Ключевые различия у СУБД
- **MySQL**: `ENUM`, `SET`, `UNSIGNED`, `YEAR`.  
- **PostgreSQL**: `ARRAY`, `UUID`, `JSONB`, `BOOLEAN`, `INET/CIDR`.  
- **SQL Server**: `MONEY`, `SMALLMONEY`, `DATETIME2`, `UNIQUEIDENTIFIER`, `VARCHAR(MAX)`.  
- **Oracle**: `VARCHAR2`, `NUMBER`, `DATE` (всегда с временем), `CLOB`, `BLOB`, `NCLOB`.

---

## Numeric — размеры и диапазоны
| Тип        | Размер | Диапазон                         | Пример использования |
|------------|--------|----------------------------------|-----------------------|
| TINYINT    | 1 байт | -128..127 / 0..255 (UNSIGNED)    | возраст, маленькие числа |
| SMALLINT   | 2 байта| -32K..32K                        | год выпуска |
| INT        | 4 байта| ±2 млрд                          | ID, счётчики |
| BIGINT     | 8 байт | ±9 квинтиллионов                 | транзакции, научные данные |
| DECIMAL(p,s), NUMERIC(p,s) | переменный | до 10^38 | финансы |
| FLOAT, REAL| 4–8 байт | большие приближённые значения | научные расчёты |

---

## Date/Time
- `DATE` — только дата (`YYYY-MM-DD`)  
- `TIME` — только время (`HH:MM:SS`)  
- `DATETIME` — дата и время  
- `TIMESTAMP` — количество секунд от 1970-01-01 UTC  
- `YEAR` — год (2 или 4 цифры)  

---

## Strings
- `CHAR(n)` — фиксированная длина (короткие коды, ISO-коды стран).  
- `VARCHAR(n)` — переменная длина, оптимально для имён, email и т.п.  
- `TEXT` — длинные тексты (статьи, комментарии).  
- Unicode: `NCHAR`, `NVARCHAR`, `NTEXT` (SQL Server) или `utf8mb4` (MySQL).  

---

## Binary
- `BINARY(n)` — фиксированная длина (хэши).  
- `VARBINARY(n)` — переменная длина (иконки, QR-коды).  
- `BLOB` — большие файлы (фото, PDF, аудио).  

---

## Специализированные типы
- `BOOLEAN` — логика (MySQL = TINYINT(1)).  
- `UUID` — уникальные 128-битные ключи.  
- `JSON`, `XML` — полуструктурированные данные.  
- `CLOB`, `NCLOB` — большие тексты (Oracle).  

---

## Кастинг и конвертация
- **Неявная**: СУБД сама приводит тип (может быть риск/потери).  
- **Явная**:
  - `CAST(expr AS target_type)` — стандарт ANSI SQL.  
  - `CONVERT(type, expr, style)` — SQL Server.  

---

## Лучшие практики
1. Используй **минимальный подходящий тип**.  
   - Возраст → `TINYINT UNSIGNED`.  
   - UserID → `INT`, а не `BIGINT`.  
   - Статусы → `ENUM` или `TINYINT`.  
2. Понимай данные (нужны ли отрицательные? дробные?).  
3. Планируй рост, но **без переусложнения**.  
4. CHAR vs VARCHAR:  
   - `CHAR` для фиксированной длины (например, ISO-коды стран).  
   - `VARCHAR` — почти всегда лучше.  

---

## FAQ
- **Основные категории**: Numeric, String, Date/Time, Binary, Misc.  
- **VARCHAR vs TEXT**:  
  - `VARCHAR` — ограниченная длина, быстро.  
  - `TEXT` — большие тексты, хранение отдельно.  
- **MySQL vs PostgreSQL**:  
  - MySQL: `ENUM`, `SET`, `UNSIGNED`.  
  - PostgreSQL: `ARRAY`, `UUID`, `JSONB`.  
- **INT по умолчанию**: 4 байта, диапазон `-2,147,483,648` до `2,147,483,647` (или `0..4,294,967,295` UNSIGNED).

---
