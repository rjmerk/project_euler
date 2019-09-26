import os

i = 1
while True:
    if os.system(f"python problem_{i:03d}.py"):
        break
    print("=" * 80)
    i += 1
