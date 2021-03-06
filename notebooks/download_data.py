import os, glob
from zipfile import ZipFile  #for opening the zip file and download the data
import requests, shutil
import tarfile


def data_structures(folder=""):
    """ Download and extract the data for the structures of the planets"""
    
    os.chdir(folder)
    
    all_files = {'Ini_No_DTcmb.zip',
            "Ini_No_DTcmb_moreFeCases.zip",
        "Ini_With_DTcmb_moreFeCases.zip",
        "Ini_With_DTcmb.zip"}

    url = "http://geodyn-chic.de/wp-content/uploads/2020/04/"

    # downloading the zip files
    for file in all_files:
        if not os.path.isfile(file):
            print("Downloading {} from {}".format(file, url))
            r = requests.get(url+file, allow_redirects=True)
            open(file, 'wb').write(r.content)
        else:
            print("{} already present.".format(file))

    # extracting the zip files
    for file in all_files:
        with ZipFile(file, 'r') as zip: 
            # printing all the contents of the zip file 
            # zip.printdir() 
            # extracting all the files 
            print('{}: Extracting all the files now...'.format(file)) 
            zip.extractall("./") 
            print('Done!')
            
    # removing the zip files
    #for file in all_files:
    #    os.remove(file)

    # merging the correct folders (to remove the additional _moreFecases)
    sources = ["Ini_No_DTcmb", "Ini_With_DTcmb"]
    for src in sources:
        # join the two summaries
        with open(src+'/summary_total.txt','wb') as wfd:
            for f in [src+'/summary.txt',src+'_moreFeCases/summary.txt']:
                with open(f,'rb') as fd:
                    shutil.copyfileobj(fd, wfd)
        # join the two data_IS.res
        with open(src+'/data_IS_total.res','wb') as wfd:
            for f in [src+'/data_IS.res',src+'_moreFeCases/data_IS.res']:
                with open(f,'rb') as fd:
                    shutil.copyfileobj(fd, wfd)
        os.remove(src+'/data_IS.res')
        os.remove(src+'_moreFeCases/data_IS.res')
        os.remove(src+'/summary.txt')
        os.remove(src+'_moreFeCases/summary.txt')
        # copying No_DTcmb_moreFecases in No_DTcmb
        src_files = os.listdir(src+"_moreFeCases")
        #print(src_files)
        print(src)
        for file_name in src_files:
            full_file_name = os.path.join(src+'_moreFeCases/', file_name)
            if os.path.isfile(full_file_name):
                print("copy ", file_name, " to ", src)
                shutil.copy(full_file_name, src)
        shutil.rmtree(src+"_moreFeCases")


# def data_qcmb(folder):
#     
#     qcmb_folder = "/Q_CMB/"
#     if not os.path.exists(folder+qcmb_folder):
#         os.makedirs(folder+qcmb_folder)
#     os.chdir(folder+qcmb_folder)
#     
#     url = "https://box.fu-berlin.de/s/ycDpD4DfKTcRDix/download"
#     all_files = ["Core_Heatflux_Hot_New_AllMasses_10Myr.tar"]
#     
#     #downloading the zip files
#     for filename in all_files:
#         if not os.path.isfile(filename):
#             print("Downloading {} from {}".format(filename, url))
#             r = requests.get(url+filename, allow_redirects=True)
#             if r.status_code == 200:
#             	with open(filename, 'wb') as f:
#             		f.write(r.content)
#             else:
#             	print("problem with download:", r.status_code)
#         else:
#             print("{} already present.".format(filename))
    
    
#     for filename in glob.glob("*.tar"):
#        print(filename)
#        my_tar = tarfile.open(filename)
#        my_tar.extractall('./') # specify which folder to extract to
#        my_tar.close()
#         with ZipFile(filename, 'r') as zip: 
#            print('{}: Extracting all the files now...'.format(filename)) 
#            zip.extractall("./") 
#            print('Done!')
#    print("Please extract the QCMB tar file manually")

def data_qcmb(folder):
    qcmb_folder = "/Q_CMB/"
    if not os.path.exists(folder+qcmb_folder):
        os.makedirs(folder+qcmb_folder)
    os.chdir(folder+qcmb_folder)


if __name__ == "__main__": 
    
    #data_structures("../data/")# download an extract the structures
    data_qcmb("./data/") # extract the qcmb data
    
    
    
    