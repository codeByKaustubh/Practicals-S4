class PDA:
    def __init__(self):
        self.stack = []

    def accept_wcwr(self, input_string):
        n = len(input_string)
        if n < 3 or 'C' not in input_string:
            return False
        
        c_index = input_string.index('C')
        w = input_string[:c_index]
        wR = input_string[c_index + 1:]
        
        if wR[::-1] != w:
            return False
        
        for char in w:
            self.stack.append(char)
        
        if input_string[c_index] != 'C':
            return False
        
        for char in wR:
            if not self.stack or self.stack.pop() != char:
                return False
        
        return len(self.stack) == 0

if __name__ == "__main__":
    pda = PDA()
    input_string = input("Enter a string: ")
    if pda.accept_wcwr(input_string):
        print("Accepted")
    else:
        print("Rejected")