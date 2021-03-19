read_transac = open("C:/Users/DEMILADE SOMIDE/Data Science/transacub.txt", mode = "r", encoding = "utf-8")
quick_peek = read_transac.readlines()
for num in range(len(quick_peek)):
    quick_peek[num] = quick_peek[num].rstrip("\n")

transachub_list = quick_peek.copy()

names_list = []
amount_list = []
date_list = []

for data in transachub_list:
    name_to_append = data.split(" :")[0]
    names_list.append(name_to_append)

    amount_to_append = data.split(" : ")[1].split(" on ")[0].lstrip("₦")
    amount_list.append(amount_to_append)


    date_to_append = data.split(" on ")[1]
    date_list.append(date_to_append)

agent_set = set(names_list)
agent_set_sales_list = []

for name in agent_set:
    individual_sales = 0
    for index, item in enumerate(names_list):
        if name == item:
            individual_sales += int(amount_list[index])
        else:
            pass 
    agent_set_sales_list.append(individual_sales)       

total_sales = sum(agent_set_sales_list)

# Top 5 peforming agents
sorted_agent_set_sales_list = sorted(agent_set_sales_list, reverse = True)
top_5performers_sales_list = list(sorted_agent_set_sales_list[:5])
top_performers_name = []


for sales in top_5performers_sales_list:
    for names, items in zip(agent_set, agent_set_sales_list):
        if sales == items:
            top_performers_name.append(names)
        else:
            pass    
            

## METHOD  TWO
def solution_2():
    for sales in top_5performers_sales_list:
        for index, items in enumerate(agent_set_sales_list):
            if sales == items:
                name_position = index   
                for index2, name in enumerate(agent_set):
                    if name_position == index2:
                        top_performers_name.append(name)
                    else:
                        pass    
            else:
                pass 
    return top_performers_name      



## MONTH WITH THE HIGHEST AND LOWEST SALES 
month_list = ["Jan", "Feb", "Mar" , "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov"]
month_total_sales = []

for num in month_list:
    month_sales = 0
    for months in transachub_list:
        date_position = months.split(" on ")[1]
        converted_date = dt.strptime(date_position, "%d-%m-%Y")
        if converted_date.strftime("%b-%Y") == num +"-"+"2020":
            amount = months.split(" : ")[1].split(" on ")[0].lstrip("₦")
            month_sales += int(amount)
        else:
            pass  
    month_total_sales.append(month_sales)  

print(month_total_sales)

max_month_sale = str(max(month_total_sales))
min_month_sale = str(min(month_total_sales))
for index, month in enumerate(month_total_sales):
    month = str(month) 
    if max_month_sale == month:
        highest_month = dt.strptime(month_list[index], "%b")
        full_month1 = highest_month.strftime("%B")
        print(f"The highest sales month is {full_month1}")
    elif min_month_sale == month:
        lowest_month = dt.strptime(month_list[index], "%b")
        full_month2 = lowest_month.strftime("%B")
        print(f"The lowest sales month is {full_month2}")


# LEAST PERFORMING AGENT
sorted_agent_set_sales_list_2 = sorted(agent_set_sales_list)
least_agent_total_sale = list(sorted_agent_set_sales_list_2[:1])
least_agent = []
for sales in least_agent_total_sale:
     for names, items in list(zip(agent_set, agent_set_sales_list)):
        if sales == items:
            least_agent.append(names)
        else:
            pass    

## METHOD  TWO
def solution_3():
    for sales in top_5performers_sales_list:
        for index, items in enumerate(agent_set_sales_list):
            if sales == items:
                name_position = index
                for index2, name in enumerate(agent_set):
                    if name_position == index2:
                        least_agent.append(name)
                    else:
                        pass    



#NUMBER OF SALES DATE
number_of_date = len(unique_sorted_dates)



