import csv
from config import name_to_department

def row_formater(row):
  formated_row = row[0].split(',')
  return formated_row 

def find_department(name):
  return name_to_department[name]

def is_person_exist(persons, name):
  for person in persons:
    if person[2] == name:
      return True
  return False

def create_new_person(department, position, name):
  return [department, position, name, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def add_record_to_person(persons, name, month, pay, time, money):
  for person in persons:
    if person[2] == name:
      person[month*3+0] = pay
      person[month*3+1] = time
      person[month*3+2] = money

def read_file_and_add_to_record(persons, file_name, month):
  with open(file_name, newline='') as file:
    reader = csv.reader(file, delimiter=' ', quotechar='|')
    for row in reader:
      formated_row = row_formater(row)

      department = find_department(formated_row[1])
      position = formated_row[0]
      name = formated_row[1]
      time = int(formated_row[3])+int(formated_row[4])
      pay = int(formated_row[5])
      money = int(formated_row[6])

      # 0  , 1  ,  2  , 3      ,  4       , 5       , 6       , ...
      # 部門, 職別, 姓名, 時數(1月), 金額(1月), 時數(2月), 金額(2月), ...
      if is_person_exist(out_rows, name) == False:
        out_rows.append(create_new_person(department, position, name))

      add_record_to_person(out_rows, name, month, pay, time, money)

if __name__ == '__main__':
  out_rows = []
  out_file_name = './data/result.csv'
  months = [1, 2, 3, 4, 5, 6, 7, 8]

  for month in months:
    file_name = './data/' + str(month) + '.csv'
    read_file_and_add_to_record(out_rows, file_name, month)

  with open(out_file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    for person in out_rows:
      writer.writerow( person )
