-- CREATE DATABASE IF NOT EXISTS dm_data;
USE dm_data;

CREATE TABLE IF NOT EXISTS personajes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_personaje VARCHAR(100) NOT NULL,
    raza VARCHAR(50) NOT NULL,
    clase VARCHAR(50) NOT NULL,
    nivel INT DEFAULT 1,
    fuerza INT DEFAULT 10,
    destreza INT DEFAULT 10,
    constitucion INT DEFAULT 10,
    inteligencia INT DEFAULT 10,
    sabiduria INT DEFAULT 10,
    carisma INT DEFAULT 10,
    trasfondo TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
