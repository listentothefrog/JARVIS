host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

websites = ['www.youtube.com', "https://www.youtube.com"]
def start_focus(): 
    with open(host_path, "r+") as fileptr: 
        content = fileptr.read()
        for website in websites: 
            if website in content: 
                pass
            else: 
                fileptr.write(redirect+"      "+website+"\n")
    print("blocked all entertainment websites")            
                
def end_focus(): 
    print("end focus")
    with open(host_path, 'r+') as fileptr:
            content=fileptr.readlines()
            fileptr.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    fileptr.write(line)
  
            # removing hostnmes from host file
            fileptr.truncate()
    
    print("unblocked all entertainment websites")