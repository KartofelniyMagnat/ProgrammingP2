import re

with open("raw.txt", "r", encoding="utf-8") as f:
    txt = f.read()


prices = re.findall(r'\d{1,3}(?: \d{3})*,\d{2}', txt)
print("Prices:")
for p in prices:
    print(p)


products = re.findall(r'\d+\.\n(.+?)\n\d+,\d{3}\s+x', txt, re.DOTALL)
print("\nProducts:")
for product in products:
    print(product.strip())


total = re.search(r'ИТОГО:\n(\d{1,3}(?: \d{3})*,\d{2})', txt)
print("\nTotal amount:")
if total:
    print(total.group(1))


date_time = re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2})', txt)
print("\nDate and time:")
if date_time:
    print(date_time.group(1))


payment = re.search(r'(Банковская карта|Наличные)', txt)
print("\nPayment method:")
if payment:
    print(payment.group(1))