
import java.io.*;
import java.util.*;
public class Main {
	public static int [] arr;
	public static boolean [] ch;
	
	public static void DFS (int n, int m, int L) {
		if(m==L) {
			for(int x :arr) {
				System.out.print(x+" ");
			}
			System.out.println();
			return;
		}
		else {
			for(int i =0; i<n;i++) {
				if(ch[i]==false) {
					ch[i] = true;
					arr[L] =i+1;
					DFS(n,m,L+1);
					ch[i]=false;
				}
			}
				}
			}
	public static void main(String[] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	StringTokenizer st = new StringTokenizer(br.readLine());
	int n = Integer.parseInt(st.nextToken());
	int m = Integer.parseInt(st.nextToken());
	arr = new int[m];
	ch = new boolean[n];
	DFS(n,m,0);
	}

}