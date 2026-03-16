import pandas

data = pandas.read_csv("nato-alphabet.csv")

nato_dict = {row.Letra: row.Palavra for index, row in data.iterrows()}
print(nato_dict)

user_input = input("Enter a word: ").upper()

output_list = [nato_dict[letter] for letter in user_input]
print(output_list)