from random import randint

def prod_punto(vector1: list, vector2: list) -> float:
    """
    Calcula el producto punto entre dos vectores
    """
    lenVector1 = len(vector1)

    assert lenVector1 == len(vector2) , 'Los vectores tienen dimensiones\
    diferentes y no tienen un producto punto'
    prods = 0

    for ii in range(lenVector1):
        prods = prods + vector1[ii] * vector2[ii]

    return(prods)


def op_fila_escalar(vector: list, escalar: float) -> list:
    """
    Operación de fila 1: Entrega un vector_escalado con las multiplicaciones
    de cada elemento del vector entregado por un escalar dado.
    No altera el vector original.
    """
    lenVector = len(vector)
    vector_escalado = [0] * lenVector #Prealocación

    for i in range (lenVector):
        vector_escalado[i] = vector[i] * escalar

    return vector_escalado


def op_suma_filas(vector1: list, vector2: list) -> list:
    """
    Operación de fila 2: Suma término a término dos vectores ingresados,
    retorna un nuevo vector con los resultados de estas sumas.
    No altera los vectores originales.
    """

    lenVector1 = len(vector1)

    assert lenVector1 == len(vector2) , 'Los vectores tienen dimensiones\
    diferentes y no se pueden sumar'

    vector_suma = [0] * lenVector1 #Prealocación

    for i in range(lenVector1):
        vector_suma[i] = vector1[i] + vector2[i]
    return vector_suma


def op_suma_fila_escalar(vector1: list, vector2: list, escalar: float) -> list:
    """
    Combinación de las operaciones de fila 1 y 2, primero multiplica el segundo
    vector ingresado por un escalar dado y luego lo suma al valor del primer
    vector ingresado. Puede usarse como una resta usando el escalar - 1.
    No altera los vectores originales.
    """
    operando = op_fila_escalar(vector2,escalar)
    operando = op_suma_filas(vector1,operando)

    return operando


def op_cambio_fila(lista1: list, lista2: list) -> None:
    """
    Operación de fila 3: Intercambia los elementos que almacenan dos listas del
    mismo tamaño.
    ALTERA las listas ingresadas.
    """
    for i in range(len(lista1)):
        lista1[i], lista2[i] = lista2[i], lista1[i]


