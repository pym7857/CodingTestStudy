import java.util.HashMap;

public class OpenChat {
    public String[] solution(String[] record) {
    	//찍힌 로그의 개수, 들어왔다 나갔다 개수, 결과의 개수
        int logCount = record.length;
        int ioCount = 0;
        int num = 0;
        //해시 맵
        HashMap<String, String> hs = new HashMap<String, String>();

        for(int i=0; i<logCount;i++){			//들어오고 나간 수 계산
            String[] tmp = spl(record[i]);      //로그를 토큰화

            if(tmp[0].equals("Enter")){         
                if(hs.containsKey(tmp[1])){     //다시 들어온 경우
                    hs.remove(tmp[1]);
                    hs.put(tmp[1],tmp[2]);
                }else{                          //처음 들어온 경우
                    hs.put(tmp[1],tmp[2]);
                }
                ioCount++;
            }else if(tmp[0].equals("Change")){  //닉네임 변경
                hs.remove(tmp[1]);
                hs.put(tmp[1],tmp[2]);
            }else if(tmp[0].equals("Leave")){   //나가는 경우
                ioCount++;
            }

        }

        String[] answer = new String[ioCount];   //결과 입력 변수

        for(int i=0; i<logCount;i++){
            String[] tmp = spl(record[i]);

            if(tmp[0].equals("Enter"))           //들어온 경우 텍스트
                answer[num++] = hs.get(tmp[1]) + "님이 들어왔습니다.";
            else if(tmp[0].equals("Leave"))
                answer[num++] = hs.get(tmp[1]) + "님이 나갔습니다.";

        }
        return answer;
    }
    public String[] spl(String prev){            //split
        String[] result = prev.split(" ");
        return result;
    }
}