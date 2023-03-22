### Информация для разработки

### Запуск проекта:
    
Параллельный запуск следующих процессов:

Окно 1 (redis):
```
redis-server
```

Окно 2 (celery):
```
celery -A django_stepik worker -l INFO
```