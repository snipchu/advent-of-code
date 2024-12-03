import java.util.*;
import java.util.regex.*;
import java.io.*;
import java.lang.*;

public class day3 {
  public static void main(String[] args) throws IOException {
    Scanner scan = new Scanner(new File("./day3.txt"));
    int count = 0;
    int count2 = 0;
    boolean enabled = true;
    while (scan.hasNextLine()) {
      String line = scan.nextLine();
      Matcher m = Pattern.compile("mul\\((\\d+),(\\d+)\\)").matcher(line);
      while (m.find()) {
        String getlast = line.substring(0,m.start());
        if (getlast.lastIndexOf("do()")>getlast.lastIndexOf("don't()")) {
          enabled = true;
        } else if (getlast.lastIndexOf("do()")<getlast.lastIndexOf("don't()")) {
          enabled = false;
        }
        count += Integer.valueOf(m.group(1)) * Integer.valueOf(m.group(2));
        if (enabled)
          count2 += Integer.valueOf(m.group(1)) * Integer.valueOf(m.group(2));
      }
    }
    System.out.println("Part 1: "+count);
    System.out.println("Part 2: "+count2);
  }
}
