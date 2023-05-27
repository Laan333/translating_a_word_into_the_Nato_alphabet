import pandas
user_word = list(input("Write a word: ").upper())
data_nato_alph = pandas.read_csv("nato_phonetic_alphabet.csv")
# for key,value in data_nato_alph.iterrows():
#     print(value)

my_dict_alph = {value.letter:value.code for key,value in data_nato_alph.iterrows()}
new_nato_word = [my_dict_alph[word] for word in user_word]
print(new_nato_word)
