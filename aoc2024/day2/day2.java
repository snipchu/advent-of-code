import java.util.*;
import java.io.*;
import java.lang.*;

public class day2 {
  public static boolean checkjumps(ArrayList<Integer> lol) {
    for (int i=0; i<lol.size()-1; i++) {
      int x = lol.get(i);
      int y = lol.get(i+1);
      if (x==y || Math.abs(x-y)>3) { return false; }
    } return true;
  }
  public static boolean sorted(ArrayList<Integer> lol) {
    ArrayList<Integer> foo = (ArrayList)lol.clone();
    Collections.sort(foo);
    ArrayList<Integer> foo2 = (ArrayList)foo.clone();
    Collections.reverse(foo2);
    return (lol.equals(foo) || lol.equals(foo2));
  }
  public static void main(String[] args) throws IOException {
    Scanner scan = new Scanner(new File("./day2.txt"));
    int count = 0;
    int count2 = 0;
    while (scan.hasNextLine()) {
      boolean increasing = true;
      ArrayList<Integer> c = new ArrayList<Integer>();
      for (String i:scan.nextLine().split(" ")) {c.add(Integer.valueOf(i));}
      if (c.get(0)>c.get(c.size()-1)) {increasing = false;}

      if (sorted(c) && checkjumps(c)) {
        //part1
        count++;
        count2++;
        System.out.println(c+" - All good!");
      } else {
        System.out.println(c+" - ?");
        for (int i=0; i<c.size(); i++) {
          ArrayList<Integer> foo = (ArrayList)c.clone();
          foo.remove(c.get(i));
          if (sorted(foo) && checkjumps(foo)) {
            count2++;
            System.out.println(c+" - Part 2 good!");
            break;
          }
        }
      }
    }
    System.out.println("Part 1: "+count);
    System.out.println("Part 2: "+count2);
  }
}
