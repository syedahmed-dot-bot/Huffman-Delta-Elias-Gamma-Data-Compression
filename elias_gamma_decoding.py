def elias_gamma_decode(decoded):
    eg_decoded = []
    i = 0

    while i< len(decoded):
        zero_count = 0
        while i < len(decoded) and decoded[i] == '0':
            zero_count += 1
            i +=1
        
        length = zero_count+1
        binary = decoded[i: i +length]
        value = int(binary, 2)
        eg_decoded.append(value)
        i += length
    
    return eg_decoded