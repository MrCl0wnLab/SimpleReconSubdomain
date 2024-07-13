import subprocess
import concurrent.futures
import sys



# Autor:    MrCl0wn
# Blog:     http://blog.mrcl0wn.com
# GitHub:   https://github.com/MrCl0wnLab
# Twitter:  https://twitter.com/MrCl0wnLab
# Email:    mrcl0wnlab\@\gmail.com
#
# Th4nk Y0u: @ofjaaah
#
# WARNING
# +------------------------------------------------------------------------------+
# |  [!] Legal disclaimer: Usage of afdWordpress for attacking                   |
# |  targets without prior mutual consent is illegal.                            |
# |  It is the end user's responsibility to obey all applicable                  |
# |  local, state and federal laws.                                              |
# |  Developers assume no liability and are not responsible for any misuse or    |
# |  damage caused by this program                                               |
# +------------------------------------------------------------------------------+

import subprocess
import concurrent.futures
import sys

try:
    # List command
    command_list = [
        f'''curl -s "https://rapiddns.io/subdomain/TARGET?full=1#result" | awk -v RS='<[^>]+>' '/TARGET/' |grep "\w.*TARGET$"| sort -u >>TARGET-rapiddns.txt''',
        f'''curl -s "https://riddler.io/search/exportcsv?q=pld:TARGET""|cut -d, -f6|grep TARGET|sort -u >>TARGET-riddler.txt''',
        f'''curl -s "https://jldc.me/anubis/subdomains/TARGET" | jq -r '.[]' 2>/dev/null|sort -u >>TARGET-jldc.txt''',
        f'''curl -s "https://crt.sh/?q=%25.TARGET&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u >>TARGET-crt.txt''',
        f'''curl -s "https://dns.bufferover.run/dns?q=.TARGET" | jq -r '.FDNS_A[]' 2>/dev/null|cut -d, -f2|sort -u >>TARGET-bufferover.txt''',
        f'''curl -s https://urlscan.io/domain/TARGET | grep "/domain" | grep TARGET | grep  -v "<span" | cut -d"/" -f3 | cut -d">" -f1 | sed 's/"//g' | sort -u >>TARGET-urlscan.txt''',
        f'''cat TARGET-*.txt | sort -u >TARGET.txt;cat TARGET.txt -n'''
    ]

    def exe_cmd(command_str: str):
        str_format = command_str.replace('TARGET', TARGET)
        print('[ + ] PROCESS:', str_format)
        result = str(subprocess.run(
            str_format, capture_output=True,shell=True).stdout.decode('utf-8')
        )
        if result:
            print(result)

    # Using as command line
    if __name__ == '__main__':
        if len(sys.argv) == 2:
            TARGET = sys.argv[1]
            with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
                futures = []
                for cmd in command_list:
                    futures.append(executor.submit(exe_cmd, cmd))
                executor.shutdown(wait=True)

except KeyboardInterrupt:
    pass
