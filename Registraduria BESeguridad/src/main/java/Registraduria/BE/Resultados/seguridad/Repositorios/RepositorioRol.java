package Registraduria.BE.Resultados.seguridad.Repositorios;

import Registraduria.BE.Resultados.seguridad.Modelos.Rol;
import org.springframework.data.mongodb.repository.MongoRepository;


public interface RepositorioRol extends MongoRepository<Rol,String> {
}
