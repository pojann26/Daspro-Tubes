# Nama File : list.py
# Deskripsi : berisi type dan operasi list
# Pembuat   : Muhammad Fauzan Akbar-24060124140139
# Tanggal   : 6 Novermber 2025

# DEFINISI DAN SPESIFIKASI TYPE
# Konstruktor menambahkan elemen di awal, notasi prefix
# type List: [] atau [e o list]
# Konstruktor menambahkan elemen di akhir, notasi postfix
# type list: [] atau [list o e]

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Konso : elemen, List -> List
# Konso(e, L) menghasilkan sebuah list dari e dan L dengan e sebagai elemen pertama
# Realisasi
def Konso(e, L) : 
    return [e] + L

# Konsi : List, elemen -> List
# Konsi(L, e) -> menghasilkan sebuah list dari L dan e dengan e sebagai elemen terakhir
# Realisasi
def Konsi(L, e) :
    return L + [e]

# DEFINISI DAN SEPESIFIKASI SELEKTOR 
# FirstElmt: List tidak kosong -> elemen
# FirstElmt(L) -> menghasilkan elemen pertama dari list L
# Realisasi
def FirstElmt(L) :
    return L[0]

# Tail : List tidak kosong -> List
# Tail(L) : menghasilkan list tanpa elemen pertama list L, mungkin kosong
# Realisasi 
def Tail(L) :
    return L[1:]

# LastElmt : List tidak kosong -> elemen
# LastElmt(L) -> menghasilkan elemen terakhir dari list L
# Realisasi
def LastElmt(L) :
    return L[-1]

# Head : List tidak kosong -> List
# Head(L) -> menghasilkan list tanpa elemen terakhir list L, mungkin kosong
# Realisasi 
def Head(L) :
    return L[:-1]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEmpty : List -> boolean 
# IsEmpty(L) -> benar jika list kosong
# Realisasi 
def IsEmpty(L) :
    return L == []

# ISOneElmt: List -> boolean
# IsOneElmt(X, L) -> adalah benar jika list L hanya mempunyai satu elemen
# Realisasi 
def IsOneElmt(L) :
    if IsEmpty(L) :
        return False
    else : 
        return Tail(L) == [] and Head(L) == []

# IsMember : elemen, List -> boolean
# IsMember (X, L) : benar jika X adalah elemen list L
def isMember(e, L) : 
    if IsEmpty(L) : 
        return False
    else : 
        if e == FirstElmt(L) : 
            return True
        else : 
            return isMember(e, Tail(L))

# IsPalindrom(L) : List of character -> boolean
# Ispalindrom(L) benar jika L merupakan kata palindrom yaitu kata yang sama jika dibaca dari kiri atau kanan 
#   contoh : RUSAK, KASUR RUSAK, NABABAN
def IsPalindrom(L) : 
    if IsEmpty(L) :
        return True
    else : 
        if FirstElmt(L) == FirstElmt(Inverse(L)) : 
            return IsPalindrom(Head(Tail(L)))
    
# DEFINISI DAN SPESIFIKASI OPERATOR
# DEFINISI DAN SPESIFIKASI FUNGSI YANG MENGOPERASIKAN LIST
# NbElmt : List -> integer
# NbElmt(L) -> menghasilkan banyaknya elemen list, nol jika kosong
# Realisasi
def NbElmt(L) :
    if IsEmpty(L) :
        return 0
    else : 
        return 1 + NbElmt(Tail(L))
    
# ElmtKeN : integer >= 0, List -> elemen
# ElmtKeN (N, L) : Mengirimkan elemen list yang ke N, N <= NbElmt(L) dan N >= 0
def ElmtkeN(n, L) : 
    if IsEmpty(L) : 
        return []
    else :
        if n == 1 :
            return FirstElmt(L)
        else : 
            return ElmtkeN(n - 1, Tail(L))

# Copy : List -> List
# Copy(L) : menghasilkan list yang identik dengan list asal
def Copy(L) :
    if IsEmpty(L) : 
        return L
    else : 
        return Konso(FirstElmt(L), Copy(Tail(L)))

# Inverse : List -> List
# Inverse(L) : menghasilkan list L yang dibalik, yaitu yang urutan elemen nya adalah kebalikan dari list asal
def Inverse(L) :
    if IsEmpty(L) : 
        return L
    else : 
        return Konsi(Inverse(Tail(L)), FirstElmt(L))

# Konkat : 2 List -> List
# Konkat (L1, L2) : menghasilkan konkatenasi 2 buah list, dengan list L2 "sesudah" list L1
def Konkat(L1, L2) :
    if IsEmpty(L2) :
        return L1
    else :
        return Konkat(Konsi(L1, FirstElmt(L2)), Tail(L2))

