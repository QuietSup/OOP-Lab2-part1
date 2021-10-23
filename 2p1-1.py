class Rectangle:
    def __init__(self, width=None, length=None):
        if width is not None:
            if width <= 0 or width >= 20:
                raise ValueError("Width is out of range (0; 20)")
            if not isinstance(width, float):
                raise ValueError("Width is not float")
            self.__width = width
        else:
            self.__width = 1.0

        if width is not None:
            if length <= 0 or length >= 20:
                raise ValueError("Length is out of range (0; 20)")
            if not isinstance(length, float):
                raise ValueError("Length is not float")
            self.__length = length
        else:
            self.__length = 1.0

    @property
    def width(self):
        return self.__width

    @property
    def length(self):
        return self.__length

    @width.setter
    def width(self, width):
        if width <= 0 or width >= 20:
            raise ValueError("Width is out of range (0; 20)")
        if not isinstance(width, float):
            raise ValueError("Width is not float")
        self.__width = width

    @length.setter
    def length(self, length=None):
        if length is None:
            return
        if length <= 0 or length >= 20:
            raise ValueError("Length is out of range (0; 20)")
        if not isinstance(length, float):
            raise ValueError("Length is not float")
        self.__length = length

    @property
    def area(self):
        return self.__length * self.__width

    @property
    def perimeter(self):
        return 2 * (self.__length + self.__width)


a = Rectangle()
a.width = 9.5
a.length = 1.2
print("width:", a.width)
print("length:", a.length)
print("area:", a.area)
print("perimeter:", a.perimeter)

