import re
import operator

#w = 'blind'
#p = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
 
    
#w = 'Muzi'
#p = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
        
def solution(word, pages):
    basic_score = {} # set
    link_count = {} # set
    url_link = [] # list .. (url, link)를 튜플 형식으로..
    link_score = {} # set
    final_score = {}
    idx_url = [] # list
    answer = [] # list
    url_group = []
    
    # 최종점수 = 기본점수 + 링크점수
    
    # idx = 0 ... (x)
    # 단순히 index로 페이지를 나누면 안됨. 자신이 어떤 url의 사이트인지 표기 필수 !
    # <meta property="og:url" content="https://c.com"/>
    
    idx = 0 # 순서 나타내기 위한 인덱스
    
    for page in pages:
        
        # 자신의 url 알아내기 (가장먼저)
        temp = page.split('content="https://')[1:]
        # print(temp)
        url = temp[0].split('"')[0]
                
        idx_url.append( (idx, url) )
        
        # 1.기본점수 (대소문자 구분x)
        basic_score[url] = re.sub('[^a-z]', ';', page.lower()).split(';').count(word.lower()) # 전부 소문자로 치환 
        
        # 외부 링크수 
        c = 0
        link_group = page.split('a href="https://')[1:] # a href가 여러개일 수 있음 
        
        for link in link_group:
            if link.split('"')[0]:
                c += 1
                url_link.append( (url, link.split('"')[0]) )
        link_count[url] = c
        
        url_group.append(url)
        
        idx += 1
        c = 0
        
    # 2.링크점수 (곧바로 해당 url 점수에 반영)
    for url, link in url_link:
        if link in link_score:
            link_score[link] += basic_score[url] / link_count[url]
        else:
            link_score[link] = basic_score[url] / link_count[url]
        
    
    #print(basic_score)
    #print(link_count)
    #print(url_link)
    #print(link_score)
    
    # 최종 점수 (기본점수 + 링크점수)
    final_score = {}
    for url in basic_score: # 기본점수
        final_score[url] = basic_score[url]
    for url in link_score:
        if url in final_score: # "기본점수에 들어있는 url만" 해당하도록 !!!!!!
            final_score[url] += link_score[url]
        
    #print(final_score)  # {'a.com': 4.5, 'b.com': 4.0, 'c.com': 1.5}
    
    max_value = 0
    index = -1
    c2 = 0
    for url in url_group:
        if final_score[url] > max_value:
            max_value = final_score[url]
            index = c2
        c2 += 1
    return index

#solution(w, p)