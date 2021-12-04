"""Programmed by Nelson Booth
Imperial to Metric Program Version 2
This program will convert numbers from the imperial unit system to the metric unit system
and vice versa.
Acknowledgement: disabled-world.com, Link: https://www.disabled-world.com/calculators-charts/metimp.php
"""
# Updates: add more unit conversions
 
class Conversion:
 
    def __init__(self):
    # met to imp
        self.__kil_mi = 0.621371
        self.__kil_ft = 3280.84
        self.__m_ft = 3.28084
        self.__cen_in = 0.393701
        self.__milm_in = 0.0393701
        self.__m_in = 39.3701
        self.__m_yd = 1.09361
        self.__cen_yd = 0.0109361
        self.__kil_yd = 1093.61
        self.__lit_qrt = 1.05669
        self.__lit_gal = 0.264172
        self.__lit_cup = 4.22675
        self.__mil_cup = 0.00422675
        self.__mil_oun = 0.033814
        self.__kilg_ton = 0.00110231
        self.__kilg_lbs = 2.20462
        self.__g_oun = 0.035274
        self.__g_lbs = 0.00220462
        self.__milg_oun = 0.000035274
    # imp to met
        self.__in_m = 0.0254
        self.__in_cen = 2.54
        self.__in_milm = 25.4
        self.__ft_m = 0.3048
        self.__ft_kil = 0.0003048
        self.__yd_m = 0.9144
        self.__yd_cen = 91.44
        self.__yd_kil = 0.0009144
        self.__mi_kil = 1.60934
        self.__mi_m = 1609.34
        self.__oun_mil = 29.5735
        self.__cup_mil = 236.588
        self.__cup_lit = 0.236588
        self.__qrt_lit = 0.946353
        self.__gal_lit = 3.78541
        self.__oun_milg = 28349.5
        self.__oun_g = 28.3495
        self.__lbs_kilg = 0.453592
        self.__ton_kilg = 907.185
   
# met to imp helper functions
    def km_to_mi(self, num):
        self.__mi = num * self.__kil_mi
        return (f"{self.__mi} mi")
   
    def km_to_ft(self, num):
        self.__ft = num * self.__kil_ft
        return (f"{self.__ft} ft")
   
    def m_to_ft(self, num):
        self.__ftv2 = num * self.__m_ft
        return (f"{self.__ftv2} ft")
   
    def cen_to_in(self, num):
        self.__in = num * self.__cen_in
        return (f"{self.__in} in")
   
    def milm_to_in(self, num):
        self.__inv2 = num * self.__milm_in
        return (f"{self.__inv2} in")
   
    def m_to_in(self, num):
        self.__inv3 = num * self.__m_in
        return (f"{self.__inv3} in")
   
    def m_to_yd(self, num):
        self.__yd = num * self.__m_yd
        return (f"{self.__yd} yd")\
       
    def cen_to_yd(self, num):
        self.__ydv2 = num * self.__cen_yd
        return (f"{self.__ydv2} yd")
 
    def kil_to_yd(self, num):
        self.__ydv3 = num * self.__kil_yd
        return (f"{self.__ydv3} yd")
 
    def lit_to_qrt(self, num):
        self.__qrt = num * self.__lit_qrt
        return (f"{self.__qrt} qrts")
 
    def lit_to_gal(self, num):
        self.__gal = num * self.__lit_gal
        return (f"{self.__gal} gal")
   
    def lit_to_cup(self, num):
        self.__cupv2 = num * self.__lit_cup
        return (f"{self.__cupv2} cups")
   
    def mil_to_cup(self, num):
        self.__cup = num * self.__mil_cup
        return (f"{self.__cup} cups")
 
    def mil_to_oun(self, num):
        self.__oun = num * self.__mil_oun
        return (f"{self.__oun} oz")
 
    def kilg_to_ton(self, num):
        self.__ton = num * self.__kilg_ton
        return (f"{self.__ton} tons")
 
    def kilg_to_lbs(self, num):
        self.__lbs = num * self.__kilg_lbs
        return (f"{self.__lbs} lbs")
   
    def g_to_oun(self, num):
        self.__ounv2 = num * self.__g_oun
        return (f"{self.__ounv2} oz")
   
    def g_to_lbs(self, num):
        self.__lbsv2 = num * self.__g_lbs
        return (f"{self.__lbsv2} lbs")
   
    def milg_to_oun(self, num):
        self.__ounv3 = num * self.__milg_oun
        return (f"{self.__ounv3} oz")
   
    def cel_to_fah(self, num):
        self.__fah = num * (9/5) + 32
        return (f"{self.__fah} F")
   
