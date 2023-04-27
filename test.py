import zapv2
import time

target = 'http://localhost:8000'
apikey = '12345'

# create a ZAP instance
zap = zapv2.ZAPv2(apikey=apikey)

# spider the target to identify all the endpoints
print('Spidering target {}'.format(target))
scanid = zap.spider.scan(target)
while (int(zap.spider.status(scanid)) < 100):
    time.sleep(5)
print('Spider completed')

# scan the target for vulnerabilities
print('Scanning target {}'.format(target))
scanid = zap.ascan.scan(target)
while (int(zap.ascan.status(scanid)) < 100):
    time.sleep(5)
print('Scan completed')

# generate a report of the vulnerabilities found
report = zap.core.htmlreport()
with open('report.html', 'w') as f:
    f.write(report)
print('Report generated')