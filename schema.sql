CREATE DATABASE cvcreator;
USE cvcreator;
CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);
CREATE TABLE curriculums (
    id_curriculum INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_plantilla INT NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_ultima_modificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    archivo_json JSON ,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);