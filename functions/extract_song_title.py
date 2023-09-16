def extract_song_title(message_content):               
    parts = message_content.split("play", 1)             
    if len(parts) == 2:
        song_title = parts[1].strip()
        song_title = song_title.replace("by", "").strip()
        return song_title
    else:
        return None