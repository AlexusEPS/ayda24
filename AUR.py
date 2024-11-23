# algoritmo de busqueda lineal

def busqueda_lineal(lista, objetivo):
    # Recorremos cada elemento de la lista
    for indice, elemento in enumerate(lista):
        # Comparamos el elemento con el objetivo
        if elemento == objetivo:
            return indice  # Retorna el índice del objetivo
    return -1  # Retorna -1 si no se encuentra el objetivo

# Ejemplo de uso
mi_lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
objetivo = 50

resultado = busqueda_lineal(mi_lista, objetivo)

if resultado != -1:
    print(f"El objetivo {objetivo} se encuentra en el índice {resultado}.")
else:
    print(f"El objetivo {objetivo} no se encuentra en la lista.")



  # algoritmo de busqueda binaria  

def busqueda_binaria(lista, objetivo):
    # Definimos los índices inicial y final
    bajo = 0
    alto = len(lista) - 1

    # Mientras el rango no esté vacío
    while bajo <= alto:
        # Encontramos el índice medio
        medio = (bajo + alto) // 2
        
        # Comparamos el objetivo con el valor en el medio
        if lista[medio] == objetivo:
            return medio  # Retorna el índice si se encuentra
        elif lista[medio] < objetivo:
            bajo = medio + 1  # Si el objetivo es mayor, descartar la mitad inferior
        else:
            alto = medio - 1  # Si el objetivo es menor, descartar la mitad superior
    
    return -1  # Si no se encuentra, retorna -1

# Ejemplo de uso
mi_lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
objetivo = 80

resultado = busqueda_binaria(mi_lista, objetivo)

if resultado != -1:
    print(f"El objetivo {objetivo} se encuentra en el índice {resultado}.")
else:
    print(f"El objetivo {objetivo} no se encuentra en la lista.")
