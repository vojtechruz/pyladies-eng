items = []
for number in range(10):
    items.append(number)

print(items)

deck = []
colors = ['♠', '♥', '♦', '♣']
values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
for color in colors:
    for value in values:
        deck.append(value + color)

print(deck)
