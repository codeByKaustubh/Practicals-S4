#Program1: Design a Program for creating machine that accepts three consecutive one.
class ThreeConsecutiveOnesFSM:
    def __init__(self):
        self.state = 0  
    
    def transition(self, input_bit):
        if self.state == 0:
            if input_bit == '1':
                self.state = 1
            else:
                self.state = 0
        elif self.state == 1:
            if input_bit == '1':
                self.state = 2
            else:
                self.state = 0
        elif self.state == 2:
            if input_bit == '1':
                self.state = 3  
            else:
                self.state = 0
        elif self.state == 3:
            if input_bit == '1':
                self.state = 3
            else:
                self.state = 0
    
    def accepts(self, input_string):
        self.state = 0  
        for bit in input_string:
            self.transition(bit)
            if self.state == 3:
                return True  
        return False

fsm = ThreeConsecutiveOnesFSM()
test_cases = ["101110", "000", "111", "11011", "1001110"]
for test in test_cases:
    print(f"Input: {test}, Accepted: {fsm.accepts(test)}")
