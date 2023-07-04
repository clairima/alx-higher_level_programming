#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if hasattr(self, name):
            super().__setattr__(name, value)
        elif name == 'first_name':
            super().__setattr__(name, value)
        else:
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
