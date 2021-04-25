
# coding: utf-8

# In[8]:


from collections import OrderedDict
def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text
URL=Segment=Sub_Segment=Sub_Sub_Segment=Sub_Sub_Sub_Segment=Price=Source_offer_price=Brand=Model_no=DisplayName=Description=Subtitle=Specifications=Features=Image_URLS=breadcrumb=Size=Color=Categories=Tags=""
Brand="Nykaa Fashion"
ns_active_flag="1"
source_affiliates="B2B"
head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
"Accept": "*/*",
"Accept-Language": "en-US,en;q=0.5",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"X-Requested-With": "XMLHttpRequest",
"Origin": "https://www.bennye.com",
"Connection": "keep-alive",
"Referer": "https://www.bennye.com/product/artistry/face-body-paint/creme-colors/",
"Cache-Control": "max-age=0"}
new=[]
allz=[]
try:
    dfd=pd.read_csv('Done URL.csv')
    df1d=dfd['URL']
    df2d=list(df1d)
    for idd in range(len(df2d)):
        linkd=df2d[idd]
        allz.append(linkd)
except:
    pass
try:
    ndfd=pd.read_csv('Not Done URL.csv')
    ndf1d=ndfd['NotURL']
    ndf2d=list(ndf1d)
    for nidd in range(len(ndf2d)):
        nlinkd=ndf2d[nidd]
        new.append(nlinkd)
except:
    pass
