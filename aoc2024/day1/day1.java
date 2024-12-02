import java.util.*;
import java.io.*;
import java.lang.*;

public class day1 {
  public static void main(String[] args) throws IOException {
    Scanner scan = new Scanner(new File("./day1.txt"));
    ArrayList<Integer> c1 = new ArrayList<Integer>();
    ArrayList<Integer> c2 = new ArrayList<Integer>();

    while (scan.hasNextLine()) {
      String[] line = scan.nextLine().split("   ");
      c1.add(Integer.valueOf(line[0]));
      c2.add(Integer.valueOf(line[1]));
    }
    Collections.sort(c1);
    Collections.sort(c2);

    // part 1
    int sum = 0;
    for (int i=0; i<c1.size(); i++) {
      sum += Math.abs(c1.get(i)-c2.get(i));
    }
    System.out.println("Part 1: " + sum);
    // part 2
    sum = 0;
    for (int i=0; i<c1.size(); i++) {
      sum += c1.get(i)*Collections.frequency(c2, c1.get(i));
    }
    System.out.println("Part 2: " + sum);
  }
}
