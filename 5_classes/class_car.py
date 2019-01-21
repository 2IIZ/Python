class Car:

    def __init__(self, color):

        self.color = color

    # getters

    def _get_color(self):
        print("The car's color is :", self.color)

    def _set_color(self, color):
        self.color = color
        print("Seems that the car's color is changed, now is :", self.color)


    # method spécial
    # https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python/233046-les-methodes-speciales
