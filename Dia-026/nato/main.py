import pandas

data = pandas.read_csv("nato-alphabet.csv")

nato_dict = {row.Letra: row.Palavra for index, row in data.iterrows()}
print(nato_dict)



while True:
    user_input = input("Enter a word: ").upper()
    try:
        output_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry only letters a-z")
    else:
        print(output_list)
        break


