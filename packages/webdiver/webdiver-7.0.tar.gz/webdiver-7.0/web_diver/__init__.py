#pip install requests beautifulsoup4 sqlite3 pandas
import requests
import sqlite3
import schedule
import time
from datetime import datetime
import threading
from bs4 import BeautifulSoup

_www_uri = 'false'
_www_db_sql = 'wwwpy_db_sqlite.db'
_data = 'false'
_data_r = ''
_uri_www_diver = []
__dom_filter = []
__www_task_schudele = 'false'
__www_task_schudele_type = 'false'
__www_task_schudele_filter = []
__hour = 0
__minute = 0

def set_task_uri(uri):
	global _www_uri
	_www_uri = str(uri)
	print(_www_uri)

def www_diver(_filter,limit=0):
	global _data
	global _data_r
	_scraped_data = []
	_text_tx = []
	_count = 4
	_flag_count = 0
	_url = _www_uri
	response = requests.get(_url)
	_dom_filter = _filter[0]
	_dom_tag = str(_dom_filter["tag"])
	_dom_tag_class = str(_dom_filter['class_tag'])
	_filter.remove(_dom_filter)
	soup = BeautifulSoup(response.text, 'html.parser')
	quotes = soup.find_all(_dom_tag, class_=_dom_tag_class)
	for quote in quotes:
		for _dom_tag_fx0 in _filter:
			_dom_tag_fx = str(_dom_tag_fx0["tag"])
			_dom_tag_fx_class = str(_dom_tag_fx0["class_tag"])
			_text = quote.find(_dom_tag_fx, class_=_dom_tag_fx_class).text
		_author = _url
		_quote = str(_text)
		_quote_cpz_f0x0 = [str(_quote),str(_author)]
		_scraped_data.append(_quote_cpz_f0x0)
		sql_add(_quote_cpz_f0x0)
		time.sleep(2)
		_flag_count += 1
		if(_flag_count == _count and limit != 0):
			break;

def www_diver_text():
	global _data
	global _data_r
	_count = 4
	_flag_count = 0
	_url = _www_uri
	print(_url)
	response = requests.get(_url)
	print(response.text)
	_rem = response.text
	soup = BeautifulSoup(response.text, 'html.parser')
	_rem_text = soup.get_text(separator=' ',strip=True)
	_scraped_data = []
	_quote_cpz_f0x0 = [str(_rem_text),str(_url)]
	_scraped_data.append(_quote_cpz_f0x0)
	sql_add(_quote_cpz_f0x0)
	time.sleep(2)
	#_flag_count += 1
	#if(_flag_count == _count):
	#	break;

def www_diver_html():
	global _data
	global _data_r
	_count = 4
	_flag_count = 0
	_url = _www_uri
	print(_url)
	response = requests.get(_url)
	print(response.text)
	_rem = response.text
	_scraped_data = []
	_quote_cpz_f0x0 = [str(_rem),str(_url)]
	_scraped_data.append(_quote_cpz_f0x0)
	sql_add(_quote_cpz_f0x0)
	time.sleep(2)
	#_flag_count += 1
	#if(_flag_count == _count):
	#	break;

def www_diver_download():
	_file = guid
	url = uri
	try:
		response = requests.get(url, stream=true)
		if(response.status_code == 200):
			with open(_file,'wb') as _f_x:
				for _flag_x in response.iter_content(chunck_size=8192):
					file.write(_flag_x)
			_r = {file}
			_data = _r
		else:
			_r = 'false'
	except e:
		_r = {e}
	return _r

def www_diver_shedule():
	print(f'*uri:{__www_task_schudele}')
	set_task_uri(__www_task_schudele)
	print(f'*#uri:{__www_task_schudele}')
	match(__www_task_schudele_type):
		case "_text":
			www_diver_text()
		case "_html":
			www_diver_html()
		case "_filter":
			for _fil_x0 in __www_task_schudele_filter:
				_fil_x0x0 = _fil_x0["tag"]
				_fil_x0x1 = _fil_x0["class_tag"]
				www_add_filter(_fil_x0x0,_fil_x0x0)
			www_diver()

def get_task():
	_r = _data
	return _r

def sql_setup(db_name):
	global _www_db_sql
	_www_db_sql = db_name
	conn = sqlite3.connect(_www_db_sql)
	cursor = conn.cursor()
	cursor.execute('CREATE TABLE IF NOT EXISTS quotes (id INTEGER PRIMARY KEY, quote TEXT, author TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)')
	# Commit and close the connection
	conn.commit()
	conn.close()

def sql_add(_data):
	conn = sqlite3.connect(_www_db_sql)
	cursor = conn.cursor()
	_cmd = 'INSERT INTO quotes (quote, author) VALUES (?, ?)'
	cursor.execute(_cmd,(_data[0],_data[1]))
	conn.commit()
	conn.close()

def set_task(uri, hour, minute, _type, _filter='false'):
	global __www_task_schudele
	global __www_task_schudele_type
	global __www_task_schudele_filter
	global __hour
	global __minute
	__www_task_schudele = str(uri)
	__www_task_schudele_type = _type
	__hour = str(hour)
	__minute = str(minute)
	if(_filter != 'false'):
		__www_task_schudele_filter = _filter
	_t = threading.Thread(target=thread_set_task)
	_t.start()

def thread_set_task():
	__true = True
	while __true:
		__check_schudell = f"{__hour}:{__minute}"
		__time_curr = datetime.now().strftime("%H:%M")
		if(__check_schudell == str(__time_curr)):
			_w = f"CHECK:{str(__check_schudell)} == {str(__time_curr)}"
			print(_w)
			www_diver_shedule()
			_w = f"CHECKED:{str(__check_schudell)} == {str(__time_curr)}"
			print(_w)
			__true = False
		time.sleep(10)

def rem_html_tag(_content):
	global _data_r
	_data_r = str(_content)
	try:
		_data_fx = str(_content)
		_data_index_fx0 = _data_fx.index('<')
		_data_index_fx0x1 = _data_fx.index('>')
		_data_fx0_tx = _data_fx[_data_index_fx0:_data_index_fx0x1 + 1]
		_data_fx0 = _data_fx.replace(_data_fx0_tx,'')
		_data_r = str(_data_fx0)
		if(_data_fx0.index('<') > 0 or _data_fx0.index('>') > 0):
			rem_html_tag(_data_fx0)
	except:
		print(f'_r:{_data_r}')

def www_diver_add_task(_uri):
    global _uri_www_diver
    _uri_www_diver.append(_uri)

def www_add_filter(_dom_tag,_class_name):
	global __dom_filter
	__filter = {"tag":str(_dom_tag),"class_tag":str(_class_name)}
	__dom_filter.append(__filter)

def www_diver_start(db_name,_type):
	sql_setup(db_name)
	for _flag_index in _uri_www_diver:
		set_task_uri(f'{_flag_index}')
		match _type:
			case "_text":
				www_diver_text()
			case "_html":
				www_diver_html()
			case "_filter":
				www_diver(__dom_filter)
