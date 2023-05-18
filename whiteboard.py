#Given two strings containing only capital and lowercase letters, write a function that returns true if they are anagrams of each other and false otherwise.
#An anagram is a word, phrase, or name formed by rearranging the letters of another word.

s1 = "anagram"
t1 = "nagaram"
# Output:
# True

#s2 = "rat"
#t2 = "car"
#Output:
# False

#s3 = "stops"
#t3 = "pots"
#Output:
# False

#True if it can be re arranged
#false if not
#compare the letters of each list
def solution(w1, w2):
    #see if the first letter matches the other letters in the other word
    letters_w1 = {}
    letters_w2 = {}
    w1 = w1.lower()
    w2 = w2.lower()
    if len(w1) == len(w2): #checking length
        for index in range(len(w1)):
            if w1[index] not in letters_w1:
                letters_w1[w1[index]] = 1
            else:
                letters_w1[w1[index]] += 1
        for index in range(len(w2)):
            if w2[index] not in letters_w2:
                letters_w2[w2[index]] = 1
            else:
                letters_w2[w2[index]] += 1
        return letters_w1 == letters_w2
    #if there was an a, see how many in each word
    #compare the letters of each list









