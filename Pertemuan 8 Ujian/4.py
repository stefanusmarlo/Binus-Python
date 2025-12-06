def rerata_nilai_mhs(nama, dataDict):
    if nama in dataDict:
        nilai_list = dataDict[nama]
        for nilai in nilai_list:
            print(nilai, end=' ')
        print()
        rerata = sum(nilai_list) / len(nilai_list)
        print("Rerata = {int(rerata)}")
    else:
        print("Data untuk mahasiswa '{nama}' tidak ditemukan.") 
        
dataDict = {
    'Icha': [80, 70, 70, 80],
    'Budi': [75, 85, 90, 80],
    'Sari': [60, 70, 65, 75]
