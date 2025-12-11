# settranskrip.py
# TIPE SET TRANSKRIP

from list import IsEmpty, FirstElmt, Tail, Konso, Konsi
from mahasiswa import GetNIM
from transkrip import *
from matkul import *

# KONSTRUKTOR
def MakeSetTranskrip():
    # MakeSetTranskrip: -> SetTranskrip
    # {MakeSetTranskrip() membuat SetTranskrip kosong (list kosong)}
    return []

# OPERATOR
def AddTranskrip(S, T):
    # AddTranskrip: SetTranskrip, Transkrip -> SetTranskrip
    # {AddTranskrip(S, T) menambahkan transkrip T ke akhir SetTranskrip S
    # jika NIM mahasiswa pada T belum ada di S. Jika sudah ada, tidak ditambahkan}}
    
    def sudahAda(nim, listT):
        if IsEmpty(listT):
            return False
        elif GetNIM(GetMhs(FirstElmt(listT))) == nim:
            return True
        else:
            return sudahAda(nim, Tail(listT))

    if sudahAda(GetNIM(GetMhs(T)), S):
        return S
    else:
        return Konsi(S, T)

def AddNilaiMatkul(S, nim, namaMK, nilai):
    # AddNilaiMatkul: SetTranskrip, string, string, real -> SetTranskrip
    # {AddNilaiMatkul(S, nim, namaMK, nilai) menambahkan nilai baru 
    # ke mata kuliah namaMK pada transkrip mahasiswa dengan NIM nim di
    # SetTranskrip S}
    
    def UpdateListMatkul(listMK, namaMK, nilaiBaru):
        if IsEmpty(listMK):
            return []
        MK = FirstElmt(listMK)
        if GetNamaMK(MK) == namaMK:
            return Konso(
                MakeMatkul(GetNamaMK(MK), GetSKS(MK), Konsi(GetNilai(MK), nilaiBaru)),Tail(listMK))
        else:
            return Konso(MK, UpdateListMatkul(Tail(listMK), namaMK, nilaiBaru))
        
    def UpdateSetTranskrip(S):
        if IsEmpty(S):
            return []
        T = FirstElmt(S)
        if GetNIM(GetMhs(T)) == nim:
            return Konso(
                MakeTranskrip(GetMhs(T), UpdateListMatkul(GetListMatkul(T), namaMK, nilai)),Tail(S))
        else:
            return Konso(T, UpdateSetTranskrip(Tail(S)))

    return UpdateSetTranskrip(S)

def CariTranskripMhs(S, nim):
    # CariTranskripMhs: SetTranskrip, string -> Transkrip
    # CariTranskripMhs(S, nim) mencari dan mengembalikan transkrip pertama 
    # dengan NIM nim dari SetTranskrip S}
    
    if IsEmpty(S):
        return None
    elif GetNIM(GetMhs(FirstElmt(S))) == nim:
        return FirstElmt(S)
    else:
        return CariTranskripMhs(Tail(S), nim)

def TopIPK(S):
    # TopIPK: SetTranskrip -> Mhs
    # {TopIPK(S) menghasilkan mahasiswa dengan IPK tertinggi dari SetTranskrip S }
    if IsEmpty(S):
        return None
    
    def maxRec(listT, mhsMax):
        if IsEmpty(listT):
            return mhsMax
        T = FirstElmt(listT)
        return maxRec(Tail(listT), T if IPKTranskrip(T) > IPKTranskrip(mhsMax) else mhsMax)

    return maxRec(Tail(S), FirstElmt(S))

def CountMhsPernahMengulang(S):
    # CountMhsPernahMengulang: SetTranskrip -> integer
    # {CountMhsPernahMengulang(S) menghitung jumlah mahasiswa yang
    # pernah mengulang minimal 1 mata kuliah pada SetTranskrip S}
    
    if IsEmpty(S):
        return 0
    else:
        T = FirstElmt(S)
        if JumlahMatkulMengulang(T) > 0:
            return 1 + CountMhsPernahMengulang(Tail(S))
        else:
            return CountMhsPernahMengulang(Tail(S))

