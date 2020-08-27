# SimpleReconSubdomain
This is very basic automated recon script tool.

[![Python 3.7](https://img.shields.io/badge/python-3.7-yellow.svg)](https://www.python.org/)
[![Build](https://img.shields.io/badge/Supported_OS-Linux-orange.svg)]()
[![Build](https://img.shields.io/badge/Supported_OS-Mac-orange.svg)]()
![GitHub](https://img.shields.io/github/license/MrCl0wnLab/SenderMailgunPython?color=blue)
```
Autor:    MrCl0wn
Blog:     http://blog.mrcl0wn.com
GitHub:   https://github.com/MrCl0wnLab
Twitter:  https://twitter.com/MrCl0wnLab
Email:    mrcl0wnlab\@\gmail.com
```
## USE
```
python tool.py {domain}
python tool.py fbi.gov
```
![Screenshot](assets/img1.png)
![Screenshot](assets/img2.png)
## TARGET IS A MAGIC STRING
```bash
curl -s "https://rapiddns.io/subdomain/TARGET?full=1#result" | awk -v RS='<[^>]+>' '/$1/' | sort -u >>TARGET-rapiddns.txt

curl -s "https://rapiddns.io/subdomain/TARGET?full=1#result" | awk -v RS='<[^>]+>' '/$1/' | sort -u >>TARGET-rapiddns.txt

curl -s "https://riddler.io/search/exportcsv?q=pld:TARGET" | grep -Po "(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | sort -u >>TARGET-riddler.txt

curl -s "https://jldc.me/anubis/subdomains/TARGET" | grep -Po "((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | sort -u >>TARGET-jldc.txt

curl -s "https://crt.sh/?q=%25.TARGET&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u >>TARGET-crt.txt

curl -s "https://dns.bufferover.run/dns?q=.TARGET" | jq -r .FDNS_A[] | sed -s 's/,/\\n/g'  | sort -u  >>TARGET-bufferover.txt

cat TARGET-*.txt | sort -u >TARGET.txt;cat TARGET.txt -n
```
## OUTPUT
```
TARGET-rapiddns.txt
TARGET-riddler.txt
TARGET-jldc.txt
TARGET-crt.txt
TARGET-bufferover.txt
```
## OUTPUT SORT UNIQ
```
TARGET.txt
```
### Th4nk Y0u
```
@ofjaaah
```
