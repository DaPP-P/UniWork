import platform
import geojson
import subprocess
import re

# Video Recording: https://www.youtube.com/watch?v=-evhaihKboU

valid = True
valid2 = True
valid3 = True
noOfNS = 0
noOfEW = 0
latitude = 1000.00
longitude = 1000.00
name = ""

# Function checking if a string can be converted to a float
def can_convert_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
    
# Function for converting DMS to standard format
def dms_to_standard(degree, minute, second, positive):
    minutes_decimal = float(minute) / 60
    seconds_decimal = float(second) / 3600

    decimal_degree = float(degree) + minutes_decimal + seconds_decimal

    if positive == False:
        decimal_degree = -decimal_degree

    return decimal_degree
    
# Function for converting DMM to standard form
def dmm_to_standard(degree, minute, positive):
    decimal_degree = float(degree) + (float(minute) / 60)

    if positive == False:
        decimal_degree = -decimal_degree
    
    return decimal_degree

# Function Checking if a string contains a special character
def containsSpecialCharacters(coordinates):
    for item in coordinates[:-1]:
        if "°" in item or "′" in item or '"' in item or "'" in item or "″" in item: # Resub: Updated for "″"
            return True
    return False


# Read input from the user
coordinates = input("Enter your coordinates: ")
# Following five lines have been added for the resubmission
coordinates = re.sub(r'°', '° ', coordinates)
coordinates = re.sub(r'"', '" ', coordinates)
coordinates = re.sub(r"′", "′ ", coordinates)
coordinates = re.sub(r"'","' ", coordinates)
coordinates = re.sub("″", "″ ", coordinates)
splits = re.split(r',\s*|\s+', coordinates)
cords = list(filter(lambda x: x != "", splits))
noOfCords = len(cords)

print(cords)

# Checking Standard Format

if noOfCords == 2:

    # Checks if the first item in the string is valid
    if (can_convert_float(cords[0])):
        cords[0] = float(cords[0])
        if (cords[0] > 90 or cords[0] < -90):
            valid = False
    else:
        valid = False

    # Checks if the second item in the string is valid
    if (can_convert_float(cords[1])):
        cords[1] = float(cords[1])
        if (cords[1] > 180 or cords[1] < -180):
            valid = False
    else:
         valid = False

    if valid:
        latitude = cords[0]
        longitude = cords[1]

elif noOfCords > 2 and noOfCords < 8 and containsSpecialCharacters(cords) == False:

     # Checks if the first item in the string is valid
    if can_convert_float(cords[0]):
        cords[0] = float(cords[0])
        latitude = cords[0]
    else:
        valid = False

    # Checks if the second item in the string is valid
    if can_convert_float(cords[1]):
        cords[1] = float(cords[1])
        longitude = cords[1]
    else:
        cordAsUpper1 = cords[1].upper()
        if cordAsUpper1 == "N" or cordAsUpper1 == "NORTH":
            latitude = cords[0]
            noOfNS += 1
        elif cordAsUpper1 == "S" or cordAsUpper1 == "SOUTH":
            latitude = -cords[0]
            noOfNS += 1
        elif cordAsUpper1 == "E" or cordAsUpper1 == "EAST":
            longitude = cords[0]
            noOfEW += 1
        elif cordAsUpper1 == "W" or cordAsUpper1 == "WEST":
            longitude = -cords[0]
            noOfEW += 1
        else:
            valid = False

    # Checks if the third item in the string is valid
    if can_convert_float(cords[2]):
        cords[2] = float(cords[2])
        if longitude == 1000.00:
            longitude = cords[2]
        else:
            latitude = cords[2]
    else:
        cordAsUpper2 = cords[2].upper()
        if cordAsUpper2 == "N" or cordAsUpper2 == "NORTH":
            latitude = cords[1]
            longitude = cords[0]
            noOfNS += 1
        elif cordAsUpper2 == "S" or cordAsUpper2 == "SOUTH":
            latitude = cords[1]
            longitude = cords[0]
            noOfNS += 1
        elif cordAsUpper2 == "E" or cordAsUpper2 == "EAST":
            longitude = cords[1]
            noOfEW += 1
        elif cordAsUpper2 == "W" or cordAsUpper2 == "WEST":
            longitude = -cords[1]
            noOfEW += 1
        elif latitude != 1000.00 and longitude != 1000.00:
            name = cords[2]

    # Checks if a fourth item in the string is valid
    if noOfCords > 3:
        if can_convert_float(cords[3]):
            cords[3] = float(cords[3])
            valid = False
        else:
            cordAsUpper3 = cords[3].upper()
            if cordAsUpper3 == "N" or cordAsUpper3 == "NORTH":
                if can_convert_float(cords[2]):
                    latitude = cords[2]
                noOfNS += 1
            elif cordAsUpper3 == "S" or cordAsUpper3 == "SOUTH":
                if can_convert_float(cords[2]):
                   latitude = -cords[2]
                noOfNS += 1
            elif cordAsUpper3 == "E" or cordAsUpper3 == "EAST":
                if can_convert_float(cords[2]):
                    longitude = cords[2]
                noOfEW += 1
            elif cordAsUpper3 == "W" or cordAsUpper3 == "WEST":
                if can_convert_float(cords[2]):
                    longitude = -cords[2]
                noOfEW += 1
            elif latitude != 1000.00 and longitude != 1000.00:
                    name = cords[3]

    # Checks if there is a fifth item which would always be a name
    if noOfCords > 4:
        name = cords[4]


    # Checks to make sure North/South or East/West haven't been entered more then once
    if noOfNS > 1:
        valid = False
    if noOfEW > 1:
        valid = False
    

