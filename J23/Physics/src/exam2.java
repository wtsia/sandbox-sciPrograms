import java.util.Scanner;
import java.lang.Math.*;

public class exam2 {
	public static double questionOne(double q_a, double q_b, double r_0, double r_f) {
	      // some calculations and logic
		return 9*q_a*q_b*(1/r_0-1/r_f)/10*-1;
	}
	
	public static double questionTwo(double q2_1, double m2_1, double r2_0, double d2) {
	      // some calculations and logic
		double lambda2 = r2_0 + d2/100;
		double quantity2 = 1/r2_0 - 1/lambda2;
		double numerator2 = 9*1.6*q2_1*2*quantity2;
		return Math.sqrt(numerator2/9.1)*1000;
	}
	
	public static double questionThree(double r_0, double v_0, double lambda, double q, double m) {
	      // some calculations and logic
		double num3 = m*Math.pow(v_0, 2)*Math.PI*2*8.85;
		double den3 = 2*q*lambda;
		double rhs3 = num3/den3/-1000;
		return r_0*Math.exp(rhs3);
	}
	/*
	public static double questionFour() {
	      // some calculations and logic
		return //return val; //convert V to microV
	}
	/*
	public static double questionFive() {
	      // some calculations and logic
		return //return val;
	}
	/*
	public static double questionTwo() {
	      // some calculations and logic
		return //return val;
	}
	/*
	public static double questionThree() {
	      // some calculations and logic
		return //return val;
	}
	/*
	public static double questionFour() {
	      // some calculations and logic
		return //return val; //convert V to microV
	}
	/*
	public static double questionFive() {
	      // some calculations and logic
		return //return val;
	}
	/*
	public static double questionTwo() {
	      // some calculations and logic
		return //return val;
	}
	/*
	public static double questionThree() {
	      // some calculations and logic
		return //return val;
	}
	/*
	public static double questionFour() {
	      // some calculations and logic
		return //return val; //convert V to microV
	}
	/*
	public static double questionFive() {
	      // some calculations and logic
		return //return val;
	}
	/*
	public static double questionTwo() {
	      // some calculations and logic
		return //return val;
	}
	/*
	public static double questionThree() {
	      // some calculations and logic
		return //return val;
	}
	/*
	public static double questionFour() {
	      // some calculations and logic
		return //return val; //convert V to microV
	}
	/*
	public static double questionFive() {
	      // some calculations and logic
		return //return val;
	}
	*/
	
