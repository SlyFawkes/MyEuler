'''
Created on 8 Dec 2014

@author: vera
'''
dictionary = {"0":0, "1":3, "2":3, "3":5, "4":4, "5":4, "6":3, "7":5, "8":5, "9":4,
              "10":3, "11":6, "12":6, "13":8, "14":8, "15":7, "16":7, "17":9, "18":8, "19":8,
              "20":6, "30":6, "40":5, "50":5, "60":5, "70":7, "80":6, "90":5,
              "100":7}

def run():
    allTen = 3+3+5+4+4+3+5+5+4
    hundies = 99*13*10
    allHundred = (7*9) + allTen
    thousand = 11
    allTeens = 3+6+6+8+8+7+7+9+8+8
    allTwenty = (6*10)+allTen
    allThirty = allTwenty
    allForty = (5*10)+allTen
    allFifty = allForty
    allSixty = allForty
    allSeventy = (7*10)+allTen
    allEighty = allTwenty
    allNinety = allTwenty
    
    
    upTo99 = allTen+allTeens+allTwenty+allThirty+allForty+allFifty+allSixty+allSeventy+allEighty+allNinety
    total = allHundred + upTo99*10 + thousand + hundies - 11*allTen
    
    print total
    
run()