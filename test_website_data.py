import pytest
from website_data import get_websites_data, WebsiteData

# Параметризованный тест для проверки значений уникальных посетителей
@pytest.mark.parametrize("threshold", [10**7, 1.5 * 10**7, 5 * 10**7, 10**8, 5 * 10**8, 10**9, 1.5 * 10**9])
def test_visitor_threshold(threshold):
    websites_data = get_websites_data()  # Получаем данные о веб-сайтах
    errors = []  # Создаем пустой список для хранения ошибок

    for website_data in websites_data:
        if website_data.visitors_per_month < threshold:  # Проверяем, удовлетворяет ли количество посетителей пороговому значению
            error_message = f"{website_data.website} (Frontend: {website_data.frontend}| Backend: {website_data.backend}) has {website_data.visitors_per_month} unique visitors per month. (Expected more than {threshold})"  # Формируем сообщение об ошибке
            errors.append(error_message)  # Добавляем сообщение об ошибке в список ошибок

    assert not errors, f"Threshold {threshold} errors:\n" + "\n".join(errors)  # Проверяем наличие ошибок и выводим их, если они есть
