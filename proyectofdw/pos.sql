CREATE TABLE productos(
    codigo int not null UNIQUE,
    nombre varchar(255) not null,
    precio float(9,2) not null
);

INSERT INTO productos VALUES
("1", "cafe", "20.00"),
("2", "Coca", "13.00"),
("3", "Doritos", "24.00"),
("4", "Emperador", "18.00"),
("5", "Fritos", "15.00"),
("6", "Arroz", "10.00"),
("7", "Celular", "1000.00"),
("8", "Lentes", "300.00"),
("9", "Cinto", "150.00"),
("10", "Robin", "200000.00");