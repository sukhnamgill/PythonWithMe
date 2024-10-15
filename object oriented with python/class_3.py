class Mother:
    Eyes_color="blue"

    def hair(self):
        print("Color of my hair is gray")

class Son(Mother):
    Skin_color="Pink"

    def height(self):
        print("My height is 5ft 07 inch")

object_parent=Mother()
object_child=Son()


#taking onlye parent class value
# object_parent.Eyes_color
# print(Mother.Eyes_color)
# print(object_parent.Eyes_color)
# object_parent.hair()

# now taking child vlaue
object_child.hair()
print(object_child.Eyes_color,object_child.Skin_color)
object_child.height()