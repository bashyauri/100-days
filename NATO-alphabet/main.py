import os
import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


{"A": "Alfa", "B": "Bravo"}
path = os.getcwd()
df = pandas.read_csv(os.path.join(
    path, "NATO-alphabet", "nato_phonetic_alphabet.csv"))

new_dict = {rows.letter: rows.code for (index, rows) in df.iterrows()}


print(new_dict)
ask = True
while ask:
    word = input("Enter a word: ")
    try:
        word_list = [new_dict[x.upper()] for x in word]
    except KeyError:
        print("Sorry, only letters in the alphabets please")
    else:
        print(word_list)
        ask = False
