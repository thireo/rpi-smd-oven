EESchema Schematic File Version 4
LIBS:rpismdoven-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector:Raspberry_Pi_2_3 J1
U 1 1 5C862A2B
P 5025 3850
F 0 "J1" H 5025 5328 50  0000 C CNN
F 1 "Raspberry_Pi_2_3" H 5025 5237 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_2x20_P2.54mm_Vertical" H 5025 3850 50  0001 C CNN
F 3 "https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/rpi_SCH_3bplus_1p0_reduced.pdf" H 5025 3850 50  0001 C CNN
	1    5025 3850
	1    0    0    -1  
$EndComp
$Comp
L Sensor_Temperature:MAX31855TASA U1
U 1 1 5C862CC5
P 8450 2925
F 0 "U1" H 8650 2575 50  0000 C CNN
F 1 "MAX31855TASA" H 8450 2925 50  0000 C CNN
F 2 "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm" H 9450 2575 50  0001 C CIN
F 3 "http://datasheets.maximintegrated.com/en/ds/MAX31855.pdf" H 8450 2925 50  0001 C CNN
	1    8450 2925
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C2
U 1 1 5C862D26
P 8775 2425
F 0 "C2" H 8775 2500 50  0000 L CNN
F 1 "10uF" H 8775 2350 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 8775 2425 50  0001 C CNN
F 3 "~" H 8775 2425 50  0001 C CNN
	1    8775 2425
	1    0    0    -1  
$EndComp
$Comp
L Device:C_Small C3
U 1 1 5C862D90
P 9100 2425
F 0 "C3" H 9100 2500 50  0000 L CNN
F 1 "10uF" H 9100 2350 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 9100 2425 50  0001 C CNN
F 3 "~" H 9100 2425 50  0001 C CNN
	1    9100 2425
	1    0    0    -1  
$EndComp
$Comp
L Device:Ferrite_Bead_Small L1
U 1 1 5C862E74
P 7350 2825
F 0 "L1" V 7400 2900 50  0000 C CNN
F 1 "Ferrite_Bead_Small" V 7250 2825 50  0000 C CNN
F 2 "Inductor_SMD:L_0603_1608Metric" V 7280 2825 50  0001 C CNN
F 3 "~" H 7350 2825 50  0001 C CNN
	1    7350 2825
	0    1    1    0   
$EndComp
$Comp
L Device:Ferrite_Bead_Small L2
U 1 1 5C862ED2
P 7350 3025
F 0 "L2" V 7400 3100 50  0000 C CNN
F 1 "Ferrite_Bead_Small" V 7475 3025 50  0000 C CNN
F 2 "Inductor_SMD:L_0603_1608Metric" V 7280 3025 50  0001 C CNN
F 3 "~" H 7350 3025 50  0001 C CNN
	1    7350 3025
	0    1    1    0   
$EndComp
$Comp
L Device:C_Small C1
U 1 1 5C862F50
P 7675 2925
F 0 "C1" H 7767 2971 50  0000 L CNN
F 1 "10nF" H 7767 2880 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 7675 2925 50  0001 C CNN
F 3 "~" H 7675 2925 50  0001 C CNN
	1    7675 2925
	1    0    0    -1  
$EndComp
Wire Wire Line
	8050 2825 7675 2825
Wire Wire Line
	7675 2825 7450 2825
Connection ~ 7675 2825
Wire Wire Line
	7450 3025 7675 3025
Wire Wire Line
	7675 3025 8050 3025
Connection ~ 7675 3025
$Comp
L power:GND #PWR09
U 1 1 5C86304D
P 8450 3400
F 0 "#PWR09" H 8450 3150 50  0001 C CNN
F 1 "GND" H 8455 3227 50  0000 C CNN
F 2 "" H 8450 3400 50  0001 C CNN
F 3 "" H 8450 3400 50  0001 C CNN
	1    8450 3400
	1    0    0    -1  
$EndComp
Wire Wire Line
	8450 3400 8450 3350
Wire Wire Line
	8775 2325 8775 2275
Wire Wire Line
	8775 2275 8450 2275
Wire Wire Line
	8450 2275 8450 2525
Wire Wire Line
	9100 2325 9100 2275
Wire Wire Line
	9100 2275 8775 2275
Connection ~ 8775 2275
Wire Wire Line
	8925 3350 8450 3350
