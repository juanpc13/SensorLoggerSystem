CREATE TABLE registros(
    id_reg serial PRIMARY KEY,
    nombre VARCHAR (64),
    co2 integer,
    h integer,
    radon integer,
    fecha date,
    activo boolean
);