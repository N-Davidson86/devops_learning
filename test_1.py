import subprocess
import sys

try:
    result = subprocess.run(['du', '-sh', '/var/log'], capture_output=True, text=True, check=True)
    print("STDOUT:", result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Ошибка: команда упала с кодом {e.returncode}")
    print(f"STDERR: {e.stderr}")
    sys.exit(1)


#print("STDOUT:", result.stdout)
#print("STDERR:", result.stderr)
#print("RETURN CODE:", result.returncode)
