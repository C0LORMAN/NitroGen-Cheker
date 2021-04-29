import os
import random
import string
import time
import ctypes

try: 
    from discord_webhook import DiscordWebhook 
except ImportError: 
    input(f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nPress enter to exit") 
    exit() 
try: 
    import requests 
except ImportError: 
    input(f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nPress enter to exit")
    exit() 


class NitroGen: 
    def __init__(self): 
        self.fileName = "Nitro Codes.txt" 

    def main(self): 
        os.system('cls' if os.name == 'nt' else 'clear') 
        if os.name == "nt": 
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW("Nitro Generator and Checker - Créer par Inc.#1968") 
        else: 
            print(f'\33]0;Nitro Generator and Checker - Créer par Inc.#1968\a', end='', flush=True) 

        print(""" Créer par Inc.#1968""") 
        time.sleep(2) 
        self.slowType("Black shop", .02) 
        time.sleep(1) # Wait a little more
        self.slowType("\nCombien veux-tu de code nitro gen & check: ", .02, newLine = False) # Print the first question

        num = int(input('')) # Ask the user for the amount of codes

        self.slowType("\nDo you wish to use a discord webhook? \nIf so type it here or press enter to ignore: ", .02, newLine = False)
        url = input('') # Get the awnser
        webhook = url if url != "" else None 
        # print() 

        valid = [] 
        invalid = 0 

        for i in range(num): # Loop over the amount of codes to check
            try: # Catch any errors that may happen
                code = "".join(random.choices( # Generate the id for the gift
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                ))
                url = f"https://discord.gift/{code}" # Generate the url

                result = self.quickChecker(url, webhook) # Check the codes

                if result: # If the code was valid
                    valid.append(url) # Add that code to the list of found codes
                else: # If the code was not valid
                    invalid += 1 # Increase the invalid counter by one
            except Exception as e: # If the request fails
                print(f" Error | {url} ") # Tell the user an error occurred

            if os.name == "nt": # If the system is windows
                ctypes.windll.kernel32.SetConsoleTitleW(f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Créer par Inc.#1968") 
                print("")
            else: # If it is a unix system
                print(f'\33]0;Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Créer par Inc.#1968\a', end='', flush=True) 

        print(f"""
Results:
 Valid: {len(valid)}
 Invalid: {invalid}
 Valid Codes: {', '.join(valid )}""") 

        input("\nThe end! Press Enter 5 times to close the program.") 
        [input(i) for i in range(4,0,-1)] 


    def slowType(self, text, speed, newLine = True): 
        for i in text: # Loop over the message
            print(i, end = "", flush = True) 
            time.sleep(speed) 
        if newLine: 
            print() 

    def generator(self, amount): 
        with open(self.fileName, "w", encoding="utf-8") as file: 
            print("Wait, Generating for you") 

            start = time.time() 

            for i in range(amount): 
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k = 16
                )) 

                file.write(f"https://discord.gift/{code}\n") 

            print(f"Genned {amount} codes | Time taken: {round(time.time() - start, 5)}s\n") #

    def fileChecker(self, notify = None): 
        valid = [] 
        invalid = 0 
        with open(self.fileName, "r", encoding="utf-8") as file: 
            for line in file.readlines(): 
                nitro = line.strip("\n") 

             
                url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

                response = requests.get(url) 

                if response.status_code == 200: 
                    print(f" Valid | {nitro} ") 
                    valid.append(nitro) 

                    if notify is not None: 
                        DiscordWebhook( 
                            url = notify,
                            content = f"Valid Nito Code detected! @everyone \n{nitro}"
                        ).execute()
                    else:  
                        break 

                else: # If the responce got ignored or is invalid ( such as a 404 or 405 )
                    print(f" Invalid | {nitro} ") 
                    invalid += 1 
        return {"valid" : valid, "invalid" : invalid} 

    def quickChecker(self, nitro, notify = None): 
        # Generate the request url
        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url) 

        if response.status_code == 200: 
            print(f" Valid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n") 
            with open("Nitro Codes.txt", "w") as file: 
                file.write(nitro) 

            if notify is not None: 
                DiscordWebhook( 
                    url = notify,
                    content = f"Valid Nito Code detected! @everyone \n{nitro}"
                ).execute()

            return True 

        else: 
            print(f" Invalid | {nitro} ", flush=True, end="" if os.name == 'nt' else "\n") 
            return False 

if __name__ == '__main__':
    Gen = NitroGen() # Create the nitro generator object
    Gen.main() 
