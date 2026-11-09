#Test driver code for implimenting wensite browsing in chat on tele
import TeleMeme

memes = TeleMeme.get_memes(30)
#print(len(memes))
[print(str(meme.src) + " on position " + str(meme.queue_position)) for meme in memes]