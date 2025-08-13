
def display_info(name,age,address,contact,email):
    """ This function displays personal information in a formatted manner."""gi
    personal_info_dict={"Name": name, "Age": age, "Address": address, "Contact": contact, "Email": email}
    for key, value in personal_info_dict.items():
        print(f"{key}:{value}")
display_info("Jeshmin",20,"Tinkune","9861786228","shresthajeshmin30@gmail.com")