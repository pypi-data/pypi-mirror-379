import re
import json
from sqlalchemy.orm.collections import InstrumentedList # type: ignore

"""
This class define diferent methods of prints with its color variants

Use
from utils.prints import Prints

p = Prints()

# Base Method
p.printTitle(title="Title", color="Red")
p.printDict("Clave", "Valor", "magenta")

"""

# Define the color codes.
end = '\033[0m'
bold = '\033[1m'
underline = '\033[4m'

colors = {
    "black": "\033[30m",
    "red": "\033[91m",
    "darkred": '\033[31m',
    "green": "\033[92m",
    "darkgreen": "\033[32m",
    "yellow": "\033[93m",
    "darkyellow": "\033[33m",
    "blue": "\033[94m",
    "darkblue": "\033[34m",
    "magenta": "\033[95m",
    "darkmagenta": "\033[35m",
    "cyan": "\033[96m",
    "darkcyan": "\033[36m",
    "white": "\033[97m",
    "darkwhite": "\033[37m",
    "gray": "\033[90m",
    "none": "\033[0m",
}

class Prints:
    def __init__(self):
        pass
    
    
    # Base Methods
    def printTitle(self, title:str, color="None"):
        color = colors[color.lower()]
        print(f"{color}={end}"*73)
        print(f"{bold}{color}{title.center(73,' ')}{end}")
        print(f"{color}={end}"*73)
    
    def printSubTitle(self, subTitle:str, color="None"):
        color = colors[color.lower()]
        lenText = len(subTitle) + 30
        print(f"{color}~{end}"*lenText)
        print(f"{bold}{color}{subTitle.center(lenText,' ')}{end}")    
        print(f"{color}~{end}"*lenText)

    def printSubTitle2(self, subTitle:str, color="None"):
        color = colors[color.lower()]
        lenText = len(subTitle) + 10
        print(f"{color}{end}"*lenText)
        print(f"{bold}{color}{subTitle.center(lenText,' ')}{end}")    
        print(f"{color}-{end}"*lenText)

    def printClass(self, nameClass:str, color="None"):
        color = colors[color.lower()]
        lenText = len(nameClass) + 6
        print("")
        print(f"{bold}{color}-----{nameClass.center(lenText,' ')}-----{end}")
        print("")

    def printMethod(self, method:str, color="None"):
        color = colors[color.lower()]
        print(f"{color}||||| {method} |||||{end}")

    def printDict(self, key:str, value:str, color="None"):
        color = colors[color.lower()]
        print(f"{color}{bold} > {key}:{end} {value}")

    def printText(self, text:str, color="None"):
        color = colors[color.lower()]
        print(f"{color}{text}{end}")

    def printObject(self, name:str, object:dict, color="None"):
        color = colors[color.lower()]
        if isinstance(object, dict):
            if object:
                print(f"{color}{bold} > {name}:{end} ", end='')
                print("{", end='')
                for index, entity in enumerate(object):
                    print(f"{color}'{entity}':{end} '{object[entity]}'", end='')
                    if index != len(object)-1:
                        print(", ", end='')
                print("}")
            else:
                print(f"{color}{bold} > {name}:{end} {object}")   
        
        elif isinstance(object, list):
            if object:
                print(f"{color}{bold} > {name}:{end} ", end='')
                print("[", end='')
                for index, item in enumerate(object):
                    if isinstance(item, dict):
                        print(f"{color}{{{end}", end='')
                        print(f"'{color}{bold}name{end}': '{item['name']}', '{color}{bold}value{end}': '{item['value']}'", end='')
                        print(f"{color}}}{end}", end='')
                    else:
                        print(item, end='')               
                    if index != len(object)-1:
                        print(", ", end='')
                print("]")
            else:
                print(f"{color}{bold} > {name}:{end} {object}") 

    def printList(self, title=None, request=None, color="None"):
        if title:
            self.printSubTitle(title, color)
        request = parse_to_json(request)
        if request and not isinstance(request, str):
            if isinstance(request, InstrumentedList):
                for element in request:
                    self.printDict(element.name, element.value, color)
            else:
                for key, value in request.items():        
                    if isinstance(value, (dict, list)):
                        self.printObject(key, value, color)
                    else:
                        self.printDict(key, value, color)
        else:
            self.printDict(title, str(request), color)
        self.printEnd()

    def printError(self, text:str, error:str):
        color = colors["darkred"]
        title = "ERROR"
        lenText = len(title) + 20
        print("")
        print(f"{bold}{color}{title.center(lenText,' ')}{end}")
        print(f"{color}{bold}^{end}"*lenText)
        print(f"{color}{bold} > {text}: {end}{color}{error}{end}")

    def printEnd(self):
        print("")

    def testColor(self):
        print("")
        self.printMethod("Test de Colores")
        for color in colors:
            self.printText(f"¡Hola! Soy el Color {color.capitalize()}", color)

        print("")
        self.printMethod("Type of Prints")
        print("")
        print('printTitle => printTitle(title="Soy un Titulo Verde", color="Green")')
        self.printTitle(title="Soy un Titulo Verde", color="Green")
        print("")
        print('printSubTitle => printSubTitle(subTitle="Soy un Subtitulo Verde", color="Green")')
        self.printSubTitle(subTitle="Soy un Subtitulo Verde", color="Green")
        print("")
        print('printSubTitle2 => printSubTitle2(subTitle="Soy un Subtitulo2 Verde", color="Green")')
        self.printSubTitle2(subTitle="Soy un Subtitulo2 Verde", color="Green")
        print("")
        print('printClass => printClass(nameClass="Soy una Clase Verde", color="Green")')
        self.printClass(nameClass="Soy una Clase Verde", color="Green")
        print("")
        print('printMethod => printMethod(method="Soy un print Method Verde", color="Green")')
        self.printMethod(method="Soy un print Method Verde", color="Green")
        print("")
        print('printDict => printDict(key="Soy una key", value="Souy un value", color="Green")')
        self.printDict(key="Soy una key", value="Soy un value", color="Green")
        print("")
        print('printText => printText(text="Soy un Texto Verde", color="Green")')
        self.printText(text="Soy un Texto Verde", color="Green")
        print("")
        print('printList => printList(title="Soy una Lista Json", request={"item1":"value1"...}, color="Green")')
        self.printList(title="Soy una Lista Json", request={"item1":"value1", "item2":"value2", "item3":"value3"}, color="Green")
             

def parse_to_json(s):
    """
    Intenta convertir un string en una estructura JSON (diccionario).
    Si no es posible, retorna el string original.
    """
    if not isinstance(s, str):
        return s

    s = s.strip()

    # 1. Intento directo como JSON válido
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        pass

    # 2. Intentar agregar llaves si parece un objeto sin llaves
    try:
        if ":" in s:
            if not s.startswith("{") and not s.endswith("}"):
                s2 = "{" + s + "}"
                return json.loads(s2)
    except json.JSONDecodeError:
        pass

    # 3. Último recurso: parseo manual con expresiones regulares
    pairs = re.findall(r'"([^"]+)"\s*:\s*"([^"]*)"', s)
    if pairs:
        return {k: v for k, v in pairs}

    return s  # No se pudo convertir

