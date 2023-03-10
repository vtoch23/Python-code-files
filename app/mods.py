def link_short(link):
    import pyshorteners
    shorter_link = pyshorteners.Shortener()
    x = shorter_link.tinyurl.short(link)
    return x
