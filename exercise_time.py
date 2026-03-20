def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665
    total_horas =(total_segundos // 3600)
    minutos = ((total_segundos % 3600) // 60)
    sgundos = (total_segundos % 60)
    print(total_horas)
    print(minutos)
    print(sgundos)
time()