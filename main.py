def workhorse(iterable):
    if len(iterable) <=1: return iterable
    anchor = iterable[len(iterable)//2]
    left = [k for k in iterable if k <= anchor]
    right = [k for k in iterable if k > anchor]
    
    return workhorse(left) + workhorse(right)

def qsort(iterable):
    if type(iterable) != list: return "ERROR: unsupported input type"
    elif not all([type(k) in [int, str] for k in iterable]): return "ERROR: incorrect input containments"
    else: return workhorse(iterable)

print(qsort([1, 3, 2, 2, 5, 4, 6, 3]))
