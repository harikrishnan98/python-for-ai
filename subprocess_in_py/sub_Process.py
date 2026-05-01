import subprocess


p1 = subprocess.run(
    "cat ./simple.txt | grep -n 6", capture_output=True, text=True, shell=True
)


if p1.returncode == 0:
    print(f"P1: Process: OUTPUT: {p1.stdout}")
else:
    print(f"Error: {p1.stderr}")
