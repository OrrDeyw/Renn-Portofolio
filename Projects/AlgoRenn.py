import pandas as pd

# Data awal dalam bentuk list 2D (nama, nilai tugas, nilai ujian)
Data_mahasiswa = [
    ["MeiMei", 85, 87],
    ["Ehsan", 90, 88],
    ["Fizi", 78, 85],
    ["Jarjit", 89, 90],
    ["Mail", 92, 90]
]


# Fungsi untuk menampilkan tabel
def show_table(data, pesan="Tabel Mahasiswa:"):
    print(f"\n{pesan}")
    df = pd.DataFrame(data, columns=["Nama", "Nilai Tugas", "Nilai Ujian"], index=range(1, len(data) + 1))
    print(df)


# Fungsi untuk mengakses data berdasarkan indeks
def akses_data():
    show_table(Data_mahasiswa)
    try:
        indeks = int(input("\nMasukkan nomor indeks data yang ingin diakses (1-{}): ".format(len(Data_mahasiswa)))) - 1
        if 0 <= indeks < len(Data_mahasiswa):
            print(
                f"\nData pada indeks {indeks + 1}: Nama: {Data_mahasiswa[indeks][0]}, Nilai Tugas: {Data_mahasiswa[indeks][1]}, Nilai Ujian: {Data_mahasiswa[indeks][2]}")
        else:
            print("Indeks tidak valid!")
    except ValueError:
        print("Masukkan angka yang valid!")


# Fungsi untuk mengubah data
def ubah_data():
    show_table(Data_mahasiswa)
    try:
        indeks = int(input("\nMasukkan nomor indeks data yang ingin diubah (1-{}): ".format(len(Data_mahasiswa)))) - 1
        if 0 <= indeks < len(Data_mahasiswa):
            print(f"Data saat ini: {Data_mahasiswa[indeks]}")
            tugas_baru = int(input("Masukkan nilai tugas baru: "))
            ujian_baru = int(input("Masukkan nilai ujian baru: "))
            Data_mahasiswa[indeks][1] = tugas_baru
            Data_mahasiswa[indeks][2] = ujian_baru
            print(f"\nData setelah diubah: {Data_mahasiswa[indeks]}")
            show_table(Data_mahasiswa)
        else:
            print("Indeks tidak valid!")
    except ValueError:
        print("Masukkan angka yang valid!")


# Fungsi untuk menghapus data berdasarkan nama
def hapus_data():
    show_table(Data_mahasiswa)
    nama = input("\nMasukkan nama mahasiswa yang ingin dihapus: ")
    for i, mahasiswa in enumerate(Data_mahasiswa):
        if mahasiswa[0].lower() == nama.lower():
            del Data_mahasiswa[i]
            print(f"\nData {nama} telah dihapus!")
            show_table(Data_mahasiswa)
            return
    print(f"Mahasiswa dengan nama {nama} tidak ditemukan!")


# Fungsi untuk menambahkan data baru
def tambah_data():
    nama = input("\nMasukkan nama mahasiswa baru: ")
    try:
        tugas = int(input("Masukkan nilai tugas: "))
        ujian = int(input("Masukkan nilai ujian: "))
        Data_mahasiswa.append([nama, tugas, ujian])
        print(f"\nData {nama} telah ditambahkan!")
        show_table(Data_mahasiswa)
    except ValueError:
        print("Masukkan nilai yang valid!")


# Fungsi utama untuk menu
def main():
    print("\n=== Data Mahasiswa ===")
    show_table(Data_mahasiswa)
    while True:
        pilihan1 = input('Apa yang akan anda pilih? "EDIT" / "KELUAR" :').lower()
        if pilihan1 == "edit":
            while True:
                pilihan2 = input('Terdapat beberapa opsi, antara lain "AKSES", "UBAH", "HAPUS", "TAMBAH" : ').lower()
                if pilihan2 in ["akses","ubah","hapus","tambah"]:
                    if pilihan2 == "akses":
                        akses_data()
                    elif pilihan2 == "ubah":
                        ubah_data()
                    elif pilihan2 == "hapus":
                        hapus_data()
                    elif pilihan2 == "tambah":
                        tambah_data()
                    break
                else:
                    print("Jangan Typo dong, ulangi ")
        elif pilihan1 == "keluar":
            print("okee, BYEEE")
            break
        else:
            print("ngetik yang bener dong anjayy wkwk")


if __name__ == "__main__":
    main()