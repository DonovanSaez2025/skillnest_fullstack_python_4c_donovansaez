CREATE DATABASE IF NOT EXISTS esquema_usuarios;
USE esquema_usuarios;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(40) NOT NULL,
    apellido_usuario VARCHAR(60) NOT NULL,
    email_usuario VARCHAR(100) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);

INSERT INTO usuarios (nombre_usuario, apellido_usuario, email_usuario)
VALUES ("Quentin", "Quail", "quentinquail@gmail.com"),
("Daffy", "Duck", "daffyduck@hotmail.com"),
("Cecil", "Turtle", "cecilturtle@gmail.com"),
("Foghorn", "Leghorn", "foghornleghorn@hotmail.com");