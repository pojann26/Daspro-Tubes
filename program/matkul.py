# matkul.py
# TIPE MATA KULIAH (Matkul)

# Import fungsi list dari list.py
from list import IsEmpty, LastElmt, NbElmt

# KONSTRUKTOR
def MakeMatkul(namamk, sks, listNilai):
    # MakeMatkul: string, integer, list of real -> Matkul
    # {MakeMatkul(nama, sks, listNilai) membuat objek Matkul}
    return [namamk, sks, listNilai]

# SELEKTOR
def GetNamaMK(MK):
    # GetNamaMK: Matkul -> string
    # {GetNamaMK(MK) mengambil nama mata kuliah dari MK}
    return MK[0]

def GetSKS(MK):
    # GetSKS: Matkul -> integer
    # {GetSKS(MK) mengambil jumlah SKS dari MK}
    return MK[1]

def GetNilai(MK):
    # GetNilai: Matkul -> list of real
    # {GetNilai(MK) mengambil list nilai dari MK}
    return MK[2]

# OPERATOR
def NilaiSekarangMK(MK):
    # NilaiSekarangMK: Matkul -> real
    # {NilaiSekarangMK(MK) mengambil nilai akhir dari MK}
    # {Jika list kosong -> -1.0}
    # {Jika tidak -> elemen terakhir}
    if IsEmpty(GetNilai(MK)):
        return -1.0
    else:
        return LastElmt(GetNilai(MK))


def SudahAmbilMK(MK):
    # SudahAmbilMK: Matkul -> boolean
    # {SudahAmbilMK(MK) mengembalikan True jika list nilai MK tidak kosong}
    return not IsEmpty(GetNilai(MK))

def MengulangMK(MK):
    # MengulangMK: Matkul -> boolean
    # {MengulangMK(MK) mengembalikan True jika panjang list nilai MK > 1}
    return NbElmt(GetNilai(MK)) > 1

def LulusMK(MK):
    # LulusMK: Matkul -> boolean
    # {LulusMK(MK) mengembalikan True jika nilai akhir MK >= 2.0}
    return NilaiSekarangMK(MK) >= 2.0

if __name__ == "__main__" : 
    MK1 = MakeMatkul("Daspro", 3, [2.0, 3.0])
    MK2 = MakeMatkul("Matdis",2,[])
    print(GetNamaMK(MK1))
    print(GetSKS(MK1))
    print(GetNilai(MK1))
    print(NilaiSekarangMK(MK1))
    print(NilaiSekarangMK(MK2))
    print(SudahAmbilMK(MK1))
    print(MengulangMK(MK1))
    print(LulusMK(MK1))