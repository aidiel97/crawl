from bs4 import BeautifulSoup
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def CrawlLpsePuData(page):
    req = requests.Session() #membuat session
    res = [] #list untuk menyimpan data seluruh pemenang

    # crawling sejumlah halaman yang ditentukan
    for i in range(1,page+1):
        url = 'https://lpse.pu.go.id/eproc/lelang/pemenangcari'
        
        if(i > 1):
            url = 'https://lpse.pu.go.id/eproc/lelang/pemenangcari.gridtable.pager/'+str(i)+'?_csrf='+requestsParameters 
            
        # awal mula pengambilan data dari halaman (sesuai dengan URL)
        page = req.get(url, verify=False)
        soup = BeautifulSoup(page.content, 'html5lib')

        # simpan token csrf untuk akses halaman (URL)
        csrf = soup.find('input', attrs = {'name' : '_csrf'})
        requestsParameters = csrf['value']

        print('Load all data on page '+str(i)+'...') #cek proses sudah sampai halaman berapa

        # dicari yang mempunyai atribut 'PEMENANG'
        for content in soup.find_all('a', attrs={'class' : 'jpopup'}, text='Pemenang'):
            # setelah data didapat, diambil link yang menuju data terkait pemenang
            urlDetail = 'https://lpse.pu.go.id'+content['href']
            
            # pengambilan data pada link baru
            pageDetail = requests.get(urlDetail, verify=False)
            soupD = BeautifulSoup(pageDetail.content, 'html5lib')
            detailSoup = soupD.find('table')

            detailData = {} #dictionary, untuk menyimpan data setiap pemenang

            for data in detailSoup.find_all('tr'):
                k = data.find('td', attrs={'class' : 'TitleLeft'}) #keterangan data
                v = data.find('td', attrs={'class' : 'horizLine'}) #data yang dibutuhkan

                key = k.get_text().replace(" ","_") #rapikan data, hilangkan spasi
                value = v.get_text()

                detailData.update({ key : value }) #data yang didapat, disimpan

            res.append(detailData)#data setiap pemenang digabungkan kedalam list

    print('\n\n===============================\nDATA PEMENANG : ')
    return res