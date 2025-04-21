if __name__ == '__main__':
    nested = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested.append([name,score])
    sorted_list = sorted(nested, key=lambda x:x[1])  
    
    
    x = set()
    for f,y in sorted_list:
        x.add(y)
           
flist = list(x)   
second_lowest = flist[1]
answer = []
for name,score in nested:
    if score==second_lowest:
        answer.append(name)
    

answer.sort()
for i in answer:
    print (i)
    
    
    
