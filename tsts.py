import json

# Daftar untuk menyimpan tugas
tugas_list = []

def tambah_tugas(tugas):
    tugas_list.append(tugas)

def hapus_tugas(index):
    if 0 <= index < len(tugas_list):
        del tugas_list[index]
    else:
        print("Indeks tidak valid.")

def cari_tugas(kata_kunci):
    hasil = [tugas for tugas in tugas_list if kata_kunci.lower() in tugas.lower()]
    return hasil

def simpan_tugas(filename):
    with open(filename, 'w') as file:
        json.dump(tugas_list, file)

def muat_tugas(filename):
    global tugas_list
    try:
        with open(filename, 'r') as file:
            tugas_list = json.load(file)
    except FileNotFoundError:
        print("File tidak ditemukan. Memulai daftar tugas baru.")

def tampilkan_tugas(tugas_list, indent=0):
    for index, tugas in enumerate(tugas_list):
        print(" " * indent + f"{index + 1}. {tugas}")

def menu():
    muat_tugas('tugas.txt')
    while True:
        print("\nMenu:")
        print("1. Tambah Tugas")
        print("2. Hapus Tugas")
        print("3. Cari Tugas")
        print("4. Tampilkan Semua Tugas")
        print("5. Simpan Tugas")
        print("6. Keluar")
        
        pilihan = input("Pilih opsi (1-6): ")
        
        if pilihan == '1':
            tugas = input("Masukkan deskripsi tugas: ")
            tambah_tugas(tugas)
        elif pilihan == '2':
            index = int(input("Masukkan nomor tugas yang ingin dihapus: ")) - 1
            hapus_tugas(index)
        elif pilihan == '3':
            kata_kunci = input("Masukkan kata kunci untuk mencari tugas: ")
            hasil = cari_tugas(kata_kunci)
            if hasil:
                print("Hasil pencarian:")
                tampilkan_tugas(hasil)
            else:
                print("Tidak ada tugas yang cocok.")
        elif pilihan == '4':
            print("Daftar Tugas:")
            tampilkan_tugas(tugas_list)
        elif pilihan == '5':
            simpan_tugas('tugas.txt')