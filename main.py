from math import radians
from tkinter import *
from tkcalendar import DateEntry

main_window = Tk()
main_window.title('Flight Reservation App')

main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)

name_label = Label(main_window, text="Name:")
name_label.grid(column=0, row=1)
name_label_field = Entry()
name_label_field.grid(column=1, row=1)

radio_button_var = IntVar()

gender_label = Label(main_window, text="Gender")
gender_label.grid(column=0, row=2)

radio_button_male = Radiobutton(main_window, 
               text="Male",
               padx = 20, 
               variable=radio_button_var, 
               value=1)

radio_button_female = Radiobutton(main_window, 
               text="Female",
               padx = 20, 
               variable=radio_button_var, 
               value=2)
radio_button_male.grid(column=0, row=3)
radio_button_female.grid(column=1, row=3)

flight_options_label = Label(main_window, text="Options")
flight_options_label.grid(column=0, row=4)


# Flight Options
first_class_var = IntVar()
first_class_check_button = Checkbutton(main_window, text="First Class", variable=first_class_var)
first_class_check_button.grid(column=1, row=5, sticky=W)
meal_var = IntVar()
meal_check_button = Checkbutton(main_window, text="Meal", variable=meal_var)
meal_check_button.grid(column=1, row=6, sticky=W)

luggage_weight_label = Label(main_window, text="Luggage Weight")
luggage_weight_label.grid(column=0, row=7)

# Luggage Weight (kg)
luggage_weight_scale = Scale(main_window, from_=0, to=200, orient=HORIZONTAL)
luggage_weight_scale.grid(column=0, row=8, columnspan = 2, sticky = W+E)

# Option Menu Widget - Departure and Arrival Destinations
destination_menu_label = Label(main_window, text="Destination")
destination_menu_label.grid(column=0, row=9)

# Create the list of options
destination_list = ["Moscow", "Pyongyang", "Damascus", "Caracas"]
  
# Variable to keep track of the option
# selected in OptionMenu
destination_value = StringVar(main_window)
# Set the default value of the variable
destination_value.set("Select a Destination")
  
# Create the optionmenu widget and passing 
# the options_list and value_inside to it.
destination_menu = OptionMenu(main_window, destination_value, *destination_list)
destination_menu.grid(column=0, row=10, columnspan = 2, sticky = W+E)

departure_date_label = Label(main_window, text="Departure Date")
departure_date_label.grid(column=0, row=11)
    
# Datepicker Widget for Date of Flight
# https://www.geeksforgeeks.org/create-a-date-picker-calendar-tkinter/
departure_date_input=DateEntry(main_window,selectmode='day', date_pattern="yyyy-mm-dd", width=10)
departure_date_input.grid(column=0, row=12)
# Fix for calendar not showing up
departure_date_input._top_cal.overrideredirect(False)

additional_comments_label = Label(main_window, text="Additional Comments")
additional_comments_label.grid(column=0, row=13)

# Additional Notes
additional_comments_field = Text(main_window, height=4, width=50, relief=GROOVE, borderwidth=2)
additional_comments_field.grid(column=0, row=16, columnspan = 2, rowspan=3, sticky = W+E)

def get_flight_input_data():
    print(name_label_field.get())
    if radio_button_var.get() == 0:
        print("Male")
    elif radio_button_var.get() == 1:
        print("Female")
    if first_class_var.get() == 1:
        print("First Class")
    else:
        print("No First Class")
    if meal_var.get() == 1:
        print("Meal")
    else:
        print("No Meal")
    print(destination_value.get())
    print(luggage_weight_scale.get())
    print(departure_date_input.get_date())
    print(additional_comments_field.get("1.0","end"))


submit_button = Button(main_window, text="Submit", command=get_flight_input_data)
submit_button.grid(column=0, row=20)

# Submit Button
# Popup with Information

main_window.mainloop()
