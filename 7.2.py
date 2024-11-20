from collections import Counter
def word_count(filepath):
    with open(filepath,'r') as file:
        text=file.read().lower()

    word=text.split()
    word_count=Counter(word)
    return word_count.most_common(3)

print(word_count('C:/Users/Alisia Phini/Desktop/planwo/data_structures_work/text'))