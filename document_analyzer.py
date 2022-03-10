data = open("document.txt", "r", encoding="utf8")

data_text = data.read()

split = data_text.split()

test_dict = {}
for i in split:
    if i.lower() not in test_dict:
        test_dict[i.lower()] = 1
    else:
        test_dict[i.lower()] += 1


output = sorted(test_dict.items(), key=lambda x: x[1])
output = sorted(output, key=lambda x: x[0])
output = sorted(output, key=lambda x: x[1], reverse=True)

for i in range(5):
    print(output[i])

data.close()
