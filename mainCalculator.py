import numpy as np
import sys
import math
import scipy

print("\033c")

class Calculator:
    def __init__(self):
        self.menu()

    def menu(self):

        print("\033c")
        print('=' * 100)
        print("Menu kalkulator. Masukkan salah satu angka yang tertera dalam menu untuk memilih.\n1. Perkalian\n2. Pembagian\n3. Penambahan\n4. Pengurangan\n5. Volume Bola\n6. Faktorial\n7. Logaritma\n8. Convert Trigonometry\n")
        print("X or x. Keluar kode")
        print('=' * 100)
        userInput = input(">>> ")
        if userInput == '1':
            self.perkalian()
        elif userInput == '2':
            self.pembagian()
        elif userInput == '3':
            self.penambahan()
        elif userInput == 'x' or userInput == 'X':
            sys.exit("Calculator terminated.")
        elif userInput == '4':
            self.pengurangan()
        elif userInput == '5':
            self.volumeBola()
        elif userInput == '6':
            self.faktorials()
        elif userInput == '7':
            self.logaritma()
        elif userInput == '8':
            self.convTrigonometric()
        else:
           self.menu()    


    def perkalian(self):

        print("\033c")
        
        list_angka = []
        
        
        try:
            brpdigit = int(input("Masukkan banyak angka yang ingin dikalikan: "))
            for i in range(1 ,brpdigit + 1):
                a = float(input(f"Masukkan angka ke-{i}: "))
                list_angka.append(a)
                hasil = np.prod(list_angka)
            print(f"Hasil perkalian tersebut adalah: {hasil}")
            back = input("Perkalian berhasil dieksekusi. Mengulang kembali? [Y/N]: ")
        except ValueError:
            print("Input yang dimasukkan bukan angka.")
            back = input("Kalkulasi gagal. Mengulang kembali? [Y/N]: ")

        if back == 'Y' or back == 'y':
            return(self.perkalian())
        else:
            self.menu()

    def pembagian(self):

        print("\033c")
        
        list_angka = []
        
        brpdigit = int(input("Masukkan banyak angka yang ingin dibagikan: "))
        pembagi = int(input("Masukkan banyak angka pembagi: "))
        
        try:
            for i in range(1 ,brpdigit + 1):
                a = float(input(f"Masukkan angka ke-{i}: "))
                list_angka.append(a)
                array = np.array(list_angka)
                hasil = array/pembagi
            print(f"Hasil pembagian tersebut adalah: {hasil}")
            back = input("Pembagian berhasil dieksekusi. Mengulang kembali? [Y/N]: ")
        except ValueError:
            print("Input yang dimasukkan bukan angka.")
            back = input("Kalkulasi gagal. Mengulang kembali? [Y/N]: ")

        if back == 'Y' or back == 'y':
            return(self.pembagian())
        else:
            self.menu()

    def penambahan(self):

        print("\033c")
        
        list_angka = []
        brpdigit = int(input("Masukkan banyak angka yang ingin ditambahkan: "))
        
        try:
            for i in range(1 ,brpdigit + 1):
                a = float(input(f"Masukkan angka ke-{i}: "))
                list_angka.append(a)
                hasil = sum(list_angka)
            print(f"Hasil tambah tersebut adalah: {hasil}")
            back = input("penambahan berhasil dieksekusi. Mengulang kembali? [Y/N]: ")
        except ValueError:
            print("Input yang dimasukkan bukan angka.")
            back = input("Kalkulasi gagal. Mengulang kembali? [Y/N]: ")

        if back == 'Y' or back == 'y':
            return(self.penambahan())
        else:
            self.menu()

    def pengurangan(self):

        print("\033c")
        
        brpdigit = int(input("Masukkan banyak angka yang ingin dikurang: "))
        
        try:
            for i in range(1 ,brpdigit + 1):
                a = float(input(f"Masukkan angka ke-{i}: "))
                hasil = float(a - a)
            print(f"Hasil pengurangan tersebut adalah: {hasil}")
            back = input("pengurangan berhasil dieksekusi. Mengulang kembali? [Y/N]: ")
        except ValueError:
            print("Input yang dimasukkan bukan angka.")
            back = input("Kalkulasi gagal. Mengulang kembali? [Y/N]: ")

        if back == 'Y' or back == 'y':
            return(self.pengurangan())
        else:
            self.menu()

    def volumeBola(self):

        print("\033c")

        try:
            print('Volume Bola\n', '=' * 10)
            jariR = int(input("Masukkan jari - jari: "))
            volBola = 4/3 * math.pi * jariR**3
            print(f"Volume Bola : {volBola:.2f}")
            back = input("pengurangan berhasil dieksekusi. Mengulang kembali? [Y/N]: ")
        except ValueError:
            print("Input yang dimasukkan bukan angka.")
            back = input("Kalkulasi gagal. Mengulang kembali? [Y/N]: ")
        
        if back == 'Y' or back == 'y':
            return(self.pengurangan())
        else:
            self.menu()
        
    def faktorials(self):

        print("\033c")

        brpdigit = int(input("Masukkan banyak angka yang ingin di-faktorial: "))

        try:
            for i in range(1 , brpdigit):
                a = int(input(f"Masukkan angka ke-{i}: "))
                hasil = math.factorial(a)

            print(f"Hasil faktorial tersebut adalah: {hasil}")
            back = input("faktorial berhasil dieksekusi. Mengulang kembali? [Y/N]: ")
        except ValueError:
            print("Input yang dimasukkan bukan angka.")
            back = input("Kalkulasi gagal. Mengulang kembali? [Y/N]: ")

        if back == 'Y' or back == 'y':
            return(self.faktorials())
        else:
            self.menu()

    def logaritma(self):

        print("\033c")
        try:
            setBase = int(input("Masukkan banyak base logaritma: "))
            setNumber = int(input("Masukkan angka logaritma: "))

            hasil = math.log(setBase, setNumber)
            print(f"Hasil logaritma tersebut adalah: {hasil}")
            back = input("logaritma berhasil dieksekusi. Mengulang kembali? [Y/N]: ")
        except ValueError:
            print("Input yang dimasukkan bukan angka.")
            back = input("Kalkulasi gagal. Mengulang kembali? [Y/N]: ")

        if back == 'Y' or back == 'y':
            return(self.logaritma())
        else:
            self.menu() 

    def convTrigonometric(self):
        print("\033c")

        selectionOps = int(input("Masukkan pilihan: \n1. Sine\n2. Cosine\n3. Tangent\n4. Arc\n>>> "))
        
        try:
            if selectionOps == 1:
                print(f"Hasil sine adalah: {math.sin(float(input('Masukkan angka: ')))}")
            elif selectionOps == 2:
                print(f"Hasil cosine adalah: {math.cos(float(input('Masukkan angka: ')))}")
            elif selectionOps == 3:
                print(f"Hasil tangent adalah: {math.tan(float(input('Masukkan angka: ')))}")
            elif selectionOps == 4:
                print("\033c")
                pilihanArc = int(input("Masukkan pilihan: \n1. Arc Sine\n2. Arc Cosine\n3. Arc Tangent\n>>> "))

                if pilihanArc == 1:
                    print(f"Hasil sine adalah: {math.asin(float(input('Masukkan angka: ')))}")
                elif pilihanArc == 2:
                    print(f"Hasil cosine adalah: {math.acos(float(input('Masukkan angka: ')))}")
                elif pilihanArc == 3:
                    print(f"Hasil tangent adalah: {math.atan(float(input('Masukkan angka: ')))}")

            back = input("Kalkulasi selesai. Mengulang kembali? [Y/N]: ")
        except ValueError:
            print("Input yang dimasukkan bukan angka.")
            back = input("Kalkulasi gagal. Mengulang kembali? [Y/N]: ")
        
        if back == 'Y' or back == 'y':
            return(self.convTrigonometric())
        else:
            self.menu()

Calculator()