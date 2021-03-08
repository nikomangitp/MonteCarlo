
import numpy as np
from prettytable import PrettyTable

print("Pemograman Simulasi")
print("Nama: Ni Komang Intan Tri Pujiani")
print("NRP: 152017096")

#Data Himpunan Awal
minta = [25, 35, 40, 45, 30, 55, 20, 15, 10, 50, 25, 55, 60, 30]
frequensi = [21, 12, 17, 4 ,24, 1, 11, 6, 8, 21, 12, 9, 4,9]

ngacak = []
interval = []
simulasi = []
untung = []

mingguke = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# Himpunan distribusi kumulatif dengan nilai awal 0
kumulatif= [0]

#Deklarasi variabel awal
freqtot = 0
distp = 0
freqi = 0
dari=0
alpha = 43
c = 37
m = 61
nilais = 0


#Fungsi untuk Menghitung Probabilitas
def kemungkinan(freq, n):
    return freq/n
    
#Fungsi untuk Mengh? ?itung angka acak dengan rumus
def angacak(x,a,c):
    return (x*a+c)
    
def mod(x,m):
    return x % m

#Fungsi untuk Mencari nilai dalam interval
def find(minta,kumulatif,interval,angka):
    for i in range(8):
        if (kumulatif[i] <= angka <=interval[i]):
            nilai = minta[i]
        else:
            pass
    return nilai

# Menghitung jumlah Frequensi
for i in range(len(frequensi)):
    freqtot += frequensi[i]
print(freqtot)

#Menghitung Probabilitas, Kumulatif dan Interval angka Acak
table1 = PrettyTable(['No', 'Permintaan','Frekuensi','Probabilitas','Probabilitas Kumulatif'])
table2 = PrettyTable(['No', 'Permintaan','Probabilitas','Probabilitas Kumulatif','Interval Angka'])

for i in range(len(minta)):
    dist = kemungkinan(frequensi[i], freqtot)
    distp += dist
    kum = round(distp, 2)
    sampai = int(kum*100)
    interval.append(sampai)
    table1.add_row([i+1,minta[i], frequensi[i], round(dist,2), kum])
    table2.add_row([i+1,minta[i], round(dist,2), kum, f'{kumulatif[i]} - {sampai}'])
    kumulatif.append(int(kum*100+1))
print(table1)
print('Total Frequensi =', freqtot)
print(table2)

#Menghitung Angka Acak
acak = np.random.randint(100)
ngacak.append(acak)

table3 = PrettyTable(['No', 'Xa+C mod M','Xi','Ui=Xi/M'])
for i in range(len(minta)):
    acak = angacak(ngacak[i],alpha,c)
    xi = mod(acak,m)
    ngacak.append(xi)
    u = round(xi / m,3)
    table3.add_row([i+1, acak, xi , u])
print(ngacak[0])
ngacak.pop(0)
print(table3)

table4 = PrettyTable(['No', 'Permintaan','Interval Angka Acak','Bilangan Acak','Simulasi Permintaan'])
for i in range(len(minta)):
    nilai = find(minta,kumulatif,interval,ngacak[i])
    table4.add_row([i+1,minta[i], f'{kumulatif[i]}-{interval[i]}', ngacak[i], nilai])
    simulasi.append(nilai)
    nilais +=nilai
print(table4)

