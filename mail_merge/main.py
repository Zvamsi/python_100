with open('Input/Names/invited_names.txt') as name_file:
    names_list=name_file.readlines()

with open('Input/Letters/starting_letters.txt') as content_file:
    template=content_file.read()
for name in names_list:

    name=name.strip('\n')
    content=template.replace('[name]',name)


    with open(f'Output/Ready_to_send/{name}_send.txt',mode='w') as write_file:
        write_file.write(content)