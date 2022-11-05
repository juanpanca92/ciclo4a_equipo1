package sprint1.seguridadBE.Repositorios;

import sprint1.seguridadBE.Modelos.Rol;
import org.springframework.data.mongodb.repository.MongoRepository;


public interface RepositorioRol extends MongoRepository<Rol,String> {
}
