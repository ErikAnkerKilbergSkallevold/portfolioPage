from http.client import *
import os


path = r'C:/Users/ErikSAppData/Local/Packages/PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0/LocalCache/local-packages/Python39/site-packages/site-packages/'

def dtsync(request,file:str):
    with open(path + file, 'rb') as f:
        response = HTTPResponse(f.read(), content_type="application/liquid")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(path + file)
        return response