Connection ~ 8450 3350
Wire Wire Line
	8450 3350 8450 3325
Wire Wire Line
	9100 2525 9100 2575
Wire Wire Line
	9100 2575 8925 2575
Wire Wire Line
	8925 2575 8925 3350
$Comp
L Device:R_Small R3
U 1 1 5C863366
P 9425 2425
F 0 "R3" H 9484 2471 50  0000 L CNN
F 1 "R_Small" H 9484 2380 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 9425 2425 50  0001 C CNN
F 3 "~" H 9425 2425 50  0001 C CNN
	1    9425 2425
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small R4
U 1 1 5C8633C0
P 9600 2425
F 0 "R4" H 9659 2471 50  0000 L CNN
F 1 "R_Small" H 9659 2380 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 9600 2425 50  0001 C CNN
F 3 "~" H 9600 2425 50  0001 C CNN
	1    9600 2425
	1    0    0    -1  
$EndComp
Wire Wire Line
	9425 2325 9425 2275
Wire Wire Line
	9425 2275 9100 2275
Connection ~ 9100 2275
Wire Wire Line
	9425 2525 9425 2725
Wire Wire Line
	9425 2725 8850 2725
Wire Wire Line
	8850 3025 9600 3025
Wire Wire Line
	9600 3025 9600 2525
Wire Wire Line
	9600 2325 9600 2275
Wire Wire Line
	9600 2275 9425 2275
Connection ~ 9425 2275
$Comp
L Diode:1N4148 D1
U 1 1 5C86398C
P 9800 2725
F 0 "D1" H 9800 2509 50  0000 C CNN
F 1 "1N4148" H 9800 2600 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 9800 2550 50  0001 C CNN
F 3 "http://www.nxp.com/documents/data_sheet/1N4148_1N4448.pdf" H 9800 2725 50  0001 C CNN
	1    9800 2725
	-1   0    0    1   
$EndComp
$Comp
L Diode:1N4148 D2
U 1 1 5C863A0A
P 9800 3025
F 0 "D2" H 9800 2809 50  0000 C CNN
F 1 "1N4148" H 9800 2900 50  0000 C CNN
F 2 "Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal" H 9800 2850 50  0001 C CNN
F 3 "http://www.nxp.com/documents/data_sheet/1N4148_1N4448.pdf" H 9800 3025 50  0001 C CNN
	1    9800 3025
	-1   0    0    1   
$EndComp
Wire Wire Line
	9650 3025 9600 3025
Connection ~ 9600 3025
Wire Wire Line
	9650 2725 9425 2725
Connection ~ 9425 2725
Wire Wire Line
	8925 2575 8775 2575
Wire Wire Line
	8775 2575 8775 2525
Connection ~ 8925 2575
Wire Wire Line
	8850 2825 10000 2825
Wire Wire Line
	9950 2725 10000 2725
Wire Wire Line
	9950 3025 10000 3025
Text Label 10000 2725 0    50   ~ 0
SCK
Text Label 10000 2825 0    50   ~ 0
SO
Text Label 10000 3025 0    50   ~ 0
CS
$Comp
L Connector:Conn_01x02_Female J3
U 1 1 5C86597B
P 6900 2975
F 0 "J3" H 6850 2925 50  0000 C CNN
F 1 "T-PROBE" H 7075 2925 50  0000 C CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 6900 2975 50  0001 C CNN
F 3 "~" H 6900 2975 50  0001 C CNN
	1    6900 2975
	-1   0    0    1   
$EndComp
Wire Wire Line
	7250 2825 7150 2825
Wire Wire Line
	7150 2825 7150 2875
Wire Wire Line
	7150 2875 7100 2875
Wire Wire Line
	7100 2975 7150 2975
Wire Wire Line
	7150 2975 7150 3025
Wire Wire Line
	7150 3025 7250 3025
$Comp
L Connector_Generic:Conn_01x06 J4
U 1 1 5C8666BC
P 9600 3700
F 0 "J4" H 9680 3692 50  0000 L CNN
F 1 "MAX31855-BREAKOUT" H 9680 3601 50  0000 L CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x06_P2.54mm_Vertical" H 9600 3700 50  0001 C CNN
F 3 "~" H 9600 3700 50  0001 C CNN
	1    9600 3700
	1    0    0    -1  
