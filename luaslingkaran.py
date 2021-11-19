print("Selamat Datang Di pengiriman Pemuda Insyaf Express")
print("="*42)

tujuan=str(input("masukkan kota tujuan:"))
berat=int(input("masukkan berat barang:"))
jenis=str(input("Express / reguler:"))

if tujuan=="Malang":
   if jenis=="Reguler":
        if berat<50:
         biaya=75000
         print("biaya pengiriman:", biaya)
        elif berat>50<=100:
         biaya=60000
         print("biaya pengiriman:", biaya)
        else:
         biaya=100000
         print("biaya pengiriman:", biaya)
   if jenis=="express":
        if berat<50:
         biaya=95000
         print("biaya pengiriman:", biaya)
        elif berat>50<=100:
         biaya=80000
         print("biaya pengiriman:", biaya)
        else:
         biaya=120000
         print("biaya pengiriman:", biaya)
if tujuan=="Banyuwangi":
    if jenis=="Reguler":
        if berat<50:
         biaya=200000
         print("biaya pengiriman:", biaya)
        elif berat>50<=100:
         biaya=250000
         print("biaya pengiriman:", biaya)
        else:
         biaya=230000
         print("biaya pengiriman:", biaya)
    if jenis=="express":
        if berat<50:
         biaya=220000
         print("biaya pengiriman:", biaya)
        elif berat>50<=100:
         biaya=270000
         print("biaya pengiriman:", biaya)
        else:
         biaya=250000
         print("biaya pengiriman:", biaya)