import markovify

with open("cala_biblia", "r") as f:
    text = f.read()

text_model = markovify.Text(text, state_size=3)

for i in range(5):
    print(text_model.make_sentence(min_words=10, tries=10000))
