import string                      #Python String module contains some constants, utility function, and classes for string manipulation.
import random

if __name__ == "__main__":

    s1 = string.digits             #0123456789
    s2 = string.ascii_lowercase    #abcdefghijklmnopqrstuvwxyz
    s3 = string.ascii_uppercase    #ABCDEFGHIJKLMNOPQRSTUVWXYZ
    s4 =  string.punctuation       #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        
    ps_len = input("Enter the desired length of the password: ")

    if ps_len.isdigit() == True:
        ps_len = int(ps_len)      
                    
        s = []      #empty list
                    
        # Type conversion to list type for extending in list  AND # Concatenating s1, s2, s3, s4 in s
        #The extend() method adds the specified list elements (or any iterable) to the end of the current list.

        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        #print(s)             #depicts un-shuffled list
        
        random.shuffle(s)     #ALTERNATE METHOD: print("".join(random.sample(s,ps_len)))
        #print(s)             #depicts shuffled list
        
        print("Your password is: ")
        print("".join(s[0:ps_len]))     
        #join() will join the characters of the list with the given delimiter
    
    else:
        print("Please enter only digits")