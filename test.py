

from typing import Final

tea_price_per_bag: Final = 0.45
tea_bags_per_box: Final = 20
coffee_price_per_kg: Final = 18.5
required_tea_boxes_for_discount:Final = 10
required_coffee_quantity_for_discount: Final = 25


print('''---------------------------------------------
*** Welcome to Beverage Wholesale  Programn ***
---------------------------------------------
      ''')

user_product = input('''Please select the type of purchase:
C: Coffee Beans
T: Tea Boxes
>>> ''').upper()
if user_product == "T":
    tea_boxes = int(input("Enter the number boxes of tea: "))
    if tea_boxes <= 0:
        print("Number of tea boxes should be > 0")
    else:
        tea_price = tea_price_per_bag * tea_boxes * tea_bags_per_box
        tea_discount_amount = 0
        if tea_boxes > required_tea_boxes_for_discount:
            discount = 0.15
            tea_discount_amount = tea_price * discount
        user_province = input("Please enter the 2-letter province abbreviation: ").upper
        if user_province == "AB":
            gst = 0.05
        elif user_province == "ON":
            gst = 0.13
        else:
            gst = 0.15
        gst_amount = gst * (tea_price - tea_discount_amount)
    
        total_price = tea_price - tea_discount_amount + gst_amount
    
        print(f'''--------------------------------------------------------------------------------------------------------------------
Product         Qty(Bags/kg)        Price before disc       GST         Total Price
  Tea              {tea_boxes}                  {tea_price:.2f}               {gst_amount:.2f}          {total_price:.2f}
--------------------------------------------------------------------------------------------------------------------
Thanks for your business, Good Bye''')
elif user_product =="C":
     coffee_weight = int(input("Enter the number kilograms (kg) of coffee: "))
     if coffee_weight <= 0:
        print("Quantity of coffee should be > 0")
     else:
        coffee_price = coffee_price_per_kg * coffee_weight
        coffee_discount_amount = 0
        if  coffee_weight > 25:
            discount = 0.1
            coffee_discount_amount = coffee_price * discount
        
        coffee_price_after_discount = coffee_price - coffee_discount_amount
        user_province = input("Please enter the 2-letter province abbreviation: ").upper()
        if user_province == "AB":
            gst = 0.05
        elif user_province == "ON":
            gst = 0.13
        else:
            gst = 0.15
        gst_amount = gst * coffee_price_after_discount
    
        total_price = coffee_price - coffee_discount_amount + gst_amount
        print(f'''--------------------------------------------------------------------------------------------------------------------
Product         Qty(Bags/kg)        Price before disc      Price after disc                 GST         Total Price
 Coffee           {coffee_weight:.2f}              {coffee_price:.2f}                   {coffee_price_after_discount:.2f}                        {gst_amount:.2f}           {total_price:.2f}
--------------------------------------------------------------------------------------------------------------------
Thanks for your business, Good Bye''')
else:
    print("Invalid input, you should enter c/C or t/T")
