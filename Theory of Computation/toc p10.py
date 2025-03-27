def turingMachine(string):
  string = list(string)
  elementToRemove = "B"
  while elementToRemove in string:
    string.remove(elementToRemove)
  n = int(len(string) / 3)
  for i in range(0, n):
    if string[i] != "a":
      return f"String {''.join(string)} is not Accepted!"
  for i in range(n, 2 * n):
    if string[i] != "b":
      return f"String {''.join(string)} is not Accepted!"
  for i in range(2 * n, 3 * n):
    if string[i] != "c":
      return f"String {''.join(string)} is not Accepted!"
  return f"String {''.join(string)} is Accepted!"
while True:
     string = input("Enter a String: ")
     print(turingMachine(string))