$EndComp
Text Label 9400 4000 2    50   ~ 0
SCK
Text Label 9400 3800 2    50   ~ 0
SO
Text Label 9400 3900 2    50   ~ 0
CS
$Comp
L power:+3V3 #PWR08
U 1 1 5C8667EA
P 8450 2175
F 0 "#PWR08" H 8450 2025 50  0001 C CNN
F 1 "+3V3" H 8465 2348 50  0000 C CNN
F 2 "" H 8450 2175 50  0001 C CNN
F 3 "" H 8450 2175 50  0001 C CNN
	1    8450 2175
	1    0    0    -1  
$EndComp
Wire Wire Line
	8450 2175 8450 2275
Connection ~ 8450 2275
$Comp
L power:+3V3 #PWR010
U 1 1 5C866DAF
P 9225 3475
F 0 "#PWR010" H 9225 3325 50  0001 C CNN
F 1 "+3V3" H 9240 3648 50  0000 C CNN
F 2 "" H 9225 3475 50  0001 C CNN
F 3 "" H 9225 3475 50  0001 C CNN
	1    9225 3475
	1    0    0    -1  
$EndComp
Wire Wire Line
	9225 3475 9225 3600
Wire Wire Line
	9225 3600 9400 3600
$Comp
L power:GND #PWR011
U 1 1 5C8673FB
P 9225 4050
F 0 "#PWR011" H 9225 3800 50  0001 C CNN
F 1 "GND" H 9230 3877 50  0000 C CNN
F 2 "" H 9225 4050 50  0001 C CNN
F 3 "" H 9225 4050 50  0001 C CNN
	1    9225 4050
	1    0    0    -1  
$EndComp
Wire Wire Line
	9400 3700 9225 3700
Wire Wire Line
	9225 3700 9225 4050
NoConn ~ 9400 3500
Text Label 4225 4350 2    50   ~ 0
SCK
Text Label 4225 3450 2    50   ~ 0
SO
Text Label 4225 4250 2    50   ~ 0
CS
$Comp
L Transistor_BJT:2N2219 Q2
U 1 1 5C858B83
P 4600 6300
F 0 "Q2" H 4791 6346 50  0000 L CNN
F 1 "2N2219" H 4791 6255 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92" H 4800 6225 50  0001 L CIN
F 3 "http://www.onsemi.com/pub_link/Collateral/2N2219-D.PDF" H 4600 6300 50  0001 L CNN
	1    4600 6300
	1    0    0    -1  
$EndComp
Text Label 3975 6300 2    50   ~ 0
PWM
Text Label 5825 4550 0    50   ~ 0
PWM
$Comp
L Device:Buzzer BZ1
U 1 1 5C858F86
P 2800 5000
F 0 "BZ1" H 2953 5029 50  0000 L CNN
F 1 "Buzzer" H 2953 4938 50  0000 L CNN
F 2 "Buzzer_Beeper:Buzzer_15x7.5RM7.6" V 2775 5100 50  0001 C CNN
F 3 "~" V 2775 5100 50  0001 C CNN
	1    2800 5000
	1    0    0    -1  
$EndComp
$Comp
L Transistor_BJT:2N2219 Q1
U 1 1 5C88006E
P 2525 5525
F 0 "Q1" H 2716 5571 50  0000 L CNN
F 1 "2N2219" H 2716 5480 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-92" H 2725 5450 50  0001 L CIN
F 3 "http://www.onsemi.com/pub_link/Collateral/2N2219-D.PDF" H 2525 5525 50  0001 L CNN
	1    2525 5525
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR02
U 1 1 5C880836
P 2650 4700
F 0 "#PWR02" H 2650 4550 50  0001 C CNN
F 1 "+5V" H 2665 4873 50  0000 C CNN
F 2 "" H 2650 4700 50  0001 C CNN
F 3 "" H 2650 4700 50  0001 C CNN
	1    2650 4700
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small R2
U 1 1 5C880E08
P 4200 6300
F 0 "R2" V 4004 6300 50  0000 C CNN
F 1 "1k" V 4095 6300 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 4200 6300 50  0001 C CNN
F 3 "~" H 4200 6300 50  0001 C CNN
	1    4200 6300
	0    1    1    0   
$EndComp
Wire Wire Line
	4100 6300 3975 6300
Wire Wire Line
	4300 6300 4400 6300
