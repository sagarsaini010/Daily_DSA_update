import threading as th
import time
def print_letters():
    for letter in "ABCDE":
        time.sleep(1)
        print(f"Letter: {letter}")

def print_number():
    for i in range(1,6):
        time.sleep(1)
        print(f"Number: {i}")

def print_sagar():
    for i in range(1,6):
        time.sleep(1)
        print(f"Number: sagar")


def print_raman():
    for i in range(1,6):
        time.sleep(1)
        print(f"Number: raman")

def print_bhakti():
    for i in range(1,6):
        time.sleep(1)
        print(f"Number: bhakti")

def print_python():
    for i in range(1,6):
        time.sleep(1)
        print(f"Number: python")

def print_akash():
    for i in range(1,6):
        time.sleep(1)
        print(f"Number: akash")

def print_william():
    for i in range(1,6):
        time.sleep(1)
        print(f"Number: William")


def print_java():
    for i in range(1,6):
        time.sleep(1)
        print(f"Number: java")

def print_c():
    for i in range(1,6):
        time.sleep(1)
        print(f"Number: c")



thread1 = th.Thread(target=print_number)
thread2 = th.Thread(target=print_letters)
thread3 = th.Thread(target=print_sagar)
thread4 = th.Thread(target=print_bhakti)
thread5 = th.Thread(target=print_raman)
thread6 = th.Thread(target=print_python)
thread7 = th.Thread(target=print_william)
thread8 = th.Thread(target=print_c)
thread9 = th.Thread(target=print_java)
thread10 = th.Thread(target=print_akash)

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()
thread10.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()
thread7.join()
thread8.join()
thread9.join()
thread10.join()

print("10 threads are done!")