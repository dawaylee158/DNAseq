def reverseComplement(s):
    complement = {'A':'T', 'C':'G', 'G':'C', 'T':'A'} 
    t = ''
    for base in s:
        t = complement[base] + t
    return t