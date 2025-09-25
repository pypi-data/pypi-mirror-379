
class Full_Field_Approach:

    def __init__(self, LOGGER):
        
        self.LOGGER = LOGGER
        for attr in ["keffNum","keffNum_EVa","keffNum_EVe","matPixels"]:
            setattr(self,attr,None) # Definition of attributes


    