sentence = "ai is ai and ml is ml and ai is fun"
words = sentence.split()
##['ai', 'is', 'ai', 'and', 'ml', 'is', 'ml', 'and', 'ai', 'is', 'fun']

counts = {}
for word in words:
    counts[word] = counts.get(word,0)+1
#counts : {'ai': 3, 'is': 3, 'and': 2, 'ml': 2, 'fun': 1}

for word, n in counts.items():
    print(word, "->", n)

