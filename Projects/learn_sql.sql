create database universitas;
use universitas;
create table dosen(
NIP varchar (18),
nama_dosen varchar (20),
alamat varchar (20),
no_hp varchar (12),
PRIMARY KEY (NIP) 
) ;
describe mata_kuliah;
select * from dosen;
INSERT INTO dosen (NIP , nama_depan, alamat, no_hp) 
VALUES (21090240024, 'CIMENG', 'SALATIGA', 082135903438 ),
	   (22090240024, 'ARDY', 'SEMARANG', 082135903438 ),
       (23090240024, 'RENOO', 'AMBARAWA', 082135903438 );

       
create table mata_kuliah(
kode_mk varchar (12),
nama_mk varchar (20),
sks int (1),
PRIMARY KEY (kode_mk) 
) ;
describe mata_kuliah;
INSERT INTO mata_kuliah(kode_mk , nama_mk, sks) 
VALUES (2200001, 'MATEMATIKA DISKRIT',3 ),
	   (2300002, 'BASIS DATA ', 3),
       (2400003, 'STATISTIKA ', 3);
       
create table ambil_mk(
NIM varchar (12),
NIP varchar (18),
kode_mk int (12)
);

INSERT INTO ambil_mk(NIM, NIP, kode_mk) 
VALUES (45001, 48002, 7),
	   (46001, 49002, 8),
       (47001, 50002, 9);
       
select * from ambil_mk;

UPDATE mata_kuliah
SET kode_mk = 14
WHERE nama_mk = 'STATISTIKAs