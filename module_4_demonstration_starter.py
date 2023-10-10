"""
Description: This program will provide salary increases of 20% to all 
executives at PiXELL-River Financial.  Prior to implementing this change, 
the program will see how many executives will end up with salaries greater than 
the high-salary mark.
Author: ACE Faculty
Edited by: Rence Mayores
Date: 10/10/2023
Usage: 
"""
data = []
new_data = []

HIGH_SALARY = 120000
RECOMMENDED_INCREASE = 0.20

file = None

#LECTURE SECTION 1
# try and if there is a problem then catch the error
try:
      file = open('module_4_dat.txt')
      data = file.readlines()

      1 / 0

except FileNotFoundError as e: #Exceptions are ordered from most specific to general
      print("Error opening file: ", e)
except Exception as e:
      print("General Exception: ", e)
finally:
      if file is not None:
            file.close()
            print("File Closed")


#LECTURE SECTION 2
# CEO/Chair of Board, Jo-Anne Sinclair, 140000
# We wouldn't need to use raise in the assignment
try:
      if len(data) == 0:
            raise Exception("No data exists.")
      else:      
            for record in data:
                  items = record.split(',')
                  title = items[0]
                  name = items[1]
                  salary = float(items[2])
                  
                  #LECTURE SECTION 3
                  #REQUIREMENT:  NOTE RECORDS THAT EXCEED OR WILL EXCEED HIGH_SALARY AMOUNT
                  salary *= (1 - RECOMMENDED_INCREASE)
                  new_data.append([title,name,salary])
except Exception as e:
      print(e)



#LECTURE SECTION 4
try:
      file = open('updated_salaries.txt', 'w')
      for record in new_data:
            row = ""
            for index, item in enumerate(record):
                  row += str(item)
                  if index < len(record) - 1:
                        row += (",")
            row += '\n'
            file.write(row)
except Exception as e:
      print(e)

#LECTURE SECTION 5
print("End of Program")

