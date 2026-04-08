import time,os

allan = r"""><(((('>"""

while True:
    for i in range(9, 20):
        os.system('cls')
        print(('\n'*(i%3)),f'{allan:{" "}>{i}}')
        time.sleep(0.2)