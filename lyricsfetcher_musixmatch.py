#Scraper to scrap lyrics from musixmatch

import requests
import bs4

def get_url(sname, aname):
    sname1 = namer(sname)
    aname1 = namer(aname)
    return "https://www.musixmatch.com/lyrics/"+ aname1 + "/" + sname1

def get_lyrics(url1):
    ret = []
    req = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'})
    if (req.status_code != 404):
        print (f"\nLyrics found! 😄\nDownloading lyrics from {url1}")
        content = req.content
        soup = bs4.BeautifulSoup(content, features="html.parser")
        lyrics = soup.find_all("span", {"class" : "lyrics__content__ok"})
        for i in lyrics:
            ret.append(i.get_text())

        return "\n".join(ret)
    else:
        return "error404"

def namer(inp):
    for i in range(0, len(inp), 1):
        if (inp[i] == " "):
            inp = inp.replace(inp[i], "-")
    return inp

def main():
    song = input("Enter song: ")
    art = input("Enter artist: ")
    url = get_url(song, art)
    print ("\nSearching lyrics on Musixmatch")
    lyrics = get_lyrics(url)
    if (lyrics != "error404"):
        print ("\nLyrics for '" + song + "' by " + "'" + art + "'" + ":\n\n" + lyrics)
        ch = input("\nDo you want to save the lyrics in a .txt file?\n\n1.Yup\n2.Nah\nEnter choice:")
        if (ch == "1"):
            fname = input(f"Enter file name (default: '{song}_{art}.txt'): ")
            if (len(fname) == 0):
                fname = song + "_" + art + "_lyrics.txt"
            with open(fname, "w") as f:
                f.write(lyrics)
    else:
        print ("\nSorry, lyrics for the song not found on Musixmatch\n")
main()
