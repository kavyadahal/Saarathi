prices = [120,80,200,50,300]
print("Total:",sum(prices))
print("Cheapest:",min(prices))
print("Dearest:",max(prices))

#Append one or more, then recount
prices.append(150)
print("Count:",len(prices))
print("Average:",sum(prices)/len(prices))

#Stretch : only abv 100

print("Above 100:")
for p in prices:
    if p>100:
        print(p)

        