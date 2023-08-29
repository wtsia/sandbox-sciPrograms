import java.util.Scanner;
import java.text.DecimalFormat;


public class exam3 {
	public static double questionOne(double radius, double unifCurrent, double magDistAxis) {
	    // some calculations and logic
		double tmpvar10 = 4*Math.PI*Math.pow(10, -7);
		double numerator1 = tmpvar10*unifCurrent*magDistAxis*Math.pow(10, -2);
		double denominator1 = 2*Math.PI*Math.pow(radius*Math.pow(10, -2), 2);
		return numerator1/denominator1;
	}
	public static double questionTwo(double solenoidLength, double strength, double stretchedLength) {	
		return strength*solenoidLength/stretchedLength;
	}
	public static double questionThree(double radius, double field, double resistance, double startT, double deltaT) {
	    // some calculations and logic
		return field*Math.PI*Math.pow(radius*Math.pow(10, -2), 2)/deltaT/resistance*1000000;
	}
	public static double questionFour(double resistance, double flatLoops, double area, double rotateRate, double magnitude) {
	    // some calculations and logic
		return Math.PI*2*flatLoops*area*rotateRate*magnitude/resistance; 
	}
	public static double questionFive(double length, double resistance, double strength, double speed) {
	    // some calculations and logic
		return Math.pow(length*strength*speed*Math.pow(10, -2), 2)/resistance;
	}
	public static double questionSix(double area, double turns, double varI, double magField, double angle) {
	    // some calculations and logic
		double tmpvar6 = 90-angle;
		return area*turns*varI*magField*Math.sin(tmpvar6*Math.PI/180)/10000;
	}
	public static double questionSeven(double charge, double mass, double difference, double uniformField) {
	    // some calculations and logic
		return 2*Math.PI*mass/(charge*uniformField*Math.pow(10, -3));
	}
	public static double questionEight(double current, double bx, double by, double bz, double xlength) {
	    // some calculations and logic
		double newJHat = Math.pow(current*(-xlength*bz),2);
		double newKHat = Math.pow(current*(xlength*by),2);
		return Math.sqrt(newJHat + newKHat);
	}
	public static double questionNine(double radiusWire, double cylinderInner, double cylinderOuter, double currentInner, double currentOuter, double magField) {
	    // some calculations and logic
		double netCurrent9 = currentOuter - currentInner;
		return 4*Math.PI*(netCurrent9)/(2*Math.PI*magField)*100;
	}
	public static double questionTen(double radius, double resistance, double current) {
	    // some calculations and logic
		double tmpvar10 = resistance*current/100;
		return tmpvar10/(Math.PI*Math.pow(radius/100, 2))/10;
	}
	public static double questionEleven(double resistor, double capacitor, double inductor, double voltage_src, double rms_voltage) {
	      // some calculations and logic
		double topDegree4 = 2*Math.PI*voltage_src*inductor*Math.pow(10, -3) - 1/(2*Math.PI*voltage_src*capacitor*Math.pow(10, -6));
		double bottomDegree4 = resistor;
		double degreetotal4 = Math.atan(topDegree4/bottomDegree4);
		return degreetotal4; // phase_angle 3.5 1210 3.99 35 10 // phase_angle 7.1 1364 2.4 36 11
	}
	public static double questionTwelve(double resistor, double capacitor, double inductor, double voltageSrc, double rmsVoltage) {
	      // some calculations and logic
		double rSq1 = Math.pow(resistor, 2);
		double rSq2 = Math.pow((2*Math.PI*inductor*voltageSrc*Math.pow(10, -3)-1/(2*Math.PI*voltageSrc*capacitor*Math.pow(10, -6))), 2);
		return Math.sqrt(rSq1 + rSq2);
	}
	public static double questionThirteen(double current, double radiusArc) {
	    // some calculations and logic
		return (4*Math.PI*Math.pow(10, -7)*current)/(2*radiusArc/100)*0.25;
	}
	public static double questionFourteen(double turns, double magField, double radius, double resistance, double angle, double time) {
	    // some calculations and logic
		double tmpFlux14 = magField*Math.pow(10, -6)*Math.PI*Math.pow(radius*Math.pow(10, -2), 2)*(1-Math.cos(angle*Math.PI/180));
		double induced_emf14 = turns*tmpFlux14/(time*Math.pow(10, -3));
		return induced_emf14/resistance*1000;
	}
	public static double questionFifteen(double resistor, double capacitor, double inductor, double voltage_src, double rms_voltage) {
	    // some calculations and logic
		double omega5 = 2*Math.PI*voltage_src;
		double tmpvar51 = omega5*(inductor*Math.pow(10, -3))-(1/(omega5*capacitor*Math.pow(10, -6)));
		double tmpvarZ5 = Math.sqrt(Math.pow(resistor, 2) + Math.pow(tmpvar51, 2));
		double v_rms5 = Math.sqrt(2)*rms_voltage;
		return v_rms5/tmpvarZ5; 
	}
	public static double questionSixteen(double a, double b, double i) {
	    // some calculations and logic
		double muZero = 4*Math.PI*Math.pow(10, -7);
		double frontConst = muZero*i/(2*Math.PI);
		double iHat = (1/b - b/(a*a));
		double jHat = (Math.sqrt(a*a - b*b)/(a*a));
		return frontConst*Math.sqrt(iHat*iHat + jHat*jHat)/10;
	}
	
