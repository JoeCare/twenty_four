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

for word in words_list:
    word_strip = word.replace("<", "").replace(">", "")
    story = story.replace(word, attributes_dict[word_strip])

print(story)


