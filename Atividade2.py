import multiprocessing
import threading
import time

# Recurso compartilhado
recurso_compartilhado = 0
lock = threading.Lock()

# Função para a thread 1
def thread_func1():
    global recurso_compartilhado
    with lock:
        for _ in range(5):
            recurso_compartilhado += 1
            print(f"Thread 1 - Recurso Compartilhado: {recurso_compartilhado}")
            time.sleep(1)

# Função para a thread 2
def thread_func2():
    global recurso_compartilhado
    with lock:
        for _ in range(5):
            recurso_compartilhado += 1
            print(f"Thread 2 - Recurso Compartilhado: {recurso_compartilhado}")
            time.sleep(1)

# Função do processo 1 (que irá criar threads)
def process_func1():
    print("Processo 1 iniciado")
    
    # Criação de duas threads
    t1 = threading.Thread(target=thread_func1)
    t2 = threading.Thread(target=thread_func2)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Processo 1 finalizado")

# Função do processo 2
def process_func2():
    global recurso_compartilhado
    print("Processo 2 iniciado")
    
    # Acesso ao recurso compartilhado sincronizado com Lock
    with lock:
        for _ in range(5):
            recurso_compartilhado += 2
            print(f"Processo 2 - Recurso Compartilhado: {recurso_compartilhado}")
            time.sleep(1)
    
    print("Processo 2 finalizado")

if __name__ == '__main__':
    # Criação dos dois processos
    p1 = multiprocessing.Process(target=process_func1)
    p2 = multiprocessing.Process(target=process_func2)

    # Inicia os processos
    p1.start()
    p2.start()

    # Aguarda os processos terminarem
    p1.join()
    p2.join()

    print("Todos os processos e threads foram concluídos.")
