import re
from collections import Counter

def analyze_log(file_content):
    # Регулярное выражение для поиска IPv4-адреса после слова "from"
    # Пример: "from 192.168.1.105" -> извлечет "192.168.1.105"
    ip_pattern = re.compile(r"from\s+(\d{1,3}(?:\.\d{1,3}){3})")
    
    ip_counts = Counter()
    
    # Проходим по каждой строке лога
    for line in file_content.splitlines():
        # Проверяем, была ли попытка неудачной
        if "Failed password" in line:
            # Ищем IP-адрес с помощью регулярного выражения
            match = ip_pattern.search(line)
            if match:
                ip = match.group(1)
                ip_counts[ip] += 1
                
    return ip_counts

def main():
    try:
        with open('auth.log', 'r', encoding='utf-8') as file:
        log_data = file.read()
    except FileNotFoundError:
        print("Файл auth.log не найден!")
        return

    # Анализируем лог
    stats = analyze_log(log_data)

    # Выводим результат. most_common() уже вернет отсортированный список от большего к меньшему
    print(f"{'IP-адрес':<20} | {'Количество попыток'}")
    print("-" * 40)
    for ip, count in stats.most_common():
        print(f"{ip:<20} | {count}")

if __name__ == "__main__":
    main()