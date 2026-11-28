from pyscript import document, display
#NO AI WAS USED FOR GENERATING CODE
listed_elements = {
        "H":("Hydrogen", 1, 1.008),
        "C":("Carbon", 6, 12.011),
        "N":("Nitrogen", 7, 14.007),
        "O":("Oxygen", 8, 15.999),
        "P":("Phosphorus", 15, 30.974),
        "S":("Sulfur", 16, 32.065),
        "Se":("Selenium", 34, 78.960),
        "Cl":("Chlorine", 17, 35.453),
        "F":("Flourine", 9, 18.998),
        "Br":("Bromine", 35, 79.904),
        "I":("Iodine", 1, 1.008),
        "Rn":("Radon", 86, 222),
        "He":("Helium", 2, 4.0026),
        "Ne":("Neon", 10, 20.180),
        "Ar":("Argon", 18, 39.948),
        "Kr":("Krypton", 36, 83.798),
        "Xe":("Xenon", 54, 131.29)
    }

def check_element (e):
    document.getElementById("output1").innerHTML = ""
    element = document.getElementById("atom").value
    element = element.title()
    
    #var2 = dict.get(element,("Element not found","-","-"))
    #document.getElementById("").innerHTML = f""" """"

    verify = listed_elements.get(element, ("-Element not found-","-","-"))
    document.getElementById("output1").innerHTML = f"""
     Symbol: {element} <br>
     Element: {verify[0]} <br>
     Atomic Number: {verify[1]} <br>
     Atomic Mass: {verify[2]} 
    """

#Random generated names by using this website: https://www.fantasynamegenerators.com/filipino-names.php
def add_brand (e):
    document.getElementById('output1').innerHTML = ""
    grade_seven = {'Glenn Alcantara', 'Arthur Fernandez', 'Meagan Escano'}
    grade_eight = {'Raina Agcaoili', 'Immanuel Arce', 'Jerald Aguilar', 'Kassidy Santos'}
    grade_nine = {'Michelle Acosta', 'Aimee Catubig', 'Inez Estillore'}
    grade_ten = {'Hayden Alonzo', 'Reid Cunanan', 'Tyra Garcia'}
    
    #retrieving values from user's input by ID name
    name_one = document.getElementById('firstname').value
    name_two = document.getElementById('lastname').value

    new_Student = name_one + " " + name_two #concantenates the two inputs with proper spacing
    #assign the value to a set variable
    new_brand_set = {new_Student.title()} #assigning the full name variable as a set datatype, accompanied with proper capitalization

    all_names = grade_seven | grade_eight | grade_nine | grade_ten | new_brand_set #joins all names with the use of the union operator
    total_members = len(grade_seven | grade_eight | grade_nine | grade_ten | new_brand_set) #gets the total length of every item available in each set
    name_list = "<br>".join(sorted(all_names)) #sorts all names alphabetically, including the user's name

    #displays using f string
    document.getElementById('output1').innerHTML = f'<br><h1><b>List of Club Members:</b></h1> <br> {name_list}'
    display(f'Number of Members: {total_members}',target="output1")

def checkname(e):
    name_list1 = ['Raina Agcaoili', 'Immanuel Arce', 'Jerald Aguilar', 'Kassidy Santos', 'Glenn Alcantara', 'Arthur Fernandez', 'Meagan Escano', 'Michelle Acosta', 'Aimee Catubig', 'Inez Estillore', 'Hayden Alonzo', 'Reid Cunanan', 'Tyra Garcia']
    firstname = document.getElementById("firstname").value
    lastname = document.getElementById("lastname").value
    fullname = (f'{firstname} {lastname}')
    con_name = fullname.lower() #coverts fullname variable into lowercase in order to confirm if the user's input is listed; acts as a decoy variable so that the user's original input will still be displayed
    confirm_name = con_name in name_list1 

    message = (f'Sorry {fullname}, your name is not found on the list.', f'Congrats {fullname}! You are now part of the Social Sciences Club.')
    document.getElementById("output1").innerHTML = message[confirm_name]