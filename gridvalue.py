import openpyxl

grid = input("enter the grid value")
wb = openpyxl.load_workbook('Grid.xlsx')
sheet = wb['Sheet1']
grid_value = str(sheet['{}'.format(grid[19:21])].value) + str(
    sheet['{}'.format(grid[24:26])].value) + str(sheet['{}'.format(grid[29:31])].value)
print(grid_value)