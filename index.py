import crawler
if __name__ == '__main__':
    print('===============================')
    print('Silahkan input jumlah halaman : ')
    n = int(input())
    print('===============================\n\n')


    # PEMANGGILAN FUNGSI CrawlLpsePuData(total Halaman yang ingin di crawling)
    data = crawler.CrawlLpsePuData(n)
    print(data)