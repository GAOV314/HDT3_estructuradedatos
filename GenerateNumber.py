import random

numberList = []#Lista en la cual se guardan los numeros generados
#Metodo para generar tres mil numeros aleatorios
def randomNumber():
    for x in range(2999):#Para al generar los 3000 numeros
        x = random.randint(0, 10000)#Genera un numero del 0 al 10000
        numberList.append(x)#Agrega el numero a la lista

randomNumber()#Se llama el metodo randomNumber

with open("generateNumbers.txt", "w") as file:#Crea archivo en caso de que no exista este en modo escritura
    for number in numberList:#Recorre la lista segun la cantidad de elementos
        file.write("%s\n" % number)#Escribe en el archivo.txt cada numero del arreglo

archiveNumbers = []#Se crea arreglo para guardar datos del archivo ya generado
with open("generateNumbers.txt", "r") as file:#Abre el archivo en modo lectura
    for line in file:#Lee linea por linea
        archiveNumbers.append(int(line.strip()))#Se retorna el valor de la fila y lo agrega en la lista


def gnome_sort(arr):#Algoritmo gnome sort
    """
GNOME SORT
    """
    index = 0
    while index < len(arr):
        if index == 0 or arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1
    return arr

def merge_sort(arr):#Metodo merge sort
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Comparación y fusión de las dos mitades ordenadas
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Verificar elementos restantes en ambas mitades
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

def shell_sort(arr): #La primera línea define una función llamada shell_sort que toma una lista de números como entrada.
    n = len(arr) #n = longitud de la lista
    gap = n // 2 #gap que se inicializa con la mitad de la longitud de la lista de entrada.
    while gap > 0: #Este bucle divide la lista en sub-listas más pequeñas y las ordena utilizando el algoritmo de ordenación por inserción.
        for i in range(gap, n): #El bucle for itera sobre los elementos de la lista y utiliza el algoritmo de ordenación por inserción para ordenar las sub-listas.
            temp = arr[i] #define una variable temporal temp que almacena el valor del elemento actual
            j = i #define una variable j que se inicializa con el índice del elemento actual.
            while j >= gap and arr[j - gap] > temp: #El bucle while se ejecuta mientras j sea mayor o igual que gap y el elemento anterior sea mayor que el elemento actual.
                #Este bucle mueve los elementos mayores a la derecha para hacer espacio para el elemento actual.

                arr[j] = arr[j - gap] #Esta y las siguientes lineas insertan el elemento actual en su posición correcta en la sub-lista.
                j -= gap
            arr[j] = temp
        gap //= 2 #divide gap por 2 para reducir el tamaño de las sub-listas.
        return arr #La última línea devuelve la lista ordenada.


def selection_sort(arr, ascending=True):
    n = len(arr)

    for i in range(n):
        # Encontrar el índice extremo en el resto de la lista
        extreme_index = i
        for j in range(i+1, n):
            if ascending:
                condition = arr[j] < arr[extreme_index]
            else:
                condition = arr[j] > arr[extreme_index]

            if condition:
                extreme_index = j

        # Intercambiar el elemento extremo encontrado con el primer elemento no ordenado
        arr[i], arr[extreme_index] = arr[extreme_index], arr[i]

#RadixSort
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]
def radixSort(array):
    max_element = max(array)

    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10

