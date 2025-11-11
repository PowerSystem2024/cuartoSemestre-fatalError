package utn.tienda_libros.modelo;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;


@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
@ToString
public class Libro {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    Integer idLibro;
    String nombreLibro;
    String autor;
    Double precio;
    Integer existencias;

//    public Integer getIdLibro() {
//        return idLibro;
//    }
//
//    public void setIdLibro(Integer idLibro) {
//        this.idLibro = idLibro;
//    }
//
//    public String getAutor() {
//        return autor;
//    }
//
//    public void setAutor(String autor) {
//        this.autor = autor;
//    }
//
//    public String getNombreLibro() {
//        return nombreLibro;
//    }
//
//    public void setNombreLibro(String nombreLibro) {
//        this.nombreLibro = nombreLibro;
//    }
//
//    public Double getPrecio() {
//        return precio;
//    }
//
//    public void setPrecio(Double precio) {
//        this.precio = precio;
//    }
//
//    public Integer getExistencias() {
//        return existencias;
//    }
//
//    public void setExistencias(Integer existencias) {
//        this.existencias = existencias;
//    }
}
