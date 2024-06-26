import java.util.Scanner;
import java.lang.Math.*;

public class quiz9 {
	public static double questionOne(double emf, double ivar, double internalRes) {
	      // some calculations and logic
		double tmpvar = emf/ivar;
		tmpvar = tmpvar - internalRes;
		return Math.pow(ivar, 2)*tmpvar;
	}
	
	public static double questionTwo(double r1, double r2, double r3, double r4, double r5, double i1, double i2) {
	      // some calculations and logic
		double tmpI = i1 + i2;
		return (i2*r2 + i2*r5 + tmpI*r4)/1000;
	}

	public static double questionThree(double r1, double r2, double r3, double voltage) {
	      // some calculations and logic
		return Math.pow((voltage/(r1 + r2)),2)*r2;
	}
	
	public static double questionFour(double vVar, double rVar, double capVar,  double rateDenominator) {
		// some calculations and logic
		System.out.println(vVar + " " + rVar + " " + capVar + " " + rateDenominator);
	  return vVar/rVar * (rateDenominator - 1)/rateDenominator;
  }
	
	public static double questionFive(double vVar, double rVar, double capVar, double rateDenominator) {
	      // some calculations and logic
		return vVar/(rVar * Math.pow(10, 3) * rateDenominator) * Math.pow(10, 6);
	}
	
	
	public static void main(String Args[]) {
		Scanner scnr = new Scanner(System.in);
		boolean checkerNum = true;
		String questionKey;
		
		System.out.println("type q to exit");
		
		while (checkerNum == true) {
			System.out.println("Enter the Question keyword (power_dissipated, battery_voltage, pow_resistor, current_circuit, curr_cir_2):");
			
			questionKey = scnr.next();
			
			System.out.println("You've chosen " + questionKey);
			
			if (questionKey != "q") {
				switch (questionKey) {
					case "power_dissipated":
						System.out.println("Give double emf, double ivar, double internalRes in that order");
						double emf = scnr.nextDouble();
						double ivar = scnr.nextDouble();
						double internalRes = scnr.nextDouble();
						System.out.println(questionOne(emf, ivar, internalRes));
						break;
						
					case "battery_voltage":
						System.out.println("Give (double) r1, r2, r3, r4, r5, i1, i2 in order");
						double r1 = scnr.nextDouble();
						double r2 = scnr.nextDouble();
						double r3 = scnr.nextDouble();
						double r4 = scnr.nextDouble();
						double r5 = scnr.nextDouble();
						double i1 = scnr.nextDouble();
						double i2 = scnr.nextDouble();
						System.out.println(questionTwo(r1, r2, r3, r4, r5, i1, i2));
						break;
					case "pow_resistor":
						System.out.println("Give (doubles) r_1, r_2, r_3, voltage in that order");
						double r_1 = scnr.nextDouble();
						double r_2 = scnr.nextDouble();
						double r_3 = scnr.nextDouble();
						double voltage = scnr.nextDouble();
						System.out.println(questionThree(r_1, r_2, r_3, voltage));
						break;
					case "current_circuit":
						System.out.println("Give (doubles) vVar (pot, source), rVar (resistor), capVar, and rateDenominator (give denominator i.e. 1/7 = 7)");
						double vVar = scnr.nextDouble();
						double rVar = scnr.nextDouble();
						double capVar = scnr.nextDouble();
						double rateDenominator = scnr.nextDouble();
						System.out.println(questionFour(vVar, rVar, capVar, rateDenominator));
						break;
					case "curr_cir_2":
						System.out.println("Give (doubles) vVar (pot, source), rVar (resistor), capVar, and rateDenominator (give denominator i.e. 1/7 = 7)");
						double vVar2 = scnr.nextDouble();
						double rVar2 = scnr.nextDouble();
						double capVar2 = scnr.nextDouble();
						double rateDenominator2 = scnr.nextDouble();
						System.out.println(questionFive(vVar2, rVar2, capVar2, rateDenominator2));
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
