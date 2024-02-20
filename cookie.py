class Cookie:
    def __init__(self, color):
        self.color = color
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
        
cookie_one = Cookie("Green")
cookie_two = Cookie("Blue")

print("cookie_one color is ", cookie_one.get_color())
print("cookie_two color is ", cookie_two.get_color())

cookie_one.set_color("Yellow")

print("\ncookie_one color is now ", cookie_one.get_color())
print("cookie_two color is ", cookie_two.get_color())