#Program1: Design a Program for creating machine that accepts the string always ending with 101.
class FSM:
    def __init__(self):
        self.state = 0  # Initial state

    def transition(self, char):
        if self.state == 0:
            if char == '1':
                self.state = 1
        elif self.state == 1:
            if char == '0':
                self.state = 2
            elif char == '1':
                self.state = 1  # Remains in state 1
        elif self.state == 2:
            if char == '1':
                self.state = 3  # Accepting state
            else:
                self.state = 0  # Reset if invalid sequence
        elif self.state == 3:
            if char == '1':
                self.state = 1  # Restart pattern search
            elif char == '0':
                self.state = 2
        
    def is_accepted(self, string):
        self.state = 0  # Reset to initial state
        for char in string:
            self.transition(char)
        return self.state == 3  # Accept only if final state is 3

# Testing the FSM
fsm = FSM()
test_strings = ["101", "1101", "000101", "1111101", "100", "10101"]

for s in test_strings:
    print(f"String: {s}, Accepted: {fsm.is_accepted(s)}")
