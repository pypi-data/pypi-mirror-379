# PyExtender
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![PyPI Version](https://img.shields.io/pypi/v/PyExtender)
![Status](https://img.shields.io/pypi/status/PyExtender)

A simple Python extension toolkit.

## Features

- **Automated Code Generation**: Dynamically create functions, lists, and variables in Python files using the `pyassist` module.
- **File Utilities**: Easily create and output to files with the `bcfo` module.
- **Enhanced Randomness**: Generate seeds and random numbers via the `PErandom` module.

## Download

We need to download PyExtender from PyPI:

```bash
pip install PyExtender
```

## Basic Usage

### Output Function

The `output` function is primarily used for writing data to files.

input:
```Python
import PyExtender

output("Hello,World!", "text.txt")
#output(text:str,file:str)
```
Now,let's open the file `text.txt`.(The file will be automatically created if it does not already exist)

output:
```text
Hello,World!
```

### Create Funtion

The `create` funtion can create a file,like this:

input:
```Python
import PyExtender

create("test.txt")
```

Now,you can see file `test.txt`:
```text
#Note: Assuming the file is located in this directory.
----test
|
|------test.py
|
|------test.txt   #create file
```
[See More Functions](https://github.com/bzjsmdl/PyExtender)

## Frequently Asked Questions (FAQ)

### Q1:
#### Does PyExtender support Python 2 or versions below Python 3.6?
### A1:
#### No, it requires Python 3.6 or higher.
***
### Q2:
#### Where can I report bugs?
### A2:
#### Please open an issue on our [GitHub Issues](https://github.com/bzjsmdl/PyExtender/issues) page.
***
### Q3:
#### Where can I find the full documentation?
### A3:
#### Sorry, our official documentation isn't ready yet.


## License
### This project is licensed under the MIT License - see the [License](LICENSE) file for details.
## Acknowledgements
- ### *Thanks to the **Python community** for inspiration and tools.*
- ### *Thanks to all **contributors and users** for their support.*

## Contact
- ### Maintainer: cnong

- ### Email: bzjsmdl88@qq.com or bzjsmdl@outlook.com

- ### GitHub: [@bzjsmdl](https://github.com/bzjsmdl)

## From the Maintainer
*Well,if you're reading this, you've got some serious patience -- though I suspect you might have just skipped to the end. But my English isn't very good.So, The vast majority of the text was translated using AI (DeepSeek). If you're wondering why, the answer is simple: internationalization.*

*It took me a long time to make the package.*

*Well, let me tell you my story:*

*In third or fourth grade, an idea suddenly hit:"Why don't I learn how to program?"*

*My father knew, so he bought a Python book for me. I was happy when it arrived. At the beginning, I saw the book every day. But,it was difficult for me at that time. So, I just gave up.*

*After two or three years, I took two months to finish reading the book. I just knew "Python" isn't hard. Then I made a very basic game.*

*Now,I'm learning C. Although, I don't know why am I learning it.*

*(Another thing: I'm a middle school student.)*

*This is my story. And here is the package's story.*

*I made the package in August or September.At the beginning, I only wrote two functions in the package. Then, I gave up. A few days ago, I added another 10 functions to it. And so, "PyExtender" was born.*

*Thank you for watching, and thank you for downloading.*

*I don't have much to say, just wishing you good morning,good afternoon and good night.*
***
*written by Maintainer cnong*

*September 20th, 2025*

*10:56 PM*