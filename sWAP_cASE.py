def swap_case(s):
    result=""
    for i in range(len(s)):
        if(s[i].isupper()):
            result+=s[i].lower()
        elif(s[i].islower()):
            result+=s[i].upper() 
        else:
            result+=s[i]  
    return result