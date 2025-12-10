# mahasiswa.py
# TIPE MAHASISWA (Mhs)

# KONSTRUKTOR
def MakeMhs(nim, nama):
    # MakeMhs: string, string -> Mhs
    # {MakeMhs(nim, nama) membuat objek Mhs dengan NIM nim dan nama nama}
    return [nim, nama]

# SELEKTOR
def GetNIM(M):
    # GetNIM: Mhs -> string
    # {GetNIM(M) mengambil NIM dari mahasiswa M}
    return M[0]

def GetNama(M):
    # GetNama: Mhs -> string
    # {GetNama(M) mengambil nama dari mahasiswa M}
    return M[1]

if __name__ == "__main__" : 
    M1 = MakeMhs("A11.2020.01234", "Reno")
    print(M1)
    print(GetNIM(M1))
    print(GetNama(M1))