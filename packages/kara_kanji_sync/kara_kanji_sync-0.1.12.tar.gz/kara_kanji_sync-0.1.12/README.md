# kara-kanji-sync

From lyrics in japanese and an already timed karaoke in romaji [Aegisub](https://aegisub.org) subtitles file (.ass), generate a new subtitle file timed in japanese.

<img src="transfo.png"> 

## Getting Started

### Notebook

Open the notebook in Google Colab, save a copy and follow the instructions.

<a target="_blank" href="https://colab.research.google.com/drive/1DSmXbQ1hEWcHCpubJ1s0VUeiW-fYAAjN?usp=sharing">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

### Pypi

```bash
pip install kara-kanji-sync
```

## Methodology

### Algorithm

1. The algorithm starts by trying to find the hiragana, katakana and english words from the original lyrics in the romaji lyrics from the already timed karaoke. It associates each group of kanji to a group of romaji syllables.
2. To associate each kanji of the group to its appropriate syllables, the algorithm tries all pronunciations of all possible combination of kanji until it finds the right one. The pronunciation for individual kanji is from Jisho and for group is from JmdictFurigana.
3. It recreates the line with punctuation and special characters from lyrics.

### Caveats

- Each lyric line has to be strictly aligned with the one from the ASS file.
- Numbers are not treated, they may have to be replaced by kanji or modified manually in the result file.
- Some words composed by multiple kanji followed by hiragana can be missed.

Cases where modifications may be needed on the input file :
- Words in "japenglish" transcribed in romaji into english won't be recognised if kana lyrics transcribed the word in katakana.
  Exemple: "Asphalt" pronounced "ASUFARUTO"
- Some karaoke timers put apostrophes on muted vowels. Those will cause errors during the first phase.
- Unusual characters or punctuation signs may cause issues, removing them when a sync error is raised is recommended.

## Recommended workflow

1. Get the lyrics (preferably on a reliable website like [Lyrical Nonsense](https://www.lyrical-nonsense.com/global/)).
2. Get the ass file.

### Using the notebook

Just the follow the instructions that globally in
1. Installing the package.
2. Uploading the file.
3. Inputting the lyrics with an interface that shows lines from uploaded ass which facilitate this phase.
4. Launching a lyrics check.
5. Launching the main algorithm.
6. Downloading the result.

### Using the package

Here a code snippet to generate from lyrics and sub
```python
import pysubs2
from kara_kanji_sync import KanjiSyncer

subs = pysubs2.load(f"path_to_ass_file.ass")
lyrics = open(f"path_to_lyrics.txt").read()

kanji_syncer = KanjiSyncer()
kanji_syncer.subtitles_file = subs
kanji_syncer.lyrics = lyrics.splitlines()

kanji_file = kanji_syncer.sync_subs("Kanji Top") # You can choose "Kanji Bottom" to have the subtitles on the bottom
kanji_file.save(f"result.ass")
print(kanji_syncer.errors) # Shows all the potential errors
```

### In Aegisub, on the result file

1. Load the ass file and the video.
2. Modify the styles *Kanji Top* and *Kanji Top - Right* (or *Kanji Bottom* and *Kanji Bottom - Right* if you chose this option in the *sync_sub* function).
3. *Automation* -> *Apply karaoke template*

## References

- [Furigana Karaoke subtitles - Aegisub documentation](https://aegisub.org/docs/latest/furigana_karaoke/)
- [Individual Kanji readings - JmdictFurigana documentation](https://github.com/Doublevil/JmdictFurigana/tree/master)
- [Jisho API](https://github.com/pedroallenrevez/jisho-api)