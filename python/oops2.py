class Vehicle:
    def __init__(self, color, brand):
        print("The brand is ",brand)
        print("Color is ", color)
 
    def goForward(self):
        print("Go forward")
    
    def goBackward(self):
        print("Go backward")
    
    def stop(self):
        print("sTOPED")

obj=Vehicle("Red", "Maruti Suzuki")
