import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.PriorityQueue;

class Muzi {
    class Time implements Comparable<Time>{//���� �ð� ������ Ŭ����
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
        
        for (int i=0; i<timeLen; i++) {//�켱���� ť ����
            if (food_times[i] > max) {//���� ū�� ����
                max = food_times[i];
            }
            minHeap.offer(new Time(food_times[i]));
        }
        
        while (cnt <= k) { //���� ���� ���� �� ������
            if (minHeap.isEmpty()) {
                return -1;
            }
            Time data = minHeap.poll();//ť���� �ϳ� ����
            if ( prev != 0 && prev == data.times) {
                timeLen--;
                continue;
            }
            cnt += (data.times - prev) * (timeLen);//���� �ð� ����
            timeLen--;//�ϳ� �ٸԾ����Ƿ� �迭�� ���� �ϳ� ����
            prev = data.times;//������ �� ���� ������ ���� ����ϱ� ���� ����
        }
        
        int index = food_times.length - 1;
        while (cnt != k) {
            if (food_times[index] >= prev) {//���� ���� �ִ� ������ ��� cnt�� ���� ==> k�� ���� ���� ����
                cnt--;
            }
            index--;//�ε����� �ϳ��� �ٿ�����
            if (index < 0) {//�� ���� ���� �ٽ� ó������ �ε����� �ʱ�ȭ ���ش�
                index = food_times.length - 1;
            }
        }
        if (index + 2 > food_times.length) {//�ε����� �ִ� ���̺��� Ŀ�� ���� 1�ۿ� �����Ƿ� ���� ó��
            return 1;
        } else {//�� ���� ���
            return index + 2;
        }
    }
}