# imp to met helper functions
    def fah_to_cel(self, num):
        self.__cel = (num - 32) * (5/9)
        return (f"{self.__cel} C")
 
    def in_to_m(self, num):
        self.__m = num * self.__in_m
        return (f"{self.__m} m")
   
    def in_to_cen(self, num):
        self.__cen = num * self.__in_cen
        return (f"{self.__cen} cm")
   
    def in_to_milm(self, num):
        self.__milm = num * self.__in_milm
        return (f"{self.__milm} mm")
   
    def ft_to_m(self, num):
        self.__mv2 = num * self.__ft_m
        return (f"{self.__mv2} m")
   
    def ft_to_kil(self, num):
        self.__kilv3 = num * self.__ft_kil
        return (f"{self.__kilv3} km")
   
    def yd_to_m(self, num):
        self.__mv3 = num * self.__yd_m
        return (f"{self.__mv3} m")
   
    def yd_to_cen(self, num):
        self.__cenv2 = num * self.__yd_cen
        return (f"{self.__cenv2} cm")
 
    def yd_to_kil(self, num):
        self.__kil = num * self.__yd_kil
        return (f"{self.__kil} km")
   
    def mi_to_kil(self, num):
        self.__kilv2 = num * self.__mi_kil
        return (f"{self.__kilv2} km")
   
    def mi_to_m(self, num):
        self.__mv4 = num * self.__mi_m
        return (f"{self.__mv4} m")
   
    def oun_to_mil(self, num):
        self.__mil = num * self.__oun_mil
        return (f"{self.__mil} ml")
   
    def cup_to_mil(self, num):
        self.__milv2 = num * self.__cup_mil
        return (f"{self.__milv2} ml")
   
    def cup_to_lit(self, num):
        self.__litv3 = num * self.__cup_lit
        return (f"{self.__litv3} l")
 
    def qrt_to_lit(self, num):
        self.__lit = num * self.__qrt_lit
        return (f"{self.__lit} l")
 
    def gal_to_lit(self, num):
        self.__litv2 = num * self.__gal_lit
        return (f"{self.__litv2} l")
 
    def oun_to_milg(self, num):
        self.__milg = num * self.__oun_milg
        return (f"{self.__milg} mg")
 
    def oun_to_g(self, num):
        self.__g = num * self.__oun_g
        return (f"{self.__g} g")
   
    def lbs_to_kilg(self, num):
        self.__kilg = num * self.__lbs_kilg
        return (f"{self.__kilg} kg")
   
    def ton_to_kilg(self, num):
        self.__kilgv2 = num * self.__ton_kilg
        return (f"{self.__kilgv2} kg")
   
