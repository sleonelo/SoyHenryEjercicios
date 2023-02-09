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