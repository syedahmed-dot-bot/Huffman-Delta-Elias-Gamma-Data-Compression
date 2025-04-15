def delta_encode(data):
    if data is None:
        return []
    
    encoded = [data[0]]

    for i in range(1, len(data)):
        value = data[i]- data[i-1]
        encoded.append(value)
    
    return encoded