	public static void main(String Args[]) {
		Scanner scnr = new Scanner(System.in);
		boolean checkerNum = true;
		String questionKey;
		//DecimalFormat formatter = new DecimalFormat("0.###E0");
        // String formattedNumber = formatter.format(number);
		
		System.out.println("type q to exit");
		
		while (checkerNum == true) {
			System.out.println("Enter the Question keyword (mag_field1; mag_field_solenoid2; mag_elec_current_loop3; max_load_current4; mag_of_bulb5; mag_of_torque6; period_of_orbit7; mag_of_magForce8; mag_magField9; mag_of_rate10; phase_angle11; impedence12; arc_mag_eField13; coil_avg_current14; current_amplitude15; net_mag_field16):");
			
			questionKey = scnr.next();
			System.out.println("You've chosen " + questionKey);
			
			if (questionKey != "q") {
				switch (questionKey) {
					case "mag_field1":
						System.out.println("(abs) Give double radius, double unifCurrent, double mag_dist_axis;");
						double radius = scnr.nextDouble();
						double unifCurrent = scnr.nextDouble();
						double mag_dist_axis = scnr.nextDouble();
						System.out.println(questionOne(radius, unifCurrent, mag_dist_axis) + "\n"); 
						// current_density1 25.3 2.4 3.2 // current_density1 31 3.4 9.9
						break;
					case "mag_field_solenoid2":
						System.out.println("Give double solenoidLength, double strength, double stretchedLength");
						double solenoidLength2 = scnr.nextDouble();
						double strength2 = scnr.nextDouble();
						double stretchedLength2 = scnr.nextDouble();
						System.out.println(questionTwo(solenoidLength2, strength2, stretchedLength2) + "\n");
						// mag_field_solenoid2 21.75 21.7 32.4
						break;
					case "mag_elec_current_loop3":
						System.out.println("Give double radius, double field, double resistance, double startT, double deltaT");
						double radius3 = scnr.nextDouble();
						double field3 = scnr.nextDouble();
						double resistance3 = scnr.nextDouble();
						double startT3 = scnr.nextDouble();
						double deltaT3 = scnr.nextDouble();
						System.out.println(questionThree(radius3, field3, resistance3, startT3, deltaT3) + "\n");
						// mag_elec_current_loop3 3.3 0.8 23 0 0.37
						break;
					case "max_load_current4":
						System.out.println("Give double resistance, double flatLoops, double area, double rotateRate, double magnitude");
						double resistance4 = scnr.nextDouble();
						double flatLoops4 = scnr.nextDouble();
						double area4 = scnr.nextDouble();
						double rotateRate4 = scnr.nextDouble();
						double magnitude4 = scnr.nextDouble();
						System.out.println(questionFour(resistance4, flatLoops4, area4, rotateRate4, magnitude4) + "\n");
						// max_load_current4 100 115 1.35 76 1.1
						break;
					case "mag_of_bulb5":
						System.out.println("Give double length, double resistance, double strength, double speed");
						double length5 = scnr.nextDouble();
						double resistance5 = scnr.nextDouble();
						double strength5 = scnr.nextDouble();
						double speed5 = scnr.nextDouble();
						System.out.println(questionFive(length5, resistance5, strength5, speed5) + "\n");
						// mag_of_bulb5 40 19 21.1 8.2
						break;
					case "mag_of_torque6":
						System.out.println("Give double area, double turns, double varI, double magField, double angle");
						double area6 = scnr.nextDouble();
						double turns6 = scnr.nextDouble();
						double varI6 = scnr.nextDouble();
						double magField6 = scnr.nextDouble();
						double angle6 = scnr.nextDouble();
						System.out.println(questionSix(area6, turns6, varI6, magField6, angle6) + "\n");
						// mag_of_torque6 1.4 180 2.1 9.4 23.4 // mag_of_torque6 5.1 180 2.1 4.1 34.2
						break;
					case "period_of_orbit7":
						System.out.println("Give double charge, double mass, double difference, double uniformField");
						double charge7 = scnr.nextDouble();
						double mass7 = scnr.nextDouble();
						double difference7 = scnr.nextDouble();
						double uniformField7 = scnr.nextDouble();
						System.out.println(questionSeven(charge7, mass7, difference7, uniformField7) + "\n");
						// period_of_orbit7 88 38 40 7.11
						break;
					case "mag_of_magForce8":
						System.out.println("Give double current, double bx, double by, doublebz, double xlength");
						double current5 = scnr.nextDouble();
						double bx5 = scnr.nextDouble();
						double by5 = scnr.nextDouble();
						double bz5 = scnr.nextDouble();
						double xlength5 = scnr.nextDouble();
						System.out.println(questionEight(current5, bx5, by5, bz5, xlength5) + "\n");
						// mag_of_magForce8 6.8 5.2 -47.2 40.9 5.56
						break;
					case "mag_magField9":
						System.out.println("Give double radiusWire, double cylinderInner, double cylinderOuter, double currentInner, double currentOuter, double magField");
						double radiusWire9 = scnr.nextDouble();
						double cylinderInner9 = scnr.nextDouble();
						double cylinderOuter9 = scnr.nextDouble();
						double currentInner9 = scnr.nextDouble();
						double currentOuter9 = scnr.nextDouble();
						double magField9 = scnr.nextDouble();
						System.out.println(questionNine(radiusWire9, cylinderInner9, cylinderOuter9, currentInner9, currentOuter9, magField9) + "\n");
						// mag_magField9 0.06 1.37 3.11 7.79 10.25 5.2 // mag_magField9 0.08 1.86 3.76 8.67 10.86 4.95
						break;
					case "mag_of_rate10":
						System.out.println("Give double radius, double resistance, double current");
						double radius10 = scnr.nextDouble();
						double resistance10 = scnr.nextDouble();
						double current10 = scnr.nextDouble();
						System.out.println(questionTen(radius10, resistance10, current10) + "\n");
						// mag_of_rate10 12.9 2.94 73.4
						break;
					case "phase_angle11":
						System.out.println("Give double resistor, double capacitor, double inductor, double voltageSrc, double voltageRms");
						double resistor11 = scnr.nextDouble();
						double capacitor11 = scnr.nextDouble();
						double inductor11 = scnr.nextDouble();
						double voltageSrc11 = scnr.nextDouble();
						double voltageRms11 = scnr.nextDouble();
						System.out.println(questionEleven(resistor11, capacitor11, inductor11, voltageSrc11, voltageRms11) + "\n");
						// phase_angle11 4.5 1496 3.99 79 11 
						break;
					case "impedence12":
						System.out.println("Give double resistor, double capacitor, double inductor, double voltage_src, double rms_voltage");
						double resistor1 = scnr.nextDouble();
						double capacitor1 = scnr.nextDouble();
						double inductor1 = scnr.nextDouble();
						double voltageSrc1 = scnr.nextDouble();
						double rmsVoltage1 = scnr.nextDouble();
						System.out.println(questionTwelve(resistor1, capacitor1, inductor1, voltageSrc1, rmsVoltage1) + "\n");
						// impedence12 7.89 307 13.4 67 17.2 
						break;
					case "arc_mag_eField13":
						System.out.println("Give double current, double radiusArc");
						double current13 = scnr.nextDouble();
						double radiusArc13 = scnr.nextDouble();
						System.out.println(questionThirteen(current13, radiusArc13) + "\n");
						// arc_mag_eField13 11.8 20.7
						break;
					case "coil_avg_current14":
						System.out.println("Give double turns, double magField, double radius, double resistance, double angle, double time");
						double turns14 = scnr.nextDouble();
						double magField14 = scnr.nextDouble();
						double radius14 = scnr.nextDouble();
						double resistance14 = scnr.nextDouble();
						double angle14 = scnr.nextDouble();
						double time14 = scnr.nextDouble();
						System.out.println(questionFourteen(turns14, magField14, radius14, resistance14, angle14, time14) + "\n");
						// coil_avg_current14 49 7.69 13.1 54 59 0.028 
						break;
					case "current_amplitude15":
						System.out.println("Give double resistor, double capacitor, double inductor, double voltage_src, double rms_voltage");
						double resistor15 = scnr.nextDouble();
						double capacitor15 = scnr.nextDouble();
						double inductor15 = scnr.nextDouble();
						double voltage_src15 = scnr.nextDouble();
						double rms_voltage15 = scnr.nextDouble();
						System.out.println(questionFifteen(resistor15, capacitor15, inductor15, voltage_src15, rms_voltage15) + "\n");
						// current_amplitude15 17 189 7.79 463 19
						break;
						case "net_mag_field16":
						System.out.println("Give double a, double b, double i");
						double a16 = scnr.nextDouble();
						double b16 = scnr.nextDouble();
						double i16 = scnr.nextDouble();
						//String formattedNum16 = formatter.format(questionSixteen(a16, b16, i16));
						//System.out.println(formattedNum16 + "\n");
						System.out.println("Make sure E is -7 " + questionSixteen(a16, b16, i16) + "\n");
						// net_mag_field16 5.74 2.98 28  // net_mag_field16 7.55 3.71 96.7 // net_mag_field16 7.42 3.94 14.6
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
