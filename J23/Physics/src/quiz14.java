import java.util.Scanner;
import java.lang.Math.*;

public class quiz14 {
	public static double questionOne(double resistor, double capacitor, double inductor, double voltageSrc, double rmsVoltage) {
	      // some calculations and logic
		double rSq1 = Math.pow(resistor, 2);
		double rSq2 = Math.pow((2*Math.PI*inductor*voltageSrc*Math.pow(10, -3)-1/(2*Math.PI*voltageSrc*capacitor*Math.pow(10, -6))), 2);
		return Math.sqrt(rSq1 + rSq2); // impedence 8.78 302 17.9 146 18.6 
	}
	
	public static double questionTwo(double resistor, double capacitor, double inductor, double voltage_src, double rms_volt) {
	      // some calculations and logic
		double cap_react2 = 1/(2*Math.PI*voltage_src*capacitor*Math.pow(10, -6));
		double induc_react2 = 2*Math.PI*voltage_src*inductor*Math.pow(10, -3);
		double impedence2 = Math.sqrt(Math.pow(resistor, 2)+Math.pow((induc_react2 - cap_react2), 2));
		return resistor/impedence2;// power_factor 1 115 11 148 13
	}
	
	public static double questionThree(double resistor, double capacitor, double inductor, double voltage_src, double rms_voltage) {
	      // some calculations and logic
		double tmpvar3 = 1/(2*Math.PI*Math.sqrt(inductor*Math.pow(10, -3)*capacitor*Math.pow(10, -6)));
		return tmpvar3; // resonance_freq 1.7 476 10.3 110 16
	}
	
	public static double questionFour(double resistor, double capacitor, double inductor, double voltage_src, double rms_voltage) {
	      // some calculations and logic
		double topDegree4 = 2*Math.PI*voltage_src*inductor*Math.pow(10, -3) - 1/(2*Math.PI*voltage_src*capacitor*Math.pow(10, -6));
		double bottomDegree4 = resistor;
		double degreetotal4 = Math.atan(topDegree4/bottomDegree4);
		return degreetotal4; // phase_angle 3.5 1210 3.99 35 10 // phase_angle 7.1 1364 2.4 36 11
	}
	
	public static double questionFive(double resistor, double capacitor, double inductor, double voltage_src, double rms_voltage) {
	      // some calculations and logic
		double omega5 = 2*Math.PI*voltage_src;
		double tmpvar51 = omega5*(inductor*Math.pow(10, -3))-(1/(omega5*capacitor*Math.pow(10, -6)));
		double tmpvarZ5 = Math.sqrt(Math.pow(resistor, 2) + Math.pow(tmpvar51, 2));
		double v_rms5 = Math.sqrt(2)*rms_voltage;
		return v_rms5/tmpvarZ5; // current_amplitude 35.9 385 3.99 926 28.5 // 
	}
	
	public static void main(String Args[]) {
		Scanner scnr = new Scanner(System.in);
		boolean checkerNum = true;
		String questionKey;
		
		System.out.println("type q to exit");
		
		while (checkerNum == true) {
			System.out.println("Enter the Question keyword (impedence; power_factor; resonance_freq; phase_angle; current_amplitude):");
			
			questionKey = scnr.next();
			
			System.out.println("You've chosen " + questionKey);
			
			if (questionKey != "q") {
				switch (questionKey) {
					case "impedence":
						System.out.println("Give double resistor, double capacitor, double inductor, double voltage source, double rmsVoltage");
						double resistor1 = scnr.nextDouble();
						double capacitor1 = scnr.nextDouble();
						double inductor1 = scnr.nextDouble();
						double voltageSrc1 = scnr.nextDouble();
						double rmsVoltage1 = scnr.nextDouble();
						System.out.println(questionOne(resistor1, capacitor1, inductor1, voltageSrc1, rmsVoltage1));
						break;
						
					case "power_factor":
						System.out.println("Give double resistor, double capacitor, double inductor, double voltage_src, double rms_volt");
						double resistor2 = scnr.nextDouble();
						double capacitor2 = scnr.nextDouble();
						double inductor2 = scnr.nextDouble();
						double voltage_src2 = scnr.nextDouble();
						double rms_volt2 = scnr.nextDouble();
						System.out.println(questionTwo(resistor2, capacitor2, inductor2, voltage_src2, rms_volt2));
						break;
					case "resonance_freq":
						System.out.println("Give double resistor, double capacitor, double inductor, double voltage_src, double rms_voltage");
						double resistor3 = scnr.nextDouble();
						double capacitor3 = scnr.nextDouble();
						double inductor3 = scnr.nextDouble();
						double voltage_src3 = scnr.nextDouble();
						double rms_voltage3 = scnr.nextDouble();
						System.out.println(questionThree(resistor3, capacitor3, inductor3, voltage_src3, rms_voltage3));
						break;
					case "phase_angle":
						System.out.println("Give double resistor, double capacitor, double inductor, double voltage_src, double rms_voltage");
						double resistor4 = scnr.nextDouble();
						double capacitor4 = scnr.nextDouble();
						double inductor4 = scnr.nextDouble();
						double voltage_src4 = scnr.nextDouble();
						double rms_voltage4 = scnr.nextDouble();
						System.out.println(questionFour(resistor4, capacitor4, inductor4, voltage_src4, rms_voltage4));
						break;
					case "current_amplitude":
						System.out.println("Give double resistor, double capacitor, double inductor, double voltage_src, double rms_voltage");
						double resistor5 = scnr.nextDouble();
						double capacitor5 = scnr.nextDouble();
						double inductor5 = scnr.nextDouble();
						double voltage_src5 = scnr.nextDouble();
						double rms_voltage5 = scnr.nextDouble();
						System.out.println(questionFive(resistor5, capacitor5, inductor5, voltage_src5, rms_voltage5));
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