# DMS input

# Resets variables to check for DMS input
splits = re.split(r',\s*|\s+', coordinates)
cords = list(filter(lambda x: x != "", splits))
noOfCords = len(cords)
noOfNS = 0
noOfEW = 0
cordAsUpper1 = ""
cordAsUpper2 = ""
cordAsUpper3 = ""
push = 0

if noOfCords < 6:
    valid2 = False
else:

    # Checks if the first DMS end with symbols
    if cords[0].endswith('°'):
        if can_convert_float(cords[0][:-1]):
            degree = cords[0][:-1]
    if cords[1].endswith("'") or cords[1].endswith("′"):
        if can_convert_float(cords[1][:-1]):
            minute = cords[1][:-1]
    if cords[2].endswith('"') or cords[2].endswith('″'):    # Resubmission added 'or cords[2].endswith('″')'
        if can_convert_float(cords[2][:-1]):
            second = cords[2][:-1]
    
    # Checks if the first DMS are of type float
    if can_convert_float(cords[0]):
        degree = cords[0]
    if can_convert_float(cords[1]):
        minute = cords[1]
    if can_convert_float(cords[2]):
        second = cords[2]
   
   # Checks the direction of the fourth input
    cordAsUpper1 = cords[3].upper()
    if cordAsUpper1 == "N" or cordAsUpper1 == "NORTH":
        noOfNS += 1
        positive = True
    elif cordAsUpper1 == "S" or cordAsUpper1 == "SOUTH":
        noOfNS += 1
        positive = False
    elif cordAsUpper1 == "E" or cordAsUpper1 == "EAST":
        noOfEW += 1
        positive = True
    elif cordAsUpper1 == "W" or cordAsUpper1 == "WEST":
        noOfEW += 1
        positive = False
    elif noOfNS == 0 and noOfEW == 0:
        noOfNS += 1
        positive = True
        push = -1
        if noOfCords == 9:
            valid2 = False
    else:
        valid2 = False

    # Converts first DMS to standard format
    if noOfNS == 1:  
        latitude = dms_to_standard(degree, minute, second, positive)
    elif noOfEW  == 1:
        longitude = dms_to_standard(degree, minute, second, positive)

    # Checks if second string of DMS has symbols
    if cords[4+push].endswith('°'):
        if can_convert_float(cords[4 + push][:-1]):
            degree = cords[4 + push][:-1]
    if cords[5 + push].endswith("'") or cords[5 + push].endswith("′"):
        if can_convert_float(cords[5 + push][:-1]):
            minute = cords[5 + push][:-1]
    if cords[6 + push].endswith('"') or cords[6 + push].endswith('″'):    # Resubmission added 'or cords[2].endswith('″')'
        if can_convert_float(cords[6 + push][:-1]):
            second = cords[6 + push][:-1]
    
    # Checks if second string of DMS does not have symbols
    if can_convert_float(cords[4 + push]):
        degree = cords[4 + push]
    if can_convert_float(cords[5 + push]):
        minute = cords[5 + push]
    if can_convert_float(cords[6 + push]):
        second = cords[6 + push]
    
    # Checks direction of the 8th input
    beforeCheck = noOfNS
    print(beforeCheck)
    cordAsUpper2 = cords[7 + push].upper()
    if cordAsUpper2 == "N" or cordAsUpper2 == "NORTH":
        noOfNS += 1
        positive = True
    elif cordAsUpper2 == "S" or cordAsUpper2 == "SOUTH":
        noOfNS += 1
        positive = False
    elif cordAsUpper2 == "E" or cordAsUpper2 == "EAST":
        noOfEW += 1
        positive = True
    elif cordAsUpper2 == "W" or cordAsUpper2 == "WEST":
        noOfEW += 1
        positive = False
    elif noOfEW == 0:
        noOfEW += 1
        positive = True
        print(cords[7 + push])
        name = cords[7 + push]
        if noOfCords == 9:
            valid2 = False
    else:
        valid2 = False

    # Calculates the standard form for the second DMS input
    if noOfNS == 1 and latitude == 1000:  
        latitude = dms_to_standard(degree, minute, second, positive)
    elif noOfEW  == 1:
        longitude = dms_to_standard(degree, minute, second, positive)
    else:
        valid2 = False

    # Checks if there is an eight item, it will always be a name
    if noOfCords == 9:
        name = cords[8]

