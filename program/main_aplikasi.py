from mahasiswa import *
from transkrip import *
from matkul import *
from set_transkrip import *


print("==== APLIKASI MAHASISWA ====")
if __name__ == "__main__" : 
    M1 = MakeMhs("A11.2020.01234", "Reno")
    print(M1)
    print(GetNIM(M1))
    print(GetNama(M1))

print("==== APLIKASI MATKUL ====")
if __name__ == "__main__" :
    MK1 = MakeMatkul("Daspro", 3, [2.0, 3.0])
    MK2 = MakeMatkul("Matdis",2,[])
    print(GetNamaMK(MK1))
    print(GetSKS(MK1))
    print(GetNilai(MK1))
    print(NilaiSekarangMK(MK1))
    print(NilaiSekarangMK(MK2))
    print(SudahAmbilMK(MK2))
    print(MengulangMK(MK1))
    print(LulusMK(MK1))

print("==== APLIKASI TRANSKRIP ====")
if __name__ == "__main__" :
    M = MakeMhs("A11.2020.01234", "Reno")
    MK1 = MakeMatkul("Daspro", 3, [2.0, 3.0])
    MK2 = MakeMatkul("Matdis", 2, [3.0, 4.0])
    T = MakeTranskrip(M, [MK1, MK2])

    print(GetMhs(T))
    print(GetListMatkul(T))
    print(CariMatkul(T, "Daspro"))
    print(TotalSKSLulus(T))
    print(JumlahMatkulMengulang(T))
    print(IPKTranskrip(T))

print("==== APLIKASI SET_TRANSKRIP ====")
if __name__ == "__main__" :
    # set transkrip kosong
    S1 = MakeSetTranskrip()
    print("S1 (kosong):", S1)
    
    # Membuat mahasiswa dan transkrip
    M1 = MakeMhs("A11.01", "Reno")
    MK1 = MakeMatkul("Daspro", 3, [2.0])
    MK2 = MakeMatkul("Matdis", 2, [3.0])
    T1 = MakeTranskrip(M1, [MK1, MK2])
    
    # Menambah transkrip
    S2 = AddTranskrip(S1, T1)
    print("Jumlah transkrip:", len(S2))
    
    # Coba tambah lagi (harusnya gak bertambah)
    S3 = AddTranskrip(S2, T1)
    print("Coba tambah T1 lagi, jumlah:", len(S3))
    
    # Tambah mahasiswa kedua
    M2 = MakeMhs("A11.02", "Andi")
    MK3 = MakeMatkul("Daspro", 3, [3.0])
    MK4 = MakeMatkul("Matdis", 2, [4.0])
    T2 = MakeTranskrip(M2, [MK3, MK4])
    S4 = AddTranskrip(S3, T2)
    print("Setelah tambah T2, jumlah:", len(S4))
    
    # Tambah mahasiswa ketiga
    M3 = MakeMhs("A11.03", "Budi")
    MK5 = MakeMatkul("Daspro", 3, [1.0, 2.0])
    MK6 = MakeMatkul("Kalkulus", 4, [3.0])
    T3 = MakeTranskrip(M3, [MK5, MK6])
    S5 = AddTranskrip(S4, T3)

    S6 = AddNilaiMatkul(S5, "A11.01", "Daspro", 3.0)
    S7 = AddNilaiMatkul(S6, "A11.02", "Daspro", 4.0)
    
    print(CariTranskripMhs(S7, "A11.01")) #Transkrip Reno
    print(CariTranskripMhs(S7, "A11.03")) #Transkrip Budi
    
    print(TopIPK(S7)) #Andi, IPK = 3.0
    print(CountMhsPernahMengulang(S7)) #(Semua mengulang Daspro)
    print(CountMhsLulusSemuaMatkul(S7)) #(Semua Lulus)
    print(MatkulPalingSeringDiulang(S7)) #(Diulang oleh 3 mahasiswa)
    print(CountMhsDenganIPKRentang(S7, 2.0, 3.0)) #(Reno Dan Budi)