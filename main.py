from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", encoding='UTF-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
pattern = r'(\+7|8)\s*[\(\s]*(\d{3})[\)\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})\s*\(*(доб.)*\s*(\d+)*\)*'
repl = r'+7(\2)\3-\4-\5\6\7'

new_contacts_list = []
new_contacts_list.append(contacts_list[0])

dict = {}

for item in contacts_list[1:]:
  lst = [item[0], item[1], item[2]]
  fio = ' '.join(lst)
  fio_list = fio.split()

  value = dict.get(fio_list[0],None)
  if value == None:
    new_line = ['','','','','','','']
  else:
    new_line = value

  for i in range(0, len(fio_list)):
    new_line[i] = fio_list[i]
  if item[3] != '':
    new_line[3] = item[3]
  if item[4] != '':
    new_line[4] = item[4]
  if item[5] != '':
    tel = re.sub(pattern, repl, item[5])
    new_line[5] = tel
  if item[6] != '':
    new_line[6] = item[6]
  dict[new_line[0]] = new_line

for value in dict.values(): 
  new_contacts_list.append(value)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='UTF-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(new_contacts_list)