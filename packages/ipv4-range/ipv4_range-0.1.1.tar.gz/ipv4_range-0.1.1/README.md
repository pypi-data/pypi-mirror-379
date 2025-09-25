# 📄 IPv4Range

## Установка

```bash
pip install ipv4-range
```

## Описание

`IPv4Range` — это класс для работы с диапазонами IPv4-адресов.
Он позволяет:

* Создавать диапазоны из строки (`10.0.0.0-10.0.0.100`), списка адресов или сети (`10.0.0.0/24`);
* Проверять, является ли диапазон корректной сетью;
* Преобразовывать диапазон в `IPv4Network`;
* Итерацию по IP-адресам внутри диапазона;
* Сравнение диапазонов и сетей;
* Проверку вхождения IP-адреса в диапазон.

## Использование

### Создание диапазона

```python
from ipv4_range import IPv4Range

rng = IPv4Range('10.0.0.0-10.0.0.100')
print(rng)  # 10.0.0.0-10.0.0.100
```

### Создание из начала и конца

```python
from ipaddress import IPv4Address

rng = IPv4Range.from_start_and_end(IPv4Address('10.0.0.1'), IPv4Address('10.0.0.10'))
print(rng)  # 10.0.0.1-10.0.0.10
```

### Создание из списка IP

```python
rngs = IPv4Range.from_ips(
    '10.0.0.1', '10.0.0.2', '10.0.0.3',
    '10.0.0.10', '10.0.0.11'
)
# Результат: [10.0.0.1-10.0.0.3, 10.0.0.10-10.0.0.11]
```

### Создание из сети

```python
rng = IPv4Range.from_network('10.0.0.0/24')
print(rng)  # 10.0.0.0-10.0.0.255
```

### Проверка, является ли диапазон сетью

```python
rng = IPv4Range('10.0.0.0-10.0.0.255')
print(rng.is_network)  # True
```

### Преобразование в `IPv4Network`

```python
rng = IPv4Range('10.0.0.0-10.0.0.255')
net = rng.to_network()
print(net)  # 10.0.0.0/24
```

### Проверка вхождения IP в диапазон

```python
rng = IPv4Range('10.0.0.0-10.0.0.10')
print('10.0.0.5' in rng)  # True
print('10.0.0.20' in rng)  # False
```

### Итерация

```python
rng = IPv4Range('10.0.0.1-10.0.0.3')
for ip in rng:
    print(ip)
# 10.0.0.1
# 10.0.0.2
# 10.0.0.3
```

### Длина диапазона

```python
rng = IPv4Range('10.0.0.0-10.0.0.255')
print(len(rng))  # 256
```

### Сравнение

```python
rng1 = IPv4Range('10.0.0.0-10.0.0.255')
rng2 = IPv4Range.from_network('10.0.0.0/24')
print(rng1 == rng2)  # True
```
