import os

# Screen-to-text langs
lang = 'rus'  # +eng


def sound():
    return os.system('afplay shum-zapuschennogo-v-tsel-noja.wav')  # for mac
# ------------------------------------------------------------------------------------
#   return os.system('aplay path/to/sound.wav')  # for linux
# ------------------------------------------------------------------------------------
# import winsound
#   return winsound.PlaySound('path/to/sound.wav', winsound.SND_FILENAME)  # for win
# ------------------------------------------------------------------------------------

