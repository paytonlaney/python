class Television:
    # Constants
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self):
        """Default values for TV"""
        self.__status = False # Sets TV to off by default
        self.__muted = False # Sets TV to unmuted by default
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        """Turns TV off and on"""
        self.__status = not self.__status

    def mute(self):
        """Mutes or unmutes the TV"""
        if self.__status:
            self.__muted = not self.__muted
            if self.__muted:
                self.__previous_volume = self.__volume # When TV is unmuted; volume goes back to previous setting
                self.__volume = Television.MIN_VOLUME

    def channel_up(self):
        """Increases the channel by one, but if it goes past 3, it resets to 0"""
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1 # Increases channel by 1

    def channel_down(self):
        """Decreases the channel by one, but if it tries to go past 0, it resets to 3"""
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1 # Decreases channel by 1

    def volume_up(self):
        """Increases volume by 1 or unmutes the TV if it is muted"""
        if self.__status:
            if self.__muted:
                self.__muted = False # Unmutes TV
                self.__volume = self.__previous_volume # Sets to previous volume before muting
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1 # Increases by 1

    def volume_down(self):
        """Decreases volume by 1 or unmuted the TV if it is muted"""
        if self.__status:
            if self.__muted:
                self.__muted = False # Unmutes TV
                self.__volume = self.__previous_volume # Sets to previous volume before muting
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1 # Decreases by one

    def __str__(self):
        """Returns the state of the TV"""
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
