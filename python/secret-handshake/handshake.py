def handshake(num):
    result = []
    a = bin(int(num))
    print a
    for i in 0,range(a),-1:
        print a[i]
        
        

def code(lst):
    pass
    


print handshake('9')

"""
Write a program that will take a decimal number, and convert it to the appropriate sequence of events for a secret handshake.

> There are 10 types of people in the world: Those who understand
> binary, and those who don't.

You and your fellow cohort of those in the "know" when it comes to
binary decide to come up with a secret "handshake".

```
1 = wink
10 = double blink
100 = close your eyes
1000 = jump


10000 = Reverse the order of the operations in the secret handshake.


from handshake import handshake, code


class HandshakeTest(unittest.TestCase):
    def test_shake_int(self):
        self.assertEqual(['wink','jump'], handshake(9))

    def test_shake_bin1(self):
        self.assertEqual(['close your eyes','double blink'], handshake('10110'))

    def test_shake_bin2(self):
        self.assertEqual(['wink','close your eyes'], handshake('101'))

    def test_shake_negative_int(self):
        self.assertEqual([], handshake(-9))

    def test_shake_bin_invalid(self):
        self.assertEqual([], handshake('121'))

    def test_unknown_action(self):
        self.assertEqual('0', code(['wink','sneeze']))

    def test_code1(self):
        self.assertEqual('1100', code(['close your eyes','jump']))

    def test_code2(self):
        self.assertEqual('11', code(['wink','double blink']))

    def test_code3(self):
        self.assertEqual('11010', code(['jump','double blink']))

    def test_composition1(self):
        self.assertEqual('11011', code(handshake(27)))

    def test_composition2(self):
        self.assertEqual('1', code(handshake(1)))

    def test_composition3(self):
        self.assertEqual('111', code(handshake('111')))

    def test_composition4(self):
        inp = ['wink','double blink','jump']
        self.assertEqual(inp, handshake(code(inp)))

"""