from django.contrib import admin
from .models import (Book, Author, Reader, BookReading)

[admin.site.register(item) for item in (Book, Author, Reader, BookReading)]
