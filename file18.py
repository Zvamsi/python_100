def format_name(f_name,l_name):
    if f_name=='' or l_name=='':
        return "parameter is missing"
    formatted_f_name=f_name.title()
    formatted_l_name=l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name(input("Enter your first name\n"),input("Enter your last name\n")))