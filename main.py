print("Ahoj, esp32: pripajam modul dht22...") # Tento riadok vypisuje správu, ktorá oznamuje začiatok skriptu
from machine import Pin  # importujeme triedu Pin z knižnice machine
from time import sleep  # importujeme funkciu sleep z knižnice time
import time # importujeme knižnicu time
import dht  # importujeme knižnicu dht
sensor = dht.DHT22(Pin(27))  # Inicializujeme senzor DHT22 a udávame, že je pripojený na pin 27

i = 1  # Inicializujeme premennú i na 1

while True:  # Vstup do nekonečnej slučky
  try:
    current_time = time.localtime() # získanie aktuálneho času
    sleep(6)  # Spánok 6 sekúnd
    sensor.measure()  # Iniciácia merania
    temp = sensor.temperature()  # Čítanie údajov o teplote
    hum = sensor.humidity()  # Čítanie údajov o vlhkosti
    temp_f = temp * (9/5) + 32.0  # Prevod teploty zo stupňov Celzia na stupne Fahrenheita
    print('Meranie %d' % i)  # Výpis poradové číslo merania
    print("Dátum a čas: " + str(current_time[2]) + "/" + str(current_time[1]) + "/" + str(current_time[0]) + " " + str(current_time[3]) + ":" + str(current_time[4]) + ":" + str(current_time[5])) # výpis dátumu a času v jednom riadku
    print('Teplota: %3.1f C' %temp)  # Výpis teploty v stupňoch Celzia
    print('Teplota: %3.1f F' %temp_f)  # Výpis teploty v stupňoch Fahrenheita
    print('Vlhkosť: %3.1f %%' %hum)  # Výpis vlhkosti
    print('-------------------')  # Oddeľenie jednotlivých meraní
    i += 1  # zvýšenie premennej i o 1
  except OSError as e:  # Ak nastane chyba pri pokuse o čítanie údajov zo senzora
    print('Nepodarilo sa prečítať senzor.')  # Výpis chybovej správy


