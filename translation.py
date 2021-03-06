class Translation(object):

      
      START_TEXT = """
ð Hi {},
I am Channel Auto Caption bot from TeaM ShowcasE.
I can automatically add pre-setted caption and button to the files.
You can also use Markdown styles.
â ï¸NOTE
âª Before seting, ensure that bot is admin in your channel with editing permission.
"""    
      DYNAMIC_TEXT = """
ð° <u>About Dynamic</u>
- You can add {variable_name} in caption, bot will replace these variables by its value according to file.
  Example: Title: {filename}
  Supported variables:
  filename, ext
  Additional variables:
  For video files: width, height
  For audio files: title, artist
"""


      MARKDOWN_TEXT = """
ð° <u>Commands</u>

- /set_cap To Set Caption
- /set_btn To Set Button
- /rmv_cap To Remove Caption
- /rmv_btn To Remove Button

ð° <u>ððð¨ð®ð­ ððð«ð¤ðð¨ð°ð§</u>

ð <b>Bold text</b>
ð <code>**text**</code>

ð <b>Italic text</b>
ð <code>__text__</code>

ð <b>Underline text</b>
ð <code>--text--</code>

ð <b>Strike text</b>
ð <code>~~text~~</code>

ð <b>Code text</b>
ð <code>`text`</code>

ð <b>Hyperlink text</b>
ð <code>[text](https://t.me/durov)</code>
"""
