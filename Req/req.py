# Импортируем библиотеку:
import requests

# Отправляем GET-запрос:
response = requests.get('http://info.cern.ch/')

print(response.status_code)  # Печатаем код запрошенной страницы.
print(response.text)
