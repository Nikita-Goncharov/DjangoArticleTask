## Django Articles project

Вебсервіс для створення статей та їх коментування.

Для запуску проекту на своєму комп'ютері потрібно:
1. Python версії **3.х**.
2. Зклонувати цей проект собі локально на комп'ютер у будь-яку директорію: **git clone https://github.com/Nikita-Goncharov/DjangoArticleTask.git**.
3. У цій же директорії створити віртуальне середовище: **python3 -m venv env**, якщо у вас віндовс, то замість **python3** треба написати **python**.
4. Активувати віртуальне середовище: **source env/bin/activate**, для віндовс існує інша команда(дивитися у google).
5. Завантажити залежності для проекту: **pip install -r requirements.txt**.
6. Створити файл **.env** за шляхом **ваша_директорія/django_articles/** та додати у нього такі змінні:
   * **DB_NAME='database_name'**
   * **DB_USER='user_name'**
   * **DB_PASSWORD='user_password'**
   * **DB_HOST='database_host'**
   * **DB_PORT='database_port'**
   * **SECRET_KEY='django_secret_key'** (будь-який набір символів з клавіатури)
7. Створити postgresql БД з ім'ям, яке ви написали у .env файлі
8. Провести міграції

