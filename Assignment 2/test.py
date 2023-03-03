def est_bit_proportion(byteArray):

    numberOfOnes = 0
    lengthOfByteArray = len(byteArray)
    byte = ""

    for i in byteArray:
        byte = format(i, "b")
        for j in byte:
            if j == "1":
                numberOfOnes = numberOfOnes + 1

    print(numberOfOnes/(lengthOfByteArray * 8))

test = bytearray(2)
test[ 0 ] = 0b00000000 
test[ 1 ] = 0b00000011
est_bit_proportion(test)
