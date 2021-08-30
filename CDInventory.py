#------------------------------------------#
# Title: CDInventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# JMagat, 2021-Aug-29, modified to add code to complete assignment_08
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        None.

    """
    # TODOne Add Code to the CD class

 
    # -- Constructor -- #
    def __init__(self, cd_id, cd_title, cd_artist):
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist
        
    @property
    def cd_id(self):
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self, new_cd_id):
        self.__cd_id = new_cd_id
    
    @property
    def cd_title(self):
        return self.__cd_title


    @cd_title.setter
    def cd_title(self, new_cd_title):
        self.__cd_title = new_cd_title
            
    @property
    def cd_artist(self):
        return self.__cd_artist


    @cd_artist.setter
    def cd_artist(self, new_cd_artist):
        self.__cd_artist = new_cd_artist

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # TODOne Add code to process data from a file
    @staticmethod
    def load_inventory(file_name, lst_Inventory):
        """Function to load inventory from a text file

        Reads the data from file identified by file_name into a 2D table

        Args:
            file_name (string): name of file used to read the data from
            lst_Inventory: 2D data structure holding data

        Returns:
            None.
        
        Raises:
            FileNotFoundError
        """
        try:
            with open(file_name, 'r') as objFile:
                lst_Inventory.clear()
                for line in objFile:
                    data = line.strip().split(',')
                    addCD = CD(int(data[0]), data[1], data[2])
                    lst_Inventory.append(addCD)
        except FileNotFoundError:
            print('File not found: ', file_name)

 
    
    # TODOne Add code to process data to a file
   
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
      
        """Function to save current CD Inventory list into text file 
        
        Args:
            file_name (string): name of file to write data to
            lst_Inventory (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """        
        try:
            with open(file_name, 'w') as objFile:
                for cd in lst_Inventory:
                    objFile.write("{},{},{}\n".format(cd.cd_id, cd.cd_title, cd.cd_artist))
        except FileNotFoundError:
            print('File not found: ', file_name)
   
 
# -- PRESENTATION (Input/Output) -- #
class IO:
    """Processes input and outputs from user and menu ptions
    
    properties:
        none
        
    methods:
        print_menu(): -> None
        menu_choice(): -> choice
        show_inventory(table): -> None
        get_cd_data(): -> ID, title, artist
        add_inventory(strID, strTitle, strArtist, lst_Inventory): -> Adds objects to a list
    """

    # TODOne add docstring
    # -- Fields -- #    
    # -- Constructor -- #
    # -- Attributes -- #
    # -- Properties -- #
    
    # TODOne add code to show menu to user
    
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] Exit\n')

    
    # TODO add code to captures user's choice
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice


    # TODOne add code to display the current data on screen
    @staticmethod
    def show_inventory(lst_Inventory):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for CD in lst_Inventory:
            print('{}\t{} (by: {})'.format(CD.cd_id, CD.cd_title, CD.cd_artist))
        print('======================================')


    # TODOne add code to get CD data from user
    @staticmethod
    def get_cd_data():

        """Function to collect CD Data from the user: CD ID, Album, Artist

        Args:
            None.

        Returns:
            ID (integer): this is the CD ID entered by the user
            title (string): this is the CD's title
            artist (string): this is the Artist of the CD      
        
        Raises:
            ValueError: When value entered is not a number

        """      
        while True:
            try:
                ID = int(input('Enter ID: ').strip())
                break
            except ValueError:
                print('That is not valid CD ID! Please enter an integer')
        title = input('What is the CD\'s title? ').strip()
        artist = input('What is the Artist\'s name? ').strip()
        return ID, title, artist

                
    @staticmethod
    def add_inventory(strID, strTitle, strArtist, lst_Inventory):
        """Function to add a new entry to the inventory

        Args:
            strID (int): this is the CD ID entered by the user
            strTitle (string): this is the CD's title
            strArtist (string): this is the Artist of the CD
            lst_Inventory: 2D data structure holding data            
   
        Returns:
            None.
        """
        try:
            intID = int(strID)
            addCD = CD(intID, strTitle, strArtist)
            lst_Inventory.append(addCD)
        except ValueError:
            print('That is not valid CD ID! Please enter an integer')


# -- Main Body of Script -- #
# TODO Add Code to the main body
# DONE: Load data from file into a list of CD objects on script start
# 1. When program starts, read in the currently saved Inventory
FileIO.load_inventory(strFileName, lstOfCDObjects)

# DONE: Display menu to user
    
# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    
    
    # DONE: let user exit program
    # 3.1 process exit first
    if strChoice == 'x':
        break

    
    # DONE: let user load inventory from file
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('Type \'yes\' to continue and reload from file. Otherwise reload will be canceled:  ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.load_inventory(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.  

        
    # DONE: let user add data to the inventory
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        intID, strTitle, strArtist = IO.get_cd_data()

        # 3.3.2 Add item to the table
        IO.add_inventory(intID, strTitle, strArtist, lstOfCDObjects)
        IO.show_inventory(lstOfCDObjects)

        continue  # start loop back at top.   
   
    
    # DONE: let user save inventory to file
    # 3.4 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            # TODOne move processing code into function
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.   
    
    
    # DONE: show user current inventory
    # 3.5 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
        
    # 3.6 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')
        


