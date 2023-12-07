import pycrib

hand = [
(9,'h'),
(2,'h'),
(7,'h'),
('Q','t')
]

turnup = ('A','h')

result = pycrib.hand_value(hand, turnup)

print(result[1])
