from dataclasses import dataclass, asdict

with open("story.txt", "r") as f:
    story = f.read()

words_list = set()
start_of_words_list = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_words = i

    if char == target_end and start_of_words != -1:
        word = story[start_of_words: i + 1]
        words_list.add(word)
        start_of_words = -1

answers = {}

@dataclass
class Words:
    emotion: str = "sadness"
    emotion2: str = "joy"
    weather_condition: str = "cloudy"
    animal: str = "turtle"
    adverb: str = "gently"
    adjective1: str = "violet"
    character: str = "Joe"
    terrain: str = "forest"
    place: str = "top of the mountain"
    place2: str = "other place"
    object: str = "plate"

w = Words()
attributes_dict = asdict(w)
print(attributes_dict)
# word_dressed = [attributes_dict[f"<{attr}>"] = value for attr, value in attributes_dict.items()]

def insert_bracket(source_string: str):
    return f"<{source_string}>"

zipped = list(zip(map(insert_bracket, attributes_dict.keys()), attributes_dict.values()))
print(zipped)

answers = ["<" + sublist[0] + ">" for sublist in zipped]
print("ans", answers)
print(attributes_dict)
# compr = [sub_zipped[0]. for sub_zipped in zipped for item in sub_zipped]
attributes = [dict(sublist) for sublist in zipped]
print(attributes)

for word in words_list:
    # word_strip = word.replace("<", "").replace(">", "")
    story = story.replace(word, attributes_dict[word])
    print(story)

print(story)


