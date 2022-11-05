package sprint1.seguridadBE.Repositorios;

import sprint1.seguridadBE.Modelos.Permiso;
import org.springframework.data.mongodb.repository.MongoRepository;


public interface RepositorioPermiso extends MongoRepository<Permiso,String> {
}
