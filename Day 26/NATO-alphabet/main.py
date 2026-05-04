import pandas

#open file
data = pandas.read_csv("nato_phonetic_alphabet.csv")
#create a dictionary using data in file in format code:word
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#create list of phonetic code words from a word user inputs
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)