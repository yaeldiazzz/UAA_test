from __future__ import absolute_import

class App:
    @staticmethod
    def add(a,b):
        return a+b

    def resta(a,b):
        return a-b

    def multiplicacion(a,b):
        return a*b

    def division(a,b):
        return a/b

    # 1. Verifica si una lista contiene un número primo
    def contiene_numero_primo(lista):
     """
     Verifica si hay al menos un número primo en la lista.
     Retorna True si hay un número primo, de lo contrario, False.
     """
     def es_primo(n):
        """Verifica si un número es primo."""
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
     for numero in lista:
        if es_primo(numero):
           return True
     return False

        
    pass

    # 2. Cuenta los números pares en un rango dado
    def contar_pares(inicio, fin):
     """
     Cuenta la cantidad de números pares en el rango desde 'inicio' hasta 'fin' (inclusive).
     Retorna la cantidad de números pares.
     """
     # Inicializamos un contador
     contador = 0

     # Iteramos desde inicio hasta fin (inclusive)
     for num in range(inicio, fin + 1):
        if num % 2 == 0:  # Verificamos si el número es par
            contador += 1

     return contador
    
    pass

    # 3. Encuentra el número máximo en una lista que sea múltiplo de un valor dado
    def maximo_multiplo(lista, multiplo):
     """
     Encuentra y retorna el valor máximo de la lista que es múltiplo del parámetro 'multiplo'.
     Si no hay múltiplos, retorna None.
     """
     # Filtramos los números que son múltiplos del valor dado
     multiplos = [num for num in lista if num % multiplo == 0]
    
     # Si hay múltiplos, retornamos el máximo; de lo contrario, retornamos None
     return max(multiplos) if multiplos else None
    pass

    # 4. Verifica si una palabra es palíndroma (se lee igual en ambos sentidos)
    def es_palindromo(palabra):
        """
        Verifica si la palabra es un palíndromo (igual al leerla al revés).
        Retorna True si es palíndromo, de lo contrario, False.
        """
        # Comparamos la palabra con su reverso
        return palabra == palabra[::-1]
    pass

    # 5. Calcula la suma de los primeros n números impares
    def suma_primeros_impares(n):
     """
     Calcula y retorna la suma de los primeros 'n' números impares.
     """
     suma = 0
     for i in range(1, 2 * n, 2):  # Generamos los primeros 'n' números impares
        suma += i
     return suma
    pass

    # 6. Verifica si todos los elementos de una lista son únicos
    def elementos_unicos(lista):
        """
        Verifica si todos los elementos de la lista son únicos.
        Retorna True si son únicos, de lo contrario, False.
        """
        pass

    # 7. Calcula el factorial de un número sin usar recursión
    def calcular_factorial(numero):
        """
        Calcula y retorna el factorial de 'numero' usando un ciclo.
        """
        pass

    # 8. Cuenta la cantidad de vocales en una cadena
    def contar_vocales(cadena):
        """
        Cuenta y retorna la cantidad de vocales en la cadena.
        """
        pass

    # 9. Encuentra el segundo número mayor en una lista
    def segundo_mayor(lista):
        """
        Encuentra y retorna el segundo número más grande en la lista.
        Si no existe, retorna None.
        """
        pass

    # 10. Calcula la serie de Fibonacci hasta n términos
    def fibonacci(n):
        """
        Genera y retorna una lista con los primeros 'n' términos de la serie de Fibonacci.
        """
        pass