#DDM input

# Resets variables to check for DDM input
splits = re.split(r',\s*|\s+', coordinates)
cords = list(filter(lambda x: x != "", splits))
noOfCords = len(cords)
degree = None
minute = None
noOfNS = 0
noOfEW = 0
cordAsUpper1 = ""
cordAsUpper2 = ""

# Checks if the number of cords is either six or seven.
if noOfCords != 6 and noOfCords != 7:
    valid3 = False
else:
    # Checks to make sure the first DMM inputs contain symbols
    if cords[0].endswith('°'):
        if can_convert_float(cords[0][:-1]):
            degree = cords[0][:-1]
    
    if cords[1].endswith("'") or cords[1].endswith("′"):
        if can_convert_float(cords[1][:-1]):
            minute = cords[1][:-1]
    
    # Checks the direction input
    cordAsUpper1 = cords[2].upper()
    if cordAsUpper1 == "N" or cordAsUpper1 == "NORTH":
        noOfNS += 1
        positive = True
    elif cordAsUpper1 == "S" or cordAsUpper1 == "SOUTH":
        noOfNS += 1
        positive = False
    elif cordAsUpper1 == "E" or cordAsUpper1 == "EAST":
        noOfEW += 1
        positive = True
    elif cordAsUpper1 == "W" or cordAsUpper1 == "WEST":
        noOfEW += 1
        positive = False
    else: 
        valid3 = False

    # Calculates the standard format
    if noOfNS == 1:  
        latitude = dmm_to_standard(degree, minute, positive)
    elif noOfEW  == 1:
        longitude = dmm_to_standard(degree, minute, positive)

    # Checks to make sure items four and five contain symbols
    if cords[3].endswith('°'):
        if can_convert_float(cords[3][:-1]):
            degree = cords[3][:-1]
    if cords[4].endswith("'") or cords[4].endswith("′"):
        if can_convert_float(cords[4][:-1]):
            minute = cords[4][:-1]

    # Checks the direction input
    cordAsUpper2 = cords[5].upper()
    if cordAsUpper2 == "N" or cordAsUpper2 == "NORTH":
        noOfNS += 1
        positive = True
    elif cordAsUpper2 == "S" or cordAsUpper2 == "SOUTH":
        noOfNS += 1
        positive = False
    elif cordAsUpper2 == "E" or cordAsUpper2 == "EAST":
        noOfEW += 1
        positive = True
    elif cordAsUpper2 == "W" or cordAsUpper2 == "WEST":
        noOfEW += 1
        positive = False
    else: 
        valid3 = False

    # Calculates the standard form
    if noOfNS == 1 and latitude == 1000:  
        latitude = dmm_to_standard(degree, minute, positive)
    elif noOfEW  == 1:
        longitude = dmm_to_standard(degree, minute, positive)
    else:
        valid3 = False

    # If there is a name inputted, set it to name
    if noOfCords == 7:
        name = cords[6]

# Final Check

# Checks to make sure latitude and longitude are in range
float(latitude)
float(longitude)
if latitude > 90 or latitude < -90 or longitude > 180 or longitude < -180:
    valid = False
    valid2 = False
    valid3 = False


# If a valid format is inputted prints the input and create GeoJSON file
if valid or valid2 or valid3:

    # Rounds the latitude and longitude to a max of 6 decimal points
    latitude = round(latitude, 6)
    longitude = round(longitude, 6)
    
    # Prints the coordinates
    print("The coordinates you inputted are:", coordinates)
    print("These relate to:", latitude, longitude, name)

    # Saves the coordinates to a geojson file
    point = geojson.Point((longitude, latitude))
    feature = geojson.Feature(geometry=point, properties={"name": name})
    feature_collection = geojson.FeatureCollection([feature])
    with open("outputtedCoordinates.geojson", "w") as file:
        geojson.dump(feature_collection, file)
        print("GeoJSON file created successfully.")


    # Sets path for the maps file and the live server
    file_path = "Etude7Map.html"
    live_server_url = "http://127.0.0.1:5500"

    if platform.system() == "Windows":
        # Use 'start' command on Windows
        subprocess.run(["start", live_server_url + "/" + file_path], shell=True)
    else:
        # Use 'open' command on macOS or Linux
        subprocess.run(["open",live_server_url + "/" + file_path])

else:
    print("Unable to process:", coordinates)

