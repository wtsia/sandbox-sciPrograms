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
	
	public static double questionFour(double r4_a, double r4_b, double k4, double l4, double v4) {
	      // some calculations and logic
		double c4 = (k4*l4)/(2*9*Math.pow(10, 9)*Math.log(r4_b/r4_a));
		return 0.5*c4*Math.pow(v4, 2)*Math.pow(10, 9); //a_cylindrical_capacitor 9.8 16 1.7 6.5 42.8
	}
	
	public static double questionFive(double c5, double v5, double percent5) {
	      // some calculations and logic
		double stored5_en = 0.5*c5*Math.pow(v5, 2);
		double d5_new = 1+percent5/100;
		double c5_new = c5/d5_new;
		double u5_new = 0.5*c5_new*Math.pow(v5, 2);
		return u5_new - stored5_en; //a_parallel_plate 2.9 11.9 29
	}
	
	public static double questionSix(double c_1, double c_2, double c_3, double v) {
	      // some calculations and logic
		double q6_0 = v/(1/c_1 + 1/(c_2 + c_3))/100;
		double v6_2 = q6_0/(c_2 +c_3);
		return v6_2*c_2*100; //in_the_figure_3 25 63 14 7
	}
	
	public static double questionSeven(double c, double v) {
	      // some calculations and logic
		
		return 3*c/5;
	}
	
	public static double questionEight(double v, double r_a, double r_b, double r) {
	      // some calculations and logic
		return 0.5*8.84*Math.pow(v/(1/r_a-1/r_b)/Math.pow(r, 2), 2)/Math.pow(10, 6); //an_air_filled_sphere 1013 26.4 30 27.4
	}
	
	public static double questionNine(double phi, double i, double r, double bigL) {
	      // some calculations and logic
		
		double bigR9 = phi*bigL/(Math.PI*Math.pow(r, 2));
		return i*bigR9/10000; //a_wire_is_made 5.5 12.5 1 63
	}
	
	public static double questionTen(double r_1, double r_2, double r_3) {
	      // some calculations and logic
		double r10_12 = r_1*r_2/(r_1 + r_2);
		return r10_12 + r_3; //resistors_of_value 102 422 840
	}
	
	public static double questionEleven(double r, double c, double v_0, double t, double charge) {
	      // some calculations and logic
		return v_0/r*(1/charge)*1000; //an_r_resistor_init_pot 181 43 11 0 7
	}
	
	public static double questionTwelve(double resis, double capac, double pot_src, double t, double percent) {
	      // some calculations and logic
		double tau12 = resis*capac/1000;
		double el12 = Math.log(percent/100)*tau12*-1;
		double roe12 = capac*pot_src*(1-percent/100);
		return 0.5*Math.pow(roe12, 2)/capac; //an_r_resistor_pot_src 24 48 15 0 79
	}
	
	public static double questionThirteen(double diameter, double current) {
	      // some calculations and logic
		double convertIn = diameter*.0254;
		return current/(8.5*1.6*Math.PI/4*Math.pow(convertIn, 2))/1000; //the_diameter_of_a_copper 0.086 16.4
	}
	
	public static double questionFourteen(double i_1, double i_2, double v_q) {
	      // some calculations and logic
		return v_q-3*i_2/1000;// in_the_figure_the_current 33 505 4.7
	}
	
	public static double questionFifteen(double i_0, double tau) {
	      // some calculations and logic
		return i_0*tau/1.6*10; // the_current_supplied 4.13 34.3
	}
	
	public static double questionSixteen(double x_start, double x_end, double x_density, double proton_release, double proton_mov) {
	      // some calculations and logic
		double x16_dev = x_end - x_start; //0.4
		double tmp16_vmin1 = (proton_release+(x16_dev))/proton_release;
		double tmp16_vmin2 = ((proton_release+proton_mov*.01)+(x16_dev))/(proton_release+proton_mov*.01);
		//System.out.println(tmp16_vmin1 + " " + tmp16_vmin2);
		double del16_v = -9*x_density*(Math.log(tmp16_vmin1) - Math.log(tmp16_vmin2));
		double pot16_eng = del16_v*1.6*10;
		System.out.println("Values: " + x16_dev + " " + tmp16_vmin1 + " " +  tmp16_vmin2 + " " +  del16_v + " " +  pot16_eng);
		return Math.sqrt(pot16_eng*-1*2/1.67*10000); // a_line_of_charge_is_placed -0.4 0 4.15 8.67 10
		
	}
	
	public static void main(String Args[]) {
		Scanner scnr = new Scanner(System.in);
		boolean checkerNum = true;
		String questionKey;
		
		System.out.println("type q to exit");
		
		while (checkerNum == true) {
			System.out.println("\nEnter the Question keyword (two_elec_charges; a_charge_and_mass; a_particle_of_charge; a_cylindrical_capacitor;a_parallel_plate; in_the_figure_3; in_the_figure_all; an_air_filled_sphere; a_wire_is_made; resistors_of_value; an_r_resistor_init_pot; an_r_resistor_pot_src; the_diameter_of_a_copper; in_the_figure_the_current; the_current_supplied; a_line_of_charge_is_placed):");
			
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
						// two_elec_charges 7.1 19 76 20
						// two_elec_charges 2.6 20 83 25
						break;
						
					case "a_charge_and_mass":
						System.out.println("(abs) Give double q_1, double m_1, double r_0, double d;");
						double q2_1 = scnr.nextDouble();
						double m2_1 = scnr.nextDouble();
						double r2_0 = scnr.nextDouble();
						double d2 = scnr.nextDouble();
						System.out.println(questionTwo(q2_1, m2_1, r2_0, d2)); 
						// a_charge_and_mass 3.6 5.2 4.2 36
						// a_charge_and_mass 5.8 5.2 5.5 28
						break;
					case "a_particle_of_charge":
						System.out.println("(abs) Give double r_0, double v_0, double lambda, double q, double m;");
						double r3_0 = scnr.nextDouble();
						double v3_0 = scnr.nextDouble();
						double lambda3 = scnr.nextDouble();
						double q3 = scnr.nextDouble();
						double m3 = scnr.nextDouble();
						System.out.println(questionThree(r3_0, v3_0, lambda3, q3, m3)); 
						// a_particle_of_charge 80 24 157 2.9 16 
						// a_particle_of_charge 87 36 124 2.7 16
						break;
					case "a_cylindrical_capacitor":
						System.out.println("(abs) Give double R_a, double R_b, double k, double L, double V"); 
						double r4_a = scnr.nextDouble();
						double r4_b = scnr.nextDouble();
						double k4 = scnr.nextDouble();
						double l4 = scnr.nextDouble();
						double v4 = scnr.nextDouble();
						System.out.println(questionFour(r4_a, r4_b, k4, l4, v4)); 
						// a_cylindrical_capacitor 9.6 18 4.7 6.2 44.2 
						// a_cylindrical_capacitor 9.8 16 1.7 6.5 42.8
						break;
					case "a_parallel_plate":
						System.out.println("(abs) Give double C, double V, double %");
						double c5 = scnr.nextDouble();
						double v5 = scnr.nextDouble();
						double percent5 = scnr.nextDouble();
						System.out.println(questionFive(c5, v5, percent5)); 
						// a_parallel_plate 1.1 2.7 39
						// a_parallel_plate 2.9 11.9 29
						break;
						
					case "in_the_figure_3":
						System.out.println("(abs) Give double c_1, double c_2, double c_3, double v");
						double c6_1 = scnr.nextDouble();
						double c6_2 = scnr.nextDouble();
						double c6_3 = scnr.nextDouble();
						double v6 = scnr.nextDouble();
						System.out.println(questionSix(c6_1, c6_2, c6_3, v6)); 
						// in_the_figure_3 26 52 15 22
						// in_the_figure_3 25 63 14 7
						break;
					case "in_the_figure_all":
						System.out.println("(abs) Give double c, double v");
						double c7 = scnr.nextDouble();
						double v7 = scnr.nextDouble();
						System.out.println(questionSeven(c7, v7)); 
						// in_the_figure_all 18.4 32
						// in_the_figure_all 31.5 16
						break;
					case "an_air_filled_sphere":
						System.out.println("(abs) Give double v, double r_a, double r_b, double r");
						double v8 = scnr.nextDouble();
						double r8_a = scnr.nextDouble();
						double r8_b = scnr.nextDouble();
						double r8 = scnr.nextDouble();
						System.out.println(questionEight(v8, r8_a, r8_b, r8)); 
						// an_air_filled_sphere 1263 26.8 29 27.1
						// an_air_filled_sphere 1013 26.4 30 27.4
						break;
					case "a_wire_is_made":
						System.out.println("(abs) Give double phi, double i, double r, double bigL");
						double phi9 = scnr.nextDouble();
						double i9 = scnr.nextDouble();
						double r9 = scnr.nextDouble();
						double bigL9 = scnr.nextDouble();
						System.out.println(questionNine(phi9, i9, r9, bigL9)); 
						// a_wire_is_made 1.1 21.3 1 82
						// a_wire_is_made 5.5 12.5 1 63
						break;
						
					case "resistors_of_value":
						System.out.println("(abs) Give double r_1, double r_2, double r_3");
						double r10_1 = scnr.nextDouble();
						double r10_2 = scnr.nextDouble();
						double r10_3 = scnr.nextDouble();
						System.out.println(questionTen(r10_1, r10_2, r10_3)); 
						//resistors_of_value 102 422 840
						//resistors_of_value 102 422 840
						break;
					case "an_r_resistor_init_pot":
						System.out.println("(abs) give double r, double c, double v_0, double t, double charge (denominator)");
						double r11 = scnr.nextDouble();
						double c11 = scnr.nextDouble();
						double v11_0 = scnr.nextDouble();
						double t11 = scnr.nextDouble();
						double charge11 = scnr.nextDouble();
						System.out.println(questionEleven(r11, c11, v11_0, t11, charge11)); 
						// an_r_resistor_init_pot 136 39 10 0 6
						// an_r_resistor_init_pot 181 43 11 0 7
						break;
					case "an_r_resistor_pot_src":
						System.out.println("(abs) give double resis, double capac, double pot_src, double t, double percent");
						double resis12 = scnr.nextDouble();
						double capac12 = scnr.nextDouble();
						double pot_src12 = scnr.nextDouble();
						double t12 = scnr.nextDouble();
						double percent12 = scnr.nextDouble();
						System.out.println(questionTwelve(resis12, capac12, pot_src12, t12, percent12)); 
						// an_r_resistor_pot_src 80 23 10 0 21
						// an_r_resistor_pot_src 24 48 15 0 79
						break;
					case "the_diameter_of_a_copper":
						System.out.println("(abs) give double diameter, double current");
						double diameter = scnr.nextDouble();
						double current = scnr.nextDouble();
						System.out.println(questionThirteen(diameter, current)); 
						// the_diameter_of_a_copper 0.012 22.5 
						// the_diameter_of_a_copper 0.086 16.4
						break;
						
					case "in_the_figure_the_current":
						System.out.println("(abs) give double i_1, double i_2, double v_q");
						double i14_1 = scnr.nextDouble();
						double i14_2 = scnr.nextDouble();
						double v14_q = scnr.nextDouble();
						System.out.println(questionFourteen(i14_1, i14_2, v14_q)); 
						// in_the_figure_the_current 16 313 8.7
						// in_the_figure_the_current 33 505 4.7
						break;
					case "the_current_supplied":
						System.out.println("(abs) give double i_0, double tau");
						double i15_0 = scnr.nextDouble();
						double tau15 = scnr.nextDouble();
						System.out.println(questionFifteen(i15_0, tau15)); 
						// the_current_supplied 4.9 41.2
						// the_current_supplied 4.13 34.3
						break;
					case "a_line_of_charge_is_placed":
						System.out.println("(abs) give double x_start, double x_end, double x_density, double proton_release, double proton_mov");
						double x16_start= scnr.nextDouble();
						double x16_end = scnr.nextDouble();
						double x16_density = scnr.nextDouble();
						double proton16_release = scnr.nextDouble();
						double proton16_mov = scnr.nextDouble();
						System.out.println(questionSixteen(x16_start, x16_end, x16_density, proton16_release, proton16_mov) + "(this is in 10^2 ms^-1)"); 
						// a_line_of_charge_is_placed -0.4 0 9.63 4.04 10
						// a_line_of_charge_is_placed -0.4 0 4.15 8.67 10
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
