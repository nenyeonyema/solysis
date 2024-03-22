#!/usr/bin/python3
from console import HBNBCommand
from models.base_model import BaseModel

my_console = HBNBCommand()
my_console.do_create("BaseModel")
print("Created new BaseModel instance")
my_console.do_show("BaseModel " + BaseModel._all_instances[0].id)
print("Showed BaseModel instance")
my_console.do_all("BaseModel")
print("Listed all BaseModel instances")
