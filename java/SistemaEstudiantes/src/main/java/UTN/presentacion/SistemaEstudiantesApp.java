package UTN.presentacion;
import UTN.conexion.Conexion;
import UTN.datos.EstudianteDao;
import UTN.dominio.Estudiante;

import java.util.Scanner;

public class SistemaEstudiantesApp {
    public static void main(String[] args) {
        var salir = false; // recuerden esto ya lo hicimos antes
        var consola = new Scanner(System.in); // para leer informacion de la consola

        // Se crea una instancia de la clase servicio, esto lo hacemos fuera del ciclo
        var estudianteDao = new EstudianteDao(); // Esta instancia debe hacerse una vez

        while (!salir) {
            try {
                mostrarMenu(); // Mostramos el menu
                // Este serà el metodo ejecutar Opciones que devolverá un booleano
                salir = ejecutarOpciones(consola, estudianteDao); // Este arroja una exception
            } catch (Exception e) {
                System.out.println("Ocurrió un error al ejecutar la operacion :" + e.getMessage());
            }
        }
    } // fin main

    private static void mostrarMenu() {
        System.out.println(""" 
                ********** Sistema de estudiantes **********
                1. Listar Estudiantes
                2. Buscar Estudiantes
                3. Agregar Estudiantes
                4. Modificar Estudiante
                5. Eliminar Estudiante
                6. Salir
                """);
    }
        // Metdo para ejecutar las opciones , va a regresar un valor booleano, ya que es el que
        // puede modificar el valor de la variable salir , si es verdadero termina el ciclo while
        private static  boolean ejecutarOpciones(Scanner consola, EstudianteDao estudiantesDao){
        var opcion = Integer.parseInt(consola.nextLine());
        var salir = false;
        switch (opcion) {
            case 1 -> { // listar estudiantes
                System.out.println("listado de estudiantes :");
                // no muestra la informacion, solo recupera la info y regresa una lista

                var estudiantes = estudiantesDao.listarEstudiantes(); // recibe el listado

                // vamos a iterar cada objeto de tipo estudiante
                estudiantes.forEach(System.out::println); // para imprimir la lista
            } // fin caso 1

            case 2 -> { // buscar por estudiante por id
                System.out.println(" Introduce el id_estudiante a buscar :");
                var idEstudiante = Integer.parseInt(consola.nextLine());
                var estudiante = new Estudiante(idEstudiante);
                var encontrado = estudiantesDao.buscarEstudiantePorId(estudiante);
                if(encontrado)
                    System.out.println("Estudiante encontrado :"+estudiante);
                else
                    System.out.println("Estudiante NO encontrado:"+estudiante);
            } // fin caso 2

            case 3 -> { // Agregar estudiante
                System.out.println("Agregar estudiante: ");
                System.out.println("nombre:");
                var nombre = consola.nextLine();
                System.out.println("Apellido:");
                var apellido = consola.nextLine();
                System.out.println("Telefono:");
                var telefono = consola.nextLine();
                System.out.println("Email:");
                var email = consola.nextLine();

                // crear objeto estudiante (sin id)
                 var estudiante = new Estudiante(nombre,apellido,telefono,email);
                 var agregado = estudiantesDao.agregarEstudiante(estudiante);
                 if (agregado)
                     System.out.println("Estudiante agregado :"+estudiante);
                 else
                     System.out.println("Estudiante NO agregado:" +estudiante);
            } // fin caso 3

            case 4 -> { // modficar estudiante
                        System.out.println("Modificar estudiante :");
                        // aqui lo primero es especificar cual es el id del objeto a modificar
                        System.out.println(" ID Estudiante:");
                        var idEstudiante = Integer.parseInt(consola.nextLine());
                        System.out.println("Nombre:");
                        var nombre = consola.nextLine();
                        System.out.println("Apellido:");
                        var apellido = consola.nextLine();
                        System.out.println("Telefono:");
                        var telefono = consola.nextLine();
                        System.out.println("Email:");
                        var email = consola.nextLine();
                        // crea objeto estudiante a modificar
                        var estudiante = new Estudiante(idEstudiante,nombre,apellido,telefono,email);
                        var modificado = estudiantesDao.modificarEstudiante(estudiante);
                        if (modificado)
                            System.out.println("Estudiante modificado :"+estudiante);
                        else
                            System.out.println("Estudiante no modificado:"+estudiante);
                    } // fin caso 4

            case 5 -> { // Eliminar estudiante
                System.out.println("Eliminar estudiante:");
                System.out.println("ID estudiante:");
                var idEstudiante = Integer.parseInt(consola.nextLine());
                var estudiante = new Estudiante(idEstudiante);
                var eliminado = estudiantesDao.eliminarEstudiante(estudiante);
                if (eliminado)
                    System.out.println("Estudiante eliminado :"+estudiante);
                else
                    System.out.println("Estudiante NO eliminado:"+estudiante);
            } // fin caso 5

            case 6 -> { // salir
                System.out.println(" Hasta pronto !!!");
                salir = true;
            } // fin caso 6
            default -> System.out.println("opcion no reconocida, ingrese otra opcion");
        } // fin switch
        return salir;

    } // fin clase


}