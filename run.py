import pycrib


deck = pycrib.Deck()
hand = deck.draw()[:4]
turnup = deck.remaining(hand).draw(1)[0]

result = pycrib.hand_value(hand, turnup)

print(hand, turnup)
print(result[1])
