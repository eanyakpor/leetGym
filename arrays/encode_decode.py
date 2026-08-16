'''
RAMP

R - restate the problem
    write an algoritm for both encode to encode and decode to decode strings
    any character could appear 
    no libraries allwoed 

A - ask questions
    how big could the input get so any time/space fcosntraints? 
M - make examples
    input = ['emi', 'loves', 'chicken']
    # could encode with 5's in between emi55555loves5555chicken
    output = ['emi', 'loves', 'chicken']
    
    would be wrong because 5 is apart of 256 ascii content too 
    meaning you could get an output of all 5's 
P - pick a pattern 
    two pointers or just string manipulation to be honest 
E - explain in plain english 
    given this example
    input = ['emi', 'loves', 'chicken']
    emi#3loves#5chicken#7
               i
                        j
    we will encodde with the message above
    utilize two pointers 
    once j hits a number after # move i that many times
    once i hits # have i and j point at the same thing + 1 to correctly move on to the next word 

    output = ['emi', 'loves', 'chicken']
R - review 



    input = ['emi', 'loves', 'chicken']
    emi#3loves#5chicken#7
    i
       j
'''
def encode(strs):
    res = ''
    for word in strs:
        res += (str(len(word)) + '#' + word)
    print('encode res',res)
    return res


def decode(s):
    i,j = 0,0
    word = ''
    res = []
    while j < len(s):
        while s[j] != '#':
            j += 1
        count = int(s[i:j])
        i = j + 1
        while count > 0:
            word += s[i]
            i += 1
            count -= 1
        j = i
        res.append(word)
        word = ''
    print('res decode', res)
    return res 
