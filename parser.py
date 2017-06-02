## -*- coding: utf-8 -*-
#"""
#Created on Mon Apr 10 13:40:01 2017
#
#@author: Vidya Vishwanathan
#"""
'''LAICE DATABASE PARSER'''

#IMPORT STATEMENTS
import sys
import binascii
import struct
import codecs
import StringIO

'''
Level 0 - upload data file
'''
#USER PROMPT FOR FILE NAME
#filename = raw_input("What's your file called?")
#filename = "./" + filename
'''
TEST DATA FILES
*uncomment the file name you want to test, or use the above user prompt*
'''
#filename = "vtPowerUpData.bin" #TEST DATA FILE (BINARY) FROM JEREMY DEJOURNETT (UIUC)
#filename = "SampleVidyaTest3.txt" #TEST FILE (HEX) FROM STEPHEN NOEL (VT)
#filename = "VidyaTest3out.txt" #ABOVE TEST FILE IN BINARY
#filename = "VidyaTest4allonOUT.txt" #TEST FILE FROM STEPHEN NOEL (VT) IN BINARY, TEXT FILE
#filename = "VidyaTest4allonOUT.bin" #TEST FILE FROM STEPHEN NOEL (VT) IN BINARY, .BIN FILE
filename = "VidyaTest4allonOUTb.bin" #ABOVE TEST FILE CREATED THROUGH NEW CONVERSION PROCESS

#Byte Count
byte_fmt = '>B'#for unsigned one byte
short_fmt = '>H'#for unsigned two bytes
byte_fmts = '>b'#for signed one byte
short_fmts = '>h'#for signed two bytes


