"""
convert old MT posts to Jekyl-style files in _posts/
"""

import os
import sys
import re
import unicodedata

EXPORT_DIR = os.path.join(os.environ['HOME'],'botzilla-zip')
MT_SRC = os.path.join(EXPORT_DIR, 'mt-exported-june2018.txt')

class Jeklr:
	def __init__(self, Sourcefilename=MT_SRC):
		self.src = Sourcefilename
		self.content = {}
		self.init_keys()
		self.blank()

	def init_keys(self):
		self.pat = {}
		self.pat['author'] = re.compile('^AUTHOR: (.*)')
		self.pat['title'] = re.compile('^TITLE: (.*)')
		self.pat['email'] = re.compile('^EMAIL: (.*)')
		self.pat['ip'] = re.compile('^IP: (.*)')
		self.pat['url'] = re.compile('^URL: (.*)')
		self.pat['status'] = re.compile('^STATUS: (.*)')
		self.pat['comments'] = re.compile('^ALLOW COMMENTS: (.*)')
		self.pat['convert'] = re.compile('^CONVERT BREAKS: (.*)')
		self.pat['pings'] = re.compile('^ALLOW PINGS: (.*)')
		self.pat['primary category'] = re.compile('^PRIMARY CATEGORY: (.*)')
		self.pat['category'] = re.compile('^CATEGORY: (.*)')
		self.pat['date'] = re.compile('^DATE: (\d\d)/(\d\d)/(\d\d\d\d)')
		self.pat['body'] = re.compile('^BODY:$')
		self.pat['extbody'] = re.compile('^EXTENDED BODY:$')
		self.pat['excerpt'] = re.compile('^EXCERPT:$')
		self.pat['keywords'] = re.compile('^KEYWORDS:$')
		self.pat['comment'] = re.compile('^COMMENT:$')
		self.pat['chunk'] = re.compile('^(BODY|EXTENDED BODY|EXCERPT|COMMENT|KEYWORDS|PING)')
		self.pat['section'] = re.compile('^-----$')
		self.pat['break'] = re.compile('^--------$')
		self.pat['empty'] = re.compile('^\s*$')

	def blank(self):
		'we reset these for each post'
		self.year = 0
		self.month=1
		self.day=1
		self.name='none'
		self.convert = False
		self.publish = True
		self.content['BODY'] = ''
		self.content['COMMENT'] = ''
		self.content['PING'] = ''
		self.content['EXTENDED BODY'] = ''
		self.content['EXCERPT'] = ''
		self.content['KEYWORDS'] = ''
		self.content['category'] = ''
		self.content['categories'] = []
		self.accumulate = ''

	def post_name(self):
		bufname = re.sub('\W+','-',self.name)
		bufname = re.sub('-+$','',bufname)
		return '%04d-%02d-%02d-%s.%s'%(self.year,self.month,self.day,bufname, 'md' if self.convert else 'html')

	def kramdown(self,text):
		'convert MT-style text to kramdown, where possible'
		p = '(?P<prior>.*)<img(\\s+('+\
			'src="(?P<src>[^"]*)"|'+\
			'title="(?P<title>[^"]*)"|'+\
			'class="(?P<class>[^"]*)"'+\
			'))+(?P<tail>[^>]*)>(?P<post>.*)'
		imgPat = re.compile(p)
		m = imgPat.match(text)
		while m:
			url = m.group('src')
			m = imgPat.match(text)
		return text

	def write_post(self):
		if self.content['BODY'] == '':
			print("empty post, none written")
			return
		destFolder = '_posts' if self.publish else '_drafts'
		postPath = os.path.join(destFolder,self.post_name())
		f = open(postPath,'w')
		f.write('---\n')
		f.write('layout: post\n')
		f.write('title: "%s"\n'%(self.name))
		tryTags = True
		if tryTags:
			f.write('categories: [%s]\n'%(self.content['category']))
			if len(self.content['categories']) > 0:
				f.write('tags: [%s]\n'%(','.join(self.content['categories'])))
		else:
			if len(self.content['categories']) < 2:
				f.write('categories: [%s]\n'%(self.content['category']))
			else:
				'to-do: slice out primary category FIRST'
				f.write('categories: [%s]\n'%(','.join(self.content['categories'])))
		f.write('---\n')
		b = self.content['BODY']
		if self.content['EXTENDED BODY'] != '':
			b = b+ '\n<!--more-->\n' + self.content['EXTENDED BODY']
		if self.convert:
			b = self.kramdown(b)
		f.write(b)
		f.close()

	def clean_text(self,text):
		b = text
		b = re.sub('\xc6','f',b)
		b = re.sub('\x83','f',b)
		b = re.sub('\xe1','&aacute;',b)
		b = re.sub('\xe9','&eacute;',b)
		b = re.sub('\x91',"'",b)
		b = re.sub('\x92',"'",b)
		b = re.sub('\x93',"&quot;",b)
		b = re.sub('\x94',"&quot;",b)
		b = re.sub('\x85'," ",b)
		b = re.sub('\x96',"&mdash;",b)
		b = re.sub('\x97'," ",b)
		b = re.sub('"/bpix','"http://www.botzilla.com/bpix',b)
		try:
			b = b.encode('utf8')
		except:
			# print("Woah, '%s'"%(b))
			print("Unexpected error in %s:"%(self.name), sys.exc_info())
		return b

	def extract_posts(self):
		self.blank()
		oddlines = 0
		totallines = 0
		sf = open(self.src)
		for ln in sf.readlines():
			totallines += 1
			if self.pat['break'].match(ln):
				self.write_post()
				self.blank()
				continue
			m = self.pat['title'].match(ln)
			if m:
				self.name = re.sub(r'"','&quot;',m.groups()[0])
				continue
			m = self.pat['primary category'].match(ln)
			if m:
				self.content['category'] = m.groups()[0]
				continue
			m = self.pat['category'].match(ln)
			if m:
				self.content['categories'].append(m.groups()[0])
				continue
			m = self.pat['status'].match(ln)
			if m:
				self.publish = m.groups()[0] == 'Publish'
				continue
			m = self.pat['convert'].match(ln)
			if m:
				self.convert = m.groups()[0] == '__default__'
				continue
			m = self.pat['pings'].match(ln)
			if m:
				'ignore'
				continue
			m = self.pat['comments'].match(ln)
			if m:
				'ignore'
				continue
			m = self.pat['section'].match(ln)
			if m:
				self.accumulate = ''
				continue
			m = self.pat['author'].match(ln)
			if m:
				'ignore'
				continue
			m = self.pat['chunk'].match(ln)
			if m:
				self.accumulate = m.groups()[0]
				continue
			m = self.pat['date'].match(ln)
			if m:
				self.month = int(m.groups()[0])
				self.day = int(m.groups()[1])
				self.year = int(m.groups()[2])
				continue
			if self.accumulate != '':
				self.content[self.accumulate] += self.clean_text(ln)
			elif self.pat['empty'].match(ln):
				'ignore'
				continue
			else:
				oddlines += 1
				whut.append(ln)
		sf.close()
		self.write_post() # if any
		print("Processed %d lines, %d unaccounted"%(totallines, oddlines))


if __name__ == '__main__':
	## os.chdir(EXPORT_DIR)
	os.chdir('..')
	j = Jeklr()
	j.extract_posts()
	print("Done")
