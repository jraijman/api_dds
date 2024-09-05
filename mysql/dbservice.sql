use db;

CREATE TABLE centro_donacion(
    id int not null AUTO_INCREMENT,
    nombre varchar(255),
    lat float,
    long float,
    direccion varchar(255) ,
    PRIMARY KEY (id)
);