def parse(soupd1e):
    try:
        soups=yaml.load(soupd1e)
        try:
            Image_URLS1=soups['details']['skuData']['product']['productMedia']
            Image_URLS2=[]
            for Image_URLS3 in Image_URLS1:
                Image_URLS4=Image_URLS3['url']
                Image_URLS2.append(Image_URLS5)
            Image_URLS=(' ~ ').join(Image_URLS2)
            print(Image_URLS)
        except:
            Image_URLS=""
        try:
            des=soups['details']['skuData']['product']['productInfo']
            des4=[]
            for des1 in des:
                des2=des1['title']
                if des2=="Description":
                    des3=des1['value']
                    des4.append(des3)
            Description=(' ~ ').join(des4).replace('u003cbru003e',' ')
            print(Description)
        except:
            Description=""
        try:
            Floor_Pla=soups['details']['skuData']['product']['productInfo']
            Floor_Pl=[]
            for Floor_Pl1 in Floor_Pla:
                Floor_Pl2=Floor_Pl1['slug']
                if Floor_Pl2=="address_of_manufacturer":
                    Floor_Pl3=Floor_Pl1['value']
                    Floor_Pl.append(Floor_Pl3)
            Address=(' ~ ').join(Floor_Pl).replace('u003cbr/u003e',' ')
            print(Address)
        except:
            Address=""
        try:
            adds=Address.replace(' ','')
            phoneNumRegex = re.compile(r'\d\d\d\d\d\d') 
            mo = phoneNumRegex.search(str(adds)) 
            pincode=mo.group()
        except:
            pincode=" "
        print(pincode)

        try:
            Floor_Pla=soups['details']['skuData']['product']['productInfo']
            Floor_Pl=[]
            for Floor_Pl1 in Floor_Pla:
                Floor_Pl2=Floor_Pl1['slug']
                if Floor_Pl2=="name_of_manufacturer":
                    Floor_Pl3=Floor_Pl1['value']
                    Floor_Pl.append(Floor_Pl3)
            manufacturer=(' ~ ').join(Floor_Pl).replace('u003cbr/u003e',' ')
            print(manufacturer)
        except:
            manufacturer=""
        try:
            Floor_Pla=soups['details']['skuData']['product']['productInfo']
            Floor_Pl=[]
            for Floor_Pl1 in Floor_Pla:
                Floor_Pl2=Floor_Pl1['slug']
                if Floor_Pl2=="sold_by":
                    Floor_Pl3=Floor_Pl1['value']
                    Floor_Pl.append(Floor_Pl3)
            sold_by=(' ~ ').join(Floor_Pl)
            print(sold_by)
        except:
            sold_by=""
        try:
            Floor_Pla=soups['details']['skuData']['product']['productInfo']
            Floor_Pl=[]
            for Floor_Pl1 in Floor_Pla:
                Floor_Pl2=Floor_Pl1['slug']
                if Floor_Pl2=="pack_contains":
                    Floor_Pl3=Floor_Pl1['value']
                    Floor_Pl.append(Floor_Pl3)
            pack_contains=(' ~ ').join(Floor_Pl)
            print(pack_contains)
        except:
            pack_contains=""
        try:
            Floor_Pla=soups['details']['skuData']['product']['meta_data']['keywords']
            Floor_Pla1=Floor_Pla.split(',')
            try:
                Segment=Floor_Pla1[1]
            except:
                Segment=""
            try:
                Sub_Segment=Floor_Pla1[2]
            except:
                Sub_Segment=""
            try:
                Sub_Sub_Segment=Floor_Pla1[3]
            except:
                Sub_Sub_Segment=""
            try:
                Sub_Sub_Sub_Segment=Floor_Pla1[4]
            except:
                Sub_Sub_Sub_Segment=""
            print(Segment)
            print(Sub_Segment)
            print(Sub_Sub_Segment)
            print(Sub_Sub_Sub_Segment)
        except:
            Segment=""
            Sub_Segment=""
            Sub_Sub_Segment=""
            Sub_Sub_Sub_Segment=""
        try:
            Floor_Pla=soups['details']['skuData']['product']['productInfo']
            Floor_Pl=[]
            for Floor_Pl1 in Floor_Pla:
                try:
                    Floor_Pl2=Floor_Pl1['attributes']
                    for sos in Floor_Pl2:
                        sos1=sos['key']+":"
                        Floor_Pl.append(sos1)
                        sos2=sos['value']+"~"
                        Floor_Pl.append(sos2)
                except:
                    pass
            Specifications=(' ~ ').join(Floor_Pl).replace(': ~ ',':').replace('~ ~ ','~').replace('u003cbru003e',' ')
            print(Specifications)
        except:
            Specifications=""
        soups1=soups['details']['skuData']['product']['sizeOptions']
        for soup in soups1:
            try:
                nam=soup['title']
                od = OrderedDict([('u003cbr/u003e',' '),('\n',' '),('\r',''),('\t',''),('  ',''),('Product Specifications',''),('  ','')])
                DisplayName=replace_all(str(nam),od)
                print(DisplayName)
            except:
                DisplayName=""
            try:
                cod=soup['color']['name']
                od = OrderedDict([('u003cbr/u003e',' '),('\n',''),('\r',''),('\t',''),('[',''),(']',''),('\'',''),('~',''),('Color',''),('Tile Size',''),(':',''),('"',''),('',''),('}','')])
                Color=replace_all(str(cod),od)
                print(Color)
            except:
                Color=""
            try:
                cod=soup['price']
                od = OrderedDict([('u003cbr/u003e',' '),('\n',''),('\r',''),('\t',''),('[',''),(']',''),('\'',''),('~',''),('Color',''),('Tile Size',''),(':',''),('"',''),('',''),('}','')])
                Price=replace_all(str(cod),od)
                print(Price)
            except:
                Price=""
            try:
                cod=soup['discountedPrice']
                od = OrderedDict([('u003cbr/u003e',' '),('\n',''),('\r',''),('\t',''),('[',''),(']',''),('\'',''),('~',''),('Color',''),('Tile Size',''),(':',''),('"',''),('',''),('}','')])
                Source_offer_price=replace_all(str(cod),od)
                print(Source_offer_price)
            except:
                Source_offer_price=""
            try:
                cod=soup['sku']
                od = OrderedDict([('u003cbr/u003e',' '),('\n',''),('\r',''),('\t',''),('[',''),(']',''),('\'',''),('~',''),('Color',''),('Tile Size',''),(':',''),('"',''),('',''),('}','')])
                Model_no=replace_all(str(cod),od)
                print(Model_no)
            except:
                Model_no=""
            try:
                nam=soup['subTitle']
                od = OrderedDict([('u003cbr/u003e',' '),('\n',' '),('\r',''),('\t',''),('  ',''),('Product Specifications',''),('  ','')])
                Subtitle=replace_all(str(nam),od)
                print(Subtitle)
            except:
                Subtitle=""
            try:
                nam=soup['sizeName']
                od = OrderedDict([('u003cbr/u003e',' '),('\n',' '),('\r',''),('\t',''),('  ',''),('Product Specifications',''),('  ','')])
                Size=replace_all(str(nam),od)
                print(Size)
            except:
                Size=""
            row=[URL,Segment,Sub_Segment,Sub_Sub_Segment,Sub_Sub_Sub_Segment,Price,Source_offer_price,Brand,Model_no,DisplayName,Subtitle,Description,Specifications,Features,Image_URLS,breadcrumb,Size,Color,Categories,Tags,Address,pincode,manufacturer,sold_by,pack_contains]
            with open('Nykaa Fashion.csv','a',encoding='utf-8',newline='') as writeFile:
                writer = csv.writer(writeFile,delimiter='|')
                writer.writerow(row)
            allz.append(URL)
            row=[URL]
            with open('Done URL.csv','a',encoding='utf-8',newline='') as writeFile:
                writer = csv.writer(writeFile,delimiter='|')
                writer.writerow(row)
    except:
        if URL not in new:
            new.append(URL)
            row=[URL]
            with open('Not Done URL.csv','a',encoding='utf-8',newline='') as writeFile:
                writer = csv.writer(writeFile,delimiter='|')
                writer.writerow(row)
    return
