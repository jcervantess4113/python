def major(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n3 and n2>n1:
        return n2
    elif n3>n2 and n3>n1:
        return n3 
    
n1 = raw_input('write a number:')
n2 = raw_input('write a number:')
n3 = raw_input('write a number:')
print 'el mayor es:' + major(n1,n2,n3)

    