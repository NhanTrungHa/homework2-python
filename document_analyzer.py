from collections import Counter

data = open("document.txt", "r", encoding="utf8")

data_text = data.read()

split = data_text.split()


#Counter = Counter(split)

#occurrences = Counter.most_common(5)

#output = list(occurrences)

for i in output:
    print(i)

data.close()