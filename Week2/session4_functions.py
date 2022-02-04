def month_to_term_if(month):
    if month == "January":
        print("You are in term 1")
    elif month == "May":
        print("You are in term 2")
    elif month == "September":
        print("You are in term 3")
    else:
        print("You are in month where no term begins")

month = input("Enter Month")
month_to_term_if(month)

term_month_map = {"January":"Term1", "May": "Term2", "September":"Term3"}

def month_to_term_try(month = "dnsAn"):
    try:
        print("You are in "+term_month_map[month])
    except:
        print("You are in month " + month + " where no term begins")

month = input("Enter Month")
month_to_term_try(month)
month_to_term_try()

def month_to_term_dict(month):
    return("You are in "+term_month_map.get(month,"month where no term begins"))

month = input("Enter Month")
print(month_to_term_dict(month))


def gate_entry(batch_id):
    if batch_id == "good":
        print("You are allowed inside the gate")
    else:
        print("Wait till you have good batch_id")
        gate_entry(input("Is his batch id good?"))

gate_entry(input("Is his batch id good?"))

# Implement Factorial logic