
import pyshorteners

link = input("\nEnter your link: ")

shorter_link = pyshorteners.Shortener()
x = shorter_link.tinyurl.short(link)

return x
