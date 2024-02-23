#!/usr/bin/python3
class Fruit:
    def __init__(self,name):
        self._name=name
    @property
    def fruit_name(self):
        print("{} was accessed".format(self._name))
    @fruit_name.setter
    def fruit_name(self,value):
        try:
            if type(value)=int:
                self.name_=value

