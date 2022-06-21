import speedtest
import time

st = speedtest.Speedtest()

print("-------Internet Speedtest--------")
time.sleep(1)
while True:
    choise = float(input("1- Download\n"
                         "2- Upload\n"
                         "3- Both\n"
                         "Your choise: "))
    time.sleep(1)

    if (choise<1 or choise>3):
        print()
        print("Please enter values 1-3 only")
        print()
    else:
        break
print()
print("One more second please...")
print()
download = round(st.download() / 1000000, 3)
upload = round(st.upload() / 1000000, 3)

if choise == 1:
    print("Your Download Speed: ", download,"Mbps")
if choise == 2:
    print("Your Upload Speed: ", upload,"Mbps")
if choise == 3:
    print("Your Download Speed: ", download,"Mbps")
    print("Your Upload Speed: ", upload, "Mbps")