def main():
    x = Conversion()
    name = input(f"\nPlease enter you name to begin: ")
    print(f"\n\tHello {name}! Welcome to Imperial / Metric Convertor!\n")
    print(f"\t{name}, the following will prompt you to enter a number.\n")
    while True:
       
        try:
            num = float(input("Enter Number: "))
            print(f"\n\tGreat! Now select what unit(s) you will be converting from and what unit(s) you want to convert to!\n")
            print(f"\tYour available units are: 'ft', 'mi', 'cm', 'km', 'in', 'yd', 'qrt', 'gal', 'cup', 'oz', 'ton', 'lb', 'F', 'C', 'm', 'mm', 'ml', 'l', 'mg', 'g', 'kg'\n")
               
            while True:
                unit1 = str(input("Unit(s) Converting From: "))
                if unit1 == 'ft':
                    print(f"\n\tAvailable conversions: m, km\n")
                    break
 
                elif unit1 == 'mi':
                    print(f"\n\tAvailable conversions: km, m\n")
                    break
 
                elif unit1 == 'cm':
                    print(f"\n\tAvailable conversions: in, yd\n")
                    break
 
                elif unit1 == 'km':
                    print(f"\n\tAvailable conversions: mi, ft\n")
                    break
 
                elif unit1 == 'in':
                    print(f"\n\tAvailable conversions: m, cm, mm\n")
                    break
 
                elif unit1 == 'yd':
                    print(f"\n\tAvailable conversions: m, cm, km\n")
                    break
 
                elif unit1 == 'qrt':
                    print(f"\n\tAvailable conversions: l\n")
                    break
 
                elif unit1 == 'gal':
                    print(f"\n\tAvailable conversions: l\n")
                    break
 
                elif unit1 == 'cup':
                    print(f"\n\tAvailable conversions: ml, l\n")
                    break
 
                elif unit1 == 'oz':
                    print(f"\n\tAvailable conversions: ml, mg, g\n")
                    break
 
                elif unit1 == 'ton':
                    print(f"\n\tAvailable conversions: kg\n")
                    break
 
                elif unit1 == 'lb':
                    print(f"\n\tAvailable conversions: kg\n")
                    break
 
                elif unit1 == 'F':
                    print(f"\n\tAvailable conversions: C\n")
                    break
 
                elif unit1 == 'C':
                    print(f"\n\tAvailable conversions: F\n")
                    break
 
                elif unit1 == 'm':
                    print(f"\n\tAvailable conversions: ft, in, yd\n")
                    break
 
                elif unit1 == 'mm':
                    print(f"\n\tAvailable conversions: in\n")
                    break
 
                elif unit1 == 'ml':
                    print(f"\n\tAvailable conversions: cup, oz\n")
                    break
 
                elif unit1 == 'l':
                    print(f"\n\tAvailable conversions: qrt, gal, cup\n")
                    break
 
                elif unit1 == 'mg':
                    print(f"\n\tAvailable conversions: oz\n")
                    break
 
                elif unit1 == 'g':
                    print(f"\n\tAvailable conversions: oz, lb\n")
                    break
 
                elif unit1 == 'kg':
                    print(f"\n\tAvailable conversions: ton, lb\n")
                    break
                   
                else:
                    print(f"\n\tInvalid unit(s). Please try again.\n")
                    continue
 
            while True:
                unit2 = str(input("Unit(s) Converting To: "))
                if unit1 == 'km' and unit2 == 'mi':
                    print(f"\n{x.km_to_mi(num)}\n")
                    break
 
                elif unit1 == 'km' and unit2 == 'ft':
                    print(f"\n{x.km_to_ft(num)}\n")
                    break
 
                elif unit1 == 'm' and unit2 == 'ft':
                    print(f"\n{x.m_to_ft(num)}\n")
                    break
 
                elif unit1 == 'cm' and unit2 == 'in':
                    print(f"\n{x.cen_to_in(num)}\n")
                    break
 
                elif unit1 == 'mm' and unit2 == 'in':
                    print(f"\n{x.milm_to_in(num)}\n")
                    break
 
                elif unit1 == 'm' and unit2 == 'in':
                    print(f"\n{x.m_to_in(num)}\n")
                    break
 
                elif unit1 == 'm' and unit2 == 'yd':
                    print(f"\n{x.m_to_yd(num)}\n")
                    break
 
                elif unit1 == 'cm' and unit2 == 'yd':
                    print(f"\n{x.cen_to_yd(num)}\n")
                    break
 
                elif unit1 == 'km' and unit2 == 'yd':
                    print(f"\n{x.kil_to_yd(num)}\n")
                    break
 
                elif unit1 == 'l' and unit2 == 'qrt':
                    print(f"\n{x.lit_to_qrt(num)}\n")
                    break
 
                elif unit1 == 'l' and unit2 == 'gal':
                    print(f"\n{x.lit_to_gal(num)}\n")
                    break
 
                elif unit1 == 'ml' and unit2 == 'cup':
                    print(f"\n{x.mil_to_cup(num)}\n")
                    break
 
                elif unit1 == 'l' and unit2 == 'cup':
                    print(f"\n{x.lit_to_cup(num)}\n")
                    break
 
                elif unit1 == 'ml' and unit2 == 'oz':
                    print(f"\n{x.mil_to_oun(num)}\n")
                    break
 
                elif unit1 == 'kg' and unit2 == 'ton':
                    print(f"\n{x.kilg_to_ton(num)}\n")
                    break
 
                elif unit1 == 'kg' and unit2 == 'lb':
                    print(f"\n{x.kilg_to_lbs(num)}\n")
                    break
 
                elif unit1 == 'g' and unit2 == 'oz':
                    print(f"\n{x.g_to_oun(num)}\n")
                    break
 
                elif unit1 == 'g' and unit2 == 'lb':
                    print(f"\n{x.g_to_lbs(num)}\n")
                    break
 
                elif unit1 == 'mg' and unit2 == 'oz':
                    print(f"\n{x.milg_to_oun(num)}\n")
                    break
 
                elif unit1 == 'C' and unit2 == 'F':
                    print(f"\n{x.cel_to_fah(num)}\n")
                    break
 
                elif unit1 == 'F' and unit2 == 'C':
                    print(f"\n{x.fah_to_cel(num)}\n")
                    break
 
                elif unit1 == 'in' and unit2 == 'm':
                    print(f"\n{x.in_to_m(num)}\n")
                    break
 
                elif unit1 == 'in' and unit2 == 'cm':
                    print(f"\n{x.in_to_cen(num)}\n")
                    break
 
                elif unit1 == 'in' and unit2 == 'mm':
                    print(f"\n{x.in_to_milm(num)}\n")
                    break
 
                elif unit1 == 'ft' and unit2 == 'm':
                    print(f"\n{x.ft_to_m(num)}\n")
                    break
 
                elif unit1 == 'ft' and unit2 == 'km':
                    print(f"\n{x.ft_to_kil(num)}\n")
                    break
 
                elif unit1 == 'yd' and unit2 == 'm':
                    print(f"\n{x.yd_to_m(num)}\n")
                    break
 
                elif unit1 == 'yd' and unit2 == 'cm':
                    print(f"\n{x.yd_to_cen(num)}\n")
                    break
 
                elif unit1 == 'yd' and unit2 == 'km':
                    print(f"\n{x.yd_to_kil(num)}\n")
                    break
 
                elif unit1 == 'mi' and unit2 == 'km':
                    print(f"\n{x.mi_to_kil(num)}\n")
                    break
 
                elif unit1 == 'mi' and unit2 == 'm':
                    print(f"\n{x.mi_to_m(num)}\n")
                    break
 
                elif unit1 == 'oz' and unit2 == 'ml':
                    print(f"\n{x.oun_to_mil(num)}\n")
                    break
 
                elif unit1 == 'cup' and unit2 == 'ml':
                    print(f"\n{x.cup_to_mil(num)}\n")
                    break
 
                elif unit1 == 'cup' and unit2 == 'l':
                    print(f"\n{x.cup_to_lit(num)}\n")
                    break
 
                elif unit1 == 'qrt' and unit2 == 'l':
                    print(f"\n{x.qrt_to_lit(num)}\n")
                    break
 
                elif unit1 == 'gal' and unit2 == 'l':
                    print(f"\n{x.gal_to_lit(num)}\n")
                    break
 
                elif unit1 == 'oz' and unit2 == 'mg':
                    print(f"\n{x.oun_to_milg(num)}\n")
                    break
 
                elif unit1 == 'oz' and unit2 == 'g':
                    print(f"\n{x.oun_to_g(num)}\n")
                    break
 
                elif unit1 == 'lb' and unit2 == 'kg':
                    print(f"\n{x.lbs_to_kilg(num)}\n")
                    break
 
                elif unit1 == 'ton' and unit2 == 'kg':
                    print(f"\n{x.ton_to_kilg(num)}\n")
                    break
 
                else:
                    print(f"\n\tInvalid unit conversion. Please try again.\n")
                    continue
 
        except:
            print(f"\n\tInvalid number. Please try again.\n")
 
if __name__ == "__main__":
    main()
