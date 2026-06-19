def histogram(data, binWidth):
    if not data:
        return []

    max_val = max(data)
    size = (max_val // binWidth) + 1
    result = [0] * size

    for num in data:
        index = num // binWidth
        result[index] += 1

    return result