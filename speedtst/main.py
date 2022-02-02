from turtle import speed
import speedtest
speed=speedtest.Speedtest()
print(f'D speed= {speed.download()}')
print(f'U speed= {speed.upload()}')
