class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):

        # Use some `duck typing` to determine 
        # the split method exists, if it does 
        # then split it and use that instead
        if hasattr(self.lyrics, "split"):
            outObj = self.lyrics.split("\n")
        else:
            outObj = self.lyrics
        
        for line in outObj:
            print line

happy_bday = Song(["Happy birthday to you", 
    "I don't want to get sued",
    "So I'll stop right there" ])    

bulls_on_parade = Song(["They rally around the family", 
    "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

#
# Extra Duck typing
#
my_song = Song("""
Row row row your boat
gently down the street
""") 

my_song.sing_me_a_song()

# output
# 
# Happy birthday to you
# I don't want to get sued
# So I'll stop right there
# They rally around the family
# With pockets full of shells
# 
# Row row row your boat
# gently down the street
