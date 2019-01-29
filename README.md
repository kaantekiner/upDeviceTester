# Readme
Send ICMP packets to given Ip Adresses and determibe if they are up or not.  

### Prerequisites

Python v3 and scapy is enough.

```
# apt-get install python3 scapy
```

## Usage

It has a simple usage style, if you want to make it auto(recomended), it just takes your local Ip Adress and scan network devices in this range. Else, if you determine to use it in manuel mode, you can type your target Ip range and ICMP packet timeout in seconds.

Easy, which you can see that if you just type and run it with;

```
# python upDeviceTester.py
```

Help menu;

```
auto                    set mode automatic
manuel                  set mode manuel
-iprange <iprange>      set an Ip Adress range
-t <integer>            set ICMP packet timeout 
```

Usage tips;

```
python findUpDevices.py auto (take your ip adress for determine range automatically - default timeout is 0.8769 second)
```

or
```
python findUpDevices.py manuel -iprange <IPRange> -t <timeoutseconds> 
```
for an example - manuel usage: 

```
python findUpDevices.py manuel -iprange 192.168.1.0/24 -t 5 
```

After understanding that, just run the script with Python3.

```
# cd upDeviceTester
# python upDeviceTester.py auto
```

## License

MIT License

Copyright (c) 2019 Kaan Tekiner

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
