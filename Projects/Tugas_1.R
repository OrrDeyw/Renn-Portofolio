cat("
Sebuah toko online menjual 10 jenis kue lebaran. 
Agus berniat untuk membeli 5 toples. Dari 10 jenis kue lebaran tersebut, 
Agus sudah menentukan ingin membeli 3 jenis saja. 
Tentukan berapa banyak kombinasi kue lebaran yang bisa dibeli Agus!\n\n")

n <- 3  
r <- 5  
kombinasi <- choose(n + r - 1, r)
cat("Jumlah kombinasi yang mungkin adalah:", kombinasi)

