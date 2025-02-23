import re
import sys
import time

class NovaScriptObject:
    def __init__(self, class_name="", parent=None):
        self.class_name = class_name
        self.attributes = {}
        self.methods = {}
        self.parent = parent
    
    def set_attr(self, name, value):
        self.attributes[name] = value
    
    def get_attr(self, name):
        if name in self.attributes:
            return self.attributes[name]
        elif self.parent:
            return self.parent.get_attr(name)
        return f"Error: Attribute '{name}' not found"

    def call_method(self, method_name, args):
        if method_name in self.methods:
            return self.methods[method_name](*args)
        return f"Error: Method '{method_name}' not found"

def splash_screen():
    splash_text = """
 _  _  _____  _  _  __    ___   ___    __    ____  ____ 
( \( )(  _  )( \/ )/__\  / __) / __)  /__\  (  _ \( ___)
 )  (  )(_)(  \  //(__)\ \__ \( (__  /(__)\  )___/ )__) 
(_)_)(_____)  \/(__)(__)(___/ \___)(__)(__)(__)  (____)
    """
    print(splash_text)
    time.sleep(3)
    print("Starting Novascript...\n")

def execute(code):
    variables = {}
    functions = {}
    classes = {}
    lines = code.strip().split('\n')
    
    def evaluate(expression):
        try:
            return eval(expression, {}, variables)
        except Exception as e:
            return f"Error: {e}"
    
    i = 0
    while i < len(lines):
        try:
            line = lines[i].strip()
            
            if line.startswith("print "):
                content = line[6:].strip()
                print(evaluate(content))
            elif "=" in line and not line.startswith(("if", "while", "for", "class", "try")):
                var_name, value = map(str.strip, line.split("=", 1))
                variables[var_name] = evaluate(value)
            elif line.startswith("#"):
                pass
            elif line.startswith("class "):
                parts = line[6:].split(" extends ")
                class_name = parts[0].strip()
                parent_class = parts[1].strip() if len(parts) > 1 else None
                classes[class_name] = NovaScriptObject(class_name, classes.get(parent_class))
            elif line.startswith("new "):
                parts = line[4:].split(" as ")
                class_name, instance_name = parts[0].strip(), parts[1].strip()
                if class_name in classes:
                    variables[instance_name] = NovaScriptObject(class_name, classes[class_name])
                else:
                    print(f"Error: Class '{class_name}' not defined")
            elif line.startswith("set "):
                parts = line[4:].split(".")
                instance_name, attr_expr = parts[0].strip(), parts[1].strip()
                attr_name, value = attr_expr.split("=")
                if instance_name in variables and isinstance(variables[instance_name], NovaScriptObject):
                    variables[instance_name].set_attr(attr_name.strip(), evaluate(value.strip()))
            elif line.startswith("get "):
                parts = line[4:].split(".")
                instance_name, attr_name = parts[0].strip(), parts[1].strip()
                if instance_name in variables and isinstance(variables[instance_name], NovaScriptObject):
                    print(variables[instance_name].get_attr(attr_name))
            else:
                print(f"Error: Unknown syntax '{line}'")
            i += 1
        except Exception as e:
            print(f"Runtime Error: {e}")
            break

if __name__ == "__main__":
    splash_screen()
    
    if len(sys.argv) < 2:
        print("Usage: python novascript.py <filename>.nsc")
        sys.exit(1)
    
    try:
        with open(sys.argv[1], "r") as f:
            code = f.read()
        execute(code)
    except Exception as e:
        print(f"Error: {e}")
