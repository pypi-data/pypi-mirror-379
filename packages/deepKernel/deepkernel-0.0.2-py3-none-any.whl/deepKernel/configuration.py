import deepline,base
import os, sys, json,requests,time

def init(path:str): 
    deepline.init(path)
    base.set_config_path(path)