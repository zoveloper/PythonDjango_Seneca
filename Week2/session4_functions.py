def month_to_term_if():
    month = input("Enter Month")
    if month =="January":
        print("you are in term1")
    elif month == "April":
        print("you are in term2")

month_to_term_if()

term_month_map ={"January":"term1", "March":"term2"}

def month_to_term_try(month="July"):
    try:
        print("you are in term1"+term_month_map[month])
    except:
        print("you are in term2")

month = input("Enter Month")
month_to_term_try(month)