from enum import Enum
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


if __name__ == "__main__":
    for match_score in range (-5, 10):
        for deviation_score in range(-5,10):
            for difference_score in range(-5,10):
                print("match " + str(match_score) + " | deviation " + str(deviation_score) + 
                " | difference " + str(difference_score))
                print(Result.MATCH)



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
        
      
    