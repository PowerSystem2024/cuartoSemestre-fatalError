package utn.tienda_libros;

import org.springframework.boot.WebApplicationType;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.context.ConfigurableApplicationContext;
import utn.tienda_libros.vista.LibroFrom;

@SpringBootApplication
public class TiendaLibrosApplication {

    public static void main(String[] args) {
        // Iniciamos el contexto de Spring Boot
        ConfigurableApplicationContext contextoSpring =
                new SpringApplicationBuilder(TiendaLibrosApplication.class)
                        .headless(false)
                        .web(WebApplicationType.NONE)
                        .run(args);

        contextoSpring.getBean(LibroFrom.class);
    }
}