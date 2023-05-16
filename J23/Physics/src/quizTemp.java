import java.util.Scanner;
import java.lang.Math.*;

public class quizTemp {
	public static double questionOne(double emf, double ivar, double internalRes) {
	      // some calculations and logic
		double tmpvar = emf/ivar;
		tmpvar = tmpvar - internalRes;
		return Math.pow(ivar, 2)*tmpvar;
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
			System.out.println("Enter the Question keyword (power_dissipated):");
			
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
						/*
					case "MY CASE":
						System.out.println("CASE INSTRUCTIONS");
						double var1 = scnr.nextDouble();
						double var2 = scnr.nextDouble();
						double var3 = scnr.nextDouble();
						System.out.println(questionTwo(var1, var2, var3));
						break;/*
					case "MY CASE":
						System.out.println("CASE INSTRUCTIONS");
						double var1 = scnr.nextDouble();
						double var2 = scnr.nextDouble();
						double var3 = scnr.nextDouble();
						System.out.println(questionTwo(var1, var2, var3));
						break;/*
					case "MY CASE":
						System.out.println("CASE INSTRUCTIONS");
						double var1 = scnr.nextDouble();
						double var2 = scnr.nextDouble();
						double var3 = scnr.nextDouble();
						System.out.println(questionTwo(var1, var2, var3));
						break;/*
					case "MY CASE":
						System.out.println("CASE INSTRUCTIONS");
						double var1 = scnr.nextDouble();
						double var2 = scnr.nextDouble();
						double var3 = scnr.nextDouble();
						System.out.println(questionTwo(var1, var2, var3));
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
