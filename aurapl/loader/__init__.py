import aurapl as apl
import aurapl.pixelmdl as pmdl
from aurapl import *
from aurapl.pixelmdl import *

validated = []
failed = []

def lvl():
    print("Preparing Validation Tools for aurapl and pixelmdl...")
    print("Starting Validation for aurapl...")
    print("Please ignore anything that does not say [Loader] at the front.")
    apl.square()
    answer = input("Did it open up a screen and show a square? (yes/no)")
    if answer == "yes":
        print("Thank you for validating this")
        validated.append("square")
    else:
        print("Please report this through our Security Form available on Github")
        failed.append("square")
    apl.triangle()
    answer = input("Did it open up a screen and show a triangle? (yes/no)")
    if answer == "yes":
        print("Thank you for validating this")
        validated.append("triangle")
    else:
        print("Please report this through our Security Form available on Github")
        failed.append("triangle")
    print("Moving on to validating PixelMDL")
    pmdl.hello()
    answer = input("Did it print Hello World? (yes/no)")
    if answer == "yes":
        print("Appreciating support for validating!")
        validated.append("hello")
    else:
        print("Please report this through Github on our Security Form.")
        failed.append("hello")
    print("Please answer the questions for this function")
    pmdl.quiz()
    answer = input("Did the quit fully work? (yes/no)")
    if answer == "yes":
        print("Function successful")
        validated.append("quiz")
    else:
        print("Immediately report to our Security Form available on Github.")
        failed.append("quiz")
    pmdl.dumby()
    answer = input("Did it give the answer of 21?")
    if answer == "yes":
        print("21! Thank you")
        validated.append("dumby")
    else:
        print("Did it not say 21...")
        failed.append("dumby")
    print("Thank you for answering all of these questions")
    print("Validated: ", validated)
    print("Failed: ", failed)