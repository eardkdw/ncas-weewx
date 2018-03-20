#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# vim: tabstop=8 expandtab shiftwidth=3 softtabstop=3
#argument parser
from argparse import ArgumentParser

#particular to this program
from sympy.physics import units
from decimal import Decimal
import csv, os.path

desc ='''Converts a CUSTOM-ARC file produced from the Wview or WeeWX database to 
SI units'''

def FtoC(Ftemp):
    '''converts absolute temp in °F to °C'''
    return (5.0/9.0)*(Ftemp-32)

class options(object):
   pass

units.mph = units.miles / units.hours
units.inHg = 3386.389 * units.Pa
units.hPa = 100 * units.Pa

def convert(filename):
   with open(filename, 'rb') as csvfile:
      csvreader = csv.DictReader(csvfile, dialect="excel")
      (root, ext) = os.path.splitext(filename)
      csvoutfilename = root + '-METRIC' + ext
      csvwriter = csv.writer(open(csvoutfilename,'w'), dialect="excel")
   
      csvwriter.writerow(['Timestamp (UTC)','Temp / °C','Chill / °C','HIndex / °C','Humid%', 'Dewpt / °C','Wind / ms¯¹', 'HiWind / ms¯¹', 'Winddir / °', 'Rain / mm','RainRate / mmhr¯¹', 'Pressure / hPa', 'InsideTemp / °C', 'InsideHumid%','Radiation / Wm¯²','UV'])
      for row in csvreader:
         outrow = {}
         outrow['Timestamp'] = row['Timestamp']
         for each in ['Temp','Chill','HIndex','Dewpt','InsideTemp']:
            '''convert all the temps to centigrade'''
            try:
               outrow[each] = round(FtoC(float(row[each])),1) 
            except ValueError: #probably an empty string rather than a number
               outrow[each] = float('NaN') #Not A Number, i.e. no data

         for peach in ['Humid','InsideHumid']:
            try:
               outrow[peach] = round(float(row[peach]),1) 
            except ValueError:
               outrow[peach] = float('NaN')
         
         for pear in ['Wind', 'HiWind']:   
            try:
               outrow[pear] = round(float(row[pear]) * units.mph / (units.m / units.s),1)
            except ValueError:
               outrow[pear] = float('NaN') 

         for plum in ['Rain', 'RainRate']:
            try:
                outrow[plum] = round(float(row[plum]) * units.inch / units.mm,1)
            except ValueError:
                outrow[plum] = float('NaN')
         
         try:
            outrow['Barom'] = round(float(row['Barom']) * units.inHg / units.hPa,1)
         except ValueError:
            outrow['Barom'] = float('NaN')

         #Winddir is fine as it is
         outrow['WindDir'] = row['WindDir']
         outrow['Solar'] = row['Solar']
         outrow['UV'] = row['UV']
         csvwriter.writerow([outrow['Timestamp'], outrow['Temp'], outrow['Chill'], outrow['HIndex'], outrow['Humid'], outrow['Dewpt'], outrow['Wind'], outrow['HiWind'], outrow['WindDir'], outrow['Rain'], outrow['RainRate'], outrow['Barom'], outrow['InsideTemp'], outrow['InsideHumid'],outrow['Solar'], outrow['UV']])


parser = ArgumentParser(description=desc)
parser.add_argument ('infile', nargs='+')
parser.parse_args(namespace=options)
for each in options.infile:
   convert(each)

