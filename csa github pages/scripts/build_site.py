#!/usr/bin/env python3
"""Build static GitHub Pages website with per-page absolute SEO URLs and sitemap.
No dependencies. In GitHub Actions the GitHub repository determines the live URL.
For custom domains, add a CNAME file at the site root or pass --site-url.
"""
import argparse
import json
import os
import re
import shutil
from html import escape
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
LANGS = ('tr','en','es','fr','de','pt','zh','ja','ko','ru','nl','az','it','pl')
HREFLANG = {lang: ('zh-Hans' if lang=='zh' else lang) for lang in LANGS}
LOCALES={'tr':'tr_TR','en':'en_US','es':'es_ES','fr':'fr_FR','de':'de_DE','pt':'pt_PT','zh':'zh_CN','ja':'ja_JP','ko':'ko_KR','ru':'ru_RU','nl':'nl_NL','az':'az_AZ','it':'it_IT','pl':'pl_PL'}
TYPES = ('index','gallery','privacy','eula','contact')
ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9')
ET.register_namespace('xhtml','http://www.w3.org/1999/xhtml')


def base_url(override):
    if override:
        base=override.strip().rstrip('/')+'/'
    elif (ROOT/'CNAME').exists():
        domain=(ROOT/'CNAME').read_text('utf8').strip()
        if '/' in domain or ':' in domain or not domain: raise ValueError('CNAME should contain only the domain name')
        base=f'https://{domain}/'
    else:
        repo=os.environ.get('GITHUB_REPOSITORY','')
        if not repo or '/' not in repo:
            raise RuntimeError('Set --site-url https://user.github.io/repository/ or use GitHub Actions.')
        owner,name=repo.split('/',1)
        suffix='' if name.lower()==f'{owner.lower()}.github.io' else f'{name}/'
        base=f'https://{owner.lower()}.github.io/{suffix}'
    p=urlsplit(base)
    if p.scheme!='https' or not p.netloc or p.query or p.fragment: raise ValueError('A valid HTTPS site URL is required')
    return base


def route(lang,ptype):
    prefix='' if lang=='tr' else lang+'/'
    return prefix + ('' if ptype=='index' else ptype+'.html')


def build(base):
    output=ROOT/'_site'
    if output.exists(): shutil.rmtree(output)
    output.mkdir()
    shutil.copytree(ROOT/'assets',output/'assets')
    shutil.copyfile(ROOT/'.nojekyll',output/'.nojekyll')
    if (ROOT/'CNAME').exists(): shutil.copyfile(ROOT/'CNAME',output/'CNAME')
    for lang in LANGS:
        out_dir=output if lang=='tr' else output/lang
        out_dir.mkdir(exist_ok=True)
        for ptype in TYPES:
            page=ROOT/(lang if lang!='tr' else '')/(ptype+'.html')
            source=page.read_text('utf8')
            head=re.search(r'</head\s*>',source,re.I)
            if not head: raise ValueError(f'Missing head in {page}')
            title_match=re.search(r'<title>(.*?)</title>',source,re.I|re.S)
            meta_match=re.search(r'<meta\s+[^>]*name="description"[^>]*>',source,re.I|re.S)
            if not title_match or not meta_match:raise ValueError(f'Missing title or description: {page}')
            title=__import__('html').unescape(re.sub(r'<[^>]+>','',title_match.group(1)))
            desc_match=re.search(r'content="([^"]*)"',meta_match.group(0))
            description=__import__('html').unescape(desc_match.group(1)) if desc_match else title
            canonical=base+route(lang,ptype)
            meta=[f'<link rel="canonical" href="{escape(canonical,quote=True)}">']
            for other in LANGS:
                meta.append(f'<link rel="alternate" hreflang="{HREFLANG[other]}" href="{escape(base+route(other,ptype),quote=True)}">')
            meta.append(f'<link rel="alternate" hreflang="x-default" href="{escape(base+route("tr",ptype),quote=True)}">')
            for name,value in [('og:type','website'),('og:site_name','Car Service Archiver'),('og:locale',LOCALES[lang]),('og:title',title),('og:description',description),('og:url',canonical),('og:image',base+'assets/social-preview.png'),('og:image:width','1200'),('og:image:height','630')]:
                meta.append(f'<meta property="{name}" content="{escape(value,quote=True)}">')
            meta.extend(['<meta name="twitter:card" content="summary_large_image">',f'<meta name="twitter:title" content="{escape(title,quote=True)}">',f'<meta name="twitter:description" content="{escape(description,quote=True)}">',f'<meta name="twitter:image" content="{escape(base+"assets/social-preview.png",quote=True)}">'])
            graph={"@context":"https://schema.org","@type":"SoftwareApplication" if ptype=='index' else 'WebPage',"name":"Car Service Archiver" if ptype=='index' else title,"url":canonical,"description":description,"inLanguage":lang}
            if ptype=='index':graph.update({"operatingSystem":"Windows","applicationCategory":"BusinessApplication","brand":{"@type":"Brand","name":"KupferSoft"},"image":base+'assets/social-preview.png',"sameAs":"https://apps.microsoft.com/detail/9N3FVX0PR4BX"})
            # Never fabricate ratings, reviews, or business identity; store link was supplied by the product owner.
            meta.append('<script type="application/ld+json">'+json.dumps(graph,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')+'</script>')
            result=source[:head.start()]+''.join(meta)+source[head.start():]
            (out_dir/(ptype+'.html')).write_text(result,encoding='utf8')
    ns='{http://www.sitemaps.org/schemas/sitemap/0.9}'
    xh='{http://www.w3.org/1999/xhtml}'
    root=ET.Element(ns+'urlset')
    for lang in LANGS:
        for ptype in TYPES:
            u=ET.SubElement(root,ns+'url')
            ET.SubElement(u,ns+'loc').text=base+route(lang,ptype)
            for other in LANGS:
                ET.SubElement(u,xh+'link',attrib={'rel':'alternate','hreflang':HREFLANG[other],'href':base+route(other,ptype)})
            ET.SubElement(u,xh+'link',attrib={'rel':'alternate','hreflang':'x-default','href':base+route('tr',ptype)})
    ET.ElementTree(root).write(output/'sitemap.xml',encoding='utf-8',xml_declaration=True)
    (output/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {base}sitemap.xml\n',encoding='utf8')
    print(f'Build finished: {len(LANGS)*len(TYPES)} pages, sitemap.xml, robots.txt at {output}. URL: {base}')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--site-url',help='Full public site base URL, including any repository folder')
    args=parser.parse_args()
    build(base_url(args.site_url))
