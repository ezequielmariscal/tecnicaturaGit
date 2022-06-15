/*
 Guillermo tiene N dólares. Luis tiene la mitad de lo que posee
 Guillermo. Juan tiene la mitad de lo que poseen Luis y Guillermo juntos.
 Hacer un programa que calcule e imprima la cantidad de dinero que
 tienen entre los tres.
Crear un nuevo proyecto ejercicio_6
 */
package ejercicio_6;

import java.util.Scanner;

public class Ejercicio_6 {

   
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float guillermo,luis,juan,total;      
        System.out.println("Introduzca la cantidad de dinero que tiene Guillermo: ");
        guillermo = Float.parseFloat(entrada.nextLine());
        
        luis = guillermo / 2;
        juan = (luis + guillermo)/2;
        total = luis + guillermo + juan;
        System.out.println("\nEl dinero de luis es: U$D"+luis);
        System.out.println("El dinero de juan es: U$D"+juan);
        System.out.println("El total de dinero que tienen los tres es: U$D"+total);
    }
    
}
