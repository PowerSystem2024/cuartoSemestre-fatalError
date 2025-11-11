package UTN.conexion;

import java.sql.Connection; //2ª aparece cuando hacemos "primero"
import java.sql.DriverManager;
import java.sql.SQLException;

public class Conexion {
    public static Connection getConnection(){ //primero
        Connection conexion = null;
        //ahora crearemos variables para conectarnos a la base de datos
        var baseDatos = "estudiantes";
        var url = "jdbc:mysql://localhost:3306/" + baseDatos;
        //var usuario = "root";
        var usuario = "irene";
        //var password = "admin";
        var password = "123456";


        // ahora cargamos la clase del driver de mysql en memoria
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            conexion = DriverManager.getConnection(url, usuario, password);
        } catch (ClassNotFoundException | SQLException e){
            System.out.println("Ocurrio un error en la conexion:"+ e.getMessage());
        }
        //fin catch
        return conexion;
    } // fin metodo connection
}
