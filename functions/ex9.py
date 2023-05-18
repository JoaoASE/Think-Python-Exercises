#exercicio de uso de função com laço while

def get_formated_names(first_name, last_name):
    full_name = first_name + ' '+last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name(press 'q' to leave): ")

    f_name=input("First name:  ") 
    if f_name == 'q':
        break
    l_name = input("Last name:  ")
    if l_name == 'q':
        break
    formated_names = get_formated_names(f_name,l_name)
    print("Hello "+formated_names)