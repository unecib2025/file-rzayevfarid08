# ================== ЗАДАНИЕ 1 ==================
print("Задание 1")

users = {"amir": "12345", "lale": "qwertyuio", "nik": "pass12"}

weak_users = []

for name, password in users.items():
    if len(password) < 8:
        weak_users.append(name)

print("Пользователи со слабым паролем:", ", ".join(weak_users))
print()


# ================== ЗАДАНИЕ 2 ==================
print("Задание 2")

users_2fa = {
    "user1": {"password": "123", "2fa": True},
    "user2": {"password": "456", "2fa": False},
    "user3": {"password": "789", "2fa": True}
}

count_2fa = 0

for info in users_2fa.values():
    if info["2fa"]:
        count_2fa += 1

print("Пользователей с 2FA:", count_2fa)
print()


# ================== ЗАДАНИЕ 3 ==================
print("Задание 3")

log1 = {"192.168.0.1": 5, "192.168.0.2": 3}
log2 = {"192.168.0.2": 4, "192.168.0.3": 10}

merged_logs = log1.copy()

for ip, count in log2.items():
    merged_logs[ip] = merged_logs.get(ip, 0) + count

print("Объединённые логи:", merged_logs)
print()


# ================== ЗАДАНИЕ 4 ==================
print("Задание 4")

domains = {"vk.com": False, "facebook.com": True, "spam.net": False}

print("Запрещённые домены:")
for domain, allowed in domains.items():
    if not allowed:
        print(domain)
print()


# ================== ЗАДАНИЕ 5 ==================
print("Задание 5")

threats = {
    "trojan": "high",
    "adware": "low",
    "ransomware": "high",
    "worm": "medium"
}

threat_stats = {}

for level in threats.values():
    threat_stats[level] = threat_stats.get(level, 0) + 1

print("Статистика угроз:", threat_stats)
print()


# ================== ЗАДАНИЕ 6 ==================
print("Задание 6")

activity = {"10.0.0.1": 15, "10.0.0.2": 3, "10.0.0.3": 25}

max_ip = None
max_activity = 0

for ip, count in activity.items():
    if count > max_activity:
        max_activity = count
        max_ip = ip

print("Самый активный IP:", max_ip)
print()


# ================== ЗАДАНИЕ 7 ==================
print("Задание 7")

attempts = {
    "amir": [True, False, False, True],
    "rustam": [False, False, False],
    "sevil": [True, True]
}

print("Пользователи с >50% неуспешных попыток:")
for user, logs in attempts.items():
    failed = logs.count(False)
    total = len(logs)

    if failed / total > 0.5:
        print(user)
print()


# ================== ЗАДАНИЕ 8 ==================
print("Задание 8")

devices = {
    "router": {"ip": "192.168.1.1", "os": "IOS", "vulnerabilities": 5},
    "server": {"ip": "192.168.1.10", "os": "Linux", "vulnerabilities": 1},
    "camera": {"ip": "192.168.1.20", "os": "Custom", "vulnerabilities": 12}
}

print("Устройства с уязвимостями > 3:")
for device, info in devices.items():
    if info["vulnerabilities"] > 3:
        print(device)
print()


# ================== ЗАДАНИЕ 9 ==================
print("Задание 9")

db1 = {"amir": "admin", "rustam": "user", "leyla": "guest"}
db2 = {"amir": "user", "sevil": "guest", "rustam": "user"}

print("Пользователи в обеих базах:")
for user in db1:
    if user in db2:
        print(user, "-", db1[user], "/", db2[user])
print()


# ================== ЗАДАНИЕ 10 ==================
print("Задание 10")

permissions = {
    "admin": {"read": True, "write": True, "delete": True},
    "user": {"read": True, "write": False, "delete": False},
    "guest": {"read": True, "write": False, "delete": False}
}

role = input("Введите роль пользователя: ")

default_permissions = {"read": False, "write": False, "delete": False}
user_permissions = permissions.setdefault(role, default_permissions)

print("Права доступа:", user_permissions) 




1. Что такое словарь и чем он отличается от списка?
Словарь — это структура данных, которая хранит пары ключ : значение.
Отличия от списка:
	•	в списке доступ по индексу (0, 1, 2…),
	•	в словаре доступ по ключу (строка, число и т.д.),
	•	словарь не хранит элементы просто по порядку, а по уникальным ключам.

⸻

2. Какие типы данных могут быть ключами словаря?
Ключами могут быть неизменяемые (immutable) типы данных:
	•	int, float
	•	str
	•	tuple (если внутри тоже только неизменяемые элементы)
	•	bool

⸻

3. Чем отличаются методы keys(), values(), items()?
	•	keys() — возвращает все ключи словаря
	•	values() — возвращает все значения
	•	items() — возвращает пары (ключ, значение)

⸻

4. Для чего используется метод get()?
get() используется для безопасного получения значения по ключу.
Если ключа нет — ошибки не будет, вернётся None или значение по умолчанию.

d = {"a": 1}
d.get("b", 0)  # вернёт 0

5. Как работает метод update()?
update() добавляет новые пары или обновляет существующие ключи.

d = {"a": 1}
d.update({"b": 2, "a": 10})
# результат: {'a': 10, 'b': 2}


6. Что такое вложенный словарь?
Это словарь, в котором значением является другой словарь.

user = {
    "name": "Ali",
    "stats": {"age": 18, "height": 180}
}




7. Можно ли использовать изменяемые типы данных как ключи? Почему?
❌ Нельзя.
Потому что ключи должны быть неизменяемыми и хешируемыми.
Список или словарь можно изменить, из-за этого Python не сможет корректно их найти.

⸻

8. Для чего используется метод setdefault()?
Он возвращает значение по ключу, а если ключа нет — создаёт его с заданным значением.

d = {}
d.setdefault("a", 5)
# {'a': 5}


9. Можно ли перебрать элементы словаря в определённом порядке?
Да.
Начиная с Python 3.7 словарь сохраняет порядок добавления элементов.
Также можно отсортировать при переборе:


for k in sorted(d):
    print(k)



10. Чем отличаются удаление с помощью del и pop()?
	•	del — просто удаляет элемент
	•	pop() — удаляет и возвращает значение




d = {"a": 1}
x = d.pop("a")  # x = 1
