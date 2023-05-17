import java.util.Scanner;
import java.lang.Math.*;


public class exam3 {
	public static double questionOne(double radius, double unifCurrent, double magDistAxis) {
	    // some calculations and logic
		double tmpvar10 = 4*Math.PI*Math.pow(10, -7);
		double numerator1 = tmpvar10*unifCurrent*magDistAxis*Math.pow(10, -2);
		double denominator1 = 2*Math.PI*Math.pow(radius*Math.pow(10, -2), 2);
		return numerator1/denominator1;
		// current_density1 25.3 2.4 3.2 // current_density1 31 3.4 9.9
	}
	/*
	public static double questionThree() {
	    // some calculations and logic
		return 0;
	}/*
	public static double questionFour() {
	    // some calculations and logic
		return 0;
	}/*
	public static double questionFive() {
	    // some calculations and logic
		return 0;
	}/*
	public static double questionSix() {
	    // some calculations and logic
		return 0;
	}/*
	public static double questionSeven() {
	    // some calculations and logic
		return 0;
	}/*
	public static double questionEight() {
	    // some calculations and logic
		return 0;
	}/*
	public static double questionNine() {
	    // some calculations and logic
		return 0;
	}/*
	public static double questionTen() {
	    // some calculations and logic
		return 0;
	}/*
	public static double questionEleven() {
	    // some calculations and logic
		return 0;
	}/*
	public static double questionTwelve() {
	    // some calculations and logic
		return 0;
	}/*
	public static double questionThirteen() {
	    // some calculations and logic
		return 0;
	}/*
	public static double questionFourteen() {
	    // some calculations and logic
		return 0;
	}/*
	public static double questionFifteen() {
	    // some calculations and logic
		return 0;
	}/*
	public static double questionSixteen() {
	    // some calculations and logic
		return 0;
	}
	*/
	public static void main(String Args[]) {
		Scanner scnr = new Scanner(System.in);
		boolean checkerNum = true;
		String questionKey;
		
		System.out.println("type q to exit");
		
		while (checkerNum == true) {
			System.out.println("Enter the Question keyword (current_density1):");
			
			questionKey = scnr.next();
			System.out.println("You've chosen " + questionKey);
			
			if (questionKey != "q") {
				switch (questionKey) {
					case "current_density1":
						System.out.println("(abs) Give double radius, double unifCurrent, double mag_dist_axis;");
						double radius = scnr.nextDouble();
						double unifCurrent = scnr.nextDouble();
						double mag_dist_axis = scnr.nextDouble();
						System.out.println(questionOne(radius, unifCurrent, mag_dist_axis)); 
						break;/*
					case "REPLACE_THIS_CASE":
						System.out.println("Give double");
						double v1 = scnr.nextDouble();
						System.out.println(questionTwo(v1));
						break;/*
					case "REPLACE_THIS_CASEe":
						System.out.println("Give double");
						double v1 = scnr.nextDouble();
						System.out.println(questionThree(v1));
						break;/*
					case "REPLACE_THIS_CASE":
						System.out.println("Give double");
						double v1 = scnr.nextDouble();
						System.out.println(questionFour(v1));
						break;/*
					case "REPLACE_THIS_CASE":
						System.out.println("Give double");
						double v1 = scnr.nextDouble();
						System.out.println(questionFive(v1));
						break;/*
					case "REPLACE_THIS_CASE":
						System.out.println("Give double");
						double v1 = scnr.nextDouble();
						System.out.println(questionSix(v1));
						break;/*
					case "REPLACE_THIS_CASE":
						System.out.println("Give double");
						double v1 = scnr.nextDouble();
						System.out.println(questionSeven(v1));
						break;/*
					case "REPLACE_THIS_CASE":
						System.out.println("Give double");
						double v1 = scnr.nextDouble();
						System.out.println(questionEight(v1));
						break;/*
					case "REPLACE_THIS_CASEe":
						System.out.println("Give double");
						double v1 = scnr.nextDouble();
						System.out.println(questionNine(v1));
						break;/*
					case "REPLACE_THIS_CASE":
						System.out.println("Give double");
						double v1 = scnr.nextDouble();
						System.out.println(questionTen(v1));
						break;/*
					case "REPLACE_THIS_CASE":
						System.out.println("Give double");
						double v1 = scnr.nextDouble();
						System.out.println(questionEleven(v1));
						break;/*
					case "REPLACE_THIS_CASE":
						System.out.println("Give double");
						double v1 = scnr.nextDouble();
						System.out.println(questionTwelve(v1));
						break;/*
					case "REPLACE_THIS_CASE":
						System.out.println("Give double");
						double v1 = scnr.nextDouble();
						System.out.println(questionThirteen(v1));
						break;/*
					case "REPLACE_THIS_CASE":
						System.out.println("Give double");
						double v1 = scnr.nextDouble();
						System.out.println(questionFourteen(v1));
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
