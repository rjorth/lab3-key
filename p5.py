x = []

def word_count(x, n, str):
    filter(lambda b: str.length > n, x)
    reduce(lambda w, v: w.update([(v, w.get(v, 0)+1)]) or w, x.split(), [])
    return word_count(x, n, str)
