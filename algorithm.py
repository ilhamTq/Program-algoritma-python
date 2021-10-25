#Nama : Ilham Taufiq
#Kelas : A TI Pagi
#Prodi : Teknik Informatika

import random
import timeit
from anytree import Node, RenderTree

jkel = int(input("Masukkan jumlah anggota keluarga: "))
dkel = []
for i in range(0, jkel):
    print("\n")
    print("Data Anggota ke -", i+1, ":")
    elemen = [input("Inisial :"), int(input("Tahun Lahir :"))]
    dkel.append(elemen)
    
print("\n")
print("List Anggota Keluarga :")
print(*dkel, sep="\n")

random.shuffle(dkel)
print("\n")
print("Hasil list acak :")
print(*dkel, sep="\n")

dkel_sort1 = dkel
dkel_sort2 = dkel

def bubblesort(aList):
    l = len(aList)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (aList[j][1] > aList[j + 1][1]):
                tempo = aList[j]
                aList[j] = aList[j + 1]
                aList[j + 1] = tempo
    return aList

def selectionsort(aList):
    l = len(aList)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (aList[j][1] > aList[j + 1][1]):
                tempo = aList[j]
                aList[j] = aList[j + 1]
                aList[j + 1] = tempo
    return aList

mulai_sorting_1 = timeit.default_timer()
bubblesort(dkel_sort1)
berhenti_sorting_1 = timeit.default_timer()
waktu_sorting_1 = berhenti_sorting_1 - mulai_sorting_1

print("\n")
print("Hasil list Bubble Sort: ")
print(*dkel_sort1, sep="\n")

mulai_sorting_2 = timeit.default_timer()
bubblesort(dkel_sort1)
berhenti_sorting_2 = timeit.default_timer()
waktu_sorting_2 = berhenti_sorting_2 - mulai_sorting_2

print("\n")
print("Hasil list Selection Sort: ")
print(*dkel_sort2, sep="\n")

print("\n")
print("Waktu sorting Bubble Sort  = %f" % waktu_sorting_1)
print("Waktu sorting Selection Sort  = %f" % waktu_sorting_2)
print("\n")

A = Node(dkel[0])
B = Node(dkel[2], parent=A)
C = Node(dkel[4], parent=A)
D = Node(dkel[5], parent=A)
E = Node(dkel[3], parent=A)
F = Node(dkel[7], parent=B)
G = Node(dkel[8], parent=B)
H = Node(dkel[9], parent=B)
I = Node(dkel[10], parent=B)
J = Node(dkel[11], parent=B)

for pre, fill, node in RenderTree(A):
    print("%s%s" % (pre, node.name))