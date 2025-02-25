class FSM:
    def __init__(self):
        self.state = 0  # Initial state

    def transition(self, char):
        if self.state == 0:
            if char == 'a':
                self.state = 1
        elif self.state == 1:
            if char == 'a':
                self.state = 2
            elif char == 'b':
                self.state = 0  # Reset if incorrect pattern
        elif self.state == 2:
            if char == 'b':
                self.state = 3  # Accepting state
            elif char == 'a':
                self.state = 2  # Stay in state 2
            else:
                self.state = 0  # Reset if invalid sequence
        elif self.state == 3:
            if char == 'a':
                self.state = 1  # Restart pattern search
            elif char == 'b':
                self.state = 0
        
    def is_accepted(self, string):
        self.state = 0  # Reset to initial state
        for char in string:
            self.transition(char)
        return self.state == 3  # Accept only if final state is 3

# Testing the FSM
fsm = FSM()
test_strings = ["aab", "aaab", "baab", "aaaab", "ab", "aabaab"]

for s in test_strings:
    print(f"String: {s}, Accepted: {fsm.is_accepted(s)}")
