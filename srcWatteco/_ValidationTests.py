#!python
# -*- coding: utf-8 -*-

# TODO: Continuer ce fichier de tests automatisés (pour Non reg ou autres ...)

from _TestsTools import *

WTCParseInit()

# Analog input: Power duration configuration
WTCParseBuildTest(STDFrame, "11 05 000C 8003 21 9410",PRINT_JSON_IF_OK=False)
# Analog input: Accelero TAP (Chock/Clicks) configuration
WTCParseBuildTest(STDFrame, "11 05 000C 8004 19 9410",PRINT_JSON_IF_OK=False)
# Analog input: Accelero Angle disp
#  Report Configuration Batch :
# . ANGLEDISP (TAP/LIS2DE) ** Angle (°) **
#   Min 4h => 0x80F0(angle measurement period), Max 24H, Delta=5 (0x40a00000) [1 (0x3f800000)],    resol=0,1(0x3dcccccd),   Tag Label 1, Tag Size 3, Type Float 12
WTCParseBuildTest(STDFrame, "11 06 000C 1D 0055 00 80F0 85A0 40a00000 3dcccccd 0B",PRINT_JSON_IF_OK=False)

# Number/U16: Accelero (Chock/Clicks) max acceleration
#  Report Std :
WTCParseBuildTest(STDFrame, "11 0A 800E 0000 21 03E8",PRINT_JSON_IF_OK=False)
#  Report Configuration Std :
# . Basic Delta  configuration (TAP/LIS2DE) ** Acc(mg) **
#   Min 10s, Max 30 mn, Delta 100mg
WTCParseBuildTest(STDFrame, "11 06 800E 00 0000 21 000A 801E 0064",PRINT_JSON_IF_OK=False)
# . New configuration (TAP/LIS2DE) ** Acc(mg) **
#   Min 10s, Max 10 mn, Threshold 1000mg, Gap 100mg, Exceed and Fall, Alarm, Confirmed if Alarm, 2 occurences
WTCParseBuildTest(STDFrame, "11 06 800E 88 0000 21 000A 800A f0 03E8 0064 02",PRINT_JSON_IF_OK=False)

#  Report Configuration Batch :
# . ACCELERATION (TAP/LIS2DE) ** Acc(mg) **
#   Min 1s => 0x0001 (Note: this min sets the min maximum acc measurement when chocks occures), 
#   Max 24h, Delta=0,    resol=1,   Tag Label 0, Tag Size 3, Type U16 6
WTCParseBuildTest(STDFrame, "11 06 800E 15 0000 00 0001 85A0 0000 0001 03",PRINT_JSON_IF_OK=False);
WTCParseBuildTest(STDFrame, "11 06 800E 15 0000 00 0001 85A0 0000 0001 03;UserAttributeType=UInt16",PRINT_JSON_IF_OK=False);

# Voltage-current-Metering
WTCParseBuildTest(STDFrame, "110A800B00004106000000000112",PRINT_JSON_IF_OK=True)
# Voltage-current-multi_Metering
WTCParseBuildTest(STDFrame, "110A800D00004112000000000112000000000000000000000000",PRINT_JSON_IF_OK=True)

## Various Concentration cluster actions
# Read Unit
WTCParseBuildTest(STDFrame, "11 01 800C 8004 00 20 06")
# Classification
WTCParseBuildTest(STDFrame, "11 0A 800C 0001 20 00")
# Last Calibraton Status
WTCParseBuildTest(STDFrame, "11 01 800C 8000 00 41 12 0000000A 0000000B 01 01 02 00 FFF0 00FF 00EE")
# ClassificationLevels
WTCParseBuildTest(STDFrame, "11 01 800C 8010 00 41 0A 0226 02BC 044C 0514 06A4")

# Test Write Attribute (with response) (only for scalar value at the moment)
WTCParseBuildTest(STDFrame, "11 02 0013 0055 20 11")
WTCParseBuildTest(STDFrame, "11 04 0013 00 0055")
WTCParseBuildTest(STDFrame, "11 04 0013 96 0055")

# XYZAcceleration
WTCParseBuildTest(STDFrame, "11 05 800F 8000 41 17 0064 03E8 0003 1B58 0136 0136 0136 0000 03E8 4E20 90 03 07")
WTCParseBuildTest(STDFrame, "1101800F80000041170064271000031B5800A000A00136000003E84E20901407")
# WTCParse("11 05 800F 8000 41 17 0064 03E8 0003 1B58 0136 0136 0136 0000 03E8 4E20 90 03 87")
WTCParseBuildTest(STDFrame, "11 0a 800f 0000 41 16 0000 0001 0000 0000 0000 0000 0000 0000 023f 0399 1522 98")
WTCParseBuildTest(STDFrame, "11 0a 800f 0003 41 14 0001 0236 0312 1b62 0236 0312 1b62 0236 0312 1b62")

