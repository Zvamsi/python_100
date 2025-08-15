import pandas

# {"A": "Alfa", "B": "Bravo"}

data=pandas.read_csv('nato_phonetic_alphabet.csv')
# print(data)
dict_data={row.letter:row.code for (index,row) in data.iterrows()}
print(dict_data)

def generate_phenatic():
    user_input=input("Enter a word: ").upper()
    try:
        result=[dict_data[item] for item in user_input]
    except KeyError:
        print("only alphabets are allowed")
        generate_phenatic()
    else:
        print(result)
generate_phenatic()