--------------------------------------------------------------------------------
CREATE TABLE fotografo(
	id SERIAL PRIMARY KEY,
	id_perfil INTEGER REFERENCES perfil(id) on update cascade on delete cascade,
	fotos_subidas INTEGER,
	puntos INTEGER
);

--------------------------------------------------------------------------------

CREATE TABLE cliente(
	id SERIAL PRIMARY KEY,
	id_perfil INTEGER REFERENCES perfil(id) on update cascade on delete cascade,
	fotos_compradas INTEGER
);

--------------------------------------------------------------------------------

CREATE TABLE perfil(
	id SERIAL PRIMARY KEY,
	usuario VARCHAR(30),
	contrasenia VARCHAR(10),
	description VARCHAR(100),
	tipo VARCHAR(1)
);

--------------------------------------------------------------------------------

CREATE TABLE permisos(
	id SERIAL PRIMARY KEY,
	descarga bool,
	publicaciones bool,
	guardar bool
);

--------------------------------------------------------------------------------
