import urllib.request
import os
import re
import time

am = 0

# Main/core class.
class Main(object):
    # Function to download a file from its link.
    def Download(self, url, size):
        file_name = url.split('/')[-1]
        u = urllib.request.urlopen(url)
        f = open(file_name, 'wb')
        meta = u.info()
        file_size = str(u.getheader('Content-Length'))
        size = u.info()['Content-Length']
        size = float(size)
        # print("Downloading: %s Bytes: %s" % (file_name, file_size))
        print("Downloading: %s " % (file_name))

        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break
            file_size_dl += len(buffer)
            f.write(buffer)
            file_size = float(file_size)
            status = r"%10d - [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + ' ' + chr(8) * (len(status) + 1)
            print(status)
        f.close()
    # Returns true/false.
    def isUpdate(self):
        def Download(url):
            global update
            file_name = url.split('/')[-1]
            u = urllib.request.urlopen(url)
            f = open(file_name, 'wb')
            meta = u.info()
            # file_size = str(u.getheader('Content-Length'))
            try:
                size = u.info()['Content-Length']
                size = float(size)
            except:
                size = 000000000
            file_size = size
            file_name.replace("%20", " ")
            # print("Downloading: %s Bytes: %s" % (file_name, file_size))
            print("Downloading latest file from GitHub...")
            file_size_dl = 0
            block_sz = 8192
            while True:
                buffer = u.read(block_sz)
                if not buffer:
                    break
                file_size_dl += len(buffer)
                f.write(buffer)
                try:
                    status = r"%10d - [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
                    status = status + ' ' + "▮" * (len(status) + 1)
                    print(status)
                except:
                    print("Downloading...", file_size_dl * 100. / file_size)
            f.close()
            print("Downloaded successfully!")
        Download("https://raw.githubusercontent.com/DreaMMachine69/NEA12/master/Weather%20GUI%20NEA.py")
        try:
            file2 = open("Weather.py", "r+")
        except:
            pass
        lines2 = file2.readlines()
        file3 = open("Weather%20GUI%20NEA.py", "r+")
        lines3 = file3.readlines()
        v1 = lines2[0]
        v2 = lines3[0]
        ver1 = float(re.search(r'\d+', v1).group())
        ver2 = float(re.search(r'\d+', v2).group())
        if ver2 > ver1:
            file2.close()
            file3.close()
            file4 = open("Versions.txt", "r+")
            ver1 = str(ver1)
            ver2 = str(ver2)
            file4.write(ver1)
            file4.write("\n")
            file4.write(ver2)
            file4.close()
            return(True)
        else:
            file4 = open("Versions.txt", "r+")
            ver1 = str(ver1)
            ver2 = str(ver2)
            file4.write(ver1)
            file4.write("\n")
            file4.write(ver2)
            file2.close()
            file3.close()
            file4.close()
            return(False)
        
    def Update(self):
        def Download(url):
            print("FUNC2")
            file_name = url.split('/')[-1]
            u = urllib.request.urlopen(url)
            f = open(file_name, 'wb')
            meta = u.info()
            # file_size = str(u.getheader('Content-Length'))
            try:
                size = u.info()['Content-Length']
                size = float(size)
            except:
                size = 000000000
            file_size = size
            file_name.replace("%20", " ")
            # print("Downloading: %s Bytes: %s" % (file_name, file_size))
            print("Downloading latest file from GitHub...")
            file_size_dl = 0
            block_sz = 8192
            while True:
                buffer = u.read(block_sz)
                if not buffer:
                    break
                file_size_dl += len(buffer)
                f.write(buffer)
                try:
                    status = r"%10d - [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
                    status = status + ' ' + "▮" * (len(status) + 1)
                    print(status)
                except:
                    print("Downloading...", file_size_dl * 100. / file_size)
            f.close()
            print("Downloaded successfully!")
        Download("https://raw.githubusercontent.com/DreaMMachine69/NEA12/master/Weather%20GUI%20NEA.py")
        try:
            os.rename("Weather%20GUI%20NEA.py", "Up Weather GUI NEA.py")
        except:
            print("There is currently an update file saved.")
            print("Continuing with the update will remove the previous update file.")
            con = input("Would you like to continue? [Y/N]").upper()
            if con == "Y":
                try:
                    os.remove("Weather%20GUI%20NEA.py")
                    print("File removed.")
                except:
                    try:
                        os.remove("Up Weather GUI NEA.py")
                        print("File removed.")
                    except:
                        print("File was not removed...")
                        exit()
            else:
                exit()
        try:
            file2 = open("Weather GUI NEA.py", "r+")
        except:
            file2 = open("Old Weather GUI NEA.py", "r+")
        lines2 = file2.readlines()
        file3 = open("Up Weather GUI NEA.py", "r+")
        lines3 = file3.readlines()
        v1 = lines2[0]
        v2 = lines3[0]
        ver1 = float(re.search(r'\d+', v1).group())
        ver2 = float(re.search(r'\d+', v2).group())
        if ver2 > ver1:
            print("")
            print("Update found...")
            print("Current version:", ver1)
            print("Latest version:", ver2)
            up = input("Update? [Y/N] ").upper()
            if up == "Y":
                try:
                    for filename in os.listdir("."):
                            file2.close()
                            file3.close()
                            try:
                                os.rename("Weather GUI NEA.py", "Old Weather GUI NEA.py")
                            except:
                                pass
                            os.rename("Up Weather GUI NEA.py", "Weather GUI NEA.py")
                            print("")
                            print("Updated successfully!")
                            done = 1
                # If any other error occurs.
                except Exception as e:
                    try:
                        if done == 0:
                            if e.__class__.__name__ == "PermissionError":
                                print("Could not rename the file (no permission, perhaps the file is open?")
                            elif e.__class__.__name__ == "FileExistsError":
                                print("Could not rename the file (perhaps the file already exists.")
                            else:
                                print("Could not rename the file. [" + e.__class__.__name__ + "]")
                    except:
                        pass
            else:
                try:
                    print("Deleting update file...")
                    file2.close()
                    file3.close()
                    os.remove("Up Weather GUI NEA.py")
                except:
                    print("Error deleting update file.")
        elif ver1 > ver2:
            print("")
            print("You are ahead of the online file...")
            print("If this version wasn't uploaded, run \'Send Update.sh\'")
            print("Current version:", ver1)
            print("Latest version:", ver2)
        else:
            print("")
            print("No update was found...")
            print("Current version:", ver1)
            print("Latest version:", ver2)
            try:
                file2.close()
                file3.close()
                os.remove("Up Weather GUI NEA.py")
            except:
                pass
    def FullUpdate(self):
        print("If an update is found it will delete all the current files.")
        print("Please back-up files if neccessary.")
        con = input("Would you still like to continue with the full update? [Y/N] ").upper()
        if con == "Y":
            def Download(url):
                print("FUNC3")
                file_name = url.split('/')[-1]
                u = urllib.request.urlopen(url)
                f = open(file_name, 'wb')
                meta = u.info()
                # file_size = str(u.getheader('Content-Length'))
                size = u.info()['Content-Length']
                size = float(size)
                file_size = size
                file_name.replace("%20", " ")
                # print("Downloading: %s Bytes: %s" % (file_name, file_size))
                print("Downloading latest files from GitHub...")
                
                file_size_dl = 0
                block_sz = 8192
                while True:
                    buffer = u.read(block_sz)
                    if not buffer:
                        break
                    file_size_dl += len(buffer)
                    f.write(buffer)
                    perc = file_size_dl * 100. / file_size
                    perc = str(perc)
                    am = 0
                    am += 1
                    am = str(am)
                    # 20 Files
                    print("Downloading... " + perc + "%" + " [" + am + "/20]")
                    am = int(am)
                f.close()
                print("Downloaded successfully!")
            Download("https://raw.githubusercontent.com/DreaMMachine69/NEA12/master/Updater.py")
        else:
            print("Program closing in 5 seconds...")
            time.sleep(5)
