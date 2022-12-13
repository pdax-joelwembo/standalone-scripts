import  jpype     
import  asposecells     
jpype.startJVM() 
from asposecells.api import Workbook
workbook = Workbook("result2.xlsx")
workbook.Save("Output.json")
jpype.shutdownJVM()