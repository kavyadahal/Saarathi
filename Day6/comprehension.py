
#1 Even number 1-20

even = [n for n in range(1,21) if n%2==0]
print(even)

#Length of each words:
words = ["ai","ml","rag","llm"]
lengths = [len(w) for w in words]
print(lengths)

#Dict:words->length
word_length = {w:len(w) for w in words}
print(word_length)

#Same as 1 but as a normal loop

even_loop = []
for i in range(1,21):
    if i%2 == 0:
        even_loop.append(i)
print(even_loop==even)

#Stretch : Unique word length from a sentence :
sentence  = "ai and ml power modern data tools"
unique_length = {len(w) for w in sentence.split()}
print(unique_length)