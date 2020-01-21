import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.PriorityQueue;

class Muzi {
    class Time implements Comparable<Time>{//남은 시간 저장할 클래스
        int times;     
        Time(int times){
            this.times = times;
        }
        @Override
        public int compareTo(Data target) {
            if (times > target.times) {
                return 1;
            }
            else {
                return -1;
            }
        }
    }
    public int solution(int[] food_times, long k) {
        int answer = 0;
        PriorityQueue<TIme> minHeap = new PriorityQueue();
        int max = -1;
        int timeLen = food_times.length;
        long cnt = 0;
        long prev = 0;
        
        for (int i=0; i<timeLen; i++) {//우선순위 큐 생성
            if (food_times[i] > max) {//제일 큰값 저장
                max = food_times[i];
            }
            minHeap.offer(new Time(food_times[i]));
        }
        
        while (cnt <= k) { //음식 양이 아직 더 작을때
            if (minHeap.isEmpty()) {
                return -1;
            }
            Time data = minHeap.poll();//큐에서 하나 빼기
            if ( prev != 0 && prev == data.times) {
                timeLen--;
                continue;
            }
            cnt += (data.times - prev) * (timeLen);//지난 시간 측정
            timeLen--;//하나 다먹었으므로 배열의 길이 하나 빼줌
            prev = data.times;//이전에 다 먹은 음식의 양을 기억하기 위해 저장
        }
        
        int index = food_times.length - 1;
        while (cnt != k) {
            if (food_times[index] >= prev) {//아직 남아 있는 음식의 경우 cnt를 빼줌 ==> k와 같아 질때 까지
                cnt--;
            }
            index--;//인덱스를 하나씩 줄여나감
            if (index < 0) {//한 바퀴 돌면 다시 처음으로 인덱스를 초기화 해준다
                index = food_times.length - 1;
            }
        }
        if (index + 2 > food_times.length) {//인덱스가 최대 길이보다 커진 경우는 1밖에 없으므로 예외 처리
            return 1;
        } else {//그 외의 경우
            return index + 2;
        }
    }
}