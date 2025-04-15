def delta_decode(eg_decoded):
    if not eg_decoded:
        return []

    decoded_final = [eg_decoded[0]]

    for i in range(1, len(eg_decoded)):
        value = decoded_final[-1] + eg_decoded[i]
        decoded_final.append(value)

    return decoded_final