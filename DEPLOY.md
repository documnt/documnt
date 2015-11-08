# How do I push code to production?

### First: Develop on the develop branch

  1. do your development work on the develop branch, not master `git clone -b develop https://github.com/documnt/documnt`
  2. code away
  3. rebase your copy onto the latest main document repository develop branch (do this often): `git pull --rebase`
  4. push to the development branch once things mostly work: `git push` (this means when we run `git pull --rebase`, your changes will be merged into our work as if we had started working after you)

### Second: Fast-forward the master branch to get your changes

  1. test until you're confident that your code should go into production
  2. pull the latest master branch which should be behind develop by a few commits: `git pull origin master`
  3. fast-forward-merge master to get new develop changes: `git checkout master && git merge --ff-only develop`
  4. push those changes to the server: `git push origin master`
  5. check out your development branch again now so you don't forget later: `git checkout develop`

### Second: Give the production server the latest code

  1. create a [new bash console](https://www.pythonanywhere.com/user/documnt/consoles/bash/new) in pythonanywhere
  2. run `./update.sh && exit` and verify that the update went okay AND the console has been killed; there's cost associated with it sitting idle
  3. go to the [web configuration](https://www.pythonanywhere.com/user/documnt/webapps/#tab_id_documnt_pythonanywhere_com) and click the button to reload the site

### Finally: Play on documnt to make sure everything works all right
