# Reads the code and tokenizes it.
with open('code.skib', 'r') as raw_source_code:
    global tokens
    tokens = [word for line in raw_source_code for word in line.split()]
# Sets up variables for Memory Slots and Pointer Slot
memory_spots = [0 for i in range(20)]
pointer = 0
# Main Loop with Checks for a Command in each Token
for token in tokens:

    if token == "deuces":
        break
    elif token == "rizz" and pointer < 20 :
        pointer += 1
    elif token == "unrizz" and pointer > 0:
        pointer -= 1
    elif token == "stonks":
        memory_spots[pointer] += 1
    elif token == "burn":
        memory_spots[pointer] -= 1
    elif token == "yap": 
        print(memory_spots[pointer])
    elif token == "bet":
        memory_spots[pointer] = input("> ")
    # Check for invalid command and exit loop if the user entered one
    else:
        print("Invalid command!")
        break
