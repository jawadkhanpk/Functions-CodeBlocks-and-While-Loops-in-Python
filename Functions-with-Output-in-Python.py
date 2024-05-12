# Functions with Outputs
def format_name(f_name, l_name):
    # .title() function in python is used to convert string into a Title Case
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


title_case = format_name("jawaD", "KhAN")
print(title_case)
