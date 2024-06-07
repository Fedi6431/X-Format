import subprocess
from colorama import init, Fore as cc
import os

clear = os.system('cls')
dr = DR = r = R = cc.LIGHTRED_EX
init()

dr = DR = r = R = cc.LIGHTRED_EX
def Xformat():
    while True:
        clear = os.system('cls')

        clear

        banner = f''' 
{r}▒██   ██▒          █████▒▒█████   ██▀███   ███▄ ▄███▓ ▄▄▄     ▄▄▄█████▓
{r}▒▒ █ █ ▒░        ▓██   ▒▒██▒  ██▒▓██ ▒ ██▒▓██▒▀█▀ ██▒▒████▄   ▓  ██▒ ▓▒
{r}░░  █   ░        ▒████ ░▒██░  ██▒▓██ ░▄█ ▒▓██    ▓██░▒██  ▀█▄ ▒ ▓██░ ▒░
{r} ░ █ █ ▒         ░▓█▒  ░▒██   ██░▒██▀▀█▄  ▒██    ▒██ ░██▄▄▄▄██░ ▓██▓ ░ 
{r}▒██▒ ▒██▒ ██▓    ░▒█░   ░ ████▓▒░░██▓ ▒██▒▒██▒   ░██▒ ▓█   ▓██▒ ▒██▒ ░ 
{r}▒▒ ░ ░▓ ░ ▒▓▒     ▒ ░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒ ░░   
{r}░░   ░▒ ░ ░▒      ░       ░ ▒ ▒░   ░▒ ░ ▒░░  ░      ░  ▒   ▒▒ ░   ░    
{r} ░    ░   ░       ░ ░   ░ ░ ░ ▒    ░░   ░ ░      ░     ░   ▒    ░      
{r} ░    ░    ░                ░ ░     ░            ░         ░  ░        
{r}           ░              
{r}Type "Help" to see all commands
'''

        print(f"{banner}")
        Com = input("-->")

        if Com == 'help':
            Helplist = '''
Help            see all commands
Format          Format your computer
FormatUsb       Format your USB / Hard disk
Version         Show version
Info            Show infos 
'''
            print(f"{Helplist}")
            input("Press enter to get back to the main screen")

        if Com == 'info':
            Infoss = '''
|-------------------------------------|
|Author: Fedi6431                     |
|-------------------------------------|
|Github: https://Github.com/Fedi6431  |
|-------------------------------------|
'''
            print(f"{Infoss}")
            input("Press enter to get back to the main screen")

        if Com == 'version':
            Ver1 = '''
|-------------------------|
|   Verision   |   Type   |
|--------------|----------|
|   1.0        |   Beta   |
|-------------------------|
'''
            print(f"{Ver1}")
            input("Press enter to get back to the main screen")

        if Com == 'formatsb':
            selectFormat = '''
|---------|-----------------------------------------------------Function--------------------------------------------------------|
|  FAT32  | Doen't carry files larger than 4GB - Readable by as many devices as possible                                        |
|  NTFS   | Right choice for formatting internal and external hard drives - Can store files up to 16TB in size                  |
|  exFAT  | As light as FAT32, but without the limitations of the latter and without the "extra" features that distinguish NTFS |
|---------|---------------------------------------------------------------------------------------------------------------------|
'''
            print(f"{selectFormat}")

            def format_usb_drive(usb_path, file_system='FAT32'):
                import os 
                try:
                    format_command = os.path.join(os.getenv('SystemRoot'), 'System32', 'format.com')
                    subprocess.run([format_command, usb_path, '/FS:' + file_system, '/Q', '/X'], check=True)
                    print(f'USB / Hard disk {usb_path} successfully formatted.')
                except subprocess.CalledProcessError as e:
                    print(f'Error while formatting the USB / Hard disk: {e}')

            file_system = input('Type the format of the USB / Hard disk that you want: ')

            
            usb_path = input('Type USB / Hard disk address (Eg. E: D:): ')

            format_usb_drive(usb_path, file_system)
            print(f"\n")
            input("Press enter to get back to the main screen")

        if Com == 'format':
            format2 = '''
|------------------------------|
|1 C:\\                        |
|------------------------------|
|2 C:\\Users\\                 |
|------------------------------|
'''

            print(f"{format2}")

            ask1 = input("--> ")
            
            if ask1 == '1':
                def format_system_drive1(file_system='NTFS'):
                    try:
                        
                        format_command = os.path.join(os.getenv('SystemRoot'), 'System32', 'format.com')

                        subprocess.run([format_command, 'C:', '/FS:' + file_system, '/Q', '/X'], check=True)

                        print('Drive C: Successfully formatted. The operating system has been removed.')
                    except subprocess.CalledProcessError as e:
                        print(f'Error formatting drive C: {e}')

                
                confirmation = input('Are you sure you want to format the C: drive? (Yes for continue the operation): ')
                if confirmation.upper() == 'yes':
                    format_system_drive1()

                if confirmation.upper() == 'Yes':
                    format_system_drive1()
                else:
                    print('Operation canceled')
                input("Press enter to get back to the main screen")

            if ask1 == '2':
                    def format_system_drive2(file_system='NTFS'):
                        try:
                            
                            format_command = os.path.join(os.getenv('SystemRoot'), 'System32', 'format.com')

                            subprocess.run([format_command, 'C:\\Users', '/FS:' + file_system, '/Q', '/X'], check=True)

                            print('Drive C:\\Users Successfully formatted, the operating system has been removed.')

                        except subprocess.CalledProcessError as e:
                            print(f'Error formatting drive C: {e}')

                    
                    confirmation = input('Are you sure you want to format the C: drive? (Yes for continue the operation): ')
                    if confirmation.upper() == 'yes':
                        format_system_drive2()

                    if confirmation.upper() == 'Yes':
                        format_system_drive2()
                    else:
                        print('Operation canceled')
                    input("Press enter to get back to the main screen")

        if Com == 'Help':
            Helplist = '''
Help            see all commands
Format          Format your computer
FormatUsb       Format your USB / Hard disk
Version         Show version
Info            Show infos 
'''
            print(f"{Helplist}")
            input("Press enter to get back to the main screen")

        if Com == 'Info':
            Infoss = '''
|-------------------------------------|
|Author: Fedi6431                     |
|-------------------------------------|
|Github: https://Github.com/Fedi6431  |
|-------------------------------------|
'''
            print(f"{Infoss}")
            input("Press enter to get back to the main screen")

        if Com == 'Version':
            Ver1 = '''
|-------------------------|
|   Verision   |   Type   |
|--------------|----------|
|   1.0        |   Beta   |
|-------------------------|
'''
            print(f"{Ver1}")
            input("Press enter to get back to the main screen")

        if Com == 'Formatusb':
            selectFormat = '''
|---------|-----------------------------------------------------Function--------------------------------------------------------|
|  FAT32  | Doen't carry files larger than 4GB - Readable by as many devices as possible                                        |
|  NTFS   | Right choice for formatting internal and external hard drives - Can store files up to 16TB in size                  |
|  exFAT  | As light as FAT32, but without the limitations of the latter and without the "extra" features that distinguish NTFS |
|---------|---------------------------------------------------------------------------------------------------------------------|
'''
            print(f"{selectFormat}")

            def format_usb_drive(usb_path, file_system='FAT32'):
                import os 
                try:
                    format_command = os.path.join(os.getenv('SystemRoot'), 'System32', 'format.com')
                    subprocess.run([format_command, usb_path, '/FS:' + file_system, '/Q', '/X'], check=True)
                    print(f'USB / Hard disk {usb_path} successfully formatted.')
                except subprocess.CalledProcessError as e:
                    print(f'Error while formatting the USB / Hard disk: {e}')

            file_system = input('Type the format of the USB / Hard disk that you want: ')

            
            usb_path = input('Type USB / Hard disk address (Eg. E: D:): ')

            format_usb_drive(usb_path, file_system)
            print(f"\n")
            input("Press enter to get back to the main screen")


        if Com == 'FormatUsb':
            selectFormat = '''
|---------|-----------------------------------------------------Function--------------------------------------------------------|
|  FAT32  | Doen't carry files larger than 4GB - Readable by as many devices as possible                                        |
|  NTFS   | Right choice for formatting internal and external hard drives - Can store files up to 16TB in size                  |
|  exFAT  | As light as FAT32, but without the limitations of the latter and without the "extra" features that distinguish NTFS |
|---------|---------------------------------------------------------------------------------------------------------------------|
'''
            print(f"{selectFormat}")

            def format_usb_drive(usb_path, file_system='FAT32'):
                import os 
                try:
                    format_command = os.path.join(os.getenv('SystemRoot'), 'System32', 'format.com')
                    subprocess.run([format_command, usb_path, '/FS:' + file_system, '/Q', '/X'], check=True)
                    print(f'USB / Hard disk {usb_path} successfully formatted.')
                except subprocess.CalledProcessError as e:
                    print(f'Error while formatting the USB / Hard disk: {e}')

            file_system = input('Type the format of the USB / Hard disk that you want: ')

            
            usb_path = input('Type USB / Hard disk address (Eg. E: D:): ')

            format_usb_drive(usb_path, file_system)
            print(f"\n")
            input("Press enter to get back to the main screen")

        if Com == 'formatusb':
            selectFormat = '''
|---------|-----------------------------------------------------Function--------------------------------------------------------|
|  FAT32  | Doen't carry files larger than 4GB - Readable by as many devices as possible                                        |
|  NTFS   | Right choice for formatting internal and external hard drives - Can store files up to 16TB in size                  |
|  exFAT  | As light as FAT32, but without the limitations of the latter and without the "extra" features that distinguish NTFS |
|---------|---------------------------------------------------------------------------------------------------------------------|
'''
            print(f"{selectFormat}")

            def format_usb_drive(usb_path, file_system='FAT32'):
                import os 
                try:
                    format_command = os.path.join(os.getenv('SystemRoot'), 'System32', 'format.com')
                    subprocess.run([format_command, usb_path, '/FS:' + file_system, '/Q', '/X'], check=True)
                    print(f'USB / Hard disk {usb_path} successfully formatted.')
                except subprocess.CalledProcessError as e:
                    print(f'Error while formatting the USB / Hard disk: {e}')

            file_system = input('Type the format of the USB / Hard disk that you want: ')

            
            usb_path = input('Type USB / Hard disk address (Eg. E: D:): ')

            format_usb_drive(usb_path, file_system)
            print(f"\n")
            input("Press enter to get back to the main screen")



        if Com == 'Format':
            format2 = '''
|------------------------------|
|1 C:\\                        |
|------------------------------|
|2 C:\\Users\\                 |
|------------------------------|
'''

            print(f"{format2}")

            ask1 = input("--> ")
            
            if ask1 == '1':
                def format_system_drive1(file_system='NTFS'):
                    try:
                        
                        format_command = os.path.join(os.getenv('SystemRoot'), 'System32', 'format.com')

                        subprocess.run([format_command, 'C:', '/FS:' + file_system, '/Q', '/X'], check=True)

                        print('Drive C: Successfully formatted. The operating system has been removed.')
                    except subprocess.CalledProcessError as e:
                        print(f'Error formatting drive C: {e}')

                
                confirmation = input('Are you sure you want to format the C: drive? (Yes for continue the operation): ')
                if confirmation.upper() == 'yes':
                    format_system_drive1()

                if confirmation.upper() == 'Yes':
                    format_system_drive1()
                else:
                    print('Operation canceled')
                input("Press enter to get back to the main screen")

            if ask1 == '2':
                    def format_system_drive2(file_system='NTFS'):
                        try:
                            
                            format_command = os.path.join(os.getenv('SystemRoot'), 'System32', 'format.com')

                            subprocess.run([format_command, 'C:\\Users', '/FS:' + file_system, '/Q', '/X'], check=True)

                            print('Drive C:\\Users Successfully formatted, the operating system has been removed.')

                        except subprocess.CalledProcessError as e:
                            print(f'Error formatting drive C: {e}')

                    
                    confirmation = input('Are you sure you want to format the C: drive? (Yes for continue the operation): ')
                    if confirmation.upper() == 'yes':
                        format_system_drive2()

                    if confirmation.upper() == 'Yes':
                        format_system_drive2()
                    else:
                        print('Operation canceled')
                    input("Press enter to get back to the main screen")
Xformat()