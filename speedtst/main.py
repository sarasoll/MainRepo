from turtle import speed
import speedtest
speed=speedtest.Speedtest()
print(f'Down speed= {speed.download()}')
print(f'Up speed= {speed.upload()}')



