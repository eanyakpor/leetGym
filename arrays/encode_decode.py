'''
RAMPER
R - restate the problem
design a class with methods that 
enocde : sort a list of strings in a formulated pattern
decode : decode the original list 

A - ask a question
none currently 

M - make an example 
    input = ["emi"]
    encode = "e#m#i"
    decode = emi

P - pick a pattern
    two pointers + string methods 
E - explain the plan 
   ['emi', 'loves','to', 'code'] 
   encode = 3emi#5loves#2to#4code#
   decode = 3emi#5loves#2to#4code# == ['emi', 'loves','to', 'code'] 

   read the first number move r that many times until we see a #
    insert the length of letters which should be avalid word into a res list
   than repeate the process once we see a #
   reset i once j len thats infront of word times  
   j need to be moved + 1 to begin at number that ocunts how many times it needs to move 
   ['3','4','##','5']
   enode = 13#14#2###15#
   decode = 13#14#2###15#
                        j
                        i
            [3,4]
  sepaerate each word with len(word) + word + #
  have i start at number so j knows how many times to move
  post j reaching the len of word and a # is seen 
  have i move to j + 1 to find the number after delimeter # 
  and have j move to i + 1
  repeate the algo
'''
def encode(strs):
    res = ''
    for word in strs:
        res += str(len(word)) + '#' + word
    return res

'''
'13#abcdefghijklm'
 i
  js             length
'''
def decode(s):
    ans = []
    i,j = 0,0
    while j < len(s):
        while s[j] != '#':
            j += 1

        length = s[i:j]
        length = int(length)

        wordStart = j + 1

        wordEnd = j + 1 + length
        ans.append(s[wordStart:wordEnd])
        i = wordEnd
        j = i
    return ans




