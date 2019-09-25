from sys import exit
import textwrap
import xlsxwriter
import os

class ToExcel(object):
    def __init__(self):
        self.row_label = None
        self.row_length = None
        self.row_data = []
        self.column_length = None
        self.column_data = None
        self.file_name = None
        self.spacer = "~_.._"



    def intro(self):
        intro = """
        \n\t format:
        \n\t |__column1___ |__column2__|__column3__| ....
        \n\t | row1 data   | row1 data | row1 data | ....
        \n\t | row2 data   | row2 data | row2 data | ....
        \n\t | ....        | .....     | ......    | ....\n
        \n\t This project will ask for information to write to your excel file.
        \n\t The data it will ask for ( in order ):
        \n\t file_name:  the program will add the file extension for you.
        \n\t number of columns in table (max 20)
        \n\t name of columns or None-for no names
        \n\t the number of rows in the columns (max 50)
        \n\t the data for the rows (format: 1.1, 2.2, 3.3, 49.0 or: lost, found, misplaced, destroyed)\n        
        \n\t type help or ?? in prompt at any time to repeat this information

        """
        print(self.spacer * 8)
        print(textwrap.dedent(intro))
        print(self.spacer * 8)
    
    def write(self):
        array = self.row_data
        ### printing in terminal:
        if self.file_name == None:
            print("No file name given to create.")
            self.print_attribs()
        else:
            
            array = self.row_data
            workbook = xlsxwriter.Workbook(self.file_name) #name your file here
            worksheet = workbook.add_worksheet()
            row = 0
            col = 0
            if len(self.column_data) > 0:
                for item in self.column_data:
                    worksheet.write(row, col, item)
                    col += 1
                    
                    
            row = 1
            col = 0
            row_count = 0
            col_count = 0
            

            for item in self.row_data:
                count = 0
                for data in item:
                    worksheet.write(row + count, col, data)
                    count += 1
                col += 1
                
         
            
               
            print(f"file created under file name: {self.file_name}")
            Current_path = os.getcwd()
            print("file is currently saved in this directory: ", Current_path)
            workbook.close()
            

    def get_row_len(self):
        user_input = input("Number of rows =")
       
        if user_input in ['help', 'HELP', 'Help', '??']:
            self.intro()
            self.get_row_len()
        else:
            try:
                user_input = int(user_input)
            except:
                print("input for number of rows must be a whole number integer from 1-50.")
                self.get_row_len()

            if type(user_input) == int:
                if user_input > 50:
                    print("Maximum number or rows is exceeded, please limit to number of rows to  at or below 50")
                    self.get_row_len()
                elif user_input < 1:
                    print("minimum number of rows is 1.  Please enter a integer greater than or equal to 1.")
                    self.get_row_len()
                else:
                    print("storing row length as : ", user_input)
                    self.row_length = user_input
                    count = self.column_length
                    self.get_row_data(count)
            else:
                print("input for number of rows must be a whole number integer from 1-50.")
                self.get_row_len()
      
    def get_row_data(self, count):
        if len(self.column_data) > 0:
            index = self.column_length - count
            name = self.column_data[index]
            print(index)
        else:
            name = self.column_length - count + 1
            
        

        data = input(f"please enter row data for column {name}:")
        if data in ['help', 'HELP', 'Help', '??']:
            self.intro()
            self.get_row_data(count)
        else:
            try:
                data = str(data)
            except:
                print("this data is converted into strings, data input was not compatible")
                self.get_row_data(count)
        #data = data.split(' ')
        # for class:
        data = data.split(';')
        # clean out trailing or extra whitespace:
        new_data = []
        for item in data:
            if item in ["", " ", "  ", "   "]:
                pass
            else:
                new_data.append(item)
        data = new_data

        if len(data) != self.row_length:
            print("data items entered: ", len(data))
            print("data = ", data)
            print("row length = ", self.row_length)
            print("data items entered is not equal to number of rows.")
            question = "restart?   Enter 'row' to enter new row length, 'data' to re-enter data:"
            user_answer = input(question)
            if user_answer in ["row", "ROW", "Row"]:
                self.get_row_len()
            elif user_answer in ["data", "DATA", "Data"]:
                self.get_row_data(count)
            elif user_answer in ['help', 'HELP', 'Help', '??']:
                self.intro()
                self.get_row_data(count)
            elif user_answer in ['quit', 'exit', 'EXIT', 'QUIT']:
                exit()
        else:
           
            count = count - 1
            if count <= 0:
                self.row_data.append(data)
                print(self.row_data)
                print(self.spacer * 5)
                print("row data saved as:")
                for item in self.row_data:
                    print(item)
                print(self.spacer * 5)
                self.print_attribs()
            else:
                self.row_data.append(data)
                print(self.row_data)
                self.get_row_data(count)

            

    def get_column_len(self):
        user_input = input("Number of columns =")
       
        if user_input in ['help', 'HELP', 'Help', '??']:
            self.intro()
            self.get_column_len()
        else:
            try:
                user_input = int(user_input)
            except:
                print("input for number of columns must be a whole number integer from 1-20.")
                self.get_column_len()

            if type(user_input) == int:
                if user_input > 20:
                    print("Maximum number or columns is exceeded, please limit to number of rows to  at or below 20")
                    self.get_column_len()
                elif user_input < 1:
                    print("minimum number of columns is 1.  Please enter a integer greater than or equal to 1.")
                    self.get_column_len()
                else:
                    print("storing column length as : ", user_input)
                    self.column_length = user_input
                    self.name_columns()
                    
            else:
                print("input for number of rows must be a whole number integer from 1-50.")
                self.get_column_len()


    def name_columns(self):
        print(self.spacer * 8)
        print("If column title is to be left blank:  Type Null for the data input for that column.")
        print("example:  toads frogs mudpuppies Null total")
        print("If you do not wish to name any columns with this feature, type None in prompt.")
        print(self.spacer * 8)
        data = input("please enter column data/names:")
        if data in ['help', 'HELP', 'Help', '??']:
            self.intro()
            self.name_columns()
        elif data in ['none', 'NONE', 'None']:
            # column data will be empty, with write() check for empty list here and pass on entering this data.
            self.column_data = []
            self.get_column_len()
        else:
            try:
                data = str(data)
            except:
                print("this data is converted into strings, data input was not compatible")
                self.name_columns()
        data = data.split(' ')
        # clean out trailing or extra whitespace:
        new_data = []
        for item in data:
            if item in ["", " ", "  ", "   "]:
                pass
            else:
                new_data.append(item)
        data = new_data

        if len(data) != 0 and len(data) != self.column_length:
            print("data items entered: ", len(data))
            print("data = ", data)
            print("row length = ", self.row_length)
            print("data items entered is not equal to number of columns.")
            question = "restart?   Enter 'col' to enter new column length, 'data' to re-enter data:"
            print(self.spacer * 10)
            user_answer = input(question)
            if user_answer in ["col", "COL", "Col"]:
                self.get_column_len()
            elif user_answer in ["data", "DATA", "Data"]:
                self.name_columns()
            elif user_answer in ['help', 'HELP', 'Help', '??']:
                self.intro()
                self.name_columns()
            elif user_answer in ['quit', 'exit', 'EXIT', 'QUIT']:
                exit()
            else:
                print("Invalid input, please enter column names:")
                self.name_columns()
        else:
            print("column name/data is entered as: ", data)
            self.column_data = data
            self.get_row_len()
            

    def get_file_name(self, final=None):
        # final is the prompt at the completion if a file_name was not given,
        # but user proceeded anyways.
        if final == None:
            if self.file_name == None:
                prompt = input("Type the name for your excel file to be saved as:")
                if type(prompt) == str:
                    if prompt.endswith('.xlsx'):
                        self.file_name = prompt
                        self.get_column_len()
                    else:
                        self.file_name = prompt + '.xlsx'
                        print(self.file_name)
                        self.get_column_len()
                else:
                    print("Invalid file name.")
                    prompt = input("type 'C' to continue without a file name, or type file name to continue:")
                    if prompt == 'C':
                        self.get_column_len()
                    else:
                        self.get_file_name()
            else: 
                print(f"file name already exists in this instance as: {self.file_name}")
                self.print_attribs()
        else:
             if self.file_name == None:
                prompt = input("Type the name for your excel file to be saved as:")
                if type(prompt) == str:
                    if prompt.endswith('.xlsx'):
                        self.file_name = prompt
                        self.get_column_len()
                    else:
                        self.file_name = prompt + '.xlsx'
                        print(self.file_name)
                        self.get_column_len()
             else: 
                print(f"file name already exists in this instance as: {self.file_name}")
                self.print_attribs()


    def start(self):
        self.get_file_name()


    def print_attribs(self):
        
        print("\nThe stored data is:")
        print(self.spacer * 10)
        i = 0
        all_attribs = vars(self)
        for key in all_attribs:
            value = str(all_attribs.get(key))
            arrow = " ---->  "
            message = "\t" + key + arrow + value 
            print(message)
        print(self.spacer * 10)
        if self.file_name == None:
            prompt = input("NO file name was given, data is not saved in an excel file. Do to do that now?  (Y)es--let's save this or (N)o--exit:")
            if prompt == 'Y':
                self.get_file_name(final="yes")
            else:
                print("Thank you for using this module.  Good day.")
                exit()
        else:
            self.write()
                
        
        
                


def test1():
    print("--- TEST 1 : print attributes of toExcel ---\n")
    mymod = ToExcel()
    mymod.print_attribs()
    print("\n---            END TEST 1              ---\n")
    

def test2():
    print("--- TEST 2 : test attributes are setting properly ---")
    
    mymod = ToExcel()
    #  starts with get_column_len()
    #  each user_input function is dependant on the next 
    mymod.get_column_len()
   

    mymod.print_attribs()

    print("\n--               END TEST 2                    ---\n")

def test3():
    print("--- TEST 3 : test naming the file, or No file) ---")
    mymod = ToExcel()
    mymod.get_file_name()
    print("---                END TEST 3                      ---")

def test4():
    print("--- TEST 4 :  write data to file, run program ---")
    mymod = ToExcel()
    mymod.start()
    print("---                  END TEST 4               ---")

test4()


