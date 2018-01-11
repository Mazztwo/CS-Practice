def reverseParentheses(s):
        
    s_list = []
    open_parens = []
    close_parens = []
    index = 0
        
    # locate indicies of all parens ######
    for c in s:
                
        if( c == '(' ):
            open_parens.append(index)
        elif( c == ')' ):
            close_parens.append(index)

        s_list.append(c)

        index += 1
    #######################################

    # reverse parens to have proper pairing starting from inner
    open_parens = open_parens[::-1] 
    #######################################

    # check to make sure that pairings are correct
    for q in range(0, len(open_parens)):

        if(open_parens[q] > close_parens[q]):

            temp = open_parens[q+1]
            open_parens[q+1] = open_parens[q]
            open_parens[q] = temp

    #######################################


    # reverse strings in paren pairs #######
    c_index = 0

    for i in range(0, len(close_parens)):
           
        reverse = s_list[open_parens[i]+1:close_parens[i]]
        reverse = ''.join(reverse)
        reverse = reverse[::-1]
           
        for n in range(open_parens[i]+1, close_parens[i]):
            s_list[n] = reverse[c_index]
            c_index += 1

        c_index = 0

    c_index = 0
    #######################################


    # remove parens from s_list and cast to string
    s_list[:] = [c for c in s_list if(c != '(')]
    s_list[:] = [c for c in s_list if(c != ')')]


    return ''.join(s_list)
    #############################################    


print reverseParentheses("a(bcdefghijkl(mno)p)q")
#                       apmnolkjihgfedcbq

#print reverseParentheses("The ((quick (brown) (fox) jumps over the lazy) dog)")
#                           The god quick nworb xof jumps over the lazy