WTCParseBuildTest(STDFrame, "11 06 800F 84 0001 41 8001 85A0 01 00", ERR_SYM_EXP=True)
WTCParseBuildTest(STDFrame, "11 06 800F 84 0001 41 8001 85A0 00")
WTCParseBuildTest(STDFrame, "11 06 800F 98 0000 41 0003 801E 06 C8 00 00000001")

# Using configuration Cluster
WTCParseBuildTest(STDFrame, "11 0A 0050 0006 41 05 01 04 0D50 04")
WTCParseBuildTest(STDFrame, "110000500004")
WTCParseBuildTest(STDFrame, "110100500004004C001F02000800500406000F800A0402040504030400000104040204050403800A00")
# Config batch wit New configuraton on NodePowerDescriptor
WTCParseBuildTest(STDFrame, "110600509F000604800AA76001B10BB800640100011B")

# Simple-Metering
WTCParseBuildTest(STDFrame, "11010052000000410C000000000002000300040005")

# Calibration
WTCParseBuildTest(STDFrame, "310000528000")
WTCParseBuildTest(STDFrame, "31010052800000410901032c100006632000")
WTCParseBuildTest(STDFrame, "510000528000")
WTCParseBuildTest(STDFrame, "51010052800000410901019e1000068f4000")

# Binary input
WTCParseBuildTest(STDFrame, "310A000C00553944f5e000E84844f5e000")
WTCParseBuildTest(STDFrame, "310A000C00553944f5e000E8B044f5e00044f5e000434944f5e000")
WTCParseBuildTest(STDFrame, "310A000C00553944f5e000E8B044f5e00044f5e000800001FFFF4944f5e000")
#report Alarme with Long cause Binary Input Count
WTCParseBuildTest(STDFrame, "118a000f0402230000000aa0d00000000a0000000001")


# Configure std report on Binary EP 5 and expected response
WTCParseBuildTest(STDFrame, "b106000f00005510000a800a01")
WTCParseBuildTest(STDFrame, "b107000f00000402")
# Configure batch report on Binary EP 5 and expected response
WTCParseBuildTest(STDFrame, "b106000f1d0402000000800a000000640000000101")
WTCParseBuildTest(STDFrame, "b107000f00010402")

# TIC CBE report
WTCParseBuildTest(STDFrame, "110A005405004119 260706082122 0000000D 0000000E 0000000F 41 414243444500", ERR_SYM_EXP=True)
WTCParseBuildTest(STDFrame, "110A005405004119 260607082122 0000000D 0000000E 0000000F 41 414243444500")
# TIC CBE Config report. ERR_SYM_EXP because beter desc format choosen when rebuild ! !
WTCParseBuildTest(STDFrame, 
"11 06 0054 00 0200 41 8001 800A"             "16" + # 22 (Sum)
"260607082122"                                     + #  6
"24060708 0000000D 0000000E 0000000F"              + # 16
"", ERR_SYM_EXP=True) 
#TIC STD. ERR_SYM_EXP because beter desc format choosen when rebuild ! !
WTCParseBuildTest(STDFrame, "11 0A 0056 0100 41 1F 27000102030405 426f6e6a6f7572202100 80 45010203040506 0F 08 80000000", ERR_SYM_EXP=True)
# TIC STD, PRODUCTEUR
WTCParseBuildTest(STDFrame,"110a00560000411f06018010002b303231393736303635363832000219000002a10167dfac0f0f")
# TIC STD, Read reporting configuration avec Descripteur citères vide
WTCParseBuildTest(STDFrame, "110900560000000041000085a00706018010002b21")

