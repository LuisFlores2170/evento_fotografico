--------------------------------------------------------------------------------
CREATE TABLE fotografo(
	id SERIAL PRIMARY KEY,
	id_perfil INTEGER REFERENCES perfil(id) on update cascade on delete cascade,
	fotos_subidas INTEGER,
	puntos INTEGER
);
select * from fotografo
drop table fotografo
--------------------------------------------------------------------------------

CREATE TABLE cliente(
	id SERIAL PRIMARY KEY,
	id_perfil INTEGER REFERENCES perfil(id) on update cascade on delete cascade,
	fotos_compradas INTEGER
);
SELECT * FROM CLIENTE
drop table cliente

--------------------------------------------------------------------------------

CREATE TABLE perfil(
	id SERIAL PRIMARY KEY,
	usuario VARCHAR(30),
	contrasenia VARCHAR(10),
	description VARCHAR(100),
	tipo VARCHAR(10)
);
select * from perfil
drop table perfil

delete from perfil where id = 2
SELECT id FROM perfil WHERE usuario = '123'
SELECT id FROM perfil WHERE usuario = 'Luis'
--------------------------------------------------------------------------------

CREATE TABLE permisos(
	id SERIAL PRIMARY KEY,
	descarga bool,
	publicaciones bool,
	guardar bool
);

--------------------------------------------------------------------------------
