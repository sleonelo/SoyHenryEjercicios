def factorial(num):
    inicial=1
    i=2
    while i<=num:
        inicial*=i
        i+=1
    return inicial

print(factorial(5))  

archivo_nuevo=open('/home/silvio/Escritorio/primer_archivo.txt', 'w')
archivo_nuevo.write('prueba de escritura')
archivo_nuevo.close()
