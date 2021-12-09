from pico2d import *

class Sound:
    def __init__(self):
        self.main_bgm = load_music('Resource/sound/mario.wav')
        self.coin_bgm = load_music('Resource/sound/eatmoney.wav')
        self.enemy_die_bgm = load_music('Resource/sound/death1.wav')
        self.jump_bgm = load_music('Resource/sound/jump.wav')
        self.gameover_bgm = load_music('Resource/sound/death2.wav')

    def play_main_bgm(self, volum):
        self.main_bgm.repeat_play()
        self.main_bgm.set_volume(volum)

    def stop_main_bgm(self):
        self.main_bgm.stop()

    def play_enemy_die_bgm(self, volum):
        self.enemy_die_bgm.play(1)
        self.enemy_die_bgm.set_volume(volum)

    def play_gameover_bgm(self, volum):
        self.gameover_bgm.play(1)
        self.gameover_bgm.set_volume(volum)

    def play_jump_bgm(self, volum):
        self.jump_bgm.play(1)
        self.jump_bgm.set_volume(volum)

    def play_coin_bgm(self, volum):
        self.coin_bgm.play(1)
        self.coin_bgm.set_volume(volum)