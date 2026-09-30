CREATE DATABASE inicio_sesion_registro;
USE inicio_sesion_registro;

-- Tabla usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL,
    apellido VARCHAR(70) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    animal_favorito VARCHAR(30) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);