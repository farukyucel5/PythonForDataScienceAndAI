# import custom_module

import sys

custom_module_path = "C:/Users/Techpro/Desktop/AdvancedPythonI/modules_12072024/custom/"

sys.path.append(custom_module_path)

import custom_module

custom_module.hello()