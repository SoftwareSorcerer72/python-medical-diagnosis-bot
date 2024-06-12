welcome_prompt = "Welcome doctor, what would you like to do today?\n - To list all patients, press 1\n - To run a new diagnosis, press 2\n - To quit, press q\n"

def list_patients():
    print("Listing patients and diagnoses")

def start_new_diagnosis():
    print("Starting anew diagnosis")



def main():
    selection = input(welcome_prompt)
    while selection != "q":
        if selection =="1":
            list_patients()
            return main()
        elif selection == "2":
            start_new_diagnosis()
            return main()        
        elif selection == "q":
            return
       

main()