class Matriz():
    """
    Clase matriz n * m (filas * Columnas)
    """
    Mat_creadas = Mat_creadas = 0
                                                                #????????????????
    def __init__(self, args:list = [[1,0],[0,1]], name:any = f'Mat{Mat_creadas + 1}'):
        """
        Ingresar una lista que contenga cada fila de la matriz como una lista,
        seguido de un nombre opcional para la matriz (se sugiere nombres en
        str).
        ejemplo:
        Matriz([[1,0,3], [0,1,3]], 'Mi Matriz')
        """
        self.valores = args
        self.Ndimension = len(args) #número de filas
        self.Mdimension = len(args[0]) #número de columnas

        for i in range(self.Ndimension):
            assert len(self.valores[i]) == self.Mdimension , "La matriz debe \
tener un elemento en cada posición"

        self.name = name
        Matriz.Mat_creadas = Matriz.Mat_creadas + 1 #??????????????


    def rename(self, name: any):
        """
        Cambia el nombre de un objeto de la clase Matriz()
        """
        self.name = name


    def __getitem__(self, key: int):
        """
        Acceso a los valores de la matriz al estilo de un objeto de clase list
        """
        return self.valores[key]


    def __setitem__(self, key: int, value):
        """
        Reemplaza la matriz por una con el mismo nombre y la alteración
        correspondiente a sus valores en el key ingresado.
        Tener en cuenta las propiedades de la clase matriz al alterar sus
        valores
        """
        self.valores[key] = value
        self = Matriz(self.name, self.valores)


    def __str__(self) -> str:
        """
        Define la versión str de un objeto de la clase Matriz
        """
        printable = f'{self.name}: '

        for i in range(self.Ndimension):
            printable = printable + str(self[i])

        return printable


    def __add__ (self,other):
        """
        Suma punto a punto los valores de dos matrices de iguales dimensiones.
        Retorna un objeto matriz con esta suma. No altera las matrices 
        ingresadas.
        """
        assert self.Ndimension == other.Ndimension and self.Mdimension == \
            other.Mdimension , 'Las matrices deben tener las mismas \
dimensiones para sumarse'

        sum = [[0] * self.Mdimension for i in range(self.Ndimension)]

        for i in range(self.Ndimension):
            for j in range(self.Mdimension):
                sum[i][j] = self[i][j] + other[i][j]

        return Matriz(sum, f'{self.name} + {other.name}')


    def __sub__ (self,other):
        """
        Resta punto a punto los valores de dos matrices de iguales dimensiones.
        Retorna un objeto matriz con esta resta. No altera las matrices
        ingresadas.
        """
        assert self.Ndimension == other.Ndimension and self.Mdimension == \
            other.Mdimension , 'Las matrices deben tener las mismas \
dimensiones para restarse'

        res = [[0]*self.Mdimension for i in range(self.Ndimension)]

        for i in range(self.Ndimension):
            for j in range(self.Mdimension):
                res[i][j] = self[i][j] - other[i][j]

        return Matriz(res, f'{self.name} - {other.name}')


    def __mul__(self, other):
        """
        Retorna un objeto matriz con la multiplicación de dos matrices.
        No altera las matrices ingresadas.
        """
        assert self.Mdimension == other.Ndimension , 'Las matrices no tienen \
las dimensiones apropiadas para multiplicarse'

        #Prealocación
        producto = [[0]*other.Mdimension for i in range(self.Ndimension)]

        for ii in range(self.Ndimension):
            for jj in range(other.Mdimension):

                columna = [other.valores[fila][jj] for fila in range(other.Ndimension)]
                #Elemento jj de cada fila de other

                producto[ii][jj] = prod_punto(self.valores[ii],columna)

        return Matriz(producto, f'{self.name} * {other.name}')


    def prod_escalar(self,escalar:float):
        """
        Multiplica cada elemento de la matriz por un escalar ingresado. Altera
        la matriz ingresada.
        """
        for i in range(self.Ndimension):
            self.valores[i] = op_fila_escalar(self.valores[i],escalar)

        return self


    def prod_P_P(self,other):
        """
        Multiplica posición a posición el valor de dos matrices de dimensiones
        iguales. No altera las matrices ingresadas.
        """
        assert self.Ndimension == other.Ndimension and self.Mdimension == other.Mdimension ,\
        'Las matrices deben ser de iguales dimensiones'

        producto = [[0] * self.Mdimension for i in range(self.Ndimension)]
        for i in range(self.Ndimension):
            for j in range(self.Mdimension):
                producto[i][j] = self.valores[i][j] * other.valores[i][j]
        
        return Matriz(producto, f'{self.name} .* {other.name}')
                

    def get_transpuesta(self):
        """
        Retorna la matriz transpuesta de la ingresada. No altera la matriz
        original
        """
        #prealocación
        transpuesta = [[]] * self.Mdimension

        for ii in range(self.Mdimension):

            transpuesta[ii] = [self.valores[fila][ii] for fila in range(self.Ndimension)]

        return Matriz(transpuesta, f"{self.name}'")


    # def transpose(self): ?????????
    #     """
    #     Transpone la matriz ingresada, es decir, intercambia sus filas por sus
    #     columnas. ALTERA la matriz ingresada.
    #     """
    #     self = self.get_transpuesta()


    def get_determinante(self):
        """
        Calcula el determinante de la matriz aproximándose a su triangular
        superior
        Triangulación de la matriz:
        Se calcula una triangular superior equivalente por medio de
        operaciones de fila y se consideran alteraciones al determinante de la
        matriz original.
        Cálculo del determinante:
        Multiplica la diagonal principal de la triangular teniendo en cuenta
        las alteraciones mencionadas
        """
        assert self.Ndimension == self.Mdimension , 'La matriz debe ser \
cuadrada para tener un determinante'

        fila_nula = [0]*self.Mdimension
        for i in range(self.Ndimension):
            if self.valores[i] == fila_nula:
                return 0

        #copia de la matriz original
        triangular_superior = [self.valores[i] for i in range(self.Ndimension)]

        det = 1 #consideración para operaciones de fila

        #Asegurar que la matriz no empiece en 0 por cambio de fila
        fila_prueba = 1
        while triangular_superior[0][0] == 0 and fila_prueba < self.Ndimension:

            op_cambio_fila(triangular_superior[0], triangular_superior[fila_prueba])

            det = det * - 1
            fila_prueba = fila_prueba + 1

        #Si la primera columna tiene solo 0s
        if fila_prueba == self.Ndimension:
            return 0

        #Solo se triangulan M - 1 columnas
        #(la columna que falta es la esquina)

        for i in range(self.Mdimension - 1):
            # i indica cuántas columnas han sido trianguladas

            #se inicia en la fila siguiente a la cant. de columnas trianguladas
            for j in range(i+1, self.Ndimension):

                #Se hace un cambio de fila si la posición correspondiente a la
                #diagonal que se va a usar empieza en 0
                fila_prueba = i + 1
                while triangular_superior[i][i] == 0 and fila_prueba < self.Ndimension:

                    op_cambio_fila(triangular_superior[i], triangular_superior[fila_prueba])
                    det = det * - 1
                    fila_prueba = fila_prueba + 1

                #Si la diagonal ya tiene un 0
                if fila_prueba == self.Ndimension:
                    return 0

                #Se hace un cambio de fila si la primera fila cuyo primer
                #número se busca volver cero ya es cero antes de hacer ninguna
                #operación
                fila_prueba = j + 1
                while triangular_superior[j][i] == 0 and fila_prueba < \
                self.Ndimension:

                    op_cambio_fila(triangular_superior[j], triangular_superior[fila_prueba])
                    det = det * - 1
                    fila_prueba = fila_prueba + 1

                #Convertir el primer elemento de cada siguiente fila en 0.
                triangular_superior[j] = op_suma_fila_escalar(triangular_superior[j], triangular_superior[i], - triangular_superior[j][i] / triangular_superior[i][i])

        for i in range(self.Ndimension):
            det = det * triangular_superior[i][i]

        #Debido a las conversiones de tantas fracciones a decimales en el
        #proceso, se redondea el resultado a 3 decimales
        return round(det,4) 


    def get_inversa(self):
        """
        Calcula la matriz inversa a la matriz cuadrada ingresada por medio de
        operaciones de fila. Se le aplica a la matriz identidad las operaciones
        de fila necesarias para convertir una copia de la matriz original en la
        matriz identidad
        """
        assert self.get_determinante() != 0 , 'La matriz es singular y no \
        tiene inversa'

        #copia de la matriz original, se convertirá en la MATRIZ IDENTIDAD
        mat_identidad = [self.valores[i] for i in range(self.Ndimension)]

        #Matriz identidad, se convertirá en la MATRIZ INVERSA
        mat_inversa = [[0]*self.Mdimension for i in range(self.Ndimension)]
        for i in range(self.Ndimension):
            mat_inversa[i][i] = 1

        #Se escalona cada columna hacia abajo
        for i in range(self.Mdimension):
            #i indica cuántas columnas han sido escalonadas hacia abajo

            #Asegurar que la fila no empiece en 0 por cambio de fila
            fila_prueba = i + 1
            while mat_identidad[i][i] == 0 and fila_prueba < self.Ndimension:

                op_cambio_fila(mat_inversa[i], mat_inversa[fila_prueba])
                op_cambio_fila(mat_identidad[i], mat_identidad[fila_prueba])

                fila_prueba = fila_prueba + 1

            #La columna no puede tener solo 0s, pues el det no es 0.

            #se convierte el primer número de la fila en 1
            mat_inversa[i] = op_fila_escalar(mat_inversa[i], 1 / mat_identidad[i][i])
            mat_identidad[i] = op_fila_escalar(mat_identidad[i], 1 / mat_identidad[i][i])
            
            #se inicia en la fila siguiente a la cant. de columnas escalonadas
            for j in range(i+1, self.Ndimension):

                fila_prueba = j + 1 #cambio de fila si ya empieza en 0
                while mat_identidad[j][i] == 0 and fila_prueba < self.Ndimension:

                    op_cambio_fila(mat_inversa[j], mat_inversa[fila_prueba])
                    op_cambio_fila(mat_identidad[j], mat_identidad[fila_prueba])
                    fila_prueba = fila_prueba + 1

                #Convertir el primer elemento de cada siguiente fila en 0.
                mat_inversa[j] = op_suma_fila_escalar(mat_inversa[j], mat_inversa[i], - mat_identidad[j][i])
                mat_identidad[j] = op_suma_fila_escalar(mat_identidad[j], mat_identidad[i], - mat_identidad[j][i])

        #se escalona cada columna hacia arriba, ya teniendo una diagonal 
        #principal de solo 1s.
        for i in range(self.Mdimension - 1, - 1, - 1):
            #i = columnas a escalonar (se empieza desde la última)
            
            for j in range(i - 1, - 1, - 1):
                #j = fila de turno, orden descendiente

                #Convertir el primer elemento de cada siguiente fila en 0.
                mat_inversa[j] = op_suma_fila_escalar(mat_inversa[j],mat_inversa[i], - mat_identidad[j][i])
                mat_identidad[j] = op_suma_fila_escalar(mat_identidad[j], mat_identidad[i], - mat_identidad[j][i])

        return Matriz(mat_inversa, f'{self.name}^-1')
    

    def sist_ec_lineal(self,other):
        """
        Resuelve un sistema de ecuaciones lineales de n dimensiones de tipo:
        A * x = R
        La matriz actual se toma como matriz de coeficientes.
        La matriz ingresada debe ser un vector FILA con los valores de R
        Retorna un vector fila con los resultados de cada variable.
        """
        solucion = self.get_inversa() * other.get_transpuesta()
        solucion.rename('Variables')
        return solucion


