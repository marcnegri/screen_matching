from enum import Enum
import collections

class Result(Enum):
    MATCH = "match"
    DEVIATION = "deviation"
    DIFFERENCE = "difference"

class Rules:
    def __init__(self):
        self.ddn = []
        self.domicile = []
        self.nationality = []
        self.sanction = []
        self.gender = []

class Subject:
    def __init__(self, name_score):
        self.ddn = None
        self.domicile = []
        self.nationality = []
        self.sanction = False
        self.gender = []
        self.name_score = name_score             
        self.total_score = None

def get_ddn_score(in_ddn, wc_ddn):
    try:
        # 1 - check ddn 
            #1.1 - if format is YYYY/MM/DD
            
            #1.2 - if format is YYYY/MM/00

            #1.3 - if format is YYYY

        # 2 - compare DDN
        # 3 - Take the lower diff
        if(diff < 545):
            print("hello")


    except Exception as inst:
        print(type(inst))    
        print(inst.args)     
        print(inst)


def get_domicile_score(in_domicile, wc_domicile):
    in_lst = set(in_domicile)
    wc_lst = set(wc_domicile)
    if(in_lst == wc_lst):
        return Result.MATCH
    for x in in_domicile:
        if(x in wc_domicile):
            return Result.DEVIATION

    return Result.DIFFERENCE                    

def get_nationality_score(in_nationality, wc_nationality):
    in_lst = set(in_nationality)
    wc_lst = set(wc_nationality)
    if(in_lst == wc_lst):
        return Result.MATCH
    for x in in_nationality:
        if(x in wc_nationality):
            return Result.DEVIATION

    return Result.DIFFERENCE

def get_gender_score(in_gender, wc_gender):
    if(in_gender == wc_gender):
        return Result.MATCH
    else:
        return Result.DIFFERENCE

def get_sanction_score(is_sanction)
    if(is_sanction):
        return Result.MATCH


if __name__ == "__main__":
    '''
    for match_score in range (-5, 10):
        for deviation_score in range(-5,10):
            for difference_score in range(-5,10):
    '''
    list1 = ['a','d','e']
    list2 = ['a','d','e']                
    print(get_domicile_score(list1, list2))


        
      
    