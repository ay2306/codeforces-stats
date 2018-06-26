from bs4 import BeautifulSoup
import urllib2
print "Loading, Please wait..."
url = "http://codeforces.com/submissions/"
handle = "ay2306"
page = urllib2.urlopen(url+handle)
soup = BeautifulSoup(page,'lxml')
# print soup.prettify()
page_no = soup.find_all('span',class_='page-index')
max_page_no = 0
for i in page_no:
    if int(i.get_text()) > max_page_no:
        max_page_no = int(i.get_text())
# print "TOTAL PAGES = " + str(max_page_no)
attempt = 0
ac = 0
comp = 0
wa = 0
tle = 0
mle = 0
re = 0
ot = 0
for k in range(max_page_no):
    page = urllib2.urlopen(url+handle+'/page/'+str(k+1))
    soup = BeautifulSoup(page,'lxml')
    a = soup.find_all('span',class_='submissionVerdictWrapper')
    for i in a:
        attempt = attempt + 1
        p = i.get_text()
        if "Wrong" in p:
            wa = wa + 1
        elif "Accept" in p:
            ac = ac + 1
        elif "Compilation" in p:
            comp = comp + 1
        elif "Time" in p:
            tle = tle + 1
        elif "Memory" in p:
            mle = mle + 1
        elif "Runtime" in p:
            re = re + 1
        else:
            # print p
            ot = ot + 1
# submissionVerdictWrapper
# print "Attempt = " + str(attempt)
# print "Accepted = " + str(ac)
# print "Wrong Answer = " + str(wa)
# print "Compilation Error = " + str(comp)
# print "Time Limit Exceeded = " + str(tle)
# print "Memory Limit Exceeded = " + str(mle)
# print "Runtime error = " + str(re)
# if ot > 1:
#     print "Others = " + str(ot)
fopen = open('data.csv','w')
# fopen.write(str(attempt) + ',')
fopen.write(str(ac) + ',')
fopen.write(str(wa) + ',')
fopen.write(str(comp) + ',')
fopen.write(str(tle) + ',')
fopen.write(str(mle) + ',')
fopen.write(str(ot))
fopen.close()