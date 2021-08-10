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

    #Set IP Class Ranges

    class_a = range(1,126)
    class_b = range(127,191)
    class_c = range(192,223)

    # Generates random 32-bit number which will be used to convert to IP address
    rando_ip = random.getrandbits(32)

    # Converts the 32-bit number rando_ip into an IPv4 address
    bits_converted_to_ip = ipaddress.IPv4Address(rando_ip)

    # Change IPv4 address into string
    string_version_of_ip = str(bits_converted_to_ip)

    # Finds first octet of randomly generated IP
    first_octet = string_version_of_ip[0:string_version_of_ip.find('.')]

    # Checks what range the first octet is in
    # Generates a subnet mask held in rando_sub for how many hosts and networks game

    if int(first_octet) in class_a:
        #Generates random number 1-16777214 to be used as number of hosts required.
        hosts_required = random.randrange(1,16777214,1)
        #Sets subnet mask to classful mask
        subnet_mask = "/8"
        # Sets integer for number of subnet network bits
        network_bits = 8
        rando_sub = random.randrange(9,30,1)

    elif int(first_octet) in class_b:
        #Generates random number 1-65534 to be used as number of hosts required.
        hosts_required = random.randrange(1,65534,1)
        #Sets subnet mask to classful mask
        subnet_mask = "/16"
        # Sets integer for number of subnet network bits
        network_bits = 16
        rando_sub = random.randrange(17, 30, 1)
    else:
        #Generates random number 1-254 to be used as number of hosts required.
        hosts_required = random.randrange(1,254,1)
        #Sets subnet mask to classful mask
        subnet_mask = "/24"
        # Sets integer for number of subnet network bits
        network_bits = 24
        rando_sub = random.randrange(25, 30, 1)

    # Add string version of ip and subnet mask together to generate classful network string for how many bits game
    classful_network_string = string_version_of_ip + subnet_mask

    # Converts classful_network into an interface type with ip module
    classful_network_converted = ipaddress.ip_interface(classful_network_string)

    # Converts classful_network_converted into classful interface type with ip module
    classful_network_classful = classful_network_converted.network

    # Begin how many bits game checking logic
    # Based on the classful network given, checks the amount of hosts_required and sets the correct answer to the mask required
    if int(first_octet) in class_a:
        if hosts_required <= 2:
            correct_answer = "/30"
        elif 3 <= hosts_required <= 6:
            correct_answer = "/29"
        elif 7 <= hosts_required <= 14:
            correct_answer = "/28"
        elif 15 <= hosts_required <= 30:
            correct_answer = "/27"
        elif 31 <= hosts_required <= 62:
            correct_answer = "/26"
        elif 63 <= hosts_required <= 126:
            correct_answer = "/25"
        elif 127 <= hosts_required <= 254:
            correct_answer = "/24"
        elif 255 <= hosts_required <= 510:
            correct_answer = "/23"
        elif 511 <= hosts_required <= 1022:
            correct_answer = "/22"
        elif 1023 <= hosts_required <= 2046:
            correct_answer = "/21"
        elif 2045 <= hosts_required <= 4094:
            correct_answer = "/20"
        elif 4095 <= hosts_required <= 8190:
            correct_answer = "/19"
        elif 8191 <= hosts_required <= 16382:
            correct_answer = "/18"
        elif 16383 <= hosts_required <= 32766:
            correct_answer = "/17"
        elif 32767 <= hosts_required <= 65534:
            correct_answer = "/16"
        elif 65535 <= hosts_required <= 131070:
            correct_answer = "/15"
        elif 131071 <= hosts_required <= 262142:
            correct_answer = "/14"
        elif 262143 <= hosts_required <= 524286:
            correct_answer = "/13"
        elif 524287 <= hosts_required <= 1048574:
            correct_answer = "/12"
        elif 1048575 <= hosts_required <= 2097150:
            correct_answer = "/11"
        elif 2097151 <= hosts_required <= 4194302:
            correct_answer = "/10"
        elif 4194303 <= hosts_required <= 8388606:
            correct_answer = "/9"
        elif 8388607 <= hosts_required <= 16777214:
            correct_answer = "/8"

    elif int(first_octet) in class_b:
        if hosts_required <= 2:
            correct_answer = "/30"
        elif 3 <= hosts_required <= 6:
            correct_answer = "/29"
        elif 7 <= hosts_required <= 14:
            correct_answer = "/28"
        elif 15 <= hosts_required <= 30:
            correct_answer = "/27"
        elif 31 <= hosts_required <= 62:
            correct_answer = "/26"
        elif 63 <= hosts_required <= 126:
            correct_answer = "/25"
        elif 127 <= hosts_required <= 254:
            correct_answer = "/24"
        elif 255 <= hosts_required <= 510:
            correct_answer = "/23"
        elif 511 <= hosts_required <= 1022:
            correct_answer = "/22"
        elif 1023 <= hosts_required <= 2046:
            correct_answer = "/21"
        elif 2045 <= hosts_required <= 4094:
            correct_answer = "/20"
        elif 4095 <= hosts_required <= 8190:
            correct_answer = "/19"
        elif 8191 <= hosts_required <= 16382:
            correct_answer = "/18"
        elif 16383 <= hosts_required <= 32766:
            correct_answer = "/17"
        elif 32767 <= hosts_required <= 65534:
            correct_answer = "/16"
            
    else:
        if hosts_required <= 2:
            correct_answer = "/30"
        elif 3 <= hosts_required <= 6:
            correct_answer = "/29"
        elif 7 <= hosts_required <= 14:
            correct_answer = "/28"
        elif 15 <= hosts_required <= 30:
            correct_answer = "/27"
        elif 31 <= hosts_required <= 62:
            correct_answer = "/26"
        elif 63 <= hosts_required <= 126:
            correct_answer = "/25"
        elif 127 <= hosts_required <= 254:
            correct_answer = "/24"



    # START WHAT IS THE SUBNET GAME LOGIC / PROGRAMMING
    # Generates random number 1-30 to be used as CIDR mask (for what is the subnet game)
    rando_cidr = random.randrange(1,30,1)

    # Changes random CIDR mask integer to string type
    rando_cidr_to_string = str(rando_cidr)

    # Concatenate string to be used in converting to IP with CIDR mask to IPv4 Interface type
    guess_ip_string = string_version_of_ip + '/' + rando_cidr_to_string

    # Converts string of IP and CIDR mask to an interface type (What network is this IP In)
    string_to_ip_network = ipaddress.ip_interface(guess_ip_string)

    # Sets guess_ip_network to correct answer by changing string_to_ip_network into network, sets string variable for later checking
    guess_ip_network = string_to_ip_network.network
    check_against = str(guess_ip_network)

    # START HOW MANY BITS GAME, NEED TO CHANGE CLASS NAMES OF WHATS THE MASK GAME BECAUSE I MIXED THEM UP
    subnet_bits = rando_sub - network_bits

    # Calculates number of subnets
    number_of_subnets = 2 ** subnet_bits

    # Creates string for how many hosts and subnets game then converts to network type
    how_many_ip_string = string_version_of_ip + '/' + str(rando_sub)
    how_many_ip_network = ipaddress.ip_interface(how_many_ip_string)
    how_many_ip_network_check = how_many_ip_network.network

    # Calculates number of usable hosts
    count_of_hosts = how_many_ip_network_check.hosts()
    answer_of_hosts = sum(1 for host in count_of_hosts)



    #Gets the html template
    template = loader.get_template('labs/index.html')

    return render(request, 'labs/index.html', {
                                                'check_against': check_against, 
                                                'guess_ip_string': guess_ip_string, 
                                                'hosts_required': hosts_required, 
                                                'classful_network_classful': classful_network_classful, 
                                                'correct_answer': correct_answer,
                                                'answer_of_hosts': answer_of_hosts,
                                                'number_of_subnets': number_of_subnets,
                                                'how_many_ip_string': how_many_ip_string
                                                })






