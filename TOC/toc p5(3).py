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
            if char == '0':
                self.state = 3  # Accepting state
            elif char == '1':
                self.state = 1  # Restart pattern search
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
test_strings = ["100", "1100", "000100", "1111100", "101", "100100"]

for s in test_strings:
    print(f"String: {s}, Accepted: {fsm.is_accepted(s)}")
