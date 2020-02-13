import java.util.*;
class FindPath {
    class Node{//��� Ŭ����
        int x;
        int y;
        int index;
        Node left;
        Node right;
        
        Node(int x,int y,int index){//������
            this.x = x;
            this.y = y;
            this.index = index;
            this.left = null;
            this.right = null;
        }
    }
    class Tree{//Ʈ�� Ŭ����
        Node root;
        int[][] arr;//answer�� ������ �迭
        int pre = 0;//�迭�� �� ������ ����� �ε���
        int post = 0;//�迭�� �� ������ ����� �ε���
        
        Tree(Node newNode){//������
            this.root = newNode;
        }
        
        public void preorder(Node root){//���� ��ȸ
            if(root != null){//��Ʈ�� ���� ������
                arr[0][pre++] = (root.index);//�ش� ��Ʈ�� �ε����� �迭�� �ִ´�
                preorder(root.left);//left���� Ž��
                preorder(root.right);//right Ž��
            }
       }
       public void postorder(Node root){//���� ��ȸ == �������� ������ Ž��
           if(root != null){
                postorder(root.left);
                postorder(root.right);
                arr[1][post++] = (root.index);
            }
       }
    }
    
    public int[][] solution(int[][] nodeinfo) {
        int[][] answer = {};
        int nodeLen = nodeinfo.length; //nodeinfo �迭�� ũ�� ����
        ArrayList<Node> list = new ArrayList<Node>();
        for(int i=0;i<nodeLen;i++){//��带 ����Ʈ�� �߰�
            list.add(new Node(nodeinfo[i][0], nodeinfo[i][1], i+1));
        }
        
        Collections.sort(list, new Comparator<Node>(){//������ �迭 y�� �������� ����
            @Override
            public int compare(Node a,Node b){
                return b.y - a.y;
            }
        });
        Tree myTree = new Tree(list.get(0));//Ʈ�� ����
        myTree.arr = new int[2][nodeLen];//�迭 ����
        
        for(int i=1;i<nodeLen;i++){//����� ������ŭ �ݺ��� ����
            Node tmp = list.get(i);//�̹��� Ʈ���� ���� ��� ����
            Node parent = myTree.root;//�θ� ��� ����
            
            while(true){
                if(tmp.x < parent.x){//���� ���� ����� x���� �θ��� x���� ũ��
                    if(parent.left != null){//�θ��� left�� �������� �θ��� left�� �θ���� �ø���.
                        parent = parent.left;
                    }else{//���� ���� ����� x���� �θ��� x���� �۰ų� ������
                        parent.left = new Node(tmp.x, tmp.y, tmp.index); //���ο� ��带 �θ� ����� left�� �ִ´�
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