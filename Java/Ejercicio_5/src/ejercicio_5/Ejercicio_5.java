/* Ejercicio 5
calcular e imprimir la suma de 
tres calificaciones
Pedir las notas al usuario,
*/
package ejercicio_5;

import java.util.Scanner;


public class Ejercicio_5 {

 
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Introduzca la primera calificación: ");
        double c1 = Double.parseDouble(entrada.nextLine());
        System.out.println("Introduzca la segunda calificación: ");
        double c2 = Double.parseDouble(entrada.nextLine());
        System.out.println("Introduzca la tercera calificación: ");
        double c3 = Double.parseDouble(entrada.nextLine());
        var resultado = c1 + c2 + c3;
        System.out.println("El resultado de la suma de las tres calificaciones es: " + resultado);
        
    }
    
}
