# long sentence

# count vowels and consonants in the string
# count the number of upper-case letters
# remove the spaces without string methods

sentence = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam mollitia eos accusamus dolor adipisci eligendi ducimus animi quibusdam eveniet voluptates illum, nihil fugit fuga quia asperiores accusantium in quod modi. Lorem ipsum dolor sit amet consectetur adipisicing elit. Ex quibusdam illo ea consequatur tenetur odio sit aliquid officiis vero doloremque asperiores, dolorum, facilis quo molestias temporibus accusantium quis reprehenderit et?"

vowels_count = 0
consonants_count = 0

upper_case_count = 0
lower_case_count = 0

for character in sentence:

    if character in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ':
        continue

    if character.isupper():
        upper_case_count += 1
    else:
        lower_case_count += 1
    
    if character.lower() in ("a", "e", "i","o","u"):
        vowels_count += 1
    else:
        consonants_count += 1




print(vowels_count)
print(consonants_count)
print(upper_case_count)
print(lower_case_count)


sentence_without_space = ""

for character in sentence:
    if character != " ":
        sentence_without_space += character

print(sentence_without_space)

print(sentence.replace(" ", "") == sentence_without_space)