#TIC PMEPMI, STD, 31 premiers champs + PMAX_s et PMAX_i
WTCParseBuildTest(STDFrame, 
"11 06 0057 00 0000 41 8001 800A"  +                     "79"   + #121 (Sum)
"05FFFFFFFF 090C000000FFFFFFFF"                                 + # 14
"06 06010203040506 04 010220010203 800001 800002 800003 800004" + # 27
"800001 800002 800003 800004 04 05 8441424344 05"               + # 20 
"0000000A05 0000000B06 0000000C07 0000000D08"                   + # 20 
"05 06 010101020202 FFFF"                                       + # 10 
"1000 0000000A 2000 3000 0000000B 4000 5000 0000000C "          + # 22 
"00000E 08 00000F 09"                                           + #  8
"")
#TIC ICE, General: ;meterVersion=-
#	CONTRAT(CString),DATECOUR(DMYhms),EA(U24),ERP(U24),
#	PTCOUR(CString),DATEPA1(DMYhms),PA1(U16),
#	PA1MN(U16),PA10MN(U16),PREA10MN(U16),TGPHI(Float32),U10MN(U16)
WTCParseBuildTest(STDFrame,
"11 0A 0053 0100 41 "                         + "3C" + # 60 (sum)
"071F80000003FB"                                     + #  7
"4d6f6e436f6e7472617400 010100010130 00000A 00000B " + # 23
"48434800 44455000 010100010100 0010"                + # 16
"0010 0011 0012 0013 bfc00000 0014"                  + # 14
";meterVersion=-")
#TIC ICE ICEp1: 
#	DEBUTp1(DMYhms),Finp1(DMYhms),CAFp1(U16),
#	EAp1P(U24),ERPp1P(U24),ERNp1P(U24)
#  ERR_SYM_EXP because beter desc format choosen when rebuild ! !
WTCParseBuildTest(STDFrame,
"11 0A 0053 0102 41 "                         + "1E" + # 29 (sum)
"A7 00 01 02 04 13 22"                               + #  7
"010100010120 010100010121 1001"                     + # 14
"800010 800011 800012"                               + #  8
"",ERR_SYM_EXP=True)
WTCParseBuildTest(STDFrame,
"11 0A 0053 0102 41 "                         + "21" + # 33 (sum)
"A7 00 01 02 04 13 22"                               + #  7
"010100010120 010100010121 1001"                     + # 14
"800010 800011 800012 800013"                        + # 12
"",ERR_SYM_EXP=True)

# TIC CBE, Batch HCHC(7,U32),HCHP (8,u32)
WTCParseBuildTest(STDFrame, "11 06 0054 39 0000 07 0000 800a 00000064 00000001 01 08 0001 800b 00000065 00000002 09")
WTCParseBuildTest(STDFrame, "11 06 0054 39 0000 07 0000 800a 00000064 00000001 01 08 0001 800b 00000065 00000002 09 00",ERR_PARSE_EXP=True)
WTCParseBuildTest(STDFrame, "11 06 0054 39 0000 03 0000 800a 00000064 00000001 01 08 0001 800b 00000065 00000002 09",ERR_PARSE_EXP=True)
WTCParseBuildTest(STDFrame, "11 06 0054 39 0000 07 0000 800a 00000064 00000001 01 08 0001 800b 00000065 00000002 ",ERR_PARSE_EXP=True)
WTCParseBuildTest(STDFrame, "11 06 0054 39 0000 02 0000 800a 00000064 00000001 01 08 0001 800b 00000065 00000002 09",ERR_PARSE_EXP=True)
# TIC STD, Batch EAST(5,U32),EAIT(20,U32),SINSTS(33,U24),SINSTS(33,U24)
WTCParseBuildTest(STDFrame, "11 06 0056 69 0000 05 0000 800a 00000064 00000001 02 14 0001 800b 00000065 00000002 0A 21 0002 800c 000066 000001 12 21 0002 800c 000067 000001 1A")

# Error 00 excedent
WTCParseBuildTest(STDFrame, "11 06 0056 69 0000 05 0000 800a 00000064 00000001 02 14 0001 800b 00000065 00000002 0A 21 0002 800c 000066 000001 12 21 0002 800c 000067 000001 1A 00",ERR_PARSE_EXP=True)
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# BEWARE FOLLOWING LINE MAKES ALL VALIDATION SCRIPT BROKEN ???????!!!!!!!!!!!!!
# Error 0000 excedent
#WTCParseBuildTest(STDFrame, "11 06 0056 69 0000 05 0000 800a 00000064 00000001 02 14 0001 800b 00000065 00000002 0A 21 0002 800c 000066 000001 12 21 0002 800c 000067 000001 1A 0000",ERR_PARSE_EXP=True)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Error 000000 excedent
WTCParseBuildTest(STDFrame, "11 06 0056 69 0000 05 0000 800a 00000064 00000001 02 14 0001 800b 00000065 00000002 0A 21 0002 800c 000066 000001 12 21 0002 800c 000067 000001 1A 000000",ERR_PARSE_EXP=True)

