# transkrip.py
# TIPE TRANSKRIP

from list import IsEmpty, FirstElmt, Tail
from mahasiswa import *
from matkul import *

# KONSTRUKTOR
def MakeTranskrip(M, listMK):
    # MakeTranskrip: Mhs, list of Matkul -> Transkrip
    # {MakeTranskrip(M, listMK) membuat objek Transkrip}
    return [M, listMK]

# SELEKTOR
def GetMhs(T):
    # GetMhs: Transkrip -> Mhs
    # {GetMhs(T) mengambil data mahasiswa dari transkrip T}
    return T[0]

def GetListMatkul(T):
    # GetListMatkul: Transkrip -> list of Matkul
    # {GetListMatkul(T) mengambil list mata kuliah dari transkrip T}
    return T[1]

# OPERATOR
def CariMatkul(T, namaMK):
    # CariMatkul: Transkrip, string -> Matkul
    # {CariMatkul(T, namaMK) mencari Matkul dari transkrip T berdasarkan nama}
    def cariRekursif(listMK):
        if IsEmpty(listMK):
            return None
        elif GetNamaMK(FirstElmt(listMK)) == namaMK:
            return FirstElmt(listMK)
        else:
            return cariRekursif(Tail(listMK))
    
    return cariRekursif(GetListMatkul(T))

def TotalSKSLulus(T):
    # TotalSKSLulus: Transkrip -> integer
    # {TotalSKSLulus(T) menjumlahkan SKS dari mata kuliah yang lulus}
    def hitungRekursif(listMK):
        if IsEmpty(listMK):
            return 0
        else:
            if LulusMK(FirstElmt(listMK)):
                sks = GetSKS(FirstElmt(listMK))
            else:
                sks = 0
            return sks + hitungRekursif(Tail(listMK))
    
    return hitungRekursif(GetListMatkul(T))

def JumlahMatkulMengulang(T):
    # JumlahMatkulMengulang: Transkrip -> integer
    # {JumlahMatkulMengulang(T) menghitung jumlah mata kuliah yang diulang}
    def hitungRekursif(listMK):
        if IsEmpty(listMK):
            return 0
        else:
            if MengulangMK(FirstElmt(listMK)):
                tambah = 1
            else:
                tambah = 0
            return tambah + hitungRekursif(Tail(listMK))
    
    return hitungRekursif(GetListMatkul(T))

def IPKTranskrip(T):
    # IPKTranskrip: Transkrip -> real
    # {IPKTranskrip(T) menghitung IPK dari transkrip T}
    def hitungTotalNilaiXSKS(listMK):
        if IsEmpty(listMK):
            return 0.0
        else:
            if NilaiSekarangMK(FirstElmt(listMK)) >= 0:
                total = NilaiSekarangMK(FirstElmt(listMK)) * GetSKS(FirstElmt(listMK))
            else:
                total = 0
            return total + hitungTotalNilaiXSKS(Tail(listMK))
    
    def hitungTotalSKS(listMK):
        if IsEmpty(listMK):
            return 0
        else:
            if NilaiSekarangMK(FirstElmt(listMK)) >= 0:
                sks = GetSKS(FirstElmt(listMK))
            else:
                sks = 0
            return sks + hitungTotalSKS(Tail(listMK))
    
    if hitungTotalSKS(GetListMatkul(T)) == 0:
        return 0.0
    else:
        return hitungTotalNilaiXSKS(GetListMatkul(T)) / hitungTotalSKS(GetListMatkul(T))
    
if __name__ == "__main__" : 
    M = MakeMhs("A11.2020.01234", "Reno")
    MK1 = MakeMatkul("Daspro", 3, [2.0, 3.0])
    MK2 = MakeMatkul("Matdis", 2, [3.0, 4.0])
    MK3 = MakeMatkul("Kalkulus", 4, [3.5])
    T = MakeTranskrip(M, [MK1, MK2, MK3])

    print(GetMhs(T))
    print(GetListMatkul(T))
    print(CariMatkul(T, "Daspro"))
    print(TotalSKSLulus(T))
    print(JumlahMatkulMengulang(T))
    print(IPKTranskrip(T))