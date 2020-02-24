#!/usr/bin/python3
# simple port scanner using the nmap library
# also my first time with socket programming
from termcolor import colored
import nmap
import sys
import socket
import colorama
colorama.init()


def main(targIP, portRG):
    # check if both args were input
    if len(sys.argv) != 1:
        print(colored("User did not inout both IP and Range..\n", "cyan"))
        exit

    # set vars and print wait
    hostaddress = str(targIP)
    portrange = str(portRG)
    ipaddress = socket.gethostbyname(hostaddress)
    print(colored("Please Wait; scanning %s" % (ipaddress), "cyan"))
    print(colored("_" * 30, "cyan"))

    # initializes the port scanner
    try:
        nmScan = nmap.PortScanner()
        nmScan.scan(ipaddress, portrange)
    except nmap.PortScannerError:
        print(colored('Nmap not found', sys.exc_info()[0], "red"))
        sys.exit(0)
    except:
        print(colored("Unexpected error:", sys.exc_info()[0], "red"))
        sys.exit(0)

    # prints results
    for host in nmScan.all_hosts():
        print(colored("       Host : %s (%s)" % (host, hostaddress), "cyan"))
        print(colored("       State : %s" % nmScan[host].state(), "cyan"))
        # prints protocols
        for proto in nmScan[host].all_protocols():
            print(colored("----------" * 6, "cyan"))
            print(colored("       Protocol : %s" % proto, "cyan"))
            # get all ports for tcp/udp protocol
            ports = nmScan[host][proto].keys()
            for port in ports:
                print(colored("       port : %s\tstate : %s" % (port, nmScan[host][proto][port]['state']), "cyan"))
    print(colored("_" * 30, "cyan"))