def parse(raw):
    f = StringIO.StringIO(raw)
    #split into packages for each sensor
    #instrumentLIIB = struct.unpack('>35B', f.read(35))[0]
    #instrumentRPA = struct.unpack('>279B', f.read(279))[0]
    #instrumentSNeuPI = struct.unpack('>35B', f.read(35))[0]
    #instrumentLINAS = struct.unpack('>24B', f.read(24))[0]
    
    '''
    Level 1 - LIIB
    '''
    
    LIIB_startWordLIIB_L1_Dec = struct.unpack(byte_fmts, f.read(1))[0]
    LIIB_startWordLIIB_L1 = hex(LIIB_startWordLIIB_L1_Dec)#OUTPUT AS HEX DATA
    LIIB_LIIBModeOpMode = struct.unpack(byte_fmts, f.read(1))[0] #1 byte to split
    LIIB_LIIBMode_L1 = (LIIB_LIIBModeOpMode >> 3) & 0b11111 #0x1f # int("1f", 16.0), rs 3 mask 5
    LIIB_opMode_L1 = (LIIB_LIIBModeOpMode) & 0b111 #0x07, rs 0 mask 3
    LIIB_pos_5VD_MonitorLB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_pos_3_3V_MonitorLB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_pos_12V_MonitorLB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_pos_5VB_MonitorLB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_neg_5VB_MonitorLB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_pos_15VB_MonitorLB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_neg_15VB_MonitorLB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_temperatureMonitor3LB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_temperatureMonitor2LB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_temperatureMonitor1LB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_pos_5VB_CurrentMonitorLB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_pos_15VB_CurrentMonitorLB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_neg_5VB_CurrentMonitorLB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_neg_15VB_CurrentMonitorLB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_thermalKnife1VoltageMonitorLB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_thermalKnife2VoltageMonitorLB_L1 = struct.unpack(short_fmts, f.read(2))[0]
    LIIB_Knife1234Status_ToggleStatus = struct.unpack(byte_fmts, f.read(1))[0] #1 byte to split, last 3 bits are unused
    LIIB_thermalKnife1Status_L1 = (LIIB_Knife1234Status_ToggleStatus >> 7) & 0b1 #rs 7 mask 1
    LIIB_thermalKnife2Status_L1 = (LIIB_Knife1234Status_ToggleStatus >> 6) & 0b1 #rs 6 mask 1
    LIIB_thermalKnife3Status_L1 = (LIIB_Knife1234Status_ToggleStatus >> 5) & 0b1 #rs 5 mask 1
    LIIB_thermalKnife4Status_L1 = (LIIB_Knife1234Status_ToggleStatus >> 4) & 0b1 #rs 4 mask 1
    LIIB_tkOverrideToggleStatus_L1 = (LIIB_Knife1234Status_ToggleStatus >> 3) & 0b1 #rs 3 mask 1
         
    '''
    Level 2 - LIIB, convert to ASCII
    '''
    
    LIIB_startWordLIIB_L2 = str(unichr(LIIB_startWordLIIB_L1_Dec)) #varchar
    LIIB_LIIBMode_L2 = str(unichr(LIIB_LIIBMode_L1)) #varchar
    LIIB_opMode_L2 = str(unichr(LIIB_opMode_L1)) #varchar
    LIIB_pos_5VD_MonitorLB_L2 = ((LIIB_pos_5VD_MonitorLB_L1*5.0/65536.0)+2.5)*2.0
    LIIB_pos_3_3V_MonitorLB_L2 = ((LIIB_pos_3_3V_MonitorLB_L1*5.0/65536.0)+2.5)*(26.2/20.0)
    LIIB_pos_12V_MonitorLB_L2 = ((LIIB_pos_12V_MonitorLB_L1*5.0/65536.0)+2.5)*(95.0/20.0)
    LIIB_pos_5VB_MonitorLB_L2 = ((LIIB_pos_5VB_MonitorLB_L1*5.0/65536.0)+2.5)*2.0
    LIIB_neg_5VB_MonitorLB_L2 = ((LIIB_neg_5VB_MonitorLB_L1*5.0/65536.0)+2.5)*-4.0
    LIIB_pos_15VB_MonitorLB_L2 = ((LIIB_pos_15VB_MonitorLB_L1*5.0/65536.0)+2.5)*6.0
    LIIB_neg_15VB_MonitorLB_L2 = ((LIIB_neg_15VB_MonitorLB_L1*5.0/65536.0)+2.5)*-16.0
    LIIB_temperatureMonitor3LB_L2 = ((LIIB_temperatureMonitor3LB_L1*5.0/65536.0)+2.5)*250.0 - 273.0
    LIIB_temperatureMonitor2LB_L2 = ((LIIB_temperatureMonitor2LB_L1*5.0/65536.0)+2.5)*250.0 - 273.0
    LIIB_temperatureMonitor1LB_L2 = ((LIIB_temperatureMonitor1LB_L1*5.0/65536.0)+2.5)*250.0 - 273.0
    LIIB_pos_5VB_CurrentMonitorLB_L2 = ((LIIB_pos_5VB_CurrentMonitorLB_L1*5.0/65536.0)+2.5)*1.0
    LIIB_neg_5VB_CurrentMonitorLB_L2 = ((LIIB_neg_5VB_CurrentMonitorLB_L1*5.0/65536.0)+2.5)*0.2
    LIIB_pos_15VB_CurrentMonitorLB_L2 = ((LIIB_pos_15VB_CurrentMonitorLB_L1*5.0/65536.0)+2.5)*1.0
    LIIB_neg_15VB_CurrentMonitorLB_L2 = ((LIIB_neg_15VB_CurrentMonitorLB_L1*5.0/65536.0)+2.5)*0.2
    LIIB_thermalKnife1VoltageMonitorLB_L2 = ((LIIB_thermalKnife1VoltageMonitorLB_L1*5.0/65536.0)+2.5)*(114.7/14.7)
    LIIB_thermalKnife2VoltageMonitorLB_L2 = ((LIIB_thermalKnife2VoltageMonitorLB_L1*5.0/65536.0)+2.5)*(114.7/14.7)
    if LIIB_thermalKnife1Status_L1 == 1:
        LIIB_thermalKnife1Status_L2 = 'CLOSED'
    elif LIIB_thermalKnife1Status_L1 == 0:
        LIIB_thermalKnife1Status_L2 = 'OPEN'
    if LIIB_thermalKnife2Status_L1 == 1:
        LIIB_thermalKnife2Status_L2 = 'CLOSED'
    elif LIIB_thermalKnife2Status_L1 == 0:
        LIIB_thermalKnife2Status_L2 = 'OPEN'
    if LIIB_thermalKnife3Status_L1 == 1:
        LIIB_thermalKnife3Status_L2 = 'CLOSED'
    elif LIIB_thermalKnife3Status_L1 == 0:
        LIIB_thermalKnife3Status_L2 = 'OPEN'
    if LIIB_thermalKnife4Status_L1 == 1:
        LIIB_thermalKnife4Status_L2 = 'CLOSED'
    elif LIIB_thermalKnife4Status_L1 == 0:
        LIIB_thermalKnife4Status_L2 = 'OPEN'
    if LIIB_tkOverrideToggleStatus_L1 == 1:
        LIIB_tkOverrideToggleStatus_L2 = 'ON'
    elif LIIB_tkOverrideToggleStatus_L1 == 0:
        LIIB_tkOverrideToggleStatus_L2 = 'OFF'
    
    '''
    Level 1 - RPA
    '''
    RPA_stepSize_L1 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_ptsPerSweep_L1 = struct.unpack(byte_fmt, f.read(1))[0]
    RPA_PtsZeroRG2 = struct.unpack(byte_fmt, f.read(1))[0] #1 byte to split
    RPA_zeroPadding_L1 = (RPA_PtsZeroRG2 >> 3) & 0b11111 #0x1f # int("1f", 16.0)
    RPA_rg2Mode_L1 = (RPA_PtsZeroRG2 >> 2) & 0b1 #rs 2 mask 1
    RPA_sweepMode_rgMode_L1 = (RPA_PtsZeroRG2) & 0b11 #rs 0 mask 2
    RPA_tempMonitor_1RPA = struct.unpack(short_fmt, f.read(2))[0]
    RPA_tempMonitor_2RPA = struct.unpack(short_fmt, f.read(2))[0]
    RPA_tempMonitor_3RPA = struct.unpack(short_fmt, f.read(2))[0]
    RPA_tempMonitor_dbRPA = struct.unpack(short_fmt, f.read(2))[0]
    RPA_pos_15V_MonitorRPA = struct.unpack(short_fmt, f.read(2))[0]
    RPA_pos_5V_MonitorRPA = struct.unpack(short_fmt, f.read(2))[0]
    RPA_pos_3_3_MonitorRPA = struct.unpack(short_fmt, f.read(2))[0]
    RPA_rg2GridMonitorRPA = struct.unpack(short_fmt, f.read(2))[0]
    RPA_sgGridMonitorRPA = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample1 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample1 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample2 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample2 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample3 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample3 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample4 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample4 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample5 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample5 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample6 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample6 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample7 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample7 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample8 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample8 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample9 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample9 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample10 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample10 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample11 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample11 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample12 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample12 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample13 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample13 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample14 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample14 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample15 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample15 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample16 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample16 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample17 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample17 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample18 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample18 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample19 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample19 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample20 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample20 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample21 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample21 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample22 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample22 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample23 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample23 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample24 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample24 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample25 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample25 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample26 = struct.unpack(short_fmt, f.read(2))[0] 
    RPA_voltageSample26 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample27 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample27 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample28 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample28 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample29 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample29 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample30 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample30 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample31 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample31 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample32 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample32 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample33 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample33 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample34 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample34 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample35 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample35 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample36 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample36 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample37 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample37 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample38 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample38 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample39 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample39 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample40 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample40 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample41 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample41 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample42 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample42 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample43 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample43 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample44 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample44 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample45 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample45 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample46 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample46 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample47 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample47 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample48 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample48 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample49 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample49 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample50 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample50 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample51 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample51 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample52 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample52 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample53 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample53 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample54 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample54 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample55 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample55 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample56 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample56 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample57 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample57 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample58 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample58 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample59 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample59 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample60 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample60 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample61 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample61 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample62 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample62 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample63 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample63 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_currentSample64 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_voltageSample64 = struct.unpack(short_fmt, f.read(2))[0]
    RPA_endWordRPA = struct.unpack(byte_fmt, f.read(1))[0]
    
    '''
    Level 2 - RPA, convert
    ''' 
    RPA_stepSize_L2 = unichr(RPA_stepSize_L1).encode('ascii','ignore') #varchar #check if second parameter changes?
    RPA_ptsPerSweep_L2 = unichr(RPA_ptsPerSweep_L1).encode('ascii','ignore')#varchar
    RPA_zeroPadding_L2 = unichr(RPA_zeroPadding_L1).encode('ascii','ignore')#varchar
    RPA_rg2Mode_L2 = unichr(RPA_rg2Mode_L1).encode('ascii','ignore')#varchar
    RPA_sweepMode_rgMode_L2 = str(unichr(RPA_sweepMode_rgMode_L1))#varchar
    RPA_tempMonitor_1RPA_degC = (RPA_tempMonitor_1RPA*5.0/65536.0)-273.0
    RPA_tempMonitor_2RPA_degC = (RPA_tempMonitor_2RPA*5.0/65536.0)-273.0
    RPA_tempMonitor_3RPA_degC = (RPA_tempMonitor_3RPA*5.0/65536.0)-273.0
    RPA_tempMonitor_dbRPA_degC = (RPA_tempMonitor_dbRPA*5.0/65536.0)-273.0
    RPA_pos_15V_MonitorRPA_Volts = ((RPA_pos_15V_MonitorRPA)*5.0/65536.0)*(114.7/14.7)
    RPA_pos_5V_MonitorRPA_Volts = (RPA_pos_5V_MonitorRPA*5.0/65536.0)*2.0
    RPA_pos_3_3_MonitorRPA_Volts = (RPA_pos_3_3_MonitorRPA*5.0/65536.0)*1.147
    #rg2GridMonitorRPA_Volts #NOT USED
    #sgGridMonitorRPA_Volts #NOT USED
    
    RPA_currentSample1_Amps = 10.0**((-RPA_currentSample1-54335.0)/11469.0)
    RPA_voltageSample1_Volts = (RPA_voltageSample1*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample2_Amps = 10.0**((-RPA_currentSample2-54335.0)/11469.0)
    RPA_voltageSample2_Volts = (RPA_voltageSample2*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample3_Amps = 10.0**((-RPA_currentSample3-54335.0)/11469.0)
    RPA_voltageSample3_Volts = (RPA_voltageSample3*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample4_Amps = 10.0**((-RPA_currentSample4-54335.0)/11469.0)
    RPA_voltageSample4_Volts = (RPA_voltageSample4*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample5_Amps = 10.0**((-RPA_currentSample5-54335.0)/11469.0)
    RPA_voltageSample5_Volts = (RPA_voltageSample5*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample6_Amps = 10.0**((-RPA_currentSample6-54335.0)/11469.0)
    RPA_voltageSample6_Volts = (RPA_voltageSample6*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample7_Amps = 10.0**((-RPA_currentSample7-54335.0)/11469.0)
    RPA_voltageSample7_Volts = (RPA_voltageSample7*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample8_Amps = 10.0**((-RPA_currentSample8-54335.0)/11469.0)
    RPA_voltageSample8_Volts = (RPA_voltageSample8*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample9_Amps = 10.0**((-RPA_currentSample9-54335.0)/11469.0)
    RPA_voltageSample9_Volts = (RPA_voltageSample9*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample10_Amps = 10.0**((-RPA_currentSample10-54335.0)/11469.0)
    RPA_voltageSample10_Volts = (RPA_voltageSample10*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample11_Amps = 10.0**((-RPA_currentSample11-54335.0)/11469.0)
    RPA_voltageSample11_Volts = (RPA_voltageSample11*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample12_Amps = 10.0**((-RPA_currentSample12-54335.0)/11469.0)
    RPA_voltageSample12_Volts = (RPA_voltageSample12*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample13_Amps = 10.0**((-RPA_currentSample13-54335.0)/11469.0)
    RPA_voltageSample13_Volts = (RPA_voltageSample13*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample14_Amps = 10.0**((-RPA_currentSample14-54335.0)/11469.0)
    RPA_voltageSample14_Volts = (RPA_voltageSample14*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample15_Amps = 10.0**((-RPA_currentSample15-54335.0)/11469.0)
    RPA_voltageSample15_Volts = (RPA_voltageSample15*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample16_Amps = 10.0**((-RPA_currentSample16-54335.0)/11469.0)
    RPA_voltageSample16_Volts = (RPA_voltageSample16*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample17_Amps = 10.0**((-RPA_currentSample17-54335.0)/11469.0)
    RPA_voltageSample17_Volts = (RPA_voltageSample17*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample18_Amps = 10.0**((-RPA_currentSample18-54335.0)/11469.0)
    RPA_voltageSample18_Volts = (RPA_voltageSample18*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample19_Amps = 10.0**((-RPA_currentSample19-54335.0)/11469.0)
    RPA_voltageSample19_Volts = (RPA_voltageSample19*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample20_Amps = 10.0**((-RPA_currentSample20-54335.0)/11469.0)
    RPA_voltageSample20_Volts = (RPA_voltageSample20*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample21_Amps = 10.0**((-RPA_currentSample21-54335.0)/11469.0)
    RPA_voltageSample21_Volts = (RPA_voltageSample21*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample22_Amps = 10.0**((-RPA_currentSample22-54335.0)/11469.0)
    RPA_voltageSample22_Volts = (RPA_voltageSample22*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample23_Amps = 10.0**((-RPA_currentSample23-54335.0)/11469.0)
    RPA_voltageSample23_Volts = (RPA_voltageSample23*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample24_Amps = 10.0**((-RPA_currentSample24-54335.0)/11469.0)
    RPA_voltageSample24_Volts = (RPA_voltageSample24*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample25_Amps = 10.0**((-RPA_currentSample25-54335.0)/11469.0)
    RPA_voltageSample25_Volts = (RPA_voltageSample25*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample26_Amps = 10.0**((-RPA_currentSample26-54335.0)/11469.0)
    RPA_voltageSample26_Volts = (RPA_voltageSample26*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample27_Amps = 10.0**((-RPA_currentSample27-54335.0)/11469.0)
    RPA_voltageSample27_Volts = (RPA_voltageSample27*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample28_Amps = 10.0**((-RPA_currentSample28-54335.0)/11469.0)
    RPA_voltageSample28_Volts = (RPA_voltageSample28*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample29_Amps = 10.0**((-RPA_currentSample29-54335.0)/11469.0)
    RPA_voltageSample29_Volts = (RPA_voltageSample29*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample30_Amps = 10.0**((-RPA_currentSample30-54335.0)/11469.0)
    RPA_voltageSample30_Volts = (RPA_voltageSample30*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample31_Amps = 10.0**((-RPA_currentSample31-54335.0)/11469.0)
    RPA_voltageSample31_Volts = (RPA_voltageSample31*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample32_Amps = 10.0**((-RPA_currentSample32-54335.0)/11469.0)
    RPA_voltageSample32_Volts = (RPA_voltageSample32*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample33_Amps = 10.0**((-RPA_currentSample33-54335.0)/11469.0)
    RPA_voltageSample33_Volts = (RPA_voltageSample33*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample34_Amps = 10.0**((-RPA_currentSample34-54335.0)/11469.0)
    RPA_voltageSample34_Volts = (RPA_voltageSample34*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample35_Amps = 10.0**((-RPA_currentSample35-54335.0)/11469.0)
    RPA_voltageSample35_Volts = (RPA_voltageSample35*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample36_Amps = 10.0**((-RPA_currentSample36-54335.0)/11469.0)
    RPA_voltageSample36_Volts = (RPA_voltageSample36*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample37_Amps = 10.0**((-RPA_currentSample37-54335.0)/11469.0)
    RPA_voltageSample37_Volts = (RPA_voltageSample37*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample38_Amps = 10.0**((-RPA_currentSample38-54335.0)/11469.0)
    RPA_voltageSample38_Volts = (RPA_voltageSample38*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample39_Amps = 10.0**((-RPA_currentSample39-54335.0)/11469.0)
    RPA_voltageSample39_Volts = (RPA_voltageSample39*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample40_Amps = 10.0**((-RPA_currentSample40-54335.0)/11469.0)
    RPA_voltageSample40_Volts = (RPA_voltageSample40*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample41_Amps = 10.0**((-RPA_currentSample41-54335.0)/11469.0)
    RPA_voltageSample41_Volts = (RPA_voltageSample41*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample42_Amps = 10.0**((-RPA_currentSample42-54335.0)/11469.0)
    RPA_voltageSample42_Volts = (RPA_voltageSample42*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample43_Amps = 10.0**((-RPA_currentSample43-54335.0)/11469.0)
    RPA_voltageSample43_Volts = (RPA_voltageSample43*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample44_Amps = 10.0**((-RPA_currentSample44-54335.0)/11469.0)
    RPA_voltageSample44_Volts = (RPA_voltageSample44*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample45_Amps = 10.0**((-RPA_currentSample45-54335.0)/11469.0)
    RPA_voltageSample45_Volts = (RPA_voltageSample45*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample46_Amps = 10.0**((-RPA_currentSample46-54335.0)/11469.0)
    RPA_voltageSample46_Volts = (RPA_voltageSample46*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample47_Amps = 10.0**((-RPA_currentSample47-54335.0)/11469.0)
    RPA_voltageSample47_Volts = (RPA_voltageSample47*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample48_Amps = 10.0**((-RPA_currentSample48-54335.0)/11469.0)
    RPA_voltageSample48_Volts = (RPA_voltageSample48*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample49_Amps = 10.0**((-RPA_currentSample49-54335.0)/11469.0)
    RPA_voltageSample49_Volts = (RPA_voltageSample49*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample50_Amps = 10.0**((-RPA_currentSample50-54335.0)/11469.0)
    RPA_voltageSample50_Volts = (RPA_voltageSample50*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample51_Amps = 10.0**((-RPA_currentSample51-54335.0)/11469.0)
    RPA_voltageSample51_Volts = (RPA_voltageSample51*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample52_Amps = 10.0**((-RPA_currentSample52-54335.0)/11469.0)
    RPA_voltageSample52_Volts = (RPA_voltageSample52*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample53_Amps = 10.0**((-RPA_currentSample53-54335.0)/11469.0)
    RPA_voltageSample53_Volts = (RPA_voltageSample53*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample54_Amps = 10.0**((-RPA_currentSample54-54335.0)/11469.0)
    RPA_voltageSample54_Volts = (RPA_voltageSample54*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample55_Amps = 10.0**((-RPA_currentSample55-54335.0)/11469.0)
    RPA_voltageSample55_Volts = (RPA_voltageSample55*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample56_Amps = 10.0**((-RPA_currentSample56-54335.0)/11469.0)
    RPA_voltageSample56_Volts = (RPA_voltageSample56*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample57_Amps = 10.0**((-RPA_currentSample57-54335.0)/11469.0)
    RPA_voltageSample57_Volts = (RPA_voltageSample57*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample58_Amps = 10.0**((-RPA_currentSample58-54335.0)/11469.0)
    RPA_voltageSample58_Volts = (RPA_voltageSample58*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample59_Amps = 10.0**((-RPA_currentSample59-54335.0)/11469.0)
    RPA_voltageSample59_Volts = (RPA_voltageSample59*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample60_Amps = 10.0**((-RPA_currentSample60-54335.0)/11469.0)
    RPA_voltageSample60_Volts = (RPA_voltageSample60*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample61_Amps = 10.0**((-RPA_currentSample61-54335.0)/11469.0)
    RPA_voltageSample61_Volts = (RPA_voltageSample61*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample62_Amps = 10.0**((-RPA_currentSample62-54335.0)/11469.0)
    RPA_voltageSample62_Volts = (RPA_voltageSample62*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample63_Amps = 10.0**((-RPA_currentSample63-54335.0)/11469.0)
    RPA_voltageSample63_Volts = (RPA_voltageSample63*5.0/65536.0)*(12.0/5.0)
    RPA_currentSample64_Amps = 10.0**((-RPA_currentSample64-54335.0)/11469.0)
    RPA_voltageSample64_Volts = (RPA_voltageSample64*5.0/65536.0)*(12.0/5.0)

    RPA_endWordRPA_L2 = RPA_endWordRPA
    
    '''
    Level 1 - SNeuPI
    '''
    SN_startWordSNeuPI_L1_Dec = struct.unpack(byte_fmt, f.read(1))[0]
    SN_startWordSNeuPI_L1 = hex(SN_startWordSNeuPI_L1_Dec)#OUTPUT AS HEX DATA
    SN_ZeroHVEmission = struct.unpack(byte_fmt, f.read(1))[0] #1 byte to split
    SN_zeroPadding_L1 = (SN_ZeroHVEmission >> 3) & 0b11111 #0x1f # int("1f", 16.0)
    SN_hv_Status_L1 = (SN_ZeroHVEmission >> 2) & 0b1 #rs 2 mask 1
    SN_emissionMode_L1 = (SN_ZeroHVEmission) & 0b11 #rs 0 mask 2
    SN_pos_3_3V_MonitorSN_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_pos_5VD_MonitorSN_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_pos_5VB_MonitorSN_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_pos_15VB_MonitorSN_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_plate1MonitorSN_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_plate2MonitorSN_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_temperatureMonitor1_UpperBoard_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_temperatureMonitorDSN_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_pos_5V_Converter_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_spaceMonitor2_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_mcp_CurrentSample1_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_tipV1_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_mcp_CurrentSample2_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_tipV2_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_mcp_CurrentSample3_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_tipV3_L1 = struct.unpack(short_fmt, f.read(2))[0]
    SN_endWordSNeuPI_L1 = struct.unpack(byte_fmt, f.read(1))[0]
    
    '''
    Level 2 - SNeuPI
    '''
    
    SN_startWordSNeuPI_L2 = str(chr(SN_startWordSNeuPI_L1_Dec))#varchar 
    SN_zeroPadding_L2 = SN_zeroPadding_L1 #stay as Binary value
    SN_hv_Status_L2 = str(chr(SN_hv_Status_L1))#varchar 
    if SN_hv_Status_L1 == 1:
        SN_hv_Status_L2 = 'ON' 
    elif SN_hv_Status_L1 == 0:
        SN_hv_Status_L2 = 'OFF'
    SN_emissionMode_L2 = str(chr(SN_emissionMode_L1))#varchar 
    SN_pos_3_3V_MonitorSN_L2 = (SN_pos_3_3V_MonitorSN_L1*5.0/65536.0)/(100.0/124.0)
    SN_pos_5VD_MonitorSN_L2 = SN_pos_5VD_MonitorSN_L1*(5.0/65536.0)/(100.0/124.0)
    SN_pos_5VB_MonitorSN_L2 = SN_pos_5VB_MonitorSN_L1*(5.0/65536.0)/(100.0/124.0)
    SN_pos_15VB_MonitorSN_L2 = SN_pos_15VB_MonitorSN_L1*(5.0/65536.0)/(51.1/201.1)
    SN_plate1MonitorSN_L2 = SN_plate1MonitorSN_L1*(5.0/65536.0)
    SN_plate2MonitorSN_L2 = SN_plate1MonitorSN_L1*(5.0/65536.0)
    SN_temperatureMonitor1_UpperBoard_L2 = (SN_temperatureMonitor1_UpperBoard_L1*(5.0/65536.0)/0.004) - 273.0
    SN_temperatureMonitorDSN_L2 =SN_temperatureMonitorDSN_L1*(5.0/65536.0)/0.004 - 273.0
    SN_pos_5V_Converter_L2 = SN_pos_5V_Converter_L1*(5.0/65536.0)/(100.0/124.0)
    #SN_spaceMonitor2_L2 = #WHAT CONVERSION HERE? TM MATRIX BLANK    
    #SN_mcp_CurrentSample1_L2 = #WHAT CONVERSION HERE? TM MATRIX BLANK    
    SN_tipV1_L2 = SN_tipV1_L1*(5.0/65536.0)*(-150.0/3.0)
    #mcp_CurrentSample2_L2 = #WHAT CONVERSION HERE? TM MATRIX BLANK    
    SN_tipV2_L2 = SN_tipV2_L1*(5.0/65536.0)*(-150.0/3.0)
    #mcp_CurrentSample3_L2 = #WHAT CONVERSION HERE? TM MATRIX BLANK    
    SN_tipV3_L2 = SN_tipV3_L1*(5.0/65536.0)*(-150.0/3.0)
    SN_endWordSNeuPI_L2 = SN_endWordSNeuPI_L1
    #pressureReading1_Torr =  #WHAT CONVERSION HERE?
    #pressureReading2_Torr = #WHAT CONVERSION HERE?
    #pressureReading3_Torr =  #WHAT CONVERSION HERE?
    
    '''
    Level 1 - LINAS
    '''
    
    LINAS_header_L1_Dec = struct.unpack(byte_fmt, f.read(1))[0]
    LINAS_header_L1 = hex(LINAS_header_L1_Dec)
    LINAS_filGridGridLow = struct.unpack(byte_fmt, f.read(1))[0] #1 byte to split
    LINAS_filament_OneHalf_L1 = (LINAS_filGridGridLow >> 7) & 0b1 #rs 7 mask 1
    LINAS_gridBias_OnOff_L1 = (LINAS_filGridGridLow >> 6) & 0b1 #rs 7 mask 1
    LINAS_gridBiasSetting_L1 = (LINAS_filGridGridLow >> 2) & 0b1111 #rs 2 mask 4
    LINAS_lowhighFil = struct.unpack(byte_fmt, f.read(1))[0] #1 byte to split
    LINAS_collectorLowRange_L1 = (LINAS_filGridGridLow) & 0b1 #rs 7 mask 1 #Conctanate last bit from previous byte
    LINAS_collectorHighRange_L1 = (LINAS_lowhighFil >> 4) & 0b111 #rs 4 mask 3
    LINAS_filament_OnOff_L1 = (LINAS_lowhighFil) & 0b1111 #rs 0 mask 4
    
    LINAS_packetCounter_L1 = struct.unpack(short_fmt, f.read(2))[0]
    LINAS_powerError = struct.unpack(byte_fmt, f.read(1))[0] #1 byte to split
    LINAS_powerStatus_FilOn_FilSide_GridOn_SAFE_L1 = (LINAS_powerError >> 4) & 0b1111 #rs 4 mask 4
    LINAS_errorStatus_Range_TBD_L1 = (LINAS_powerError) & 0b1111 #rs 0 mask 4
    LINAS_watchdogTimeoutCounter_L1 = struct.unpack(byte_fmt, f.read(1))[0]
    LINAS_gaugeTemp_L1 = struct.unpack(byte_fmt, f.read(1))[0]
    LINAS_boardTemp_L1 = struct.unpack(byte_fmt, f.read(1))[0]
    LINAS_pos_12V_Monitor_L1 = struct.unpack(byte_fmt, f.read(1))[0]
    LINAS_referenceVoltage_L1 = struct.unpack(byte_fmt, f.read(1))[0]
    LINAS_filamentSupplyCurrent_L1 = struct.unpack(byte_fmt, f.read(1))[0]
    LINAS_filamentControlVoltage_L1 = struct.unpack(byte_fmt, f.read(1))[0]
    LINAS_ieReference_4096V_L1 = struct.unpack(byte_fmt, f.read(1))[0]
    LINAS_gridMonitor_L1 = struct.unpack(byte_fmt, f.read(1))[0]
    LINAS_igCollectorCurrent_L1 = struct.unpack('>4B', f.read(4))[0]
    LINAS_igEmissionCurrent_L1 = struct.unpack('>4B', f.read(4))[0]
    LINAS_endWordLINAS_L1 = struct.unpack(byte_fmt, f.read(1))[0]
    
    
    '''
    Level 2 - LINAS Conver to ASCII
    '''
    LINAS_header_L2 = str(chr(LINAS_header_L1_Dec))#varchar 
    LINAS_filament_OneHalf_L2 = str(chr(LINAS_filament_OneHalf_L1))#varchar 
    LINAS_gridBias_OnOff_L2 = str(chr(LINAS_gridBias_OnOff_L1))#varchar 
    LINAS_gridBiasSetting_L2 = str(chr(LINAS_gridBiasSetting_L1))#varchar 
    LINAS_collectorLowRange_L2 = str(chr(LINAS_collectorLowRange_L1))#varchar 
    LINAS_collectorHighRange_L2 = str(chr(LINAS_collectorHighRange_L1))#varchar 
    LINAS_filament_OnOff_L2 = str(chr(LINAS_filament_OnOff_L1))#varchar 
    packetCounter_L2 = hex(LINAS_packetCounter_L1)
    LINAS_powerStatus_FilOn_FilSide_GridOn_SAFE_L2 = str(chr(LINAS_powerStatus_FilOn_FilSide_GridOn_SAFE_L1))#varchar 
    LINAS_errorStatus_Range_TBD_L2 = str(chr(LINAS_errorStatus_Range_TBD_L1))#varchar 
    # watchdogTimeoutCounter_L2 = #in what format?
    # gaugeTemp_L2 = #look up table (see TM Matrix)
    # boardTemp_L2 = #look up table (see TM Matrix)
    LINAS_pos_12V_Monitor_L2 = (LINAS_pos_12V_Monitor_L1)*0.1963
    LINAS_referenceVoltage_L2 = (LINAS_referenceVoltage_L1)*0.01953
    LINAS_filamentSupplyCurrent_L2 = (LINAS_filamentSupplyCurrent_L1)*2.0331+5.4691
    LINAS_filamentControlVoltage_L2 = 2.3 #leave in decimal form
    LINAS_ieReference_4096V_L2 = (LINAS_ieReference_4096V_L1)*0.01953
    LINAS_gridMonitor_L2 = (LINAS_gridMonitor_L1)*0.9848-2.6025
    LINAS_igCollectorCurrent_L2 = (LINAS_igCollectorCurrent_L1-2.85328227*10.0**6.0)/(5.318529932*10.0**6.0)
    LINAS_igEmissionCurrent_L2 =(LINAS_igEmissionCurrent_L1-9.697692934*10.0**5.0)/(9.438607963*10.0**5.0)
    LINAS_endWordLINAS_L2 = LINAS_endWordLINAS_L1#varchar
#    #pressureReading1_Torr = 2.0 #WHAT CONVERSION HERE?
#    #pressureReading2_Torr = 2.0 #WHAT CONVERSION HERE?
#    #pressureReading3_Torr = 2.0 #WHAT CONVERSION HERE?

    del raw
    del f
    return locals()
    
