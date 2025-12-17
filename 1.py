import random
import subprocess
n=0
# Generate an 8-digit random number
random_number = random.randint(10000000, 99999999)
while n<10:
# Write to eng.txt
    file = open('eng.txt', 'w')
    file.write(str(random_number))
    file.close()
    # Stage and commit the changes
    subprocess.run(['git', 'add','1.py','eng.txt'])
    subprocess.run(['git', 'commit', '-m', 'Add random number generator and output file'])
    subprocess.run(['git', 'push'])
    n=n+1
