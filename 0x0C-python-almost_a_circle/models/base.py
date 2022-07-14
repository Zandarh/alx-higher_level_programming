#!/usr/bin/python3
"""
    base module
"""
import json
import csv
import turtle


class Base:
    """
        This is the base class
    """
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        """
            Initializing instances of the base class

            Args:
                id: The id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string rep. of list_dictionarie """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string to a file """
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as file:
            if list_objs is None:
                file.write(cls.to_json_string([]))
            else:
                in_list = list()
                for instance in list_objs:
                    in_list.append(instance.to_dictionary())

                file.write(cls.to_json_string(in_list))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
         # create a dummy instance
        if cls.__name__ == "Square":
            dum_obj = cls(2)
        else:
            dum_obj = cls(2, 5)

        # update dummy instance with dictionary given
        dum_obj.update(**dictionary)

        # return updated dummy instance
        return dum_obj

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances: """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            serializes in csv
            Args:
                list_objs: list of objects
        """
        # create and write to the csv file
        with open(cls.__name__ + '.csv', 'w', encoding='utf-8') as file:
            field_name = list()

            # get list of object keys
            field_name = (list_objs[0].to_dictionary()).keys()
            write_csv = csv.DictWriter(file, fieldnames=field_name)

            write_csv.writeheader()  # display the keys on the first line
            for dum in list_objs:
                write_csv.writerow(dum.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
            returns deserialized csv content
        """
        with open(cls.__name__ + '.csv', encoding='utf-8') as file:
            new_l = []
            reader_csv = csv.DictReader(file)

            new_dic = dict()
            for content in reader_csv:
                for key, value in content.items():
                    new_dic[key] = int(value)
                new_l.append(cls.create(**new_dic))

            return 

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
