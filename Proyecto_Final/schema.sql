CREATE DATABASE IF NOT EXISTS dm_data;
USE dm_data;

-- Tabla jugadores
CREATE TABLE IF NOT EXISTS jugadores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_jugador VARCHAR(100) NOT NULL,
    email VARCHAR(150),
    telefono VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla personajes
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
    puntos_golpe_max INT DEFAULT 10,
    puntos_golpe_actuales INT DEFAULT 10,
    jugador_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (jugador_id) REFERENCES jugadores(id) ON DELETE CASCADE
);

