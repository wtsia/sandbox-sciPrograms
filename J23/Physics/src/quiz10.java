import java.util.Scanner;
import java.lang.Math.*;

public class quiz10 {
	public static double questionOne(double b_x, double b_y, double b_z, double current, double length) {
	      // some calculations and logic
		return current*Math.sqrt(Math.pow(length*b_y, 2) + Math.pow(length*b_z, 2));
	}
	
	public static double questionTwo(double b_x2, double b_y2, double b_z2, double protonVel) {
	      // some calculations and logic -3.6 24.66 0 88   -8.47 32.91 0 107
		double new_y = protonVel*b_x2*1.6/1000;
		double new_x = protonVel*b_y2*-1.6/1000;
		return 180 + (Math.atan(new_y/new_x) * 180 / Math.PI);
	}
	
	public static double questionThree(double velocity_prot, double field_mag) {
	      // some calculations and logic
		return field_mag/velocity_prot;
	}
	
	public static double questionFour(double period_EL) {
	      // some calculations and logic
		return 2*Math.PI*9.1/1.6/period_EL; //convert V to microV
	}
	
	public static double questionFive(double q, double m, double delta_v, double b) {
	      // some calculations and logic
		return Math.sqrt(2*m*delta_v/q/Math.pow(b, 2)*1000);
	}
	
	
	public static void main(String Args[]) {
		Scanner scnr = new Scanner(System.in);
		boolean checkerNum = true;
		String questionKey;
		
		System.out.println("type q to exit");
		
		while (checkerNum == true) {
			System.out.println("Enter the Question keyword (wire_force; angle_force_mag; mag_field_PR; mag_field_EL; rad_mag_field):");
			
			questionKey = scnr.next();
			
			System.out.println("You've chosen " + questionKey);
			
			if (questionKey != "q") {
				switch (questionKey) {
					case "wire_force":
						System.out.println("Give double B_x, double B_y, double B_z, and double current, and double length in that order");
						double b_x1 = scnr.nextDouble();
						double b_y1 = scnr.nextDouble();
						double b_z1 = scnr.nextDouble();
						double current = scnr.nextDouble();
						double length = scnr.nextDouble();
						System.out.println(questionOne(b_x1, b_y1, b_z1, current, length));
						break;
						
					case "angle_force_mag":
						System.out.println("Give double B_x, double B_y, double B_z, and double protonVel in that order");
						double b_x2 = scnr.nextDouble();
						double b_y2 = scnr.nextDouble();
						double b_z2 = scnr.nextDouble();
						double protonVel = scnr.nextDouble();
						System.out.println(questionTwo(b_x2, b_y2, b_z2, protonVel));
						break;
					case "mag_field_PR":
						System.out.println("Give double velocity_prot, and double field_mag in that order");
						double velocity_prot = scnr.nextDouble();
						double field_mag = scnr.nextDouble();
						System.out.println(questionThree(velocity_prot, field_mag));
						break;
					case "mag_field_EL":
						System.out.println("Give double period");
						double period_EL = scnr.nextDouble();
						System.out.println(questionFour(period_EL));
						break;
					case "rad_mag_field":
						System.out.println("give double q double m double delta_v and double b");
						double q = scnr.nextDouble();
						double m = scnr.nextDouble();
						double delta_v = scnr.nextDouble();
						double b = scnr.nextDouble();
						System.out.println(questionFive(q, m, delta_v, b));
						break;
					case "q":
						checkerNum = false;
						return;
				} 
			} else {
					System.out.println("Goodbye!");
			}
		}
	}
}
