// package baekjoon;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        Deque<Integer> queue = new ArrayDeque<>();

        for (int i = 1; i <= n; i++) {
            queue.add(i);
        }

        while(queue.size() > 1) {
            queue.remove();
            queue.add(queue.poll());
        }

        System.out.println(queue.poll());
    }
}
