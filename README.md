# nikon-shuttercount

Script to simplify getting shutter count from Nikon NEF or JPG files. Uses the [ExifRead](https://github.com/ianare/exif-py) library.

## Installation

Clone this repo and run 

    pip install -e <directory with this repo>
    
## Usage

Pass in a raw or jpg image that has been imported from the camera (but not processed by Lightroom etc) and the script will read the exif data and print the shutter count entry (specifically the `TotalShutterReleases` entry in the `MakerNote` section). Examples:


    $ shuttercount DSC_8113.NEF
    9075 
       
    $ shuttercount DSC_0001.JPG
    78289

## Caveats

Only tested on D750 and D850 files, ymmv 😃


