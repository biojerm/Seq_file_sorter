## Synopsis
This is a simple script that renames moves some files around.  I built this to process the sequencing files returned to me from [QuintaraBio](http://www.quintarabio.com/) and [ELIM BIOPHARM](https://www.elimbio.com/).  The DNA sequencing files that are returned contain extra information in the file names that are not useful in my analysis.  This script organizes the files by file type and trims out the unnecessary information from the file name.  

## Code Example
Run code by:
1) Put the file inside the folder with the .seq and .ab1 files
2) In the terminal\command window navigate to the folder with the sequence files. 
3) run command:
```
 
python seq_file_sorter.py

```
4) Respond y/n if you want the file sorter to move itself to the desktop


## License

MIT License

Copyright (c) \[2017\] \[Jeremy LaBarge\]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.