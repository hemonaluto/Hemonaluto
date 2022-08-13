"""adding the project path to system path to import modules"""
import os
import sys
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH,"hemonaluto"
)
sys.path.append(SOURCE_PATH)
