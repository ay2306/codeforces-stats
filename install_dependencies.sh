pkg="python"
if dpkg --get-selections | grep -q "^$pkg[[:space:]]*install$" >/dev/null; then
echo "Python is installed"
else
    apt-get install python
fi
pkg="octave"
if dpkg --get-selections | grep -q "^$pkg[[:space:]]*install$" >/dev/null; then
echo "Octave is installed"
else
    apt-get install octave
fi
pkg="python-pip"
if dpkg --get-selections | grep -q "^$pkg[[:space:]]*install$" >/dev/null; then
echo "Python-pip is installed"
else
    apt-get install python-pip
fi
pkg="virualenv"
if python -c "import virtualenv" &> /dev/null; then
    echo 'all good'
else
    pip install virtualenv
fi
pkg="beautifulsoup"
if python -c "from bs4 import BeautifulSoup" &> /dev/null; then
    echo 'all good'
else
    pip install beautifulsoup
fi
pkg="urllib2"
if python -c "import urllib2" &> /dev/null; then
    echo 'all good'
else
    pip install urllib2
fi
