package sprint1.seguridadBE.Repositorios;

import org.springframework.data.mongodb.repository.MongoRepository;
import sprint1.seguridadBE.Modelos.PermisosRoles;


public interface RepositorioPermisosRoles extends MongoRepository<PermisosRoles,String> {
}
