def word_lengths(phrase):
    return map(lambda x:len(x),phrase.split())
print(list(word_lengths('How long are the words in this phrase')))

print("-----------------------------------")

from functools import reduce
def digits_to_num(digits):
    return reduce(lambda x,y:x*10+y,digits)
print(digits_to_num([3,4,3,2,1]))

print("-----------------------------------")

def filter_words(word_list,letter):
    return list(filter(lambda x: x.startswith(letter),word_list))
l=['hello','are','cat','dog','ham','hi','go','to','heart']
print(filter_words(l,'h'))


print("-----------------------------------")

def concatenate(L1,L2,connector):
    return [elem1+connector+elem2 for elem1,elem2 in zip(L1,L2)]
print(concatenate(['A','B'],['a','b'],'-'))

print("-----------------------------------")

def d_list(L):
    final_dic={}
    for i,v in enumerate(L):
        final_dic[v]=i
    return final_dic
print(d_list(['a','b','c']))    

print("-----------------------------------")

def count_match_index(L):
    return len([vals for vals in enumerate(L) if vals[0]==vals[1]])
print(count_match_index([0,2,2,1,5,5,6,10]))