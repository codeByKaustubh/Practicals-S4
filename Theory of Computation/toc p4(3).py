class ThreeConsecutiveBsFSM:
    def __init__(self):
        self.state = 0  
    
    def transition(self, input_char):
        if self.state == 0:
            if input_char == 'b':
                self.state = 1
            else:
                self.state = 0
        elif self.state == 1:
            if input_char == 'b':
                self.state = 2
            else:
                self.state = 0
        elif self.state == 2:
            if input_char == 'b':
                self.state = 3
            else:
                self.state = 0
        elif self.state == 3:
            if input_char == 'b':
                self.state = 3
            else:
                self.state = 0
    
    def accepts(self, input_string):
        self.state = 0  
        for char in input_string:
            self.transition(char)
            if self.state == 3:
                return True  
        return False

fsm = ThreeConsecutiveBsFSM()
test_cases = ["aabbabb", "aaaa", "bbb", "abbba", "bbbab"]
for test in test_cases:
    print(f"Input: {test}, Accepted: {fsm.accepts(test)}")
