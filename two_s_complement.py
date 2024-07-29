class two_s_complement:
    clk=0
    def __init__(self, input_str):
        # Validating that input_str is a 4-bit binary string
        assert len(input_str) == 4 and all(c in '01' for c in input_str), "You entered wrong string make sure that input must be a four-bit string."
        self.input=(list(map(lambda z: int(z), input_str)))[::-1]


    def mcculloch_pitts_neuron2(self, input1, input2, threshold, weight1, weight2):
        net = input1 * weight1 + input2 * weight2
        # Comparing the net input with the threshold
        return 1 if net >= threshold else 0

    def OR_by_mcculloch_pitts_neuron2(self, input1, input2):
        return self.mcculloch_pitts_neuron2(input1, input2, threshold=1, weight1=1, weight2=1)

    def XOR_by_mcculloch_pitts_neuron2(self, input1, input2):
        # Note: Adjusting the weights and thresholds according to XOR logic.
        p1 = self.mcculloch_pitts_neuron2(input1,  input2, threshold=1, weight1=-0.5, weight2=1)  #logic1
        p2 = self.mcculloch_pitts_neuron2(input1, input2, threshold=1, weight1=1, weight2=-0.5)  #logic2
        return self.mcculloch_pitts_neuron2(p1, p2, threshold=1, weight1=1, weight2=1)

    def whole_network(self):
        out0 = self.input[0]
        #print(out0)
        s1 = self.OR_by_mcculloch_pitts_neuron2(self.input[0], self.input[1])
        out1 = self.XOR_by_mcculloch_pitts_neuron2(self.input[0], self.input[1])
        #print(out1)
        self.clk +=1
        out2 = self.XOR_by_mcculloch_pitts_neuron2(s1, self.input[2])
        #print(out2)
        self.clk +=1
        s2 = self.OR_by_mcculloch_pitts_neuron2(s1, self.input[2])
        out3 = self.XOR_by_mcculloch_pitts_neuron2(s2, self.input[3])
        self.clk +=1
        #print(out3)
        return str(int(out3)) + str(int(out2)) + str(int(out1)) + str(int(out0))

