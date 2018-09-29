# PyGetMegabytes
Get megabytes from your string.

## Examples:

Строка: 'Тариф все за 100: 15 гб в месяц!'
Вернет: 15360 (мегабайт)

Строка: 'Тариф все за 500: 13223 кб в месяц'
Вернет: 12.91 (мегабайт)

Строка: 'Тариф все за 100: 15,1 гб в день'        
Вернет: 15462.4 (мегабайт)


То есть данный небольшой класс парсит строку и определяет комбинацию гб/кб/мб (также и на английском), регуляркой получает число (при этом, число может иметь точку или запятую в качестве разделителя (например, 15,1 гб или 13.1 гб) и в зависимости от того, какой тип (гб/кб/мб) производит операцию, округления, возвращает строку.
