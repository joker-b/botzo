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
	tagTest = False
	useAutoTags = True
	autoTags = { # tags plus potential regexes
		'Fujifilm' : ['Fuji','X100','X-?Pro','Acros\b','Neopan'],
		'Canon' : ['Canon','5D','1D','Rebel','F-?1','AE-?1', 'Cantax','EOS'],
		'Contax' : ['Contax', 'Cantax'],
		'Leica' : ['Leica', 'Leitz', 'HEGR', 'D-?Lux'],
		'Lumix' : ['Panasonic', 'Lumix', 'LX-?\d', 'P1\d+.jpg'],
		'Books' : ['ibrary', '\b[bB]ooks?\b'],
		'3D' : ['NVIDIA', 'nvidia', 'GPU', 'Direct-?X', 'Open\s?GL','e.orce', 'Pixar', 'Trion', 'Square', 'Final Fantasy', 'shader', 'Maya'],
		'Analog' : ['arkroom', 'ektol', 'gfa', 'odinal', 'TMax', 'Tri-?X', 'eopan', 'Xtol', 'Ilford', 'Kodak'],
		'Digital': ['hromebook','GPU','hader','\b[VAX]R\b', 'Facebook', 'Google', 'Instagram', '\bPDA\b']
	}
	cAutoT = {}
	def __init__(self, Sourcefilename=MT_SRC):
		self.src = Sourcefilename
		self.content = {}
		self.init_keys()
		self.blank()
		for t in self.autoTags:
			self.cAutoT[t] = [re.compile(p) for p in self.autoTags[t]]

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

	def autotag(self,text):
		n = 0
		for t in self.cAutoT:
			# print(t)
			if self.content['tags'].get(t):
				print('skip')
				continue
			for p in self.cAutoT[t]:
				if p.search(text):
					self.content['tags'][t] = True
					n = n + 1
					break
		#if n > 1:
		#	print("found %d tags: (%s) in <%s>"%(n,','.join(self.content['tags']),self.name))

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
		self.content['tags'] = {}
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
			'alt="(?P<alt>[^"]*)"|'+\
			'align="(?P<align>[^"]*)"|'+\
			'width="?(?P<width>\d+)"?|'+\
			'height="?(?P<height>\d+)"?|'+\
			'hspace="?(?P<hspace>\d+)"?|'+\
			'vspace="?(?P<vspace>\d+)"?|'+\
			'border="?(?P<border>\d+)"?|'+\
			'class="(?P<class>[^"]*)"'+\
			')'+\
			')+(?P<tail>[^>]*)>(?P<post>.*)'
		imgPat = re.compile(p)
		text = re.sub('<!--\s.*\s-->','',text)
		q = text
		m = imgPat.search(text)
		ps = 1
		while m:
			if ps > 1:
				print("%d: text '%s'\nbecame\n'%s'"%(ps,q,text))
				if ps>8:
					break
			if m.group('src') is None:
				print("woah, empty image source")
				break
			url = m.group('src')
			extra = ' | absolute_url' if re.search('http',url) else ''
			# print("%s -> {%s}"%(url,extra))
			text = ''
			if m.group('prior') is not None:
				text = text + m.group('prior') + '\n'
			text = text + '\n!'
			if m.group('title') is not None:
				text = text+'['+m.group('title')+']'
			elif m.group('alt') is not None:
				text = text+'['+m.group('alt')+']'
			else:
				text = text + '['+self.name+']'
			if m.group('align') is None:
				text = text + "({{ '%s'%s }})"%(url,extra)
			elif m.group('align') == 'right':
				text = text + "({{ '%s'%s }}){: .align-right}"%(url,extra)
			elif m.group('align') == 'left':
				text = text + "({{ '%s'%s }}){: .align-left}"%(url,extra)
			elif m.group('align') == 'center':
				text = text + "({{ '%s'%s }}){: .align-center}"%(url,extra)
			else:
				print("align was <%s>?"%(m.group('align')))
			if m.group('post') is not None:
				text = text + '\n' + m.group('post')
			text = text+'\n'
			# if re.match('Fran',text):
			# 	print(text)
			# 	exit()
			ps = ps + 1
			m = imgPat.search(text)
		return text

	def write_post(self):
		if self.content['BODY'] == '':
			print("empty post, none written")
			return
		# prepare text formattng and tagging
		b = self.content['BODY']
		if re.sub('\s+','',self.content['EXTENDED BODY']) != '':
			b = b+ '\n<!--more-->\n' + self.content['EXTENDED BODY']
		if self.convert:
			b = self.kramdown(b)
		self.autotag(b)
		# now we can write
		destFolder = '_posts' if self.publish else '_drafts'
		postPath = os.path.join(destFolder,self.post_name())
		f = open(postPath,'w')
		f.write('---\n')
		f.write('layout: post\n')
		f.write('title: "%s"\n'%(self.name))
		if self.tagTest:
			f.write('categories: [%s]\n'%(self.content['category']))
			if len(self.content['categories']) > 0:
				f.write('tags: [%s]\n'%(','.join(self.content['categories'])))
		elif self.useAutoTags:
			cat = self.content['category'] if self.content['category'] != '' else 'general'
			f.write('categories: [%s]\n'%(cat))
			if len(self.content['tags']) > 0:
				f.write('tags: [%s]\n'%(','.join(list(self.content['tags'].keys()))))
		else:
			if len(self.content['categories']) < 2:
				f.write('categories: [%s]\n'%(self.content['category']))
			else:
				'to-do: slice out primary category FIRST'
				f.write('categories: [%s]\n'%(','.join(self.content['categories'])))
		f.write('---\n')
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
		b = re.sub('"/pix20','"http://www.botzilla.com/pix20',b)
		try:
			b = b.encode('utf8')
		except:
			# print("Woah, '%s'"%(b))
			if self.publish:
				print("Unexpected error in %s:"%(self.name), sys.exc_info())
		return b if not self.convert else self.kramdown(b)

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
				self.convert = 'default' in m.groups()[0]
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
