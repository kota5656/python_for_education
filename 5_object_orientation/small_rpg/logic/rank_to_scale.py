def majorScale(baseParam: int, rank: int):
    if rank > 0: return int(baseParam * (1 + 0.5*rank))
    else: return baseParam // (1 + 0.5*rank)

def minorScale(baseParam: int, rank: int):
    if rank > 0: return int(baseParam * (1 + (1/3)*rank))
    else: return baseParam // (1 + (1/3)*rank)
