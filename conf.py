import os


# Screen-to-text langs
lang = 'rus'  # +eng


def sound():
    os.system('afplay shum-zapuschennogo-v-tsel-noja.wav')  # for mac
# ------------------------------------------------------------------------------------
#   os.system('aplay path/to/sound.wav')  # for linux
# ------------------------------------------------------------------------------------
#   import winsound
#   winsound.PlaySound('shum-zapuschennogo-v-tsel-noja.wav', winsound.SND_FILENAME)
# ------------------------------------------------------------------------------------
