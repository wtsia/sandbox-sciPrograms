import java.util.Scanner;
import java.lang.Math.*;

public class quizOne {
	public static double questionOne(double initElecRemoved) {
		return initElecRemoved*1.602*100;
	} // elec_rem 6.87 res: 1100.574

	public static double questionTwo(double pointChg, double chgDist, double elecForce) {
	      // some calculations and logic
		return chgDist*chgDist*elecForce/(9*pointChg);
	}

	public static double questionThree(double charge1, double charge2, double forceExert) {
	      // some calculations and logic
		return Math.sqrt(charge1 * Math.abs(charge2) * 9.0 / forceExert * Math.pow(10,-3));
	} // dist_btwn_chg 6.63 83 5.256 RES: 0.9707

	public static double questionFour(double charge1, double dist, double charge2, double degree) {
	      // some calculations and logic
		return 9 * charge1 * charge2 / (dist * dist) * 10;
	} // mag_force_on_chg 38.6 91.9 69.7 60 60 RES: 30.36
	// mag_force_on_chg 24.3 73.5 75 60 RES: 30.36

	public static double questionFive(double charge0, double charge1, double charge1DistY, double charge2, double charge2DistX) {
	      // some calculations and logic
		double fQ1 = -1 * 8.99 * charge0 * charge1 / Math.abs(charge1DistY * charge1DistY);
		double fQ2 = -1 * 8.99 * charge0 * charge2 / Math.abs(charge2DistX * charge2DistX);
		return Math.sqrt(Math.pow(Math.abs(fQ1),2) + Math.pow(Math.abs(fQ2),2))/1000;
	} // mag_net_force 4.2 21 1.25 -21 1.25 RES: 0.7185
	
	public static void main(String Args[]) {
		Scanner scnr = new Scanner(System.in);
		boolean checkerNum = true;
		String questionKey;
		
		System.out.println("type q to exit");
		
		while (checkerNum == true) {
			System.out.println("Enter the Question keyword (elec_rem, mag_charge, dist_btwn_chg, mag_force_on_chg, mag_net_force):");
			
			questionKey = scnr.next();
			
			System.out.println("You've chosen " + questionKey);
			
			if (questionKey != "q") {
				switch (questionKey) {
					case "elec_rem":
						System.out.println("give double initElecRemoved in 10^15");
						double initElecRemoved = scnr.nextDouble();
						System.out.println(questionOne(initElecRemoved));
						break;
					case "mag_charge":
						System.out.println("give double pointChg, chgDist, elecForce");
						double pointChg = scnr.nextDouble();
						double chgDist = scnr.nextDouble();
						double elecForce = scnr.nextDouble();
						System.out.println(questionTwo(pointChg, chgDist, elecForce));
						break;
					case "dist_btwn_chg":
						System.out.println("give double charge1, charge2, forceExert");
						double charge13 = scnr.nextDouble();
						double charge23 = scnr.nextDouble();
						double forceExert3 = scnr.nextDouble();
						System.out.println(questionThree(charge13, charge23, forceExert3));
						break;
					case "mag_force_on_chg":
						System.out.println("give double charge1, dist, charge2, degree");
						double charge14 = scnr.nextDouble();
						double dist4 = scnr.nextDouble();
						double charge24 = scnr.nextDouble();
						double degree4 = scnr.nextDouble();
						System.out.println(questionFour(charge14, dist4, charge24, degree4));
						break;
					case "mag_net_force":
						System.out.println("give double charge0, charge1, charge1DistY, charge2, charge2DistX");
						double charge05 = scnr.nextDouble();
						double charge15 = scnr.nextDouble();
						double charge1DistY5 = scnr.nextDouble();
						double charge25 = scnr.nextDouble();
						double charge2DistX5 = scnr.nextDouble();
						System.out.println(questionFive(charge05, charge15, charge1DistY5, charge25, charge2DistX5));
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
