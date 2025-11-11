package UTN.datos;
import UTN.conexion.Conexion;
import UTN.dominio.Estudiante;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

import static UTN.conexion.Conexion.getConnection;

public class EstudianteDao {
    // metodo listar
    public List<Estudiante> listarEstudiantes(){
        List<Estudiante> estudiantes = new ArrayList<>();
        //creamos algunos objetos que son necesarios para comunicarnos con la base de datos
        PreparedStatement ps; //envia la sentencia a la base de datos
        ResultSet rs; // obtenemos el resultado de la base de datos
        // creamos un objeto de tipo Connection (en este caso conexion)
        //para esto debemos importar desde la clase conxion, entonces hacemos import arriba

        //Connection con= ps.getConnection();
        Connection con = getConnection(); //forma correcta
        String sql = "SELECT * FROM estudiantes2025";
        try {
            ps = con.prepareStatement(sql);
            rs = ps.executeQuery();
            while (rs.next()){ //esto es para iterar todos los registros mientras haya.
                var estudiante = new Estudiante();
                estudiante.setIdEstudiante(rs.getInt("idestudiantes2025"));
                estudiante.setNombre(rs.getString("nombre"));
                estudiante.setApellido(rs.getString("apellido"));
                estudiante.setTelefono(rs.getString("telefono"));
                estudiante.setEmail(rs.getString("email"));
                //falta agregarlo a la lista
                estudiantes.add(estudiante);

            }
        } catch (Exception e){
            System.out.println("Ocurrió un error al seleccionar datos: " + e.getMessage());
        }
        finally {
            try {
                con.close();
            }   catch (Exception e){
                System.out.println("Ocurrio un error al cerrar la conexion: "+e.getMessage());
            }// fin catch
        } //fin finally
        return estudiantes;//fin metodo Listar
}

    // video 7 : metodo buscar por id --> fin by id
    public boolean buscarEstudiantePorId(Estudiante estudiante){
        PreparedStatement ps;
        ResultSet rs;
        Connection con = getConnection();
        String sql = "SELECT * FROM estudiantes2025 where idestudiantes2025=?";
        try {
            ps =con.prepareStatement(sql);
            ps.setInt(1,estudiante.getIdEstudiante());
            rs = ps.executeQuery();
            if (rs.next()){
                estudiante.setIdEstudiante(rs.getInt("idestudiantes2025"));
                estudiante.setNombre(rs.getString("nombre"));
                estudiante.setApellido(rs.getString("apellido"));
                estudiante.setTelefono(rs.getString("telefono"));
                estudiante.setEmail(rs.getString("email"));
                return true; // se encontro un registro
            } //fin if
        } catch (Exception e){
            System.out.println("Ocurrió un error al buscar estudiantes :"+e.getMessage());
        } finally {
            try {
                con.close();
            } catch (Exception e) {
                System.out.println("Ocurrio un error al cerrar la conexion :" + e.getMessage());
            }

        }
        return false;
}
    //metodo agregar un nuevo estudiante
     public boolean agregarEstudiante(Estudiante estudiante){
        PreparedStatement ps;
        Connection con = getConnection();
        String sql = "INSERT INTO estudiantes2025 (nombre, apellido, telefono,email) VALUES (?,?,?,?)";
        try {
            ps = con.prepareStatement(sql);
            ps.setString(1,estudiante.getNombre());
            ps.setString(2,estudiante.getApellido());
            ps.setString(3,estudiante.getTelefono());
            ps.setString(4,estudiante.getEmail());
            ps.execute();
            return true;
        } catch (Exception e){
            System.out.println("Ocurrio un error al agregar estudiante: "+e.getMessage());
        } //fin catch
         finally {
            try {
                con.close();
            } catch (Exception e){
                System.out.println("Error al cerrar la conexion:"+e.getMessage());
            } // fin catch

        } // fin finally
         return false;
    } // fin metodo agregarEstudiante

    // Metodo para modificar Estudiante
    public boolean modificarEstudiante(Estudiante estudiante){
        PreparedStatement ps;
        Connection con = getConnection();
        String sql = "UPDATE estudiantes2025 SET nombre=?, apellido=?, telefono=?, email=? WHERE idestudiantes2025=?";
        try {
            ps = con.prepareStatement(sql);
            ps.setString(1,estudiante.getNombre());
            ps.setString(2,estudiante.getApellido());
            ps.setString(3,estudiante.getTelefono());
            ps.setString(4,estudiante.getEmail());
            ps.setInt(5,estudiante.getIdEstudiante());
            return true;
        } catch (Exception e) {
            System.out.println("Error al modificar estudiante : "+e.getMessage());
        }// fin catch
        finally {
            try {
                con.close();
            } catch (Exception e){
                System.out.println("Error al cerrar la conexion:"+e.getMessage());
            }//fin catch
        } // fin finally
        return false;
    } // fin metodo modificar estudiante

    // metodo eliminar estudiante Clase 01 Aplicación Sistema Estudiantes Parte 3 - Video
    // 1.1 Método eliminar estudiante y prueba - video 01

    public boolean eliminarEstudiante(Estudiante estudiante){
        PreparedStatement ps;
        Connection con = getConnection();
        String sql = "DELETE FROM estudiantes2025 WHERE idestudiantes2025 = ?";
        try {
            ps = con.prepareStatement(sql);
            ps.setInt(1,estudiante.getIdEstudiante());
            ps.execute();
            return true;
        } catch (Exception e) {
            System.out.println("Error al eliminar estudiante :" +e.getMessage());
        }
        finally {
            try {
                con.close();
            } catch (Exception e) {
                System.out.println("Error al cerrar la conexion:"+e.getMessage());
            }
        }
        return false;
    }



    public static void main(String[] args) {
        var estudianteDao = new EstudianteDao();
    //MODIFICAR estudiante
        var estudianteModificado = new Estudiante(1, "juan carlos","juarez","784512","juancar@gmail.com");
        var modificado = estudianteDao.modificarEstudiante(estudianteModificado);
        if (modificado)
            System.out.println("estudiante modificado:"+estudianteModificado);
        else
            System.out.println("no se modificado el estudiante:"+estudianteModificado);


        // Eliminar estudiante con id=3
        var estudianteEliminar = new Estudiante(4);
        var eliminado = estudianteDao.eliminarEstudiante(estudianteEliminar);
        if(eliminado)
            System.out.println("Estudiante eliminado :" +estudianteEliminar);
        else
            System.out.println("No se eliminò estudiante:" +estudianteEliminar);



        //listar los estudiantes
         System.out.println("Listado de estudiantes:");
         List<Estudiante> estudiantes = estudianteDao.listarEstudiantes();
         //metodo por referencia -
         estudiantes.forEach(System.out::println); //funcion lambda para imprimir
    }
}
         // Agregar estudiante
//         var nuevoEstudiante = new Estudiante("Carlos", "Lara", "54216541", "carlos@gmail.com");
//         var agregado = estudianteDao.agregarEstudiante(nuevoEstudiante);
//         if (agregado)
//             System.out.println("Estudiante agregado: " + nuevoEstudiante);
//         else
//             System.out.println("No se ha agregado estudiante" + nuevoEstudiante);
//     }




//buscar por id
//         var estudiante1 = new Estudiante(1);
//         System.out.println("Estudiantes antes de la busqueda:"+estudiante1);
//         var encontrado = estudianteDao.buscarEstudiantePorId(estudiante1);
//         if (encontrado)
//             System.out.println("Estudiante encontrado :"+estudiante1);
//         else
//             System.out.println("No se encontró el estudiante"+estudiante1.getIdEstudiante());