# TIC PMEPMI, Batch PA1_s (23,U16), PA1_i (24,U16) ==> Batch config size too long since New, no more than 64 bytes!
WTCParseBuildTest(STDFrame, "11 06 0057 29 0000 17 0000 800a 0032 0001 02 18 0001 800b 0033 0001 0A ")
# TIC ICE, Batch EA(3,U24),ERP(4,U24),PA1MN(39,U16),PA10MN(40,U16),PREA1MN(41,I16),PREA10MN(42,I16)
WTCParseBuildTest(STDFrame,  "11 06 0053 81 0000 " +
"04 0000 803C 000001 000001 03 " +
"04 0000 803C 000001 000001 0B " +
"27 0000 803C 0001 0001 13 " +
"28 0000 803C 0001 0001 1B " +
"29 0000 803C FFFF FFFE 23 " +
"2A 0000 803C FFFD FFFC 2B " , ERR_PARSE_EXP=True
)
# TIC ICE, Batch EA(3,U24),ERP(4,U24),PA1MN(39,U16),PA10MN(40,U16),PREA1MN(41,I16),PREA10MN(42,I16)
WTCParseBuildTest(STDFrame,  "11 06 0053 59 0000 " +
"04 0000 803C 000001 000001 03 " +
"04 0000 803C 000001 000001 0B " +
"27 0000 803C 0001 0001 13 " +
"28 0000 803C 0001 0001 1B "
)

WTCParseBuildTest(STDFrame,"110A005700004122680102030C28293706042036018312021709150A3B300D28D6B320005A320000300A",PRINT_JSON_IF_OK=True)
WTCParseBuildTest(STDFrame,"110A005700004122680102030C28293706042036018312021709150A3B300D28D6B320005A320000300A;rev=5339",PRINT_JSON_IF_OK=True)

WTCParseBuildTest(STDFrame,"110a005700004127680102030c282937060315363704668548544120350202160d3b130f298b50a012a6660001610c",PRINT_JSON_IF_OK=True)
# BELOW ERR_PERSE because ENUM+1 not existing !
# WTCParseBuildTest(STDFrame,"110a005700004127680102030c282937060315363704668548544120350202160d3b130f298b50a012a6660001610c;rev=4966",PRINT_JSON_IF_OK=True)

#NOt already decoded frame 
WTCParseBuildTest(STDFrame, "3106005231000000800F800F7FFFFF0000010B01800F800F7FFFFF00000113")

#BAD FRAMES EXEMPLES
WTCParseBuildTest(STDFrame, "110000520000FF",ERR_SYM_EXP=True)
WTCParseBuildTest(STDFrame, "11010052000000420C000000000002000300040005")

