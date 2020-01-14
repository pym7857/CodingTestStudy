class Solution {
    public int[] solution(int N, int[] stages) {
    	//실패울 index저장,실패율 실제값 저장
        int[] answer = new int[N];
        double[] answerVal = new double[N];
        int stageLen = stages.length;
        int index = 0;

        for(int i=1;i<=N;i++){
        	//해당 스테이지 도전or성공한 사람의 수, 도전중인 사람의 수
            int manCount = 0;
            int failCount = 0;
            
            for(int j=0;j<stageLen;j++){
                if(stages[j] >= i){
                    manCount++;
                    if(stages[j] == i){
                        failCount++;
                    }
                }
            }
            double result = (double)failCount/manCount; //실패율 저장
            //일단 그냥 순서대로 값을 넣어준다.
            answer[index] = i;
            answerVal[index++] = result;
        }

        //selection sort 사용해서 제일큰놈이 앞에 오지만 값이 같을 경우 index 작은놈이 앞에 오게한다.
        for(int i=0; i<index-1; i++){
            int maxIndex = i;

            for(int j=i+1; j<index; j++){
                if(answerVal[j] > answerVal[maxIndex])       //실패율이 더 낮은 경우
                    maxIndex = j;
                else if(answerVal[j] == answerVal[maxIndex]){//실패율이 같은 경우
                     if(answer[j] < answer[maxIndex])		 //실패율은 같고 인덱스는 작은 경우 바꿔줌
                         maxIndex = j;
                }
            }
            swap(answer,maxIndex,i);
            swap(answerVal,maxIndex,i);    //스왑
        }

        return answer;
    }
    //스왑 메소드
    int[] swap(int[] arr,int a,int b){
        int tmp = arr[a];
        arr[a] = arr[b];
        arr[b] = tmp;
        return arr;
    }
    double[] swap(double[] arr,int a,int b){
        double tmp = arr[a];
        arr[a] = arr[b];
        arr[b] = tmp;
        return arr;
    }
}