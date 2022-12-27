import  jpype     
import  asposecells     
jpype.startJVM() 
from asposecells.api import Workbook
workbook = Workbook("data/result2.xlsx")
workbook.Save("data/Output.json")
jpype.shutdownJVM()