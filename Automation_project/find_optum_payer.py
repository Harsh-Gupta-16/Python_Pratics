check_file = open(r'C:\Users\Harsh.x.Gupta\Documents\Automation\optum\check.txt','r')
All_check =  open(r'C:\Users\Harsh.x.Gupta\Documents\Automation\optum\optum_p.txt','r')
for i in check_file.readlines():
    chec = i.strip()
    for line in All_check.readlines():
        if chec in line:
            print(line.strip)
            