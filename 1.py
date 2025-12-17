import random
import subprocess

# Generate an 8-digit random number
random_number = random.randint(10000000, 99999999)

# Write to eng.txt
with open('eng.txt', 'w') as file:
    file.write(str(random_number))

print(f"Random number written to eng.txt: {random_number}")
# Stage and commit the changes
subprocess.run(['git', 'add', '1.py', 'eng.txt'])
subprocess.run(['git', 'commit', '-m', 'Add random number generator and output file'])
subprocess.run(['git', 'push'])