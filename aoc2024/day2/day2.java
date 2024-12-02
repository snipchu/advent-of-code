import java.util.*;
import java.io.*;
import java.lang.*;

public class day2 {
  public static ArrayList<Integer> reverse(ArrayList<Integer> c) {
    ArrayList<Integer> copy = (ArrayList) c.clone();
    Collections.reverse(copy);
    return copy;
  }
  public static ArrayList<Integer> sort(ArrayList<Integer> c) {
    ArrayList<Integer> copy = (ArrayList) c.clone();
    Collections.sort(copy);
    return copy;
  }
  public static void main(String[] args) throws IOException {
    Scanner scan = new Scanner(new File("./day2.txt"));
    ArrayList<Integer> c = new ArrayList<Integer>();
    int count = 0;
    int count2 = 0;
    while (scan.hasNextLine()) {
      boolean safe=true;
      String[] input = scan.nextLine().split(" ");
      for (String i:input) { c.add(Integer.valueOf(i)); }
      if (!c.equals(sort(c)) && !c.equals(reverse(sort(c)))) {
        safe=false;
      }
      for (int i=1; i<c.size(); i++) {
        if (Math.abs(c.get(i)-c.get(i-1)) > 3 || c.get(i)==c.get(i-1)) {
          safe = false;
        }
      }
      if (safe) {count++;}
      c.clear();
    }
    System.out.println("Part 1: "+count);
    System.out.println("Part 2: "+count2);
  }
}
