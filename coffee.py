space = " "
coffee_choice = raw_input("Hi, what would you like? A/An ")

#Add some choices in all coffee
all_coffee = ["latte", "espresso", "machiato", "decaff"]

def customer_talk1(a):
    
    if type(a) == str and (a.lower() == all_coffee[0] or a.lower() == all_coffee[1] or a.lower() == all_coffee[2] or a.lower() == all_coffee[3] or a.lower() == all_coffee[4]):
        casual_text = "\nGreat! Our %s is definetly a very good choice, "
        return casual_text %(a.lower())
    else: return 'We don t know what do you mean'


def coffee_info(a):
    casual_text2 = "especially the %s."
    coffee_beans = ["Arabica beans", "Robustas beans" ]
    ingredients = ["Shots", "Whipped Cream"]
    milks = ["Semi-Skimmed"]
    technique = ["steamed"]
    sugars = []

    info_text = space + "with" + space

    if a.lower() == "latte":
        all_latte = ["Caffe Latte", "Flat White", "Eggnog", "Gingerbread"]
        latte_choice = raw_input (" A Caffe Latte, a flat white, an eggnog or gingerbread? A/An ",)
        base = "80% " + coffee_beans[0] + " and 20% " + coffee_beans[1]
        
        if latte_choice.lower() == "caffe latte" or latte_choice.lower() == "caffe":
            return casual_text2 %(all_latte[0]) + "\nIngredients: \n" + base + info_text + ingredients[0] + ", " + ingredients[1] + " and "+ technique[0]
        
        elif latte_choice.lower() == "flat white" or latte_choice.lower() == "white" or latte_choice.lower() == "flat":
            return casual_text2 %(all_latte[1]) + "\nIngredients: \n" + base + "\n"
        
        elif latte_choice.lower() == "eggnog" or espresso_choice.lower() == "eggnog latte":
            return casual_text2 %(all_latte[2]) + "\nIngredients: \n" + base + "\n"
        
        elif latte_choice.lower() == "gingerbread" or espresso_choice.lower() == "gingerbread latte":
            return casual_text2 %(all_latte[3]) + "\nIngredients: \n" + base + "\n"
        
  
    
    elif a.lower() == "espresso":
        all_espresso = ["Single Espresso", "Espresso Con Pana", "Espresso Machiato", "Cortado"]
        espresso_choice = raw_input ("A single, a Con Pana, a Machiato or a Cortado? A/An ")
        base = "100% " + coffee_beans[0]

        if espresso_choice.lower() == "single espresso" or espresso_choice.lower() == "single":
            return casual_text2 %(all_espresso[0]) + "\nIngredients: \n" + base + "\n"

        elif espresso_choice.lower() == "espresso con pana" or espresso_choice.lower() == "con pana":
            return casual_text2 %(all_espresso[1]) + "\nIngredients: \n" + base + info_text + ingredients[0] + " and "+ ingredients[1] + "\n"

        elif espresso_choice.lower() == "espresso machiato" or espresso_choice.lower() == "machiato":
            return casual_text2 %(all_espresso[2]) + "\nIngredients: \n" + base + info_text + ingredients[0] + " and " + milks[0] + " milk \n"

        elif espresso_choice.lower() == "espresso cortado" or espresso_choice.lower() == "cortado":
            return casual_text2 %(all_espresso[3]) + "\nIngredients: \n" + base + info_text + ingredients[0] + "\n"

        else: return "Sorry we don't understand what you would like."

    elif a.lower() == "espresso":
        info_coffee += "water"
        return info_coffee

    elif a.lower() == "espresso":
        info_coffee += "water"
        return info_coffee

    else: return"\nBUG"

def whole_order(a, b):
    if type(a + b) == int:
        total = customer_talk1(coffee_choice) + coffee_info(coffee_choice)
        return total
        
    else: return "BUG"
    
#print customer_talk1(coffee_choice)
#print coffee_info(coffee_choice)
 
print whole_order(6, 8)
