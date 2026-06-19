import requests
from bs4 import BeautifulSoup

url = "https://lenta.ru"
response = requests.get(url)

print(f"Статус: {response.status_code}")
print(f"Длина текста: {len(response.text)}")

soup = BeautifulSoup(response.text, 'html.parser')

# Найдём все h3 (заголовки)
h3_tags = soup.find_all('h3')
print(f"Найдено h3: {len(h3_tags)}")

# Покажем первые 3
for i, tag in enumerate(h3_tags[:3]):
    print(f"{i+1}. {tag.get_text(strip=True)}")

# Найдём все p (описания)
p_tags = soup.find_all('p')
print(f"\nНайдено p: {len(p_tags)}")

# Сохраним всё в файл для отладки
with open('debug.html', 'w', encoding='utf-8') as f:
    f.write(response.text)

print("HTML сохранён в debug.html")