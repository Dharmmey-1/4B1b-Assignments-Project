###Find the Top and Least 5 performing agents, find month with the least and most sales
from datetime import datetime as dt

new_file = open("/Users/drizzytom/Documents/PHYTHON/Data_Sci/Rawfile.txt", mode="r", encoding= "utf-8")
# first_line = new_file.readlines()
whole_document = new_file.readlines() #we read the whole documents here
first_five = whole_document[:5] #then read only the first 5 lines that comes in a list

# print(whole_document[:5])

for num in range(len(whole_document)):
  # this for loop strips "\n" from the end of the string
  whole_document[num]= whole_document[num].rstrip("\n")

my_copy = whole_document.copy() #created a copy of the whole document so we have our own copy
# print(my_copy[:5])
# print(len(my_copy))

# ###TO GET THE UNIQUE DATES
##question: how can you know from python that they are multiple dates
unique_dates = []
for record in my_copy:
  date = record.split(" on ")[1]
  if date in unique_dates:
    pass
  else:
    unique_dates.append(date)

# print(len(unique_dates)) ##the len of the date shows that so many dates are recurring as against the len of my_copy list
# print(unique_dates[:5])

unique_sorted_dates = sorted(unique_dates, key = lambda x: dt.strptime(x, "%d-%m-%Y")) ##This line of code sorted our dates
# print(unique_sorted_dates[:5])

sorted_transaction_list = []
for date in unique_sorted_dates:
  # we checked for all the transactions on a unique date
  for transaction in my_copy:
    if date == transaction.split(" on ")[1]:
      sorted_transaction_list.append(transaction)
    else:
      pass

# print(len(sorted_transaction_list))

# with open("/Users/drizzytom/Documents/PHYTHON/Data_Sci/transachub.txt", mode = "w", encoding="utf-8") as my_file:

#   for transac in sorted_transaction_list:
#     my_file.write("{}\n".format(transac))

# my_file.close()

read_transac = open("/Users/drizzytom/Documents/PHYTHON/Data_Sci/transachub.txt", mode = "r", encoding="utf-8")

quick_peek = read_transac.readlines()
# print(quick_peek[:5])

for num in range(len(quick_peek)):
  quick_peek[num] = quick_peek[num].rstrip("\n")

transachub_list = quick_peek.copy()
# print(transachub_list[:5])

import xlwt
from tempfile import TemporaryFile

name_list = []
amount_list = []
date_list = []

for data in transachub_list:
  name_to_append = data.split(" : ")[0]
  name_list.append(name_to_append)

  amount_to_append = data.split(" : ")[1].split(" on ")[0].lstrip("₦")
  amount_list.append(amount_to_append)

  date_to_append = data.split(" on ")[1]
  date_list.append(date_to_append)

book = xlwt.Workbook()
sheet_one = book.add_sheet("All Records")
sheet_two = book.add_sheet("Records by Agents")

# first row for sheet one
sheet_one.write(0, 0, "Name")
sheet_one.write(0, 1, "Sales")
sheet_one.write(0, 2, "Date")

# frist row for sheet two
sheet_two.write(0, 0, "AGENT NAME")
sheet_two.write(0, 1, "SALES BY AGENT")
sheet_two.write(0, 2, "CONTRIBUTION/IMPACT")
sheet_two.write(0, 3, "COMMISSION")
sheet_two.write(0, 4, "TOTAL REVENUE")
sheet_two.write(0, 5, "TOTAL AGENT COMMISSION")
sheet_two.write(0, 6, "NET PROFIT")


for index,item in enumerate(name_list):
  sheet_one.write(index+1, 0, item)

for index, item in enumerate(amount_list):
  sheet_one.write(index+1, 1, item)

for index, item in enumerate(date_list):
  sheet_one.write(index+1, 2, item)

agent_set = set(name_list)

agent_sales_list = []
for name in agent_set:
  individual_sales = 0
  for index, item in enumerate(name_list):
    if name == item:
      individual_sales += int(amount_list[index])
    else:
      pass
  agent_sales_list.append(individual_sales)


# Total Revenue
total_sales = sum(agent_sales_list)

for index, item in enumerate(agent_set):
  sheet_two.write(index+1, 0, item)

for index, item in enumerate(agent_sales_list):
  sheet_two.write(index+1, 1, item)

for index, item in enumerate(agent_sales_list):
  sheet_two.write(index+1, 2, "{0:.2f}%".format((item/total_sales) * 100))

for index, item in enumerate(agent_sales_list):
  sheet_two.write(index+1, 3, "{0:.2f}".format(0.2 * item))

sheet_two.write(1, 4, "₦{}".format(total_sales))
sheet_two.write(1, 5, "₦{0:.2f}".format(total_sales * 0.2))
sheet_two.write(1, 6, "₦{}".format(total_sales - (total_sales * 0.2)))


# name_myfile = "/Users/drizzytom/Documents/PHYTHON/Data_Sci/transachub.xls"
# book.save(name_myfile)
# book.save(TemporaryFile())

## Top 5 performing agents
list_unique_agent = list(agent_set)
list_unique_sales = list(agent_sales_list)

agent_sales = zip(list_unique_sales, list_unique_agent)
agent_sales_list = list(agent_sales)

sort_agent_sales = sorted(agent_sales_list)
# print(sort_agent_sales)
top_5_agent = sorted(sort_agent_sales[-5 : ], reverse = True)
print("Here's the top performing agents for 2020")
for agent in top_5_agent:
  print(agent[1].title())
print("\n")

# Least Performing agent
print("Here's the least performing agent for 2020")
low_5_agent = sort_agent_sales[0][1]
print(low_5_agent.title())
print("\n")

year_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
month_sales_list = []
for date in year_list:
  # sum all the sales for each month of the year
  month_sales = 0
  for index, transaction in enumerate(transachub_list):
    if date == transaction.split(" on ")[1].split("-")[1]:
      month_sales += int(amount_list[index])
    else:
      pass
  month_sales_list.append(month_sales)
print("Below is the total sales made in each month starting from January to November respectively")
print(month_sales_list)
print("\n")

highest_sales_month = max(month_sales_list)
print(f"The month of September had the highest sales with a total of ₦{highest_sales_month}")
print("\n")

lowest_sale_month = min(month_sales_list)
print(f"The month of November had the lowest sales with a total of ₦{lowest_sale_month} ") 
