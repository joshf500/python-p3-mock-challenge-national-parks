class NationalPark:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if isinstance(name, str) and not hasattr(self, "name"):
            self._name=name
        else:
            raise Exception

        

    def trips(self, new_trip=None):
        from classes.trip import Trip
        if new_trip and isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        if new_visitor not in self._visitors and isinstance(new_visitor, Visitor):
            self._visitors.append(new_visitor)

        return self._visitors
    
    def total_visits(self):
        return len(self._trips)
    
    def best_visitor(self):
        visits=[]
        for i in self._trips:
            visits.append(i.visitor)
        return max(set(visits), key=visits.count)