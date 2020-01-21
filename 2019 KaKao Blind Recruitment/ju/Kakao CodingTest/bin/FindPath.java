import java.util.*;
class FindPath {
    class Node{//노드 클래스
        int x;
        int y;
        int index;
        Node left;
        Node right;
        
        Node(int x,int y,int index){//생성자
            this.x = x;
            this.y = y;
            this.index = index;
            this.left = null;
            this.right = null;
        }
    }
    class Tree{//트리 클래스
        Node root;
        int[][] arr;//answer에 저장할 배열
        int pre = 0;//배열에 값 넣을때 사용할 인덱스
        int post = 0;//배열에 값 넣을때 사용할 인덱스
        
        Tree(Node newNode){//생성자
            this.root = newNode;
        }
        
        public void preorder(Node root){//전위 순회
            if(root != null){//루트에 뭔가 있으면
                arr[0][pre++] = (root.index);//해당 루트의 인덱스값 배열에 넣는다
                preorder(root.left);//left먼저 탐색
                preorder(root.right);//right 탐색
            }
       }
       public void postorder(Node root){//후위 순회 == 먼저왼쪽 끝부터 탐색
           if(root != null){
                postorder(root.left);
                postorder(root.right);
                arr[1][post++] = (root.index);
            }
       }
    }
    
    public int[][] solution(int[][] nodeinfo) {
        int[][] answer = {};
        int nodeLen = nodeinfo.length; //nodeinfo 배열의 크기 저장
        ArrayList<Node> list = new ArrayList<Node>();
        for(int i=0;i<nodeLen;i++){//노드를 리스트에 추가
            list.add(new Node(nodeinfo[i][0], nodeinfo[i][1], i+1));
        }
        
        Collections.sort(list, new Comparator<Node>(){//이차원 배열 y값 기준으로 정렬
            @Override
            public int compare(Node a,Node b){
                return b.y - a.y;
            }
        });
        Tree myTree = new Tree(list.get(0));//트리 생성
        myTree.arr = new int[2][nodeLen];//배열 선언
        
        for(int i=1;i<nodeLen;i++){//노드의 개수만큼 반복문 돈다
            Node tmp = list.get(i);//이번에 트리에 넣을 노드 저장
            Node parent = myTree.root;//부모 노드 저장
            
            while(true){
                if(tmp.x < parent.x){//새로 들어올 노드의 x값이 부모의 x보다 크면
                    if(parent.left != null){//부모의 left가 차있으면 부모의 left를 부모노드로 올린다.
                        parent = parent.left;
                    }else{//새로 들어올 노드의 x값이 부모의 x보다 작거나 같으면
                        parent.left = new Node(tmp.x, tmp.y, tmp.index); //새로운 노드를 부모 노드의 left에 넣는다
                        break;
                    }
                }else{
                    if(parent.right != null){
                        parent = parent.right;
                    }else{
                        parent.right = new Node(tmp.x, tmp.y, tmp.index);
                        break;
                    }
                }
            }
        }
        myTree.preorder(myTree.root);
        myTree.postorder(myTree.root);
        answer = myTree.arr;

        return answer;
    }
}