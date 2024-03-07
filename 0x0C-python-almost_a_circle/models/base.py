
#!/usr/bin/python3
"""Creating a class called Base"""

import json

class Base:
    """Creating a public class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        If id is not None, put self.id = id to the value from the user.
        Else equal to Base.__nb_objects.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries)==0:
            return []
        return (json.dumps(list_dictionaries))
    @classmethod
    def save_to_file(cls,list_objs):
        filename="{}.json".format(cls.__name__)
        if list_objs==None or len(list_objs)==0:
            with open(filename,mode='w',encoding='utf-8') as filename:
                filename.write("[]")
            
        json_string=cls.to_json_string([obj.to_dictionary() for obj in list_objs])

        
        with open(filename,mode='w',encoding="utf-8") as filename:
            filename.write(json_string)
    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string =="" :
            return "[]"
        return json.loads(json_string)
    @classmethod
    def create(cls,**dictionary):
        if cls.__name__=="Rectangle":
            dummy=cls(1,2)
        elif cls.__name__=="Square":
            dummy=cls(1)
        else:
            return None
        dummy.update(**dictionary)
        return dummy
    @classmethod
    def load_from_file(cls):
        filename="{}.json".format(cls.__name__)
        try:
            with open(filename,encoding='utf-8')as jsonfile:
                json_file=jsonfile.read()
                if json_file is None:
                    return "[]"
                dict_list=cls.from_json_string(json_file)
                for_instances=[]
                for_instances=[cls.create(cls,**dictionary)for dictionary in dict_list]
                return for_instances
        except FileNotFoundError:
            return []




