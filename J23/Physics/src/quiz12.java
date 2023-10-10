import java.util.Scanner;
import java.lang.Math.*;

public class quiz12 {
	public static double questionOne(double distance, double current) {
	      // some calculations and logic
		double tmpvar = 4*Math.PI*Math.pow(10, -7)*current/(2*Math.PI*distance*Math.pow(10, -2));
		tmpvar = Math.pow(tmpvar, 2)/(2*4*Math.PI*Math.pow(10, -7));
		return tmpvar*1000000; //energy_density_field 23 18.12
	}
	public static double questionTwo(double voltage, double idealInductor, double resistor, double time, double timeFinal) {
	      // some calculations and logic
		return voltage/resistor*(1-Math.pow(Math.E, (-resistor*timeFinal/idealInductor))); // current_in_circuit 45 20 61 0 4.42
	}
	public static double questionThree(double voltage, double inductor, double resistor, double percent) {
	      // some calculations and logic
		double tmpvar = voltage/resistor;
		tmpvar = tmpvar*percent/100;
		return 1.0/2.0*inductor*Math.pow(tmpvar, 2);// energy_in_inductor 46 18 22 45
	}
	public static double questionFour(double inductor, double current, double resistor) {
	      // some calculations and logic
		return 1.0/2.0*inductor/1000*Math.pow(current/100, 2)*10000;// energy_in_mag_field 4.8 85 33
	}
	public static double questionFive(double radius, double length, double loops, double current) {
	      // some calculations and logic
		double tmpvar = 4*Math.PI*Math.pow(10, -7)*loops*current/(length*Math.pow(10, -2));
		return Math.pow(tmpvar, 2)/(2*4*Math.PI*Math.pow(10, -7)); // energy_density_solenoid 2.17 58.71 751 3.46
	}
	public static void main(String Args[]) {
		Scanner scnr = new Scanner(System.in);
		boolean checkerNum = true;
		String questionKey;
		
		System.out.println("type q to exit");
		
		while (checkerNum == true) {
			System.out.println("Enter the Question keyword (energy_density_field, current_in_circuit, energy_in_inductor, energy_in_mag_field, energy_density_solenoid):");
			
			questionKey = scnr.next();
			
			System.out.println("You've chosen " + questionKey);
			
			if (questionKey != "q") {
				switch (questionKey) {
					case "energy_density_field":
						System.out.println("Give double distance, double current in that order");
						double distance1 = scnr.nextDouble();
						double current1 = scnr.nextDouble();
						System.out.println(questionOne(distance1, current1));
						break;
					case "current_in_circuit":
						System.out.println("Give double voltage, double idealInductor, double resistor, double time, double timeFinal in that order");
						double voltage2 = scnr.nextDouble();
						double idealI2 = scnr.nextDouble();
						double resistor2 = scnr.nextDouble();
						double time2 = scnr.nextDouble();
						double timeFinal2 = scnr.nextDouble();
						System.out.println(questionTwo(voltage2, idealI2, resistor2, time2, timeFinal2)); 
						break;
					case "energy_in_inductor":
						System.out.println("Give double voltage, double inductor, double resistor, double percent in that order");
						double voltage3 = scnr.nextDouble();
						double inductor3 = scnr.nextDouble();
						double resistor3 = scnr.nextDouble();
						double percent3 = scnr.nextDouble();
						System.out.println(questionThree(voltage3, inductor3, resistor3, percent3));
						break;
					case "energy_in_mag_field":
						System.out.println("Give double inductor, double current, double resistor in that order");
						double inductor4 = scnr.nextDouble();
						double current4 = scnr.nextDouble();
						double resistor4 = scnr.nextDouble();
						System.out.println(questionFour(inductor4, current4, resistor4));
						break;
					case "energy_density_solenoid":
						System.out.println("Give double radius, double length, double loops, double current in that order");
						double radius5 = scnr.nextDouble();
						double length5 = scnr.nextDouble();
						double loops5 = scnr.nextDouble();
						double current5 = scnr.nextDouble();
						System.out.println(questionFive(radius5, length5, loops5, current5));
						break;/*
						*/
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