mainlink=["https://www.nykaafashion.com/rest/appapi/V2/categories/products?categoryId=3&PageSize=50&sort=popularity&currentPage=","https://www.nykaafashion.com/rest/appapi/V2/categories/products?categoryId=4&PageSize=50&sort=popularity&currentPage=","https://www.nykaafashion.com/rest/appapi/V2/categories/products?categoryId=89&PageSize=50&sort=popularity&currentPage=","https://www.nykaafashion.com/rest/appapi/V2/categories/products?categoryId=6266&PageSize=50&sort=popularity&currentPage=","https://www.nykaafashion.com/rest/appapi/V2/categories/products?categoryId=3528&PageSize=50&sort=popularity&currentPage=","https://www.nykaafashion.com/rest/appapi/V2/categories/products?categoryId=77&PageSize=50&sort=popularity&currentPage=","https://www.nykaafashion.com/rest/appapi/V2/categories/products?categoryId=3946&PageSize=50&sort=popularity&currentPage=","https://www.nykaafashion.com/rest/appapi/V2/categories/products?categoryId=104&PageSize=50&sort=popularity&currentPage=","https://www.nykaafashion.com/rest/appapi/V2/categories/products?categoryId=6824&PageSize=50&sort=popularity&currentPage=","https://www.nykaafashion.com/rest/appapi/V2/categories/products?categoryId=6834&PageSize=50&sort=popularity&currentPage=","https://www.nykaafashion.com/rest/appapi/V2/categories/products?categoryId=6857&PageSize=50&sort=popularity&currentPage=","https://www.nykaafashion.com/rest/appapi/V2/categories/products?categoryId=6888&PageSize=50&sort=popularity&currentPage=","https://www.nykaafashion.com/rest/appapi/V2/categories/products?categoryId=6800&PageSize=50&sort=popularity&currentPage="]
for j in range(len(mainlink)):
    for i in range(1,5001):
        makelink= mainlink[j]+str(i)+"&filter_format=v2&currency=INR&country_code=IN"
        print(makelink)
        makelinkresponce=requests.get(makelink,headers=head)
        lo2=makelinkresponce.json()
        try:
            lo3=lo2['response']['products']
            for lo4 in lo3:
                lo5=lo4['actionUrl']
                if lo5[0:5]!="https":
                    URL="https://www.nykaafashion.com"+lo5
                    print(URL)
                    if URL not in allz:
                        responce=requests.get(URL,headers=head)
                        soupd=BeautifulSoup(responce.text,'html.parser')
                        findbyid=soupd.find(attrs={'id':'__PRELOADED_STATE__'})
                        ex1=re.findall('\"application/json\">.*?</script>',str(findbyid))
                        ex2=re.findall('\"details\".*?\},\"widgets\"',str(ex1))
                        od = OrderedDict([('\n',' '),('\r',''),('\t',''),('  ',''),('[\'','{'),(',\"widgets\"\']','}'),('\\',''),('""','\\""')])
                        soupde=replace_all(str(ex2),od)
                        soupd1e=soupde.encode()
                        parse(soupd1e)
                        
        except:
            break

