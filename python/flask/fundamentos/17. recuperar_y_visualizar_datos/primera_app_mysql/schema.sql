-- ==========================================================
-- CREAR BASE DE DATOS
-- ==========================================================
CREATE DATABASE IF NOT EXISTS primera_flask;
USE primera_flask;

-- ==========================================================
-- CREAR TABLA
-- ==========================================================
CREATE TABLE IF NOT EXISTS mascotas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(100) NOT NULL,
    color VARCHAR(100) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);

-- ==========================================================
-- INSERTAR DATOS DE PRUEBA
-- ==========================================================
INSERT INTO mascotas(nombre, tipo, color)
VALUES("Firulais", "Perro", "Café"),
    ("Michi", "Gato", "Negro"),
    ("Luna", "Perro", "Blanco"),
    ("Nala", "Gato", "Naranjo"),
    ("Coco", "Conejo", "Blanco");

-- ==========================================================
-- Ejercicio de consolidación
-- ==========================================================
-- CREAR TABLA
-- ==========================================================
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    edad INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);

-- ==========================================================
-- INSERTAR DATOS DE PRUEBA
-- ==========================================================
INSERT INTO usuarios(nombre, email, edad)
VALUES("Felipe", "felipe@gmail.com", "18"),
    ("Juan", "juan@hotmail.com", "27"),
    ("José", "jose@yopmail.cl", "86"),
    ("Alan", "alan@gmail.com", "54"),
    ("Smithy", "smithy@hotmail.com", "35");