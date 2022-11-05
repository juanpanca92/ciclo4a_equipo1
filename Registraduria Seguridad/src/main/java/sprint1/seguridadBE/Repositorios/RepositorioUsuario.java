package sprint1.seguridadBE.Repositorios;

import sprint1.seguridadBE.Modelos.Usuario;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RepositorioUsuario extends MongoRepository<Usuario,String> {
}

