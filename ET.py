#######clave:[titulo,genero,duracion_min,clasificacion,idioma,es_3d]
peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neon', 'accion', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Codigo Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficcion', 132, 'B', 'Ingles', False],
    
    
}
#######clave:[precio,cupos]
cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
}
########funciones
def cupos_por_genero(genero):
    cupos = 0
    for clave,valor in peliculas.items():
        if valor[1].lower()==genero and cartelera[clave][1]>0:
            cupos += cartelera[clave][1]
            if cupos==0:
                print("no existen cupos para ninguna pelicula en cartelera del genero seleccionado")
            else:
                print(f"existen {cupos} cupos para el genero seleccionado")
def busqueda_por_precio(minimo,maximo):
    lista=[]
    for clave,valor in cartelera.items():
        if cartelera[clave][0]<=maximo and cartelera[clave][0]>=minimo:
            nombre = peliculas[clave][0]
            lista.append([nombre+"-"+clave])
            if len(lista)==0:
                print("no hay peliculas dentro del rango solicitado")
            else:
                lista.sort()
                print(f"las peliculas encontradas son:{lista}")
def actualizar_precio(codigo,precio_nuevo):
    if codigo in peliculas:
        cartelera[codigo][0]=precio_nuevo
        return True
    else:
        return False
def agregar_pelicula(codigo,titulo,genero,duracion_min,clasificacion,idioma,dimensiones3,precio,cupos):
    if codigo in peliculas:
        return False
    if es_3d=="s":
        dimensiones3=True
    if es_3d=="n":
        dimensiones3=False
    peliculas[codigo]=(titulo,genero,duracion_min,clasificacion,idioma,dimensiones3)
    cartelera[codigo]=(precio,cupos)
    return True
def eliminar_pelicula(codigo):
    if codigo in peliculas:
        del peliculas[codigo]
        del cartelera[codigo]
        return True
    else:
        return False
########validaciones
def validar_codigo(codigo):
    if len(codigo.strip())>0:
        return True
    else:
        return False
def validar_titulo(titulo):
    if len(titulo.strip())>0:
        return True
    else:
        return False
def validar_genero(genero):
    if len(genero.strip())>0:
        return True
    else:
        return False
def validar_duracion(duracion):
    try:
        d=int(duracion)
        if d>0:
            return True
        else:
            return False
    except:
        return False
def validar_clasificacion(clasificacion):
    if clasificacion in ('A','B','C'):
        return True
    else:
        return False
def validar_idioma(idioma):
    if len(idioma.strip())>0:
        return True
    else:
        return False
def validar_3d(es_3d):
    if es_3d in ("s","n"):
        return True
    else:
        return False
def validar_precio(precio):
    try:
        p=int(precio)
        if p>0:
            return True
        else:
            return False
    except:
        return False
def validar_cupos(cupos):
    try:
        c=int(cupos)
        if c>=0:
            return True
        else:
            return False
    except:
        return False        
########menu
def menu():
    print('''========== MENÚ PRINCIPAL ==========
            1. Cupos por género
            2. Búsqueda de películas por rango de precio
            3. Actualizar precio de película
            4. Agregar película
            5. Eliminar película
            6. Salir
            =====================================''')
def seleccione():
    try:
        opcion=int(input("seleccione una opcion:"))
        return opcion
    except:
        return 0
while True:
    menu()
    op=seleccione()
    match op:
        case 1:
            while True:
                genero=input("ingrese el genero del quie desea buscar cupos:")
                cupos_por_genero(genero)
                resp=input("¿desea repetir el proceso?s/n:").lower()
                if resp=="n":
                    break
        case 2:
            while True:
                try:
                    minimo=int(input("ingrese monto minimo:"))
                    maximo=int(input("ingrese monto maximo:"))
                    if minimo<maximo:
                        busqueda_por_precio(minimo,maximo)
                    else:
                        print("el monto minimo debe ser menor al monto maximo")
                except:
                    print("debe ingresar solo valores enteros")
                resp=input("¿desea repetir la operacion?s/n:").lower()
                if resp=="n":
                    break
        case 3:
            while True:
                try:
                    codigo=input("ingrese codigo que desea actualizar su precio:").upper()
                    precio_nuevo=int(input("ingrese precio nuevo:"))
                    resp=actualizar_precio(codigo,precio_nuevo)
                    if resp==True:
                        print("Precio actualizado")
                    else:
                        print("El codigo no existe")
                except:
                    print("el precio debe ser un numero entero positivo")
                rep=input("¿Desea actualizar otro precio (s/n)?").lower()
                if rep=="n":
                    break
        case 4:
            while True:
                codigo=input("ingrese codigo nuevo:").upper()
                validar_codigo(codigo)
                if validar_codigo(codigo)==False:
                    print("ingrese un codigo valido, que no exista y de minimo 4 caracteres")
                    continue
                titulo=input("ingrese titulo de la pelicula:").lower()
                validar_titulo(titulo)
                if validar_titulo(titulo)==False:
                    print("ingrese un titulo valido")
                    continue
                genero=input("ingrese el genero:").lower()
                if validar_genero(genero)==False:
                    print("ingrese un genero valido(ejemplo:drama, accion, terror,etc):")
                    continue
                duracion=input("ingrese la duracion en minutos:")
                if validar_duracion(duracion)==False:
                    print("la duracion debe ser numeros enteros positivos, en minutos")
                    continue
                clasificacion=input("ingrese la clasificacion('A','B','C'):").upper()
                if validar_clasificacion(clasificacion)==False:
                    print("ingrese una clasificacion valida segun el ejemplo")
                    continue
                idioma=input("ingrese el idioma:")
                if validar_idioma(idioma)==False:
                    print("ingrese un ididoma valido")
                    continue
                es_3d=input("disponible en formato 3D?s/n:").lower()
                if validar_3d(es_3d)==False:
                    print("ingrese una letra valida s o n")
                    continue
                precio=input("ingrese el precio:")
                if validar_precio(precio)==False:
                    print("el precio debe ser un numero entero mayor a 0")
                    continue
                cupos=input("ingrese el numero de cupos disponibles:")
                if validar_cupos(cupos)==False:
                    print("ingrese un numero entero mayor o igual a 0")
                resp=agregar_pelicula(codigo,titulo,genero,int(duracion),clasificacion,idioma,es_3d,int(precio),cupos)
                if resp==True:
                    print("Película agregada")
                else:
                    print("El codigo ya existe")
                rep=input("¿desea repetir esta accion?s/n:").lower()
                if rep=="n":
                    break
        case 5:
            while True:
                codigo=input("ingrese codigo de pelicula que desea eliminar:").upper()
                eliminar_pelicula(codigo)
                if eliminar_pelicula(codigo)==False:
                    print("Codigo no existe")
                else:
                    print("pelicula eliminada existosamente")
                resp=input("¿desea repetir el proceso?s/n:").lower()
                if resp=="n":
                    break
        case 6:
            print("Programa finalizado")
            break
                
                    
            
                        
                
            
             

    
    