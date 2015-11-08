# documnt
backend for the documnt concrete poetry site

## How do I run this thing?

  - install python3
  - install flask: `pip3 install flask`
  - run the webapp: `sudo python3 webapp.py`
  - visit [localhost](http://0.0.0.0)

## Okay, what's there to see so far?

There's art! You can see the same filler text in three different styles!

  - shitty prose on [production](http://documnt.pythonanywhere.com/0/prose) or [locally](http://0.0.0.0/0/prose)
  - shitty traditional poetry on [production](http://documnt.pythonanywhere.com/0/poetry) or [locally](http://0.0.0.0/0/poetry)
  - shitty concrete poetry on [production](http://documnt.pythonanywhere.com/0/mono) or [locally](http://0.0.0.0/0/mono)
  - default style on [production](http://documnt.pythonanywhere.com/0) or [locally](http://0.0.0.0/0)

## How do I work on the project?

Read [DEVELOP.md](https://github.com/documnt/documnt/blob/master/DEVELOP.md).

## Theoretical CMS overview

Each artistic work gets a numeric ID. An artist can specify how s/he prefers the art to be viewed. Current viewing styles are:

  - poetry: centered lines of text one after the other
  - prose: a single column of justified text
  - mono(space): raw text, preserving all spaces, with an 80-character limit

For testing, there's this style-override you can do. The url is made up of three parts:

    documnt.url/id/style

…where `document.url` is a running instance of documnt, `id` is a positive integer, and `style` is one of the styles listed above. If style is not specified, the preferred style set for that work is used.  **Of course, explicit style selection won't be possible once the site is actually up.** It should just choose the right one and display it. This is just for testing.

We can use whatever backend you want for storing and submitting each text-art-thing. Redis would be a good choice.
