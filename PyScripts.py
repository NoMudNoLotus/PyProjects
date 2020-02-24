#!/usr/bin/python3
# assorted python projects I made inspired by Karan's python project list
# the full list can be found at https://github.com/karan/Projects
# this is a rolling project since there's a massive list of projects :)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
from termcolor import colored
import banners
import portscanner
import platform
import colorama
colorama.init()

if __name__ == '__main__':
    def returnToMenu():
        yon = input("~Would you like to return to the main menu?(Y/n)  ")
        if (yon == "Y" or yon == "y"):
            main()

    """prints the numbers from 1 to 100. But for multiples
    of three print “Fizz” instead of the number and for the multiples
    of five print “Buzz”. For numbers which are multiples
    of both three and five print “FizzBuzz"."""
    def FizzBuzz():  # FUNC 1 IN MAIN
        for i in range(101):
            if (i % 3 == 0):
                if (i % 5 == 0):
                    print(colored("FizzBuzz", "yellow"))
                elif (i % 3 == 0):
                    print(colored("Fizz", "grey", "on_white"))
            elif (i % 5 == 0):
                print(colored("Buzz", "yellow"))
            else:
                print(str(i))
        print(colored("~"*30, "yellow"))
        returnToMenu()

    # Takes a string as input and prints the reversed string
    def revString(word):  # FUNC 2 IN MAIN
        splitWord = [char for char in word]
        join = ""
        for i in reversed(splitWord):
            join = join + i
        print(colored("-"*30, "magenta"))
        print(colored(" You entered: {}".format(word), "magenta"))
        print(colored(" Reversed string: {}".format(join), "magenta"))
        print(colored("-"*30, "magenta"))
        returnToMenu()

    # prints out system information
    def sysInfo():  # FUNC 3 IN MAIN
        print(colored("_-"*30 + "\n", "cyan", attrs=['blink']))
        machineType = platform.machine()  # Machine Type (ex. i386)
        if (machineType == ""):
            print(colored("Machine type: could not be determined.", "cyan"))
        else:
            print(colored("Machine type: {}".format(machineType), "cyan"))
        node = platform.node()  # Name (ex. Macbook Pro)
        if (node == ""):
            print(colored("Name: could not be determined.", "cyan"))
        else:
            print(colored("Name: {}".format(node), "cyan"))
        platformInfo = platform.platform()  # Platform info
        if (platformInfo == ""):
            print(colored("Platform Info: could not be determined.", "cyan"))
        else:
            print(colored("Platform info: {}".format(platformInfo), "cyan"))
        system = platform.system()  # Platform system (ex. Unix)
        if (system == ""):
            print(colored("System: could not be determined.", "cyan"))
        else:
            print(colored("System: {}".format(system), "cyan"))
        processor = platform.processor()  # Platform processor
        if (processor == ""):
            print(colored("Processor: could not be determined.", "cyan"))
        else:
            print(colored("Processor: {}".format(processor), "cyan"))
        print(colored("_-"*30 + "\n", "cyan", attrs=['blink']))
        returnToMenu()

    # Simple port scanner
    def portScan(): # FUNC 4 IN MAIN
        portscanner.main(input("Input IP: "), input("Input IP range(0-x): "))
        returnToMenu()

    # Auto PEP8-compliant formatter 
    def PEP8():  # NOT DONE YET
        print("not quite done yet")

    # Wrapper function including banner
    def main():
        banners.scrollBanner()
        # User selects which function to run
        run = int(input("Which function would you like to run?\n (1)FizzBuzz\n \
(2)Reverse a String\n (3)System Info\n (4)Port Scanner\n (5)0\n~  "))
        if run == 1:
            return FizzBuzz()
        elif run == 2:
            return revString(input("\nInput string to reverse?\n~  "))
        elif run == 3:
            return sysInfo()
        elif run == 4:
            return portScan()
        elif run == 5:
            return PEP8()
        else:
            exit
    main()
