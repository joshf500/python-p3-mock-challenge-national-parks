
class Trip:
    
    def __init__(self, visitor, national_park, start_date:str, end_date:str):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

        visitor.trips(self)
        visitor.national_parks(national_park)
        national_park.trips(self)
        national_park.visitors(visitor)
    
    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self,visitor):
        from classes.visitor import Visitor
        if isinstance(visitor, Visitor):
            self._visitor=visitor
        else:
            raise Exception

    @property
    def national_parks(self):
            return self._national_park

    @visitor.setter
    def national_parks(self,national_park):
        from classes.national_park import NationalPark
        if isinstance(national_park, NationalPark):
            self._national_park=national_park
        else:
            raise Exception
    


