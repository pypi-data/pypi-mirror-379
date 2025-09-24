from .peError import *

class scaffolder:
    @staticmethod
    def functions(function_name:list = None, file:str = None):
        n = len(function_name)
        if file is None:
            raise MissingFilePathError("Please provide a file path.")
        
        if function_name is None:
            raise MissingFunctionNameError("Please provide a function" + "'s" + 'name.')
        
        if not isinstance(file,str):
            raise InvalidArgumentTypeError('The file path is not string.')
        
        if not isinstance(function_name,list):
            raise InvalidArgumentTypeError('The \"function'+ "'s" + 'name\" is not a list.')
        
        try:
            for i in range(n):
                with open(file, 'a', encoding='utf-8') as f:
                    f.write('\ndef ' + function_name[i] + '():\n    pass\n')
        except PermissionError as e:
            PermissionError(f"Permission denied: cannot write to '{file}'.")
        except FileNotFoundError as e:
            raise FileNotFoundError(f"The directory for '{file}' does not exist.")
        except OSError as e:
            raise OSError(f"Failed to write to file '{file}': {e}.")
        except Exception as e:
            raise UnkownError(f'{e}')

    @staticmethod
    def list(list_name:list = None, list_element:list = None, file:str = None):
        """Hint: The elements of the list_element list parameter are themselves also lists."""
        n = len(list_name)
        if file is None:
            raise MissingFilePathError("Please provide a file path.")
        
        if list_name is None:
            raise MissingListNameError("Please provide a function" + "'s" + 'name.')
        
        if not isinstance(file,str):
            raise InvalidArgumentTypeError('The file path is not string.')
        
        if not isinstance(list_name,list):
            raise InvalidArgumentTypeError('The \"list'+ "'s" + 'name\" is not a list.')
        
        try:
            for i in range(n):
                with open(file, 'a', encoding='utf-8') as f:
                    if list_element is None:
                        f.write(f"\n{list_name[i]}=[]")
                    if list_element is not None:    
                        s = str(list_element[i])
                        if s.startswith("[") and s.endswith("]"):
                            f.write(f"\n{list_name[i]}={list_element[i]}")
        except PermissionError as e:
            PermissionError(f"Permission denied: cannot write to '{file}'.")
        except FileNotFoundError as e:
            raise FileNotFoundError(f"The directory for '{file}' does not exist.")
        except OSError as e:
            raise OSError(f"Failed to write to file '{file}': {e}.")
        except Exception as e:
            raise UnkownError(f'{e}')
#variable_name = variable_value
    @staticmethod
    def variable(variable_name:list = None, variable_value:list = None, file:str = None):
        n = len(variable_name)
        if file is None:
            raise MissingFilePathError("Please provide a file path.")
        
        if variable_name is None:
            raise MissingVaribleNameError("Please provide a varible" + "'s" + 'name.')
        
        if variable_value is None:
            raise MissingVaribleValueError("Please provide a varible" + "'s" + 'value.')
        
        if not isinstance(file,str):
            raise InvalidArgumentTypeError('The file path is not string.')
        if not isinstance(variable_name,list):
            raise InvalidArgumentTypeError('The \"varible'+ "'s" + 'name\" must be a list.')
        if not isinstance(variable_value,list):
            raise InvalidArgumentTypeError('The \"varible'+ "'s" + 'value\" must be a list.')
        
        try:
            for i in range(n):
                with open(file, 'a', encoding='utf-8') as f: 
                    s = variable_value[i]
                    if isinstance(s, str):
                        f.write(f"\n{variable_name[i]}=\"{variable_value[i]}\"")
                    else:
                        f.write(f"\n{variable_name[i]}={variable_value[i]}")
        except PermissionError as e:
            PermissionError(f"Permission denied: cannot write to '{file}'.")
        except FileNotFoundError as e:
            raise FileNotFoundError(f"The directory for '{file}' does not exist.")
        except OSError as e:
            raise OSError(f"Failed to write to file '{file}': {e}.")
        except Exception as e:
            raise UnkownError(f'{e}')

