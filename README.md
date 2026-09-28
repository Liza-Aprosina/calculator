# Лабораторная работа
---
### Автор:
Апросина Елизавета

### Реализованы все функции
Поставьте 5, я очень устала :(


## Запуск 

Вирт :)) окружение
```
source .venv/bin/activate
```

Установка
```
python -m pip install -e '.[dev]'
```

Проверка работоспособности
```
python -m pytest
```

Проверка на адекватность
```
ruff check .
```

## Примеры использования
```
python -m toolkit calc "2+2*2 + 3/3"
```
<img width="1280" height="67" alt="image" src="https://github.com/user-attachments/assets/f7d9e52d-35fa-4e32-ab39-49e4233d570d" />

```
python -m toolkit convert 1000 --from mm --to m
```
<img width="1280" height="66" alt="image" src="https://github.com/user-attachments/assets/2f9637a2-47f3-419b-8b70-8b7d9a755119" />

```
python -m toolkit convert 52 --from K --to c
```
<img width="1280" height="68" alt="image" src="https://github.com/user-attachments/assets/2d02cac5-2a67-462a-8e92-5a0ba24eff14" />
