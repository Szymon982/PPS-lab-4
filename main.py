from thinkdsp import *
import numpy
import scipy
import matplotlib as plt
from matplotlib import pyplot
from IPython.core.display_functions import display

# wykresy dokleić do sprawozdania

def zad1():
    signal = Chirp(start=2500, end=3000)
    wave1 = signal.make_wave(duration=1,framerate=20000)
    wave1.segment(start=0, duration=0.01).make_spectrum().plot()
    decorate(xlabel='Czas (s)')
    decorate(ylabel='Częstopliwość (hz)')
    pyplot.show()

def zad2():
    wave = read_wave('glissando.wav')  # https://www.youtube.com/watch?v=-knwJRhrNZI
    wave.segment(start=10, duration=20).make_spectrogram(10).plot()
    pyplot.show()

    wave = read_wave('happy_harp_sound.wav') # https://www.youtube.com/watch?v=-knwJRhrNZI
    wave.segment(start=0, duration=5).make_spectrogram(10).plot()
    pyplot.show()
    #pyplot.yticks(range(0,6000,1000))
    #pyplot.xticks(range(0,20))


def zad3():
    wave1 = read_wave('ryancacophony__singing-bell-hit-2.wav')
    wave2 = read_wave('truthiswithin__tibetan-singing-bowl-struck.wav')
    wave3 = read_wave('qubodup__gong-bell-monkay-s-singing-bowl-modified.wav')

    segment = wave1.segment(start=9, duration=0.05)
    spectrum = segment.make_spectrum(10)
    spectrum.plot_power(linewidth=1)
    decorate(xlabel='Częstotliwość (Hz)',
             ylabel='Moc')
    loglog = dict(xscale='log', yscale='log')
    decorate(xlabel='Częstotliwość (Hz)',
             ylabel='Moc',
             **loglog)
    print("szum różowy")
    pyplot.show()

    segment = wave2.segment(start=0, duration=5)
    spectrum = segment.make_spectrum(10)
    spectrum.plot_power(linewidth=0.5)
    decorate(xlabel='Częstotliwość (Hz)',
             ylabel='Moc')
    loglog = dict(xscale='log', yscale='log')
    decorate(xlabel='Częstotliwość (Hz)',
             ylabel='Moc',
             **loglog)
    print("szum czerwony")
    pyplot.show()

    segment = wave3.segment(start=3, duration=4)
    spectrum = segment.make_spectrum(10)
    spectrum.plot_power(linewidth=0.5)
    decorate(xlabel='Częstotliwość (Hz)',
             ylabel='Moc')
    loglog = dict(xscale='log', yscale='log')
    decorate(xlabel='Częstotliwość (Hz)',
             ylabel='Moc',
             **loglog)
    print("szum czerwony")
    pyplot.show()




if __name__ == '__main__':

    #zad1()
    #zad2()
    zad3()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
