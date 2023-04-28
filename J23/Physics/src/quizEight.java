import java.util.Scanner;
import java.lang.Math.*;

public class quizEight {
	public static double questionOne(double amps, double diameter) {
	      // some calculations and logic
		double base = 10;
		int exponent = -3;
		return (3*amps*Math.pow(base, exponent))/(2*Math.PI*Math.pow((diameter/2*Math.pow(base, exponent)), 2));
	}
	
	public static double questionTwo(double watts, double voltage, double time) {
	      // some calculations and logic
		return watts*time*3600.0/Math.pow(10, 6);
	}
	
	public static double questionThree(double volts, double watts, double currentPercent) {
	      // some calculations and logic
		double I_0 = (volts/watts)*currentPercent;
		return Math.pow(I_0, 2)*(watts/Math.pow(volts/watts, 2));
	}
	
	public static double questionFour(double resivity, double current, double radius, double length) {
	      // some calculations and logic
		double resistance = (resivity*Math.pow(10, -9)*length)/(Math.PI*radius/100);
		System.out.println("Converting answer from V to microV (*10^6)");
		return current*resistance*100; //convert V to microV
	}
	
	public static double questionFive(double resivity4, double currentDensity) {
	      // some calculations and logic
		return resivity4*currentDensity/100;
	}
	
	public static void main(String Args[]) {
		Scanner scnr = new Scanner(System.in);
		boolean checkerNum = true;
		String questionKey;
		
		System.out.println("type q to exit");
		
		while (checkerNum == true) {
			System.out.println("Enter the Question keyword (choose J_0, heat_energy, bulb_power, potential_diff, and mag_ef):");
			
			questionKey = scnr.next();
			
			System.out.println("You've chosen " + questionKey);
			
			if (questionKey != "q") {
				switch (questionKey) {
					case "J_0":
						System.out.println("enter amps (mA) and diameter (mm) separated by a space i.e. 3.0 9.0:");
						double amps = scnr.nextDouble();
						double diameter = scnr.nextDouble();
						System.out.println(questionOne(amps, diameter));
						break;
					case "heat_energy":
						System.out.println("enter watts (W), voltage(V), and time (hrs) separated by a space i.e. 100.0 110 7.9:");
						double watt = scnr.nextDouble();
						double voltage = scnr.nextDouble();
						double time = scnr.nextDouble();
						System.out.println(questionTwo(watt, voltage, time));
						break;
					case "bulb_power":
						System.out.println("enter volts (V), watts (W), and current % (decimal) separated by a space i.e. 99.0 46.2 .505:");
						double volts = scnr.nextDouble();
						double watts = scnr.nextDouble();
						double currentPercent = scnr.nextDouble();
						System.out.println(questionThree(volts, watts, currentPercent));
						break;
					case "potential_diff":
						System.out.println("enter resivity (in nano, or 10^-9), current(A), radius(cm), and length(m) separated by a space i.e. 12.8 3.01 3.4 41.0:");
						double resivity = scnr.nextDouble();
						double current = scnr.nextDouble();
						double radius = scnr.nextDouble();
						double length = scnr.nextDouble();
						System.out.println(questionFour(resivity, current, radius, length));
						break;
					case "mag_ef":
						System.out.println("enter resivity (omega*m), currentDensity(A/mm^2) separated by a space i.e. 5.88 489.3:");
						double resivity4 = scnr.nextDouble();
						double currentDensity = scnr.nextDouble();
						System.out.println(questionFive(resivity4, currentDensity));
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