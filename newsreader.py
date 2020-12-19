import justpy as jp
import feedparser

NewsFeed = feedparser.parse("http://feeds.feedburner.com/realclimate/HYVV?format=xml")
title_rc = NewsFeed.entries[0].title
summary_rc = NewsFeed.entries[0].summary
summary_rc = summary_rc.replace('&#8217;','\'')
summary_rc = summary_rc.replace('&#8230;','...')
link_rc = NewsFeed.entries[0].links[0].href

content_rc = NewsFeed.entries[0].content[0].value
img_index1 = content_rc.find('src')
img_index2 = content_rc.find('width')
img_link_rc = content_rc[img_index1+5:img_index2-2]

NewsFeed = feedparser.parse("https://scilogs.spektrum.de/klimalounge/feed/")
title_kl = NewsFeed.entries[0].title
summary_kl = NewsFeed.entries[0].summary
summary_end = summary_kl.find('</p>')
summary_kl = summary_kl[3:summary_end]
summary_kl = summary_kl.replace('&#8217;','\'')
summary_kl = summary_kl.replace('&#8230;','...')
link_kl = NewsFeed.entries[0].links[0].href

content_kl = NewsFeed.entries[0].content[0].value
img_index1 = content_kl.find('src')
img_index2 = content_kl.find('width')
img_link_kl = content_kl[img_index1+5:img_index2-2]


def newsreader():
    wp = jp.WebPage()


    rc_div = jp.Div(classes='border m-2 p-2 w-200', a=wp)
    title_element = jp.get_tag('strong',a=rc_div,text='RealClimate',classes='text-4x1')
    jp.P(a=rc_div, text='ist ein englischsprachiger Blog gegründet und betrieben von den Klimawissenschaftlern Gavin Schmidt (NASA/Columbia University),\
        Michael E. Mann (Penn State University), Rasmus Benestad (Met Norway), Ray Bradley (University of Massachusetts, Amherst),\
        Stefan Rahmstorf (Potsdam Institute for Climate Impact Research), Eric Steig (University of Washington), David Archer (University of Chicago)\
        und Raymond T. Pierrehumbert (University of Chicago). Hier findet Ihr die aktuellsten Artikel:')

    jp.Br(a=rc_div)
    title_element = jp.get_tag('strong',a=rc_div,text=title_rc,classes='text-3x1')
    jp.P(a=rc_div,text=summary_rc)
    jp.A(href=link_rc,a=rc_div,text='Hier geht\'s zum Artikel...',classes='mt-3 text-base text-blue-600 underline',target='_blank')
    jp.Br(a=rc_div)

    image = jp.Img(src=img_link_rc, a=rc_div)
    image.height = 400
    image.width = 400

    jp.Br(a=rc_div)

    kl_div = jp.Div(classes='border m-2 p-2 w-200', a=wp)
    title_element = jp.get_tag('strong',a=kl_div,text='KlimaLounge',classes='text-4x1')
    jp.P(a=kl_div, text='ist ein deutschsprachiger Blog von Stefan Rahmstorf (Potsdam Institute for Climate Impact Research). Hier sind die aktuellsten Artikel:')
    jp.Br(a=kl_div)
    title_element = jp.get_tag('strong',a=kl_div,text=title_kl,classes='text-3x1')
    jp.P(a=kl_div,text=summary_kl)
    jp.A(href=link_kl,a=kl_div,text='Hier geht\'s zum Artikel...',classes='mt-3 text-base text-blue-600 underline',target='_blank')

    jp.Br(a=kl_div)

    image = jp.Img(src=img_link_kl, a=kl_div)
    image.height = 400
    image.width = 400

    return wp

jp.justpy(newsreader)
