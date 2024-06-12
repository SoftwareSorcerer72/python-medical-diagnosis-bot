welcome_prompt = """Welcome doctor, what would you like to do today?\n
- To list all patients, press 1\n
- To run a new diagnosis, press 2\n
- To quit, press q\n"""

name_prompt = "What is the patient's name?\n"
appearance_prompt = "How is the patient's general appearance?\n - 1: Normal appearance\n - 2: Irritable or lethargic\n"
eye_prompt = "How are the patient's eyes?\n - 1: Eyes normal or slightly sunken\n - 2: Eyes very sunken\n"
skin_prompt = "How is the patient's skin when you pinch it?\n - 1: Normal skin pinch\n - 2: Slow skin pinch\n"

severe_dehydration = "Severe dehydration"
some_dehydration = "Some dehydration"
no_dehydration = "No dehydration"





def list_patients():
    print("Listing patients and diagnoses")

# Try calling the 2 functions below according to the appearance_prompt input!
def assess_skin(skin):
    if skin == "1":
        return no_dehydration
    elif skin == "2":
        return severe_dehydration
    

def assess_eyes(eyes):
    if eyes == "1":
        return no_dehydration
    elif eyes == "2":
        return severe_dehydration

def assess_appearance():
    appearance = input(appearance_prompt)
    if appearance == "1":
        eyes = input(eye_prompt)
        return assess_eyes(eyes)
    elif appearance == "2":
        skin = input(skin_prompt)
        return assess_skin(skin)
   


def start_new_diagnosis():
    # Asks user to enter the patient's name
    name = input(name_prompt)
    # Asks user to enter how the general appearance of the patient is
    diagnosis = assess_appearance()
    print(name,diagnosis)

def main():
    # Executes the code within the while loop until user presses 'q'
    while(True):
        selection = input(welcome_prompt)
        if selection == "1":
            list_patients()
        elif selection == "2":
            start_new_diagnosis()
        elif selection == "q":
            # Exits the program
            return

main()