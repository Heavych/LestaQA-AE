import requests  # Импортируем библиотеку для выполнения HTTP-запросов
from bs4 import BeautifulSoup  # Импортируем BeautifulSoup для парсинга HTML
from dataclasses import dataclass  # Импортируем декоратор для создания датаклассов
import pytest  # Импортируем pytest для тестирования


# Создаем датакласс для хранения данных о веб-сайтах
@dataclass
class WebsiteData:
    website: str
    frontend: str
    backend: str
    visitors_per_month: int

# Функция для извлечения данных из таблицы на странице
def get_websites_data():
    url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"
    response = requests.get(url)  # Получаем HTML-страницу по URL
    soup = BeautifulSoup(response.text, "html.parser")  # Создаем объект BeautifulSoup для парсинга HTML

    table = soup.find("table", {"class": "wikitable"})  # Находим таблицу с указанным классом
    rows = table.find_all("tr")[1:]  # Получаем все строки таблицы, пропуская заголовок

    websites_data = []  # Создаем пустой список для хранения данных о веб-сайтах
    for row in rows:
        columns = row.find_all("td")  # Получаем все столбцы строки таблицы
        website = columns[0].text.strip()  # Извлекаем имя веб-сайта и очищаем от лишних пробелов
        visitors_text = columns[1].text.strip()  # Извлекаем числа и текст из столбца
        visitors_text = ''.join(filter(str.isdigit, visitors_text))  # Оставляем только цифры из текста
        visitors = int(visitors_text)  # Преобразуем текст в целое число
        frontend = columns[2].text.strip()  # Извлекаем используемые фронтенды
        backend = columns[3].text.strip()  # Извлекаем используемые бэкенды
        websites_data.append(WebsiteData(website, frontend, backend, visitors))  # Добавляем данные о веб-сайте в список

    return websites_data  # Возвращаем список данных о веб-сайтах

    # Создаем пустой список для хранения объектов WebsiteData
    website_objects = []

    # Добавляем данные из списка websites_data в объекты WebsiteData
    for data in websites_data:
        website_object = WebsiteData(
            website=data['website'],
            frontend=data['frontend'],
            backend=data['backend'],
            visitors_per_month=data['visitors_per_month']
        )
        website_objects.append(website_object)

    return website_objects

# Вызываем функцию get_websites_data() для получения объектов WebsiteData
websites = get_websites_data()

# Выводим созданные объекты WebsiteData
# for website in websites:
#    print(website)

# Запускаем тесты
if __name__ == "__main__":
    pytest.main(['-v'])  # Запускаем тесты с выводом более подробной информации