# A = Matriz([[9,1,9,5,9], [1,-9,-1,6,88], [6,18,25,2,7], [3,2,10,5,0], [0,0,2,0,1]], 'A')
# B = Matriz([[3,7.5,4,3], [2,5,1,8], [6,2,1,4],[3,1,5,2]], 'B')
# C = Matriz([[9,2,3,67,67,5,34,2,0],[9,5,6,4,6,23,7,34,2],[8,8,9,45,4,7,2,8,0],[8,3,6,2,8,4,6,2,89],[7,3,7,3,1,3,5,3,0],[8,2,4,7,2,6,45,6,3],[8,7,6,45,23,7,3,2,0],[8,2,7,4,7,3,6,3,24],[9,5,4,2,6,12,4,8,1]], 'C')
# D = Matriz([[0,2,3,21],[2,0,5,7],[4,5,0,2],[2,5,6,0],[2,3,4,5]], 'D')
# E = Matriz([[1,2],[2,3],[24,2],[5,3],[6,7],[76,4],[7,0],[-9,-2],[-1,-4]], 'E')
# F = Matriz([[1,2,3,4,5,6,7,8,9]], 'F')

# coeficientes0 = Matriz([[3,2],[4,-3]], 'Coeficientes')
# resultados0 = Matriz([[7],[-2]], 'Resultados')
# variables0 = coeficientes0.get_inversa() * resultados0
# print(variables0) #Da 0,99999999999 para 1