def CountMhsLulusSemuaMatkul(S):
    # CountMhsLulusSemuaMatkul: SetTranskrip -> integer
    # {CountMhsLulusSemuaMatkul(S) menghitung jumlah mahasiswa yang
    # lulus seluruh mata kuliah yang diambil pada SetTranskrip S}
    
    def semuaLulus(listMK):
        if IsEmpty(listMK):
            return True
        elif not LulusMK(FirstElmt(listMK)):
            return False
        else:
            return semuaLulus(Tail(listMK))
    
    if IsEmpty(S):
        return 0
    else:
        T = FirstElmt(S)
        if not IsEmpty(GetListMatkul(T)) and semuaLulus(GetListMatkul(T)):
            return 1 + CountMhsLulusSemuaMatkul(Tail(S))
        else:
            return CountMhsLulusSemuaMatkul(Tail(S))

def MatkulPalingSeringDiulang(S):
    # MatkulPalingSeringDiulang: SetTranskrip -> string
    # {MatkulPalingSeringDiulang(S) menghasilkan nama mata kuliah yang
    # paling sering diulang (frekuensi tertinggi) pada SetTranskrip S}

    def kumpulkanMatkulDiulang(listT):
        if IsEmpty(listT):
            return []
        else:
            T = FirstElmt(listT)
            def ambilMatkulDiulang(listMK):
                if IsEmpty(listMK):
                    return []
                elif MengulangMK(FirstElmt(listMK)):
                    return Konso(GetNamaMK(FirstElmt(listMK)), ambilMatkulDiulang(Tail(listMK)))
                else:
                    return ambilMatkulDiulang(Tail(listMK))
            
            return ambilMatkulDiulang(GetListMatkul(T)) + kumpulkanMatkulDiulang(Tail(listT))
    
    # utk ngitung frekuensi
    def hitungFrekuensi(nama, listNama):
        if IsEmpty(listNama):
            return 0
        elif FirstElmt(listNama) == nama:
            return 1 + hitungFrekuensi(nama, Tail(listNama))
        else:
            return hitungFrekuensi(nama, Tail(listNama))
    
    # cari nama frekuensi tertinggi
    def cariMaxFrekuensi(listNama, allNama):
        if IsEmpty(listNama):
            return None
        else:
            if IsEmpty(Tail(listNama)):
                return FirstElmt(listNama)
            else:
                if hitungFrekuensi(FirstElmt(listNama), allNama) > hitungFrekuensi(cariMaxFrekuensi(Tail(listNama), allNama), allNama):
                    return FirstElmt(listNama)
                else:
                    return cariMaxFrekuensi(Tail(listNama), allNama)
    
    listNama = kumpulkanMatkulDiulang(S)
    if IsEmpty(listNama):
        return None
    else:
        return cariMaxFrekuensi(listNama, listNama)

def CountMhsDenganIPKRentang(S, a, b):
    # CountMhsDenganIPKRentang: SetTranskrip, real, real -> integer
    # {CountMhsDenganIPKRentang(S, a, b) menghitung jumlah mahasiswa 
    # dengan IPK dalam rentang [a, b]}
    
    if IsEmpty(S):
        return 0
    else:
        T = FirstElmt(S)
        ipk = IPKTranskrip(T)
        if a <= ipk <= b:
            return 1 + CountMhsDenganIPKRentang(Tail(S), a, b)
        else:
            return CountMhsDenganIPKRentang(Tail(S), a, b)


if __name__ == "__main__":

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
    
    # Coba tambah lagi (harusnya tidak bertambah)
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
    
    # Menambah nilai
    S6 = AddNilaiMatkul(S5, "A11.01", "Daspro", 3.0)
    S7 = AddNilaiMatkul(S6, "A11.02", "Daspro", 4.0)
    
    # Cari transkrip
    print(CariTranskripMhs(S7, "A11.01")) #Transkrip Reno
    print(CariTranskripMhs(S7, "A11.03")) #Transkrip Budi
    
    # Top IPK
    print(TopIPK(S7)) #Andi, IPK = 3.0
    # Count mengulang
    print(CountMhsPernahMengulang(S7)) #(Semua mengulang Daspro)
    # Count lulus semua
    print(CountMhsLulusSemuaMatkul(S7)) #(Semua Lulus)
    # Matkul paling sering diulang
    print(MatkulPalingSeringDiulang(S7)) #(Diulang oleh 3 mahasiswa)
    # Count IPK rentang
    print(CountMhsDenganIPKRentang(S7, 2.0, 3.0)) #(Reno Dan Budi)