
package Ejercicio1;

import java.util.Scanner;


//Tienda de libros
public class Ejercicio1 {
       public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite el nombre del libro: ");
        String nombreLibro = entrada.nextLine();
        System.out.println("Digite el id del libro: ");
        int idLibro = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite el precio del libro: ");
        double precioLibro = Double.parseDouble(entrada.nextLine());
        System.out.println("Confirme si el envio es gratuito: ");
        boolean envioGratuito = Boolean.parseBoolean(entrada.nextLine());
        
        // Mostramos por pantalla los resultados
        System.out.println(nombreLibro+" #"+idLibro);
        System.out.println("El precio es: $"+precioLibro);
        System.out.println("El envio es gratuito?: "+envioGratuito);
    }
}