$Comp
L Device:R_Small R1
U 1 1 5C88374F
P 2100 5525
F 0 "R1" V 1904 5525 50  0000 C CNN
F 1 "1k" V 1995 5525 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 2100 5525 50  0001 C CNN
F 3 "~" H 2100 5525 50  0001 C CNN
	1    2100 5525
	0    1    1    0   
$EndComp
Wire Wire Line
	2200 5525 2325 5525
Text Label 1950 5525 2    50   ~ 0
BUZZ
Wire Wire Line
	2000 5525 1950 5525
Wire Wire Line
	2700 5100 2625 5100
Wire Wire Line
	2625 5100 2625 5325
$Comp
L Connector:Conn_01x02_Female J2
U 1 1 5C885BF8
P 5050 5900
F 0 "J2" H 5077 5876 50  0000 L CNN
F 1 "Conn_01x02_Female" H 5077 5785 50  0000 L CNN
F 2 "TerminalBlock:TerminalBlock_bornier-2_P5.08mm" H 5050 5900 50  0001 C CNN
F 3 "~" H 5050 5900 50  0001 C CNN
	1    5050 5900
	1    0    0    -1  
$EndComp
Wire Wire Line
	2650 4700 2650 4900
Wire Wire Line
	2650 4900 2700 4900
$Comp
L power:+5V #PWR03
U 1 1 5C886B71
P 4700 5825
F 0 "#PWR03" H 4700 5675 50  0001 C CNN
F 1 "+5V" H 4715 5998 50  0000 C CNN
F 2 "" H 4700 5825 50  0001 C CNN
F 3 "" H 4700 5825 50  0001 C CNN
	1    4700 5825
	1    0    0    -1  
$EndComp
Wire Wire Line
	4850 5900 4700 5900
Wire Wire Line
	4700 5900 4700 5825
Wire Wire Line
	4850 6000 4700 6000
Wire Wire Line
	4700 6000 4700 6100
$Comp
L power:GND #PWR04
U 1 1 5C880CFE
P 4700 6600
F 0 "#PWR04" H 4700 6350 50  0001 C CNN
F 1 "GND" H 4705 6427 50  0000 C CNN
F 2 "" H 4700 6600 50  0001 C CNN
F 3 "" H 4700 6600 50  0001 C CNN
	1    4700 6600
	1    0    0    -1  
$EndComp
Wire Wire Line
	4700 6600 4700 6500
$Comp
L power:GND #PWR01
U 1 1 5C881B9B
P 2625 5800
F 0 "#PWR01" H 2625 5550 50  0001 C CNN
F 1 "GND" H 2630 5627 50  0000 C CNN
F 2 "" H 2625 5800 50  0001 C CNN
F 3 "" H 2625 5800 50  0001 C CNN
	1    2625 5800
	1    0    0    -1  
$EndComp
Wire Wire Line
	2625 5725 2625 5800
$Comp
L power:+5V #PWR05
U 1 1 5C882D61
P 4875 2400
F 0 "#PWR05" H 4875 2250 50  0001 C CNN
F 1 "+5V" H 4890 2573 50  0000 C CNN
F 2 "" H 4875 2400 50  0001 C CNN
F 3 "" H 4875 2400 50  0001 C CNN
	1    4875 2400
	1    0    0    -1  
$EndComp
Wire Wire Line
	4875 2400 4875 2500
Wire Wire Line
	4875 2500 4825 2500
Wire Wire Line
	4825 2500 4825 2550
Wire Wire Line
	4875 2500 4925 2500
Wire Wire Line
	4925 2500 4925 2550
Connection ~ 4875 2500
$Comp
L power:+3V3 #PWR07
U 1 1 5C884F75
P 5175 2400
F 0 "#PWR07" H 5175 2250 50  0001 C CNN
F 1 "+3V3" H 5190 2573 50  0000 C CNN
F 2 "" H 5175 2400 50  0001 C CNN
F 3 "" H 5175 2400 50  0001 C CNN
	1    5175 2400
	1    0    0    -1  
$EndComp
Wire Wire Line
	5175 2400 5175 2500
Wire Wire Line
	5175 2500 5125 2500
Wire Wire Line
	5125 2500 5125 2550
Wire Wire Line
	5175 2500 5225 2500
Wire Wire Line
	5225 2500 5225 2550
