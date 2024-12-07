import java.util.*;
import java.util.regex.*;
import java.io.*;
import java.lang.*;

public class day7 {
  public static void main(String[] args) throws IOException {
    Scanner scan = new Scanner(new File("./day7.txt"));
    long count = 0;
    while (scan.hasNextLine()) {
      String line = scan.nextLine();
      Matcher m = Pattern.compile("^\\d+").matcher(line);
      while (m.find()) {
        // for now
        count += Long.parseLong(m.group());
      }
    }
    System.out.println("Part 1: "+count);
  }
}
