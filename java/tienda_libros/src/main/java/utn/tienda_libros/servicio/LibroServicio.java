package utn.tienda_libros.servicio;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import utn.tienda_libros.modelo.Libro;
import utn.tienda_libros.repositorio.LibroRepositorio;

import java.util.List;

@Service
public class LibroServicio implements ILibroServicio {

    @Autowired
    private LibroRepositorio librorepositorio;

    @Override
    public List<Libro> listarLibros() {
        return librorepositorio.findAll();
    }

    @Override
    public Libro buscarLibroPorId(Integer idLibro) {
        Libro libro = librorepositorio.findById(idLibro).orElse(null);
        return libro;
    }

    @Override
    public void guardarLibro(Libro libro) {
        librorepositorio.save(libro);
    }

    @Override
    public void eliminarLibro(Libro libro) {
        librorepositorio.delete(libro);
    }
}
