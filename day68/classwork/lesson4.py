def capitalize(s, ind):
    result = list(s)
    for idx in ind:
        if 0 <= idx < len(s):
            result[idx] = result[idx].upper()
    return "".join(result)