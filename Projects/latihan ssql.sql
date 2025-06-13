show databases;
create database kantor_agregat;
use kantor_agregat;
create table jam_kerja (
	Kode_karyawan varchar (12) primary key,
	Nama_karyawan varchar (40) ,
    PSW varchar (5) ,
    total_jam_kerja varchar (5),
    Gaji varchar (10)
  );

desc Matkul;

insert into jam_kerja( Kode_karyawan, Nama_karyawan, PSW, total_jam_kerja, Gaji) 
values ('50001', 'Anggi', '1' , '7', '4500000'),
	   ('50002', 'Benny', '1' , '6', '4000000'),
       ('50003', 'Cherill', '0' , '7', '5000000'),
       ('50004', 'Davi', '3' , '5', '3500000'),
	   ('50005', 'Ega', '1' , '6', '4000000'),
       ('50006', 'Fachri', '2' , '5', '3500000'),
       ('50007', 'Gaga', '5' , '2', '3500000')
       ;
       
select * from jam_kerja;

update jam_kerja 
set Nama_karyawan = 'Cherill Mangga'
where Kode_karyawan ='50003';

select Nama_mk from Matkul ;

select sum(Gaji) from jam_kerja;
select sum(Gaji) as total_gaji from jam_kerja;

select jk.Kode_karyawan, jk.Nama_karyawan, jk.Gaji 
from jam_kerja jk
group by Kode_karyawan 
having sum(Gaji) >= 4000000;

select PSW , sum(Gaji) AS totalGaji
from jam_kerja  
group by PSW ;