	public static void main(String Args[]) {
		Scanner scnr = new Scanner(System.in);
		boolean checkerNum = true;
		String questionKey;
		
		System.out.println("type q to exit");
		
		while (checkerNum == true) {
			System.out.println("Enter the Question keyword (two_elec_charges;a_charge_and_mass;a_particle_of_charge;):");
			
			questionKey = scnr.next();
			
			System.out.println("You've chosen " + questionKey);
			
			if (questionKey != "q") {
				switch (questionKey) {
					case "two_elec_charges":
						System.out.println("(abs) Give double q_a, double q_b, double r_0, double r_f;");
						double q1_a = scnr.nextDouble();
						double q1_b = scnr.nextDouble();
						double r1_0 = scnr.nextDouble();
						double r1_f = scnr.nextDouble();
						System.out.println(questionOne(q1_a, q1_b, r1_0, r1_f));
						break;
						
					case "a_charge_and_mass":
						System.out.println("(abs) Give double q_1, double m_1, double r_0, double d;");
						double q2_1 = scnr.nextDouble();
						double m2_1 = scnr.nextDouble();
						double r2_0 = scnr.nextDouble();
						double d2 = scnr.nextDouble();
						System.out.println(questionTwo(q2_1, m2_1, r2_0, d2));
						break;
					case "a_particle_of_charge":
						System.out.println("(abs) Give double r_0, double v_0, double lambda, double q, double m;");
						double r3_0 = scnr.nextDouble();
						double v3_0 = scnr.nextDouble();
						double lambda3 = scnr.nextDouble();
						double q3 = scnr.nextDouble();
						double m3 = scnr.nextDouble();
						System.out.println(questionThree(r3_0, v3_0, lambda3, q3, m3));
						break;/*
					case "CASE 1":
						System.out.println("CASE INSTRUCTIONS");
						double resivity = scnr.nextDouble();
						double current = scnr.nextDouble();
						double radius = scnr.nextDouble();
						double length = scnr.nextDouble();
						System.out.println(questionFour(resivity, current, radius, length));
						break;/*
					case "CASE 1":
						System.out.println("CASE INSTRUCTIONS");
						double resivity4 = scnr.nextDouble();
						double currentDensity = scnr.nextDouble();
						System.out.println(questionFive(resivity4, currentDensity));
						break;
						/*
					case "battery_voltage":
						System.out.println("CASE INSTRUCTIONS");
						double watt = scnr.nextDouble();
						double voltage = scnr.nextDouble();
						double time = scnr.nextDouble();
						System.out.println(questionTwo(watt, voltage, time));
						break;/*
					case "CASE 1":
						System.out.println("CASE INSTRUCTIONS");
						double volts = scnr.nextDouble();
						double watts = scnr.nextDouble();
						double currentPercent = scnr.nextDouble();
						System.out.println(questionThree(volts, watts, currentPercent));
						break;/*
					case "CASE 1":
						System.out.println("CASE INSTRUCTIONS");
						double resivity = scnr.nextDouble();
						double current = scnr.nextDouble();
						double radius = scnr.nextDouble();
						double length = scnr.nextDouble();
						System.out.println(questionFour(resivity, current, radius, length));
						break;/*
					case "CASE 1":
						System.out.println("CASE INSTRUCTIONS");
						double resivity4 = scnr.nextDouble();
						double currentDensity = scnr.nextDouble();
						System.out.println(questionFive(resivity4, currentDensity));
						break;
						/*
					case "battery_voltage":
						System.out.println("CASE INSTRUCTIONS");
						double watt = scnr.nextDouble();
						double voltage = scnr.nextDouble();
						double time = scnr.nextDouble();
						System.out.println(questionTwo(watt, voltage, time));
						break;/*
					case "CASE 1":
						System.out.println("CASE INSTRUCTIONS");
						double volts = scnr.nextDouble();
						double watts = scnr.nextDouble();
						double currentPercent = scnr.nextDouble();
						System.out.println(questionThree(volts, watts, currentPercent));
						break;/*
					case "CASE 1":
						System.out.println("CASE INSTRUCTIONS");
						double resivity = scnr.nextDouble();
						double current = scnr.nextDouble();
						double radius = scnr.nextDouble();
						double length = scnr.nextDouble();
						System.out.println(questionFour(resivity, current, radius, length));
						break;/*
					case "CASE 1":
						System.out.println("CASE INSTRUCTIONS");
						double resivity4 = scnr.nextDouble();
						double currentDensity = scnr.nextDouble();
						System.out.println(questionFive(resivity4, currentDensity));
						break;
						/*
					case "battery_voltage":
						System.out.println("CASE INSTRUCTIONS");
						double watt = scnr.nextDouble();
						double voltage = scnr.nextDouble();
						double time = scnr.nextDouble();
						System.out.println(questionTwo(watt, voltage, time));
						break;/*
					case "CASE 1":
						System.out.println("CASE INSTRUCTIONS");
						double volts = scnr.nextDouble();
						double watts = scnr.nextDouble();
						double currentPercent = scnr.nextDouble();
						System.out.println(questionThree(volts, watts, currentPercent));
						break;/*
					case "CASE 1":
						System.out.println("CASE INSTRUCTIONS");
						double resivity = scnr.nextDouble();
						double current = scnr.nextDouble();
						double radius = scnr.nextDouble();
						double length = scnr.nextDouble();
						System.out.println(questionFour(resivity, current, radius, length));
						break;/*
					case "CASE 1":
						System.out.println("CASE INSTRUCTIONS");
						double resivity4 = scnr.nextDouble();
						double currentDensity = scnr.nextDouble();
						System.out.println(questionFive(resivity4, currentDensity));
						break;
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
