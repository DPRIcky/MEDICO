import qrcode
import os
import win32com.client as win32

xlApp = win32.Dispatch('Excel.Application')
xlApp.Visible = True

path = 'C:/Users/PRAJJWAL/Downloads/VIT Downloads/ECE1030-Artificial Intelligence for Biomedical/Project'
file = 'Patient_data.csv'

dir_list = os.listdir(path)
print(dir_list)

with open(os.path.join(path, file), 'w') as fp:
    pass

dir_list = os.listdir(path)
print(dir_list)

data = "https://tinyurl.com/AI-in-BioMed-patientsdata"   #Data for which you want to make QR code
QRCodefile = "Patient_data_QR.png"      # File name of the QR code Image
QRimage = qrcode.make(data)             # Generating the QR code
QRimage.save(QRCodefile)                # Saving image into a file

