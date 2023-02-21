class Node:
    def _init__(self, prob, symbol, lewo=None, prawo=None):
        self.prob = prob
        self.symbol = symbol
        self.lewo = lewo
        self.prawo = prawo
        self.code = ''

def Calculate_Probability(data):
    symbols = dict()
    for element in data:
        if symbols.get(element) == None:
            symbols[element] = 1
        else:
            symbols[element] += 1
    return symbols

codes = dict()

def Calculate_Codes(node, val=''):
    newVal = val + str(none.code)

    if(node.lewo):
        Calculate_Codes(node.lewo, newVal)
    if(node.prawo):
        Calculate_Codes(node.prawo, newVal)
    if(not node.prawo and not node.lewo):
        codes[node.symbol] = newVal

    return codes

def Output_Encoded(data, coding):
    encoding_output = []
    for a in data:
        print(coding[a], end='')
        encoding_output.append(coding[a])

    string = ''.join([str(item) for item in encoding_output])
    return string

def Total_Gain(data, coding):
    do_compresji = len(data) * 8
    po_compresji = 0
    symbols = coding.keys()
    for symbol in symbols:
        count = data.count(symbol)
        po_compresji += count * len(coding[symbol])
    print("Spacja korzystajaca do kompresji (w bitach): ", do_compresji)
    print("Spacja korzystajaca po kompresji (w bitach): ", po_compresji)
        


def Huffman_kod(data):
    symbol_with_probs = Calculate_Probability(data)
    symbols = symbol_with_probs.keys()
    probabilities = symbol_with_probs.values()
    print('symbols: ', symbols)
    print('probabilities: ', probabilities)

    nodes = []

    for symbol in symbols:
        nodes.append(Node(symbol_with_probs.get(symbol), symbol))

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.prob)

        prawo = nodes[0]
        lewo = nodes[1]
    
        lewo.code = 0
        prawo.code = 1

        newNode = Node(lewo.prob + prawo.prob, lewo.symbol + prawo.symbol, lewo, prawo)

    huffman_kod = Calculate_Codes(nodes[0])
    print(huffman_kod)
    Total_Gain(data, huffman_kod)
    encoded_output = Output_Encoded(data, huffman_kod)
    print('Wyjscie koda: ', encoded_output)
    return encoded_output, nodes[0]
    
    
        