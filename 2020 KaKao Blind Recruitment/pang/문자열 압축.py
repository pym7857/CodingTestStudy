def solution(s):
    def compress(size):
        ret = 0
        before, count = s[:size], 1 #점수 매기기
        for i in range(size, len(s), size):#사이즈만큼 반복
            word = s[i:i+size] 
            if word == before:
                count += 1 #줄여질 수 있으면 점수 증가
            else:
                if count > 1:
                    ret += len(str(count)) #점수없을때 반영
                ret += size
                before, count = word, 1#초기화
        if count > 1:
            ret += len(str(count))
        ret += len(before)#마지막반영
        return ret

    ans = len(s)
    for size in range(1, ans+2//2):
        ans = min(ans, compress(size))#모든 경우의 수에 대하여
    return ans