#set1 = {}. so, if set_element is None, set_name = {}.[['a','b','c'],['a','b','c'],['a','b','c']]
#                                                    ______i________  _j____________________________
    @staticmethod
    def set(set_name:list = None, set_element:list = None, set_element_class:list = str, file:str = None):
        n = len(set_name)
        if file is None:
            raise MissingFilePathError("Please provide a file path.")
        if set_name is None:
            raise MissingSetNameError("Please provide a set" + "'s" + 'name.')
        
        if not isinstance(file,str):
            raise InvalidArgumentTypeError('The file path is not string.')
        if not isinstance(set_name,list):
            raise InvalidArgumentTypeError('The \"set'+ "'s" + 'name\" must be a list.')
        for i in range(n):
            s = set_element[i]
            for j in range(len(s)):
                if type(s[j]) is not set_element_class:
                    raise InvalidArgumentTypeError(f"The \"set's class\" must be a {set_element_class}.")

        try:
            for i in range(n):
                with open(file, 'a', encoding='utf-8') as f:
                    s = set_element[i]
                    if set_element[i] == []:
                        f.write(f"\n{set_name[i]}={{}}\n")
                    else:
                        f.write(f"\n{set_name[i]} = {set(s)}\n")

        except PermissionError as e:
            PermissionError(f"Permission denied: cannot write to '{file}'.")
        except FileNotFoundError as e:
            raise FileNotFoundError(f"The directory for '{file}' does not exist.")
        except OSError as e:
            raise OSError(f"Failed to write to file '{file}': {e}.")
        except Exception as e:
            raise UnkownError(f'{e}')

    @staticmethod
    def classes(class_name : list = None, parent_class : str = None, class_functions : list = None, file : str = None):
        n = len(class_name)
        cf = len(class_functions)
        if file is None:
            raise MissingFilePathError("Please provide a file path.")
        
        if class_name is None:
            raise MissingClassNameError("Please provide a varible" + "'s" + 'name.')
        
        if not isinstance(file,str):
            raise InvalidArgumentTypeError('The file path is not string.')
        if not isinstance(class_name,list):
            raise InvalidArgumentTypeError("The class's name must be a list.")
        
        try:
            for i in range(n):
                with open(file, 'a', encoding='utf-8') as f:
                    if parent_class is not None: 
                        f.write(f"\nclass {class_name[i]}({parent_class}):\n    def __init__(self):\n            pass\n")
                    if class_functions is not None:
                        f.write(f"\nclass {class_name[i]}:\n    def __init__(self):\n        pass\n")
                        for j in range(cf):
                            f.write(f"    def {class_functions[j]}(self):\n            pass\n")
                    else:
                        f.write(f"\nclass {class_name[i]}:\n    def __init__(self):\n        pass\n")
        except PermissionError as e:
            PermissionError(f"Permission denied: cannot write to '{file}'.")
        except FileNotFoundError as e:
            raise FileNotFoundError(f"The directory for '{file}' does not exist.")
        except OSError as e:
            raise OSError(f"Failed to write to file '{file}': {e}.")
        except Exception as e:
            print(f'Unknown Error:{e}')

"""
    @staticmethod
    def tuple(variable_name:list = None, variable_value:list = None, file:str = None):
        n = len(set_name)
        if file is None:
            raise MissingFilePathError("Please provide a file path.")
        if set_name is None:
            raise MissingSetNameError("Please provide a set" + "'s" + 'name.')
        
        if not isinstance(file,str):
            raise InvalidArgumentTypeError('The file path is not string.')
        if not isinstance(set_name,list):
            raise InvalidArgumentTypeError('The \"set'+ "'s" + 'name\" must be a list.')
        for i in range(n):
            s = set_element[i]
            for j in range(len(s)):
                if type(s[j]) is not set_element_class:
                    raise InvalidArgumentTypeError(f"The \"set's class\" must be a {set_element_class}.")

        try:
            for i in range(n):
                with open(file, 'a', encoding='utf-8') as f:
                    s = set_element[i]
                    if set_element[i] == []:
                        f.write(f"\n{set_name[i]}={{}}\n")
                    else:
                        f.write(f"\n{set_name[i]} = {set(s)}\n")

        except PermissionError as e:
            PermissionError(f"Permission denied: cannot write to '{file}'.")
        except FileNotFoundError as e:
            raise FileNotFoundError(f"The directory for '{file}' does not exist.")
        except OSError as e:
            raise OSError(f"Failed to write to file '{file}': {e}.")
        except Exception as e:
            raise UnkownError(f'{e}')

    @staticmethod
    def dictionary(variable_name:list = None, variable_value:list = None, file:str = None):
        n = len(set_name)
        if file is None:
            raise MissingFilePathError("Please provide a file path.")
        if set_name is None:
            raise MissingSetNameError("Please provide a set" + "'s" + 'name.')
        
        if not isinstance(file,str):
            raise InvalidArgumentTypeError('The file path is not string.')
        if not isinstance(set_name,list):
            raise InvalidArgumentTypeError('The \"set'+ "'s" + 'name\" must be a list.')
        for i in range(n):
            s = set_element[i]
            for j in range(len(s)):
                if type(s[j]) is not set_element_class:
                    raise InvalidArgumentTypeError(f"The \"set's class\" must be a {set_element_class}.")

        try:
            for i in range(n):
                with open(file, 'a', encoding='utf-8') as f:
                    s = set_element[i]
                    if set_element[i] == []:
                        f.write(f"\n{set_name[i]}={{}}\n")
                    else:
                        f.write(f"\n{set_name[i]} = {set(s)}\n")

        except PermissionError as e:
            PermissionError(f"Permission denied: cannot write to '{file}'.")
        except FileNotFoundError as e:
            raise FileNotFoundError(f"The directory for '{file}' does not exist.")
        except OSError as e:
            raise OSError(f"Failed to write to file '{file}': {e}.")
        except Exception as e:
            raise UnkownError(f'{e}')
"""
    