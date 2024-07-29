# Implementing-4-bit-two-s-complement-arithmetic-using-McCulloch-Pitts-neurons
Here you will get familiar with the simple implementation of digital circuits using McCulloch-Pitts neurons.


One of the approaches for implementing a 4-bit two's complement digital circuit at the gate level is based on XOR-OR implementation.


<img src="images/macpitz1.png" alt="Gate-level implementation of a 4-bit two's complement circuit" style="width:  100 %;" class="center">
<p><em>Figure 1: Gate-level implementation of a 4-bit two's complement circuit.</em></p>

To implement the presented circuit based on McCulloch-Pitts neurons, the XOR and OR structures can be replaced with their equivalent structures consisting of McCulloch-Pitts neurons, or simply MP neurons.

Additionally, considering all possible inputs, the output of this digital circuit should produce a truth table similar to Table 1. To quickly find the two's complement, which is equivalent to adding one single binary bit to the one's complement of that number, you can keep the bits from the rightmost bit up to the first encountered 1 unchanged, and invert the remaining bits (changing 1 to 0 and vice versa).

|  | **Binary Number** | **Two's Complement** |
| --- | --- | --- |
| 0 | 0000 | 0000 |
| 1 | 0001 | 1111 |
| 2 | 0010 | 1110 |
| 3 | 0011 | 1101 |
| 4 | 0100 | 1100 |
| 5 | 0101 | 1011 |
| 6 | 0110 | 1010 |
| 7 | 0111 | 1001 |
| 8 | 1000 | 1000 |
| 9 | 1001 | 0111 |
| 10 | 1010 | 0110 |
| 11 | 1011 | 0101 |
| 12 | 1100 | 0100 |
| 13 | 1101 | 0011 |
| 14 | 1110 | 0010 |
| 15 | 1111 | 0001 |

**Table 1:** Truth Table for 4-bit Binary Numbers and Their Two's Complement

### Network Theory Implementation

The neuron models based on XOR and OR along with their weights can be seen in Figures \ref{h3} and \ref{h2}.


<img src="images/xor_gate.PNG" alt="MP Neuron-Based XOR Implementation" style="width:  100 %;" class="center">
<p><em>Figure 2: MP Neuron-Based XOR Implementation.</em></p>

<img src="images/or_gate.PNG" alt="MP Neuron-Based OR Implementation" style="width:  100 %;" class="center">
<p><em>Figure 3: MP Neuron-Based OR Implementation.</em></p>