WTCParseBuildTest(STDFrame, "5105800a0001230000000A")
WTCParseBuildTest(STDFrame, "3106800A000000410001000A200000000000000000000000000000000000000000000000000000000000000000")
WTCParseBuildTest(STDFrame, "1106800B000000410000800106000000000000")
WTCParseBuildTest(STDFrame, "1106800b800000410001800107700007d0006401")
WTCParseBuildTest(STDFrame, "1106800a80000041000180010b7005000003e80000006401")
WTCParseBuildTest(STDFrame, "11060050800006410005000a044804000a")
WTCParseBuildTest(STDFrame, "118a000f0402230000000aa0d00000000a0000000001")
WTCParseBuildTest(STDFrame, "110a005000064107010536d80e4e01a059022ee0000001")
WTCParseBuildTest(STDFrame, "110a005000064107010536d80e4e01")
WTCParseBuildTest(STDFrame, "110a04020000290102")
WTCParseBuildTest(STDFrame, "1108000f000055")
WTCParseBuildTest(STDFrame, "1106000f000402238001800a01020304")
WTCParseBuildTest(STDFrame, "1106000fA004022300008001D00000000a0000000001")
WTCParseBuildTest(STDFrame, "11060050A0000641000580011838022ee00000010600000001000259022ee0000001020003")
WTCParseBuildTest(STDFrame, "11060050A0000641000580011830022ee000000151022ee0000001",ERR_PARSE_EXP=True)
WTCParseBuildTest(STDFrame, "1106005000000641000aa76005000400c800")
WTCParseBuildTest(STDFrame, "1107000f00000055")
WTCParseBuildTest(STDFrame, "1100000f0055")
WTCParseBuildTest(STDFrame, "1101000f0055001001")
WTCParseBuildTest(STDFrame, "110100500006004107010536d80e4e01")
WTCParseBuildTest(STDFrame, "1150000602")
WTCParseBuildTest(STDFrame, "110a000c00553911111111")
WTCParseBuildTest(STDFrame, "1106000c000055390001001011111111")
WTCParseBuildTest(STDFrame, "1107000c80000055")
WTCParseBuildTest(STDFrame, "1108000c000055")
WTCParseBuildTest(STDFrame, "1109000c00000055390001001011111111")
WTCParseBuildTest(STDFrame, "1100000c0055")
WTCParseBuildTest(STDFrame, "1101000c0055003911111111")
WTCParseBuildTest(STDFrame, "1100000c0100")
WTCParseBuildTest(STDFrame, "1101000c0100002311111111")
WTCParseBuildTest(STDFrame, "110000000002")
WTCParseBuildTest(STDFrame, "110000000003")
WTCParseBuildTest(STDFrame, "110000000004")
WTCParseBuildTest(STDFrame, "110000000005")
WTCParseBuildTest(STDFrame, "110000000006")
WTCParseBuildTest(STDFrame, "110000000010")
WTCParseBuildTest(STDFrame, "110100000010004200")
WTCParseBuildTest(STDFrame, "11010000001080")
WTCParseBuildTest(STDFrame, "11010000800100420000",ERR_SYM_EXP=True)
WTCParseBuildTest(STDFrame, "110a000f00551001")
WTCParseBuildTest(STDFrame, "1106000f000055100001001000")
WTCParseBuildTest(STDFrame, "1107000f81000055")
WTCParseBuildTest(STDFrame, "1108000f000055")
WTCParseBuildTest(STDFrame, "1109000f81000055")
WTCParseBuildTest(STDFrame, "1100000f0055")
WTCParseBuildTest(STDFrame, "1101000f0055001001")
WTCParseBuildTest(STDFrame, "110a000f04022311111111")
WTCParseBuildTest(STDFrame, "1106000f000402230001001011111111")
WTCParseBuildTest(STDFrame, "1107000f80000402")
WTCParseBuildTest(STDFrame, "1108000f000402")
WTCParseBuildTest(STDFrame, "1109000f80000402230001001011111111",ERR_SYM_EXP=True)
WTCParseBuildTest(STDFrame, "1100000f0402")
WTCParseBuildTest(STDFrame, "1101000f0402002311111111")
WTCParseBuildTest(STDFrame, "1100000f0054")
WTCParseBuildTest(STDFrame, "1101000f0054001000")
WTCParseBuildTest(STDFrame, "1105000f00541000")
WTCParseBuildTest(STDFrame, "1100000f0400")
WTCParseBuildTest(STDFrame, "1100000f0401")
WTCParseBuildTest(STDFrame, "1101000f040100210000")
WTCParseBuildTest(STDFrame, "1105000f0401210000")
WTCParseBuildTest(STDFrame, "1100000f0100")
WTCParseBuildTest(STDFrame, "1101000f0100002303010002")
WTCParseBuildTest(STDFrame, "110000500004")
WTCParseBuildTest(STDFrame, "110a0050000641050100000100",ERR_SYM_EXP=True)
WTCParseBuildTest(STDFrame, "110a005000064103010000")
WTCParseBuildTest(STDFrame, "110a00500006410501040DAC04")
WTCParseBuildTest(STDFrame, "118a00500006410501040DAC0400")
WTCParseBuildTest(STDFrame, "1106005000000641000100100501010DAC01")
WTCParseBuildTest(STDFrame, "1107005081000006")
WTCParseBuildTest(STDFrame, "11080050000006")
WTCParseBuildTest(STDFrame, "1109005081000006")
WTCParseBuildTest(STDFrame, "110000500006")
WTCParseBuildTest(STDFrame, "1101005000060041050101000001")
WTCParseBuildTest(STDFrame, "110a80080000290001")
WTCParseBuildTest(STDFrame, "1106800800000029000101001111")
WTCParseBuildTest(STDFrame, "1107800880000000")
WTCParseBuildTest(STDFrame, "11088008000000")
WTCParseBuildTest(STDFrame, "110980080000000029001001001111")
WTCParseBuildTest(STDFrame, "110080080000")
WTCParseBuildTest(STDFrame, "11018008000000291111")
WTCParseBuildTest(STDFrame, "110080080002")
WTCParseBuildTest(STDFrame, "11018008000200291111")
WTCParseBuildTest(STDFrame, "110080080003")
WTCParseBuildTest(STDFrame, "110180080003002312121212")
WTCParseBuildTest(STDFrame, "1105800800032312121212")
WTCParseBuildTest(STDFrame, "110080080004")
WTCParseBuildTest(STDFrame, "11018008000400211111")
WTCParseBuildTest(STDFrame, "110580080004211111")
WTCParseBuildTest(STDFrame, "110080080005")
WTCParseBuildTest(STDFrame, "11018008000500211111")
WTCParseBuildTest(STDFrame, "110580080005211111")
WTCParseBuildTest(STDFrame, "110080080006")
WTCParseBuildTest(STDFrame, "110180080006002311111111")
WTCParseBuildTest(STDFrame, "1105800800062311111111")
WTCParseBuildTest(STDFrame, "110a80080100291111")
WTCParseBuildTest(STDFrame, "1106800800010029000100101111")
WTCParseBuildTest(STDFrame, "1107800881000100")
WTCParseBuildTest(STDFrame, "11088008000100")
WTCParseBuildTest(STDFrame, "110980080000010029000100101111")
WTCParseBuildTest(STDFrame, "110080080100")
WTCParseBuildTest(STDFrame, "11018008010000291111")
WTCParseBuildTest(STDFrame, "110a80080101291111")
WTCParseBuildTest(STDFrame, "1106800800010129000101101111")
WTCParseBuildTest(STDFrame, "1107800880000101")
WTCParseBuildTest(STDFrame, "11088008000101")
WTCParseBuildTest(STDFrame, "1109800880000101")
WTCParseBuildTest(STDFrame, "110080080101")
WTCParseBuildTest(STDFrame, "11018008010100291111")
WTCParseBuildTest(STDFrame, "110a80080102291111")
WTCParseBuildTest(STDFrame, "1106800800010229000110001111")
WTCParseBuildTest(STDFrame, "1107800880000102")
WTCParseBuildTest(STDFrame, "11088008000102")
WTCParseBuildTest(STDFrame, "1109800882000102")
WTCParseBuildTest(STDFrame, "110080080102")
WTCParseBuildTest(STDFrame, "11018008010200291111")
WTCParseBuildTest(STDFrame, "110080040000")
WTCParseBuildTest(STDFrame, "110180040000000811")
WTCParseBuildTest(STDFrame, "1105800400000801")
WTCParseBuildTest(STDFrame, "110080040001")
WTCParseBuildTest(STDFrame, "110180040001002012")
WTCParseBuildTest(STDFrame, "1105800400012011")
WTCParseBuildTest(STDFrame, "110080040002")
WTCParseBuildTest(STDFrame, "11018004000200410400011111")
WTCParseBuildTest(STDFrame, "110580040002410411110000")
WTCParseBuildTest(STDFrame, "1101800400030041020011")
WTCParseBuildTest(STDFrame, "11058004000341020011")
WTCParseBuildTest(STDFrame, "110080040004")
WTCParseBuildTest(STDFrame, "11018004000400410411111111")
WTCParseBuildTest(STDFrame, "110580040004410411111111")
WTCParseBuildTest(STDFrame, "110080040005")
WTCParseBuildTest(STDFrame, "1101800400050041081212121212121212")
WTCParseBuildTest(STDFrame, "1105800400054108",ERR_PARSE_EXP=True)
WTCParseBuildTest(STDFrame, "1107800580000000")
WTCParseBuildTest(STDFrame, "11088005000000")
WTCParseBuildTest(STDFrame, "110080050000")
WTCParseBuildTest(STDFrame, "110a001300552011")
WTCParseBuildTest(STDFrame, "11060013000055200001100011")
WTCParseBuildTest(STDFrame, "1107001380000055")
WTCParseBuildTest(STDFrame, "110a04050000211111")
WTCParseBuildTest(STDFrame, "1106040500000021000110001111")
WTCParseBuildTest(STDFrame, "1107040581000000")
WTCParseBuildTest(STDFrame, "11080405000000")
WTCParseBuildTest(STDFrame, "110904050000000021000110001111")
WTCParseBuildTest(STDFrame, "11080013000055")
WTCParseBuildTest(STDFrame, "1109001300000055200001100001")
WTCParseBuildTest(STDFrame, "110000130055")
WTCParseBuildTest(STDFrame, "110100130055002011")
WTCParseBuildTest(STDFrame, "1105001300552011")
WTCParseBuildTest(STDFrame, "11000013004a")
WTCParseBuildTest(STDFrame, "11010013004a002011")
WTCParseBuildTest(STDFrame, "11050013004a2011")
WTCParseBuildTest(STDFrame, "110000130100")
WTCParseBuildTest(STDFrame, "11010013010000230effffff")
WTCParseBuildTest(STDFrame, "110a000600001000")
WTCParseBuildTest(STDFrame, "11060006000000100001110001")
WTCParseBuildTest(STDFrame, "1107000682000000")
WTCParseBuildTest(STDFrame, "11080006000000")
WTCParseBuildTest(STDFrame, "1109000680000000")
WTCParseBuildTest(STDFrame, "110000060000")
WTCParseBuildTest(STDFrame, "110100060000001000")
WTCParseBuildTest(STDFrame, "110004050000")
WTCParseBuildTest(STDFrame, "11010405000000211111")
WTCParseBuildTest(STDFrame, "110004050001")
WTCParseBuildTest(STDFrame, "110004050002")
WTCParseBuildTest(STDFrame, "11010405000200211111")
WTCParseBuildTest(STDFrame, "110a800300001801")
WTCParseBuildTest(STDFrame, "11068003000000180001800A11")
WTCParseBuildTest(STDFrame, "1107800382000000")
WTCParseBuildTest(STDFrame, "11088003000000")
WTCParseBuildTest(STDFrame, "1109800381000000")
WTCParseBuildTest(STDFrame, "110080030000")
WTCParseBuildTest(STDFrame, "110180030000001810")
WTCParseBuildTest(STDFrame, "110080030001")
WTCParseBuildTest(STDFrame, "110180030001004106001001001000")
WTCParseBuildTest(STDFrame, "1105800300014106001001001000")
WTCParseBuildTest(STDFrame, "110080030002")
WTCParseBuildTest(STDFrame, "110080030003")
WTCParseBuildTest(STDFrame, "11018003000300211111")
WTCParseBuildTest(STDFrame, "110080030004")
WTCParseBuildTest(STDFrame, "110180030004002854")
WTCParseBuildTest(STDFrame, "110080030005")
WTCParseBuildTest(STDFrame, "110180030005002801")
WTCParseBuildTest(STDFrame, "110080030006")
WTCParseBuildTest(STDFrame, "1101800300060041050101000100")
WTCParseBuildTest(STDFrame, "110080060000")
WTCParseBuildTest(STDFrame, "1101800600000022002580")
WTCParseBuildTest(STDFrame, "1105800600002201C200")
WTCParseBuildTest(STDFrame, "110080060001")
WTCParseBuildTest(STDFrame, "110180060001002010")
WTCParseBuildTest(STDFrame, "1105800600012011")
WTCParseBuildTest(STDFrame, "110080060002")
WTCParseBuildTest(STDFrame, "110180060002002011")
WTCParseBuildTest(STDFrame, "11058006000220",ERR_PARSE_EXP=True)
WTCParseBuildTest(STDFrame, "110080060003")
WTCParseBuildTest(STDFrame, "1105800600032000")
WTCParseBuildTest(STDFrame, "110080070000")
WTCParseBuildTest(STDFrame, "1106800700000141000110000111")
WTCParseBuildTest(STDFrame, "1107800780000001")
WTCParseBuildTest(STDFrame, "11088007000001")
WTCParseBuildTest(STDFrame, "1109800700000001410001000A0101")
WTCParseBuildTest(STDFrame, "110080070001")
WTCParseBuildTest(STDFrame, "110080070002")
WTCParseBuildTest(STDFrame, "110180070002002011")
WTCParseBuildTest(STDFrame, "110a00520000410c111111000000111100002112")
WTCParseBuildTest(STDFrame, "1106005200000041011010000c000100111111212100001111")
WTCParseBuildTest(STDFrame, "1107005280000000")
WTCParseBuildTest(STDFrame, "11080052000000")
WTCParseBuildTest(STDFrame, "1109005200000000410001000A0c000001000002000300040005")
WTCParseBuildTest(STDFrame, "110000520000")
WTCParseBuildTest(STDFrame, "11010052000000410c101010010101111100001111")
WTCParseBuildTest(STDFrame, "110a04020000291010")
WTCParseBuildTest(STDFrame, "1106040200000029000110001010")
WTCParseBuildTest(STDFrame, "1107040280000000")
WTCParseBuildTest(STDFrame, "11080402000000")
WTCParseBuildTest(STDFrame, "110004020000")
WTCParseBuildTest(STDFrame, "110904020000000029000110001111")
WTCParseBuildTest(STDFrame, "11010402000000290010")
WTCParseBuildTest(STDFrame, "110004020001")
WTCParseBuildTest(STDFrame, "11010402000100290010")
WTCParseBuildTest(STDFrame, "110004020002")
WTCParseBuildTest(STDFrame, "11010402000200291100")
WTCParseBuildTest(STDFrame, "110a800200002b10101010")
WTCParseBuildTest(STDFrame, "110680020000002b0001100011111111")
WTCParseBuildTest(STDFrame, "1107800280000000")
WTCParseBuildTest(STDFrame, "11088002000000")
WTCParseBuildTest(STDFrame, "11098002000000002b0001100011111111")
WTCParseBuildTest(STDFrame, "110080020000")
WTCParseBuildTest(STDFrame, "110180020000002b11111111")
WTCParseBuildTest(STDFrame, "1105800200002b11111111")
WTCParseBuildTest(STDFrame, "110080020001")
WTCParseBuildTest(STDFrame, "110180020001002011")
WTCParseBuildTest(STDFrame, "110a800200022811")
WTCParseBuildTest(STDFrame, "11068002000002280001100011")
WTCParseBuildTest(STDFrame, "1107800280000002")
WTCParseBuildTest(STDFrame, "11088002000002")
WTCParseBuildTest(STDFrame, "1109800200000002280001100011")
WTCParseBuildTest(STDFrame, "110080020002")
WTCParseBuildTest(STDFrame, "110180020002002811")
WTCParseBuildTest(STDFrame, "110a800200032801")
WTCParseBuildTest(STDFrame, "11068002000003280001100011")
WTCParseBuildTest(STDFrame, "1107800280000003")
WTCParseBuildTest(STDFrame, "1109800200000003280001100011")
WTCParseBuildTest(STDFrame, "110080020003")
WTCParseBuildTest(STDFrame, "110180020003002811")
WTCParseBuildTest(STDFrame, "110080080004")
WTCParseBuildTest(STDFrame, "110180020004002001")
WTCParseBuildTest(STDFrame, "110000000010")
WTCParseBuildTest(STDFrame, "1101000000030042023031")
WTCParseBuildTest(STDFrame, "110100000004004200")
WTCParseBuildTest(STDFrame, "1101000000050042023031")
WTCParseBuildTest(STDFrame, "110100500004004c00001100110000110000")
WTCParseBuildTest(STDFrame, "11060050150006020000803c0000006413")
WTCParseBuildTest(STDFrame, "1106000c1d0055000000803c3b449ba63c23d70a81")
WTCParseBuildTest(STDFrame, "3106000c1d0055000000803c000000000000000001")
WTCParseBuildTest(STDFrame, "1106000f110055000000803c010111")
WTCParseBuildTest(STDFrame, "1106000f110055000000803c000001")
WTCParseBuildTest(STDFrame, "1106000f1d0402000000803c000000000000000001")
WTCParseBuildTest(STDFrame, "11060400150000000000803c0000000a2b")
WTCParseBuildTest(STDFrame, "11060402900000290000803c480000")
WTCParseBuildTest(STDFrame, "11060402150000000000803c000003e802")
WTCParseBuildTest(STDFrame, "11060405800000210000803c100000000001")
WTCParseBuildTest(STDFrame, "11060405150000000000803c000000640a")
WTCParseBuildTest(STDFrame, "1106000f110055000000803c00011a")
WTCParseBuildTest(STDFrame, "11068008150000000000803c0000000001")
WTCParseBuildTest(STDFrame, "110080080006")
WTCParseBuildTest(STDFrame, "11068008150100000000803c000A000B01")
WTCParseBuildTest(STDFrame, "11068008150101000000803c000C000D01")
WTCParseBuildTest(STDFrame, "11068008150102000000803c000D000E01")
WTCParseBuildTest(STDFrame, "1100000f0054")
WTCParseBuildTest(STDFrame, "11060403150000000000803c0000000001")
WTCParseBuildTest(STDFrame, "11060400150000000000803c0000000001")



WTCParseConclude()


'''
# COMPILING NOT DIRECTLY WORKING ON OUR CODEC
# st=STDFrame.compile(filename="copyforinspection.py")
# print(st.parse(b"\x11\x00\x00\x50\x00\x04"))
print(STDFrame.benchmark(b"\x11\x00\x00\x50\x00\x04"))
'''