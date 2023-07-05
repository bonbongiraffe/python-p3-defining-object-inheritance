class Vehicle:
    def __init__( self, wheel_size=0, wheel_number=0 ):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def go( self ):
        return "vrrrrrrrooom!"

    def fill_up_tank( self ):
        return "filling up!"

