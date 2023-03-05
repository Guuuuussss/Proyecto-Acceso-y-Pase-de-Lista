
CREATE  TABLE accesos.usuarios ( 
	identificador        INT UNSIGNED NOT NULL     PRIMARY KEY,
	nombre               VARCHAR(30)  NOT NULL     ,
	apellido_p           VARCHAR(30)  NOT NULL     ,
	apellido_m           VARCHAR(30)  NOT NULL     ,
	matricula            INT UNSIGNED NOT NULL     ,
	tipo_usuario         VARCHAR(30)  NOT NULL     ,
	contraseña           VARCHAR(20)  NOT NULL     
 ) engine=InnoDB;

CREATE  TABLE accesos.accesos ( 
	id                   INT UNSIGNED NOT NULL   AUTO_INCREMENT  PRIMARY KEY,
	fecha_acceso         TIMESTAMP  NOT NULL,
	identificador        INT UNSIGNED NOT NULL,
	FOREIGN KEY (identificador) REFERENCES usuarios(identificador)  
 ) engine=InnoDB;

CREATE  TABLE accesos.clases ( 
	id                   INT UNSIGNED NOT NULL   AUTO_INCREMENT  PRIMARY KEY,
	nombre_materia       VARCHAR(30)  NOT NULL     ,
	salon                VARCHAR(10)  NOT NULL     ,
	horario              VARCHAR(20)  NOT NULL,
	id_profesor          INT UNSIGNED NOT NULL,
	FOREIGN KEY (id_profesor) REFERENCES usuarios(identificador)  
 ) engine=InnoDB;


INSERT INTO accesos.usuarios (identificador, nombre, apellido_p, apellido_m, matricula, tipo_usuario, contraseña)
VALUES 
(374203472, 'Juan', 'Pérez', 'García', 12345, 'P', 'password123'),
(097420342, 'Gustavo', 'Luna', 'Maya', 209070, 'P', 'password193');


INSERT INTO accesos.clases (nombre_materia, salon, horario, id_profesor)
VALUES ('Historia', 'B50', 'Martes 10:00-11:00', 374203472);

INSERT INTO accesos.accesos (fecha_acceso, identificador)
VALUES (NOW(), 374203472);

SELECT *
FROM accesos.usuarios
LEFT JOIN accesos ON usuarios.identificador = accesos.identificador
LEFT JOIN clases ON usuarios.identificador = clases.id_profesor
WHERE usuarios.identificador = 374203472;



