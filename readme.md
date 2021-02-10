# py amazfit tool
An python port of valeronm's amazfitbiptools(v.1.0.3.1) with LOTS hacks for Amazfit X.

All credit goes to Валерий Миронов(https://bitbucket.org/valeronm/amazfitbiptools/src/master/)

## what is...
* can pack/unpack .bin file for amazfit X (original watchfaces)

## what isn't...
* 100% compatibility with .json structures of X

## requirements
* python3(tested on 3.9.1)
* pillow (tested on version > 6)

## usage
* for Amazfit X
  * to unpack
    * python main.py --x --file WATCH_FACE_FILE.bin
  * to pack
    * python main.py --x --file WATCH_FACE_FILE.json
