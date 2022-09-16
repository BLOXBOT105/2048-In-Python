import sys, tty, random

layer_1 = [0, 0, 0, 0]
layer_2 = [0, 0, 0, 0]
layer_3 = [0, 0, 0, 0]
layer_4 = [0, 0, 0, 0]

def change_value(posX, posY, value):
    global layer_1
    global layer_2
    global layer_3
    global layer_4

    globals()["layer_" + str(posY)][posX] = value

def check_value(posX, posY):
    global layer_1
    global layer_2
    global layer_3
    global layer_4

    return globals()["layer_" + str(posY)][posX]

def space_occupied(posX, posY):
    global layer_1
    global layer_2
    global layer_3
    global layer_4

    if globals()["layer_" + str(posY)][posX] != 0:
        return True
    else:
        return False

def generate_block():
    global layer_1
    global layer_2
    global layer_3
    global layer_4

    got_block = False
    while True:
        posY = random.randint(1,4)
        posX = random.randint(0, len(globals()["layer_"+str(posY)])-1)
        value = random.randint(1,2)

        if not space_occupied(posX, posY):
            change_value(posX, posY, value*2)
            break

def main(Running):
    global layer_1
    global layer_2
    global layer_3
    global layer_4

    while Running:
        key = input("")
        generate_block()
        print("", layer_1, "\n", layer_2, "\n", layer_3, "\n", layer_4, "\n")

        #random
if __name__ == "__main__":
    main(Running = True)
