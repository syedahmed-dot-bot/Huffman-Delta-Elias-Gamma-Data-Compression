def elias_gamma_encode(value):
    if value  < 0:
        raise ValueError("Value must be non-negative")
    binary = bin(value)[2:]
    prefix = '0' * (len(binary) -1)
    
    return prefix + binary

def elias_gamma_encode_list(encoded):
    return''.join(elias_gamma_encode(value) for value in encoded)