# AddList : 2 List of integer -> List of Integer
# AddLIst(L1, L2) menghasilkan list baru yang setiap elemen nya adalah hasil penjumlahan setiap elemn di L1 dan L2 pada posisi yang sama
def AddList(L1, L2) : 
    if IsEmpty(L1) :
        return []
    else : 
        return Konso(FirstElmt(L1) + FirstElmt(L2), AddList(Tail(L1), Tail(L2)))

# SumElmt : List of integer -> integer
# SumElmt(L) menghasilkan jumlahan dari setiap elemen di list L
def SumElmt(L) :
    if IsEmpty(L) :
        return 0
    else :
        return FirstElmt(L) + SumElmt(Tail(L))

# AvgElmt : List of integer -> integer
# AvgElmt(L) menghasilkan nilai rata rata
def AvgElmt(L) :
    if IsEmpty(L) :
        return 0
    else :
        return SumElmt(L) / NbElmt(L)

# MaxElmt(L) : List of integer -> integer 
# MaxElmt(L) mengembalikan elemen maksimum dari list L
def MaxElmt(L) :
    if IsEmpty(L) :
        return 0
    else : 
        return max2(FirstElmt(L), MaxElmt(Tail(L)))

# MaxNB: List of integer -> <integer, integer>
# MaxNB(L) menghasilkan <max, countMax> dengan max adalah elemen maksimum dari list L dan countMax adalah banyaknya kemunculan max di list L
def MaxNB(L) :
    if IsEmpty(L) :
        return 0
    else :
        return [MaxElmt(L), countMax(MaxElmt(L), L)]

# IsEqual : 2 List -> boolean 
# {IsEqual(L1,L2) benar jika semua elemen list L1 sama dengan L2: sama urutan dan sama nilainya}
def IsEqual(L1, L2):
    if(IsEmpty(L1) and IsEmpty(L2)):
        return True
    else:
        if(FirstElmt(L1) == FirstElmt(L2)):
            return IsEqual(Tail(L1), Tail(L2))
        else:
            return False

# max2 : 2 integer -> integer
# max2 : mengembalikan nilai terbesar dari 2 integer
def max2(a, b) :
    if a > b : 
        return a
    else : 
        return b

# countMax: elemen, List of integer -> integer
# countMax(e, L) mengembalikan jumlah elemen e dalam list L
def countMax(e, L) :
    if IsEmpty(L) :
        return 0
    else : 
        if e == FirstElmt(L) :
            return 1 + countMax(e, Tail(L))
        else : 
            return countMax(e, Tail(L))

if __name__ == "__main__" : 
    # Aplikasi Latihan
    print("Ismember: ",isMember(1,[1,2,3,4]))
    print("IsPalindrom: ",IsPalindrom(['k','o','d','o','k']))
    print("ElmtkeN: ",ElmtkeN(2,[4,3,5,6]))
    print("Copy: ",Copy([4,5,6,7]))
    print("Inverse: ",Inverse([1,2,3,4,5]))
    print("Konkat: ",Konkat([1,2,3,4],[5,6,7,8]))
    print("Addlist: ",AddList([2,3],[3,2]))
    print("SumElmt: ",SumElmt([10,20,30]))
    print("AvgElmt: ",AvgElmt([5,4,3]))
    print("MaxElmt: ",MaxElmt([2,3,4,10]))
    print("MaxNB: ",MaxNB([4,5,6]))
    # print("Konso 2 ke List [3]: ",Konso(2,[3])) 
    # print("Dari listt [3,4,5] konsi 6: ",Konsi([3,4,5],6)) 
    # print("Firstelmt dari [3,4,5,6,7]: ",FirstElmt([3,4,5,6,7]))
    # print("LastELmt dari [3,4,5,6,7]: ",LastElmt([3,4,5,6,7]))
    # print("Tail dari [3,4,5,6,7]: ",Tail([3,4,5,6,7]))
    # print("Head dari [3,4,5,6,7]: ",Head([3,4,5,6,7]))
    # print("Apakah [3,4,5,6,7] List Kosong? ",IsEmpty([3,4,5,6,7]))
    # print("Apakah [] List Kosong? ",IsEmpty([])) 
    # print("Apakah [] List Satu Element? ",IsOneElmt([]))
    # print(IsOneElmt([3]))
    # print(IsOneElmt([3,4,5,6,7])) 
    # print(NbElmt([3,4,5,6,7]))