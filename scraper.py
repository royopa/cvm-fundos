# -*- coding: utf-8 -*-
from __future__ import print_function
import scraperwiki
import lxml.html
import os

os.environ['SCRAPERWIKI_DATABASE_NAME'] = 'sqlite:///data.sqlite'

# # Read in a page
for pk_partic in range(1, 990156):
    print(str(pk_partic), end=' ')
	url = 'http://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/DemContabeis/CPublicaDemContabeisFI.aspx?PK_PARTIC={}'
    pk_partic = str(pk_partic)
    html = scraperwiki.scrape(url.format(pk_partic))
    
    # Find something on the page using css selectors
    root = lxml.html.fromstring(html)

    try:
        cnpj = root.get_element_by_id("lbNrPfPj").text.replace('.', '').replace('-', '').replace('/', '')    
    except Exception as e:
        continue

    data = {
        "pk_partic": pk_partic,
        "cnpj": cnpj
    }

    # Write out to the sqlite database using scraperwiki library
    scraperwiki.sqlite.save(unique_keys=['pk_partic'], data=data)
