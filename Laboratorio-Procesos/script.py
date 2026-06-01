import sys
import time
import os
import multiprocessing

def estresar_cpu(id_hilo):
    print(f" -> [CPU] Hilo {id_hilo} iniciado (PID: {os.getpid()}). Calculando...")
    while True:
        x = 0.0001
        for i in range(1000000):
            x = x * 1.000001
            x = x / 1.000001

def estresar_ram(megabytes):
    print(f" -> [RAM] Intentando reservar {megabytes} MB de memoria física...")
    try:
        bloque_datos = bytearray(megabytes * 1024 * 1024)
        for i in range(0, len(bloque_datos), 4096):
            bloque_datos[i] = 1
        print(f" -> [RAM] {megabytes} MB asignados con éxito.")
        print(" -> [RAM] Manteniendo reserva por 60 segundos...")
        time.sleep(60)
    except MemoryError:
        print(" -> [RAM] Error: Memoria RAM insuficiente.")

if __name__ == "__main__":
    print(f"=== SCRIPT DE CAOS OPERATIVO (PID PADRE: {os.getpid()}) ===")
    
    # Lanzamos el proceso de RAM (512 MB)
    proceso_ram = multiprocessing.Process(target=estresar_ram, args=(512,))
    proceso_ram.start()
    
    # Lanzamos 4 procesos para CPU (4 núcleos)
    procesos_cpu = []
    for num in range(4):
        p = multiprocessing.Process(target=estresar_cpu, args=(num,))
        p.start()
        procesos_cpu.append(p)
        
    time.sleep(60)
    
    print("\n=== Terminando subprocesos... ===")
    proceso_ram.terminate()
    for p in procesos_cpu:
        p.terminate()
    print("=== Script finalizado ===")