Connection ~ 5175 2500
Text Label 5825 4650 0    50   ~ 0
BUZZ
NoConn ~ 5825 3550
NoConn ~ 5825 3650
NoConn ~ 5825 3750
NoConn ~ 5825 3950
NoConn ~ 5825 4050
NoConn ~ 5825 4150
NoConn ~ 5825 4250
NoConn ~ 5825 4350
NoConn ~ 5825 3250
NoConn ~ 5825 3350
NoConn ~ 5825 2950
NoConn ~ 5825 3050
NoConn ~ 4225 2950
NoConn ~ 4225 3050
NoConn ~ 4225 3250
NoConn ~ 4225 3350
NoConn ~ 4225 3650
NoConn ~ 4225 3750
NoConn ~ 4225 3850
NoConn ~ 4225 4050
NoConn ~ 4225 4150
NoConn ~ 4225 4450
NoConn ~ 4225 4550
$Comp
L power:GND #PWR06
U 1 1 5C8A6BBA
P 4925 5325
F 0 "#PWR06" H 4925 5075 50  0001 C CNN
F 1 "GND" H 4930 5152 50  0000 C CNN
F 2 "" H 4925 5325 50  0001 C CNN
F 3 "" H 4925 5325 50  0001 C CNN
	1    4925 5325
	1    0    0    -1  
$EndComp
Wire Wire Line
	5325 5150 5325 5225
Wire Wire Line
	5325 5225 5225 5225
Wire Wire Line
	4625 5225 4625 5150
Wire Wire Line
	4925 5325 4925 5275
Connection ~ 4925 5225
Wire Wire Line
	4925 5225 4825 5225
Wire Wire Line
	5225 5150 5225 5225
Connection ~ 5225 5225
Wire Wire Line
	5225 5225 5125 5225
Wire Wire Line
	5125 5150 5125 5225
Connection ~ 5125 5225
Wire Wire Line
	5125 5225 5025 5225
Wire Wire Line
	5025 5150 5025 5225
Connection ~ 5025 5225
Wire Wire Line
	5025 5225 4925 5225
Wire Wire Line
	4925 5150 4925 5225
Wire Wire Line
	4825 5150 4825 5225
Connection ~ 4825 5225
Wire Wire Line
	4825 5225 4725 5225
Wire Wire Line
	4725 5150 4725 5225
Connection ~ 4725 5225
Wire Wire Line
	4725 5225 4625 5225
$Comp
L power:PWR_FLAG #FLG01
U 1 1 5C8B3E2C
P 4650 2400
F 0 "#FLG01" H 4650 2475 50  0001 C CNN
F 1 "PWR_FLAG" H 4650 2574 50  0000 C CNN
F 2 "" H 4650 2400 50  0001 C CNN
F 3 "~" H 4650 2400 50  0001 C CNN
	1    4650 2400
	1    0    0    -1  
$EndComp
$Comp
L power:PWR_FLAG #FLG02
U 1 1 5C8B3E74
P 5450 2400
F 0 "#FLG02" H 5450 2475 50  0001 C CNN
F 1 "PWR_FLAG" H 5450 2574 50  0000 C CNN
F 2 "" H 5450 2400 50  0001 C CNN
F 3 "~" H 5450 2400 50  0001 C CNN
	1    5450 2400
	1    0    0    -1  
$EndComp
Wire Wire Line
	5450 2400 5450 2500
Wire Wire Line
	5450 2500 5225 2500
Connection ~ 5225 2500
Wire Wire Line
	4650 2500 4825 2500
Wire Wire Line
	4650 2400 4650 2500
Connection ~ 4825 2500
$Comp
L power:PWR_FLAG #FLG0101
U 1 1 5C8BA961
P 5125 5325
F 0 "#FLG0101" H 5125 5400 50  0001 C CNN
F 1 "PWR_FLAG" H 5125 5498 50  0000 C CNN
F 2 "" H 5125 5325 50  0001 C CNN
F 3 "~" H 5125 5325 50  0001 C CNN
	1    5125 5325
	-1   0    0    1   
$EndComp
Wire Wire Line
	5125 5325 5125 5275
Wire Wire Line
	5125 5275 4925 5275
Connection ~ 4925 5275
Wire Wire Line
	4925 5275 4925 5225
$EndSCHEMATC
