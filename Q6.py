"""
File: Q6.py
Author: Nathan Lam
Description: Simple GUI implemenation for california cities

Create a simple GUI of city information of California
- See attached JSON file (ca.json), which contains information of all cities in California.
- Use the data abstract from the JSON file to create a simple GUI for it
- The GUI should have a filter function based on the selection of city name (selectable)
- Display information of county full name, latitude, longitude
- Sample GUI is shown below
- Use any python library as needed
"""

from appJar import gui
import json

class simpleGUI():
    
    # Initialize class instance structures
    def __init__(self):
        self.city_data = {}
        self.city_list = []

    # Parse JSON file and store data as a list
    def inputJSONFieldData(self):
        file_name = str(raw_input("Enter JSON file name: "))
        try:
            with open(file_name) as json_data:
                cities = json.load(json_data)
                for city in cities:
                    self.city_data[city['name']] = city
                    self.city_list.append(city['name'])
                self.city_list.sort()
            self.removeUnicode()
        except IOError:
            print("ERROR: Cannot find JSON file!")
            exit(1)

    # Remove unicode from string in the city list
    def removeUnicode(self):
        for index, city in enumerate(self.city_list):
            self.city_list[index] = city.encode('ascii', 'ignore').decode('utf-8')

    # Add a new field to the GUI 
    def createNewField(self, key, description):
        self.app.addLabelEntry(key)
        self.app.setLabel(key, description)

    # Update the various fields when new city is selected
    def updateFields(self):
        self.updateFieldData('full_county_name')
        self.updateFieldData('primary_latitude')
        self.updateFieldData('primary_longitude')
  
    # Update individual field data
    def updateFieldData(self, key):
        info = self.getFieldData(self.app.getOptionBox('City'), key)
        self.setFieldData(key, info)

    # Get/set field data from database
    def getFieldData(self, city, key):
        return self.city_data[city][key]
    
    def setFieldData(self, key, data):
        self.app.setEntry(key, data)

    # Build and start application
    def startApplication(self):
        app = gui("City Information", "500x300")
        self.app = app
        app.setFont(16)
        app.setPadding([20,20])

        # Parse JSON file and insert into database
        self.inputJSONFieldData()

        # Add drop down list for cities and automatic field update
        app.addLabelOptionBox("City", self.city_list)
        app.setOptionBoxChangeFunction("City", self.updateFields)

        # Add labels and entries in the correct row & column
        self.createNewField("full_county_name", "County")
        self.createNewField("primary_latitude", "Latitude")
        self.createNewField("primary_longitude", "Longitude")

        app.go()

# Instantiate object and start GUI
App = simpleGUI()
App.startApplication()
