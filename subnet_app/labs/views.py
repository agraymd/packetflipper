from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import View
from django.template.defaulttags import register

import ipaddress
import random

# Create your views here.



def index(request):

    #Function that does the subnet finding game logic and prepares variables to compare user input to.


    #Generates random 32-bit number which will be used to convert to IP address
    rando_ip = random.getrandbits(32)

    #Converts the 32-bit number rando_ip into an IPv4 address
    bits_converted_to_ip = ipaddress.IPv4Address(rando_ip)

    #Change IPv4 address into string
    string_version_of_ip = str(bits_converted_to_ip)

    #Generates random number 1-30 to be used as CIDR mask
    rando_cidr = random.randrange(1,30,1)

    #Changes random CIDR mask integer to string type
    rando_cidr_to_string = str(rando_cidr)

    #Concatenate string to be used in converting to IP with CIDR mask to IPv4 Interface type
    guess_ip_string = string_version_of_ip + '/' + rando_cidr_to_string

    #Converts string of IP and CIDR mask to an interface type (What network is this IP In)
    string_to_ip_network = ipaddress.ip_interface(guess_ip_string)

    #Sets guess_ip_network to correct answer by changing string_to_ip_network into network, sets string variable for later checking
    guess_ip_network = string_to_ip_network.network
    check_against = str(guess_ip_network)







    #Gets the html template
    template = loader.get_template('labs/index.html')

    return render(request, 'labs/index.html', {'check_against': check_against, 'guess_ip_string': guess_ip_string})






