import os
import win32com.client as win32

xl = win32.Dispatch('Excel.Application')
xl.Application.visible = False #change to True if you are desired to make Excel visible
wb = xl.Workbooks.Open("c:\\Billing_RL\\RL_Defaulter_Template.xlsm")
xl.Application.run("RL_Defaulter_Template.xlsm!Module1.DEFAULTER")
wb.Save()
wb.Close()
# try:
#     wb = xl.Workbooks.Open("c:\\Billing_RL\\Resource_Loading_Defaulter_Automation.xlsm")
#     xl.Application.run("Resource_Loading_Defaulter_Automation.xlsm!Module1.DEFAULTER")
#     wb.Save()
#     wb.Close()
# except Exception as ex:
#         template = "An exception of type {0} occurred. Arguments:\n{1!r}"
#         message = template.format(type(ex).__name__, ex.args)
#         print(message)
xl.Application.Quit()
del xl





# if os.path.exists('C:/Billing_RL/Macro/Resource_Loading_Defaulter_Automation.xlsm'):
#     excel_macro = win32com.client.Dispatch("Excel.Application")
#     excel_path = os.path.abspath('C:/Billing_RL/Macro/Resource_Loading_Defaulter_Automation.xlsm')
#     workbook = excel_macro.Workbooks.Open(Filename=excel_path, ReadOnly=1)
#     print(workbook)
#     excel_macro.Application.Run('C:/Billing_RL/Macro/Resource_Loading_Defaulter_Automation.xlsm!Module1.DEFAULTER')
#     workbook.Save()
#     workbook.close()
#     excel_macro.Application.Quit()
#     del excel_macro






# if os.path.exists('C:/Users/jz/Desktop/test.xlsm'):
#     excel_macro = win32com.client.DispatchEx("Excel.Application") # DispatchEx is required in the newest versions of Python.
#     excel_path = os.path.expanduser('C:/Users/jz/Desktop/test.xlsm')
#     workbook = excel_macro.Workbooks.Open(Filename = excel_path, ReadOnly =1)
#     excel_macro.Application.Run("test.xlsm!Module1.Macro1") # update Module1 with your module, Macro1 with your macro
#     workbook.Save()
#     excel_macro.Application.Quit()
#     del excel_macro