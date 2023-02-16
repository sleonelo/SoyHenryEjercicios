while True:
    try:
        num= int(input('ingrese un numero: '))
        if num>0:
            print('ok')
            factorial=0
            break
        else:
            print('debe ser mayor a cero')
            continue
    except ValueError:
        print('debe ingresar un numero entero')
        
def primo(num):
    num_prueba=2
    if num==1 or num==2:
        return True
    else:
        while (num) != (num_prueba):
            # print(num_prueba)
            # print(num)
            if num%num_prueba==0:
                num_prueba+=1
                return False
            else: num_prueba+=1 
            return True
        