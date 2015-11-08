# How do I push code to production?

### First: Get code into master properly

  1. do your development work on the develop branch; don't commit to master until you deploy `git clone -b develop https://github.com/documnt/documnt`
  2. rebase your copy onto the latest main document repository develop branch (do this often): `git pull --rebase`
  3. when you're ready, fast-forward-merge master to get new develop changes: `git checkout master && git merge --ff-only develop`
  4. check out your development branch again now so you don't forget: `git checkout develop`

### Second: Give the production server the latest code

  1. create a [new bash console](https://www.pythonanywhere.com/user/documnt/consoles/bash/new) in pythonanywhere
  2. run `./update.sh && exit` and verify that the update went okay AND the console has been killed; there's cost associated with it sitting idle
  3. go to the [web configuration](https://www.pythonanywhere.com/user/documnt/webapps/#tab_id_documnt_pythonanywhere_com) and click the button to reload the site

### Finally: Make sure everything works all right
