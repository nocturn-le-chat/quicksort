def workhorse(iterable):
    if len(iterable) <= 1: return iterable 
    slices = [[], iterable[len(iterable)//2], []]
    for k in iterable:
        if k < slices[1]: slices[0].append(k)
        if k > slices[1]: slices[2].append(k)
    
    return workhorse(slices[0]) + [slices[1]] + workhorse(slices[2])

def qsort(iterable):
    if type(iterable) != list: return "ERROR: unsupported input type"
    elif not all([type(k) in [int, str] for k in iterable]): return "ERROR: incorrect input containments"
    else: return workhorse(iterable)