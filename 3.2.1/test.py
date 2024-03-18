sandwich_type = ""
subtotal = 0.0
order = ["", "", "", 0]
sandwich_index = 0
beverage_index = 1
fries_index = 2
ketchup_index = 3

# Explaining Menu Options
print("What type of sandwich would you like?")
print("chicken $5.25, beef $6.25, tofu $5.75")
sandwich_type = input("Sandwich Choice: ")
order.insert(sandwich_index, sandwich_type)

# Calculating Sandwich Price
if sandwich_type == "chicken":
    print("You chose chicken, which will be $5.25")
    subtotal += 5.25
elif sandwich_type == "tofu":
    print("You chose tofu, which will be $5.75")
    subtotal += 5.75
else:
    print("You chose beef, which will be $6.25")
    subtotal += 6.25

# Beverage Choice
bev_choice = input("Do you want a beverage? yes or no")
if bev_choice == "yes":
    bev_size = input("What size beverage would you like? Small, Medium, or Large")
    order.append("Beverage " + bev_size)
    if bev_size == "small":
        print("You chose small, so $1.00")
        subtotal += 1
    if bev_size == "medium":
        print("You chose medium, so $1.75")
        subtotal += 1.75
    if bev_size == "large":
        print("You chose large, so $2.25")
        subtotal += 2.25

# Fries
fry_choice = input("Do you want french fries? Yes or No")
if fry_choice == "yes":
    fry_size = input("What size fries would you like? Small, Medium, or Large")
    if fry_size == "small":
        supersize = input("Do you want to supersize that for $2? Yes or no")
        if supersize == "yes":
            fry_size = "large"
            order.append("Large fries")
            subtotal += 2
        else:
            print("You chose small fries for $1")
            order.append("Small fries")
            subtotal += 1
    elif fry_size == "medium":
        print("You chose medium for $1.50")
        order.append("Medium fries")
        subtotal += 1.50
    else:
        print("You chose large fries for $2")
        order.append("Large fries")
        subtotal += 2

# Kethcup
ketchup = float(input("How many ketchup packets would you like? $0.25 each"))
order.append(ketchup)
if ketchup >= 0:
    subtotal += ketchup * .25

if bev_choice == "yes" and fry_choice == "yes":
    subtotal -= 1

print(sandwich_type)
if bev_choice == "yes":
    print(bev_size)
if fry_choice == "yes":
    print(fry_size)

print(subtotal)