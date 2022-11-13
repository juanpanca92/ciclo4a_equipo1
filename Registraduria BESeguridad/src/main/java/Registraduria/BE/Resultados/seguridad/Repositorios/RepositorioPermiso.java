package Registraduria.BE.Resultados.seguridad.Repositorios;

import Registraduria.BE.Resultados.seguridad.Modelos.Permiso;
import org.springframework.data.mongodb.repository.Query;
import org.springframework.data.mongodb.repository.MongoRepository;


public interface RepositorioPermiso extends MongoRepository<Permiso,String> {
    @Query("{'url':?0,'metodo':?1}")
    Permiso getPermiso(String url, String metodo);
}
