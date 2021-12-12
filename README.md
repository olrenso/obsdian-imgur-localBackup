# Obsdian Imgur local backup
I made this simple script to create a local backup of the images in my vault hosted on Imgur, on the off chance the servers will go down.
Since it could be useful for others I thought to create e public repository.

The script iterates all the .md files in the vault, it search for Imgur images, it download them and it replace the internal links with the local images.
I suggest using it on a backup of the vault in case something goes wrong.

There are probably countless ways to make it better, but at least it works. If you have any suggestions feel free to open an issue or make a pull request!
