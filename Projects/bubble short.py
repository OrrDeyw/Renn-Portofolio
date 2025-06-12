# Data mahasiswa awal
mahasiswa = [
    {"nama": "Nafis", "NIM": "2325652", "nilai": 85},
    {"nama": "Afta", "NIM": "2325655", "nilai": 93},
    {"nama": "Iqbal", "NIM": "2325651", "nilai": 75},
    {"nama": "Luthfi", "NIM": "2325654", "nilai": 86},
    {"nama": "Aziz", "NIM": "2325653", "nilai": 72},
]

# Bubble Sort berdasarkan NIM
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j]["NIM"] > data[j + 1]["NIM"]:  
                data[j], data[j + 1] = data[j + 1], data[j] 

# Linear Search
def linear_search(data, NIM):
    for mhs in data:
        if mhs["NIM"] == NIM:
            return mhs
    return None

# Binary Search (harus dalam kondisi terurut)
def binary_search(data, NIM):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid]["NIM"] == NIM:
            return data[mid]
        elif data[mid]["NIM"] < NIM:
            low = mid + 1
        else:
            high = mid - 1
    return None

# Menampilkan data sebelum 
print("\nData sebelum diurutkan:")
for m in mahasiswa:
    print(m)

    bubble_sort(mahasiswa)

print("\nData setelah diurutkan:")
for m in mahasiswa:
    print(m)

# Input NIM dan pencarian
nim_dicari = input("\nMasukkan NIM yang ingin dicari: ")
print("Metode pencarian:\n1. Linear Search\n2. Binary Search")
pilihan = input("Pilih metode (1/2): ")

if pilihan == "1":
    hasil = linear_search(mahasiswa, nim_dicari)
elif pilihan == "2":
    sorted_by_nim = bubble_sort(mahasiswa.copy())
    hasil = binary_search(mahasiswa, nim_dicari)
else:
    hasil = None

#Contoh pencarian
target_NIM = "2325651"

print(f"\nLinear Search: mencari NIM {target_NIM}")
hasil_linear = linear_search(mahasiswa, target_NIM)
print("Ditemukan:" if hasil_linear else "Tidak ditemukan", hasil_linear)

target_NIM = "2325651"

print(f"\nBinary Search: mencari NIM {target_NIM}")
hasil_binary = binary_search(mahasiswa, target_NIM)
print("Ditemukan:" if hasil_binary else "Tidak ditemukan", hasil_binary)