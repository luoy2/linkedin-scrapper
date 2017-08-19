from urllib import request
import re
from render import selenium_render
import multiprocessing
from tqdm import tqdm
# soup = BeautifulSoup(response, 'lxml')
# index_list = [i.get_text() for i in soup.find_all('li')]

def get_urls():
    url = 'http://www.deeplearningbook.org/'
    response = request.urlopen(url)
    html_string = response.read().decode('utf-8')
    title_pattern = re.compile(r'<li.*<a href=(?P<url>.*)>(?P<name>.*)</a></li>')
    result = title_pattern.finditer(html_string)
    result_dict_list = [m.groupdict() for m in result]
    return result_dict_list

def single_page_workder(single_page):
    url = 'http://www.deeplearningbook.org/'
    full_url = url + re.findall(r'^"(.*)"$', single_page['url'])[0]
    data = selenium_render(full_url)
    # check if file name is legal
    file_name = re.sub('[^\w\s-]', '', single_page['name'])
    file = open('deep_learning_book/{}.html'.format(file_name),"wb") #open file in binary mode
    file.write(bytes(data, encoding='utf-8'))
    file.close()

if __name__ == '__main__':
    url_list = get_urls()
    p = multiprocessing.Pool(processes=multiprocessing.cpu_count()*2)
    for _ in tqdm(p.imap_unordered(single_page_workder, url_list), total=len(url_list)):
        pass