package utn.estudiantes;


import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import utn.estudiantes.modelo.Estudiantes2025;
import utn.estudiantes.servicio.EstudianteServicio;

import java.util.List;
import java.util.Scanner;

@SpringBootApplication
public class EstudiantesApplication implements CommandLineRunner {
	@Autowired
	private EstudianteServicio estudianteServicio;
	private static final Logger logger =
			LoggerFactory.getLogger(EstudiantesApplication.class);

	String nl = System.lineSeparator();

	public static void main(String[] args) {

		logger.info("Iniciando la aplicacion ..");
		//Levantar la fabrica de Spring
		SpringApplication.run(EstudiantesApplication.class, args);
		logger.info("Aplicacion finalizada ¡!");
	}

	@Override
	public void run(String... args) throws Exception {
		logger.info(nl + "Ejecutando el metodo run de Spring..." + nl);
		var salir = false;
		var consola = new Scanner(System.in);
		while (!salir) {
			mostrarMenu();
			salir = ejecutarOpciones(consola);
			logger.info(nl);
		} // fin ciclo while

	}

	private void mostrarMenu(){
		//logger.info(nl);
		logger.info("""
				********** Sistema de Estudiantes *********
				1. Listar Estudiantes
				2. Buscar Estudiantes
				3. Agregar Estudiantes
				4. Modificar Estudiantes
				5. Eliminar Estudiantes
				6. Salir

				Elija una opcion :
				""");
	}

	private boolean ejecutarOpciones(Scanner consola) {
		//logger.info("Ingrese una opción: ");
		var opcion = Integer.parseInt(consola.nextLine());
		var salir = false;

		switch (opcion) {
			case 1 -> { // Listar estudiantes
				logger.info(nl + "Listado de estudiantes:" + nl);
				List<Estudiantes2025> estudiantes = estudianteServicio.listarEstudiantes();
				estudiantes.forEach((estudiantes2025) -> logger.info(estudiantes.toString() + nl));
			}

			case 2 -> { // Buscar estudiante por ID
				logger.info("Ingrese el ID del estudiante a buscar: ");
				var idEstudiante = Integer.parseInt(consola.nextLine());

				Estudiantes2025 estudiante = estudianteServicio.buscarEstudiantePorId(idEstudiante);
				if (estudiante != null)
					logger.info("Estudiante encontrado: " + idEstudiante + nl);
				else
					logger.info("No se encontró el estudiante con ID: " + idEstudiante + nl);
			}

			case 3 -> { // Agregar estudiante
				logger.info("Agregar nuevo estudiante:" + nl);
				logger.info("Nombre: ");
				var nombre = consola.nextLine();
				logger.info("Apellido: ");
				var apellido = consola.nextLine();
				logger.info("Teléfono: ");
				var telefono = consola.nextLine();
				logger.info("Email: ");
				var email = consola.nextLine();

				// CREAR el objeto estudiante sin el id

				var nuevoEstudiante = new Estudiantes2025();
				nuevoEstudiante.setNombre(nombre);
				nuevoEstudiante.setApellido(apellido);
				nuevoEstudiante.setTelefono(telefono);
				nuevoEstudiante.setEmail(email);

				estudianteServicio.guardarEstudiante(nuevoEstudiante);

				logger.info("Estudiante agregado: " + nuevoEstudiante + nl);
			}

			case 4 -> { // Modificar estudiante
				logger.info("Modificar estudiante: " + nl);
				logger.info("Ingrese el ID del estudiante a modificar: ");
				var idEstudiante = Integer.parseInt(consola.nextLine());
				//buscamos el estudiante a modificar
				Estudiantes2025 estudiante = estudianteServicio.buscarEstudiantePorId(idEstudiante);

				if (estudiante != null) {
					logger.info("Nombre del estudiante encontrado: ");
					var nombre = consola.nextLine();
					logger.info("apellido del estudiante encontrado: ");
					var apellido = consola.nextLine();
					logger.info("Telefono del estudiante encontrado: ");
					var telefono = consola.nextLine();
					logger.info("Email del estudiante encontrado: ");
					var email = consola.nextLine();
					estudiante.setNombre(nombre);
					estudiante.setApellido(apellido);
					estudiante.setTelefono(telefono);
					estudiante.setEmail(email);
					estudianteServicio.guardarEstudiante(estudiante);
					logger.info("Estudiante modifciado:" + estudiante + nl);
				} else
					logger.info("Estudiante no encontrado con el id :" + idEstudiante + nl);
			}


			case 5 -> { // Eliminar estudiante
				logger.info("Ingrese el ID del estudiante a eliminar: ");
				var id = Integer.parseInt(consola.nextLine());
				Estudiantes2025 estudiante = estudianteServicio.buscarEstudiantePorId(id);

				if (estudiante != null) {
					estudianteServicio.eliminarEstudiante(estudiante);
					logger.info("Estudiante eliminado correctamente: " + estudiante + nl);
				} else {
					logger.info("No se encontró el estudiante con ID: " + id + nl);
				}
			}

			case 6 -> { // Salir
				logger.info("Hasta pronto...");
				salir = true;
			}

			default -> logger.info("Opción inválida. Intente nuevamente." + nl);
		}

		return salir;

	}
}


