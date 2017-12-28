def centuryFromYear(year):
    
    str_year = str(year)
    len_year = len(str_year)

    if(len_year <= 2):
        
        return 1
        
    elif(len_year == 3):
        
        if(str_year[1] == '0' and str_year[2] == '0'):
            
            return int(str_year[0]) 
        
        else:
            return int(str_year[0]) + 1
        
    else:

        if(str_year[2] == '0' and str_year[3] == '0'):
            
            return int(str_year[0:2])
        
        else:
            
            return int(str_year[0:2]) + 1



print centuryFromYear(1800)