# coeficientes1 = Matriz([[16,-6,4,1],[1,-8,1,1],[16,2,-4,1],[9,8,-3,1]], 'Coeficientes')
# resultados1 = Matriz([[-36],[-64],[-4],[-64]], 'Resultados')
# variables1 = coeficientes1.get_inversa() * resultados1
# variables1.rename('Solución')
# print(variables1)

# resultadosCcolumna = Matriz([[3],[34],[5],[12],[6],[43],[0],[12],[5]], 'Resultados')
# print(C.get_inversa() * resultadosCcolumna)
# print()

# resultadosCfila = Matriz([[3,34,5,12,6,43,0,12,5]])
# print(C.sist_ec_lineal(resultadosCfila))


# print(A)
# print(B)
# print(C)
# print(D)
# print(E)
# print(F)

# A[0] = [2,3,3,2,2]
# print(A)
# print(f'B-D')
# print(B-D)

# print(D.get_transpuesta())
# Ftrans = F.get_transpuesta()
# F.transpose() ?????????
# print(F)
# print(Ftrans)
# print(C*F)


# print(f'A*B')
# print(A*B)

# print(A.get_determinante())
# print(B.get_determinante())
# print(C.get_determinante())
# print(D.get_determinante())
# D.prod_escalar(2)
# print(D)
# print(C*E)
# print(C+E)

# print(A.get_inversa())
# print(B.get_inversa())
# print(C.get_inversa())
# print(D.get_inversa())

# arroz = Matriz([[1,0,3], [0,1,3]], 'Mi Matriz')
# print(arroz.Ndimension)