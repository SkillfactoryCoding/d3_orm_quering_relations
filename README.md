Для запуска проекта выполните: 
    python manage.py runserver

# Примеры запросов из вебинара
<i>from p_library.models import Book, Author</i> - импорт моделей необходимых для составления запросов

<i>from django.db import models</i> - модуля моделей

<i>from django.db.models import Count, Sum, F</i> - импорт спецификаторов запросов

<i>Book.objects.all()</i> - выборка всех записей из таблицы книга

<i>Author.objects.all()</i> - выборка всех записей из таблицы Автор

<i>annotated_authors = authors.annotate(Count("book_author"))</i> - аннотация количества авторов по признаку наличия произведений

<i>authors_list = annotated_authors.filter(books__gt=1)</i> - фильтрация списка авторов по признаку "более одного произведения в библиотеке" 

<i>authors = Author.objects.annotate(books=Count("book_author")).filter(books__gt=1)</i> - объединение двух предыдущих запросов

<i>books = Book.objects.filter(author__in=authors_list)</i> - фильтрация записей таблицы Книга по признаку нахождения автора в списке "authors"

<i>from django.db.models import ExpressionWrapper</i> - импорт обертки для написания составных запросов

<i>books_price = books.annotate(all_price=(ExpressionWrapper(F("price")*F("copy_count"), output_field="")))</i> - аннотирование списка Книг общей стоимостью всех копий данной Книги

<i>books_price = books.annotate(all_price=(ExpressionWrapper(F("price")*F("copy_count"), output_field=DecimalField()))).aggregate(Sum("all_price"))</i> - аггрегация общей стоимости всех копий всех Книг

<i>books_price = Book.objects.filter(author__in=authors_list).annotate(all_price=(ExpressionWrapper(F("price")*F("copy_count"), output_field=DecimalField()))).aggregate(Sum("all_price"))</i> - объединение всех предыдущих запросов

<i>from p_library.models import Reader</i> - импорт модели Читатель

<i>reader = Reader(name="Вася")</i> - создание объекта нового Читателя

<i>reader.save()</i> - вызов метода сохранения объекта Читателя в БД

Использование RelatedManager:

<i>reader.books.add(2)</i> - добавление связи Читатель-Книга

<i>reader.books</i> - менеджер отношений RelatedManager для связи Читатель-Книга
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals.ManyRelatedManager at 0x7efbf14b4400 - 

<i>reader.books.all()</i> - запрос списка Книг, связанных с Читателем
<QuerySet [<Book: Руслан и Людмила]

Добавление связи Читатель-Книга с помощью создания записи в таблице связи:

<i>new_br = BookReading(book_id=2, reader_id=1, completion=False)</i>

<i>new_br.save()</i>                                       

<i>new_br</i>
<BookReading: Руслан и Людмила-Вася-False
