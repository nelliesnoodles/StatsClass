import xlsxwriter
import re
import os


# from :  https://xlsxwriter.readthedocs.io/example_chart_line.html #
#chart1 = workbook.add_chart({'type': 'line'})
#chart1.add_series({
    #'name':       '=Sheet1!$B$1',
    #'categories': '=Sheet1!$A$2:$A$7',
    #'values':     '=Sheet1!$B$2:$B$7',
#})

class ToExcelLineChart(object):
    def  __init__(self):
        self.data = [[11, 22, 33], [1, 2, 3], [110, 110, 110]] #an array of data that will be plot points
        self.data_heading = ['time','order', 'frequency %'] # a list of headings
        self.name = "fake frequency chart"
        self.filename = None
        self.Alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M"]

    def write(self, test_filename=False, data_only=False):
        if self.filename == None:
            print("All non alphanumerics will be stripped from file name.")
            prompt = input("please name your file: ")
            filename = re.sub('[^0-9a-zA-Z]+', '', prompt)
            filename = filename + ".xlsx"
            self.filename = filename
            if test_filename==True:
                print(filename)
            #add info to excel file:
            workbook = xlsxwriter.Workbook(self.filename)
            worksheet = workbook.add_worksheet()
        if data_only:
            self.add_chart_write()
        else:
            # write headings to top row, A1
            col = 1
            row = 0
            i = 0
            for item in self.data_heading:
                item = self.data_heading[i]
                worksheet.write(row, col, item)
                i += 1
                col += 1
            row = 1
            col = 1
            start = 2

            for item in self.data:
                place = self.Alpha[col - 1] + str(start)
                worksheet.write_column(place, item)
                col += 1

                 
            valuelocation = '=Sheet1!$A$1:$A$'
            start = int(valuelocation[11])
            end = start + len(self.data[0]) - 1
            newlocation = valuelocation + str(end)
                            
            chart = workbook.add_chart({'type': 'line'})
            chart.add_series({'values': newlocation})
            worksheet.insert_chart('A7', chart)

               
            
            print(f"file created under file name: {self.filename}")
            Current_path = os.getcwd()
            print("file is currently saved in this directory: ", Current_path)
            workbook.close()
            


    def add_chart_write():
            row = 1
            col = 1
            for item in self.data:
                worksheet.write_column(row, col, item)
                col += 1
                
            # write headings to top row, A1
            col = 1
            row = 0
            i = 0
            for item in self.data_heading:
                item = self.data_heading[i]
                worksheet.write(row, col, item)
                i += 1
                col += 1
            
                
               
            print(f"file created under file name: {self.filename}")
            Current_path = os.getcwd()
            print("file is currently saved in this directory: ", Current_path)
            workbook.close()
            

  
def test1():
    chart = ToExcelLineChart()
    chart.write(test_filename=True)

def test2():
    #use default data to write to file
    chart = ToExcelLineChart()
    chart.write()

test2()







