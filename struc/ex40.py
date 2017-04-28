#define a class : Song()
#to print lyrics of a song
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print (line)

#instantiate, 实例化， 以常量形式初始化
little_star_0 = Song(["Twinkle, twinkle, little star",
"How I wonder what you are!",
"Up above the world so high",
"Like a diamond in the sky"])
little_star_0.sing_me_a_song()

#instantiate，以dict形式初始化
litt_star = {'twinkle': 'Twinkle, twinkle, little star',
'how': 'How I wonder what you are!',
'up': 'Up above the world so high',
'like': 'Like a diamond in the sky'}
little_star_1 = Song([litt_star['twinkle'],litt_star['how'],litt_star['up'],litt_star['like']])
little_star_1.sing_me_a_song()

#instantiate，以“”variable+list”形式
twinkle="Twinkle, twinkle, little star"
how="How I wonder what you are!"
up= "Up above the world so high"
like= "Like a diamond in the sky"
little_star_2 = Song([twinkle,how,up,like])
little_star_2.sing_me_a_song()
