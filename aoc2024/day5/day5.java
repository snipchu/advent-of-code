import java.util.*;
import java.io.*;
import java.lang.*;

public class day4 {
  public static void ish(String line, int row, int col) {
    if (col>3)
      System.out.printf("\tLeft of (%d, %d): %s\n", row, col, line.substring(col-3,col));
    if (col<line.length()-4)
      System.out.printf("\tRight of (%d, %d): %s\n", row, col, line.substring(col+1,col+4));
    if (row>3)
      System.out.printf("\tRight of (%d, %d): %s\n", row, col, line.substring(col+1,col+4));
    //return (line.substring(col-3,col).equals("SAM") || line.substring(col+1,col+4).equals("MAS"));
  }
  public static int searchx(String line, int col) {
    for (int i=0; i<line.length(); i++) {
      if (line.substring(i,i+1).equals("X")) {
        System.out.printf("Found X at (%d, %d)\n", col, i);
        ish(line, col, i);
      }
    }
    return 1;
  }
  public static void main(String[] args) throws IOException {
    Scanner scan = new Scanner(new File("./day4.txt"));
    int count = 0;
    int count2 = 0;
    int xmas=0;
    ArrayList<String> grid = new ArrayList<String>();
    while (scan.hasNextLine()) { grid.add(scan.nextLine()); }
    for (int i=0; i<grid.size(); i++) {
      xmas+=searchx(grid.get(i),i);
    }
    System.out.println("Part 1: "+count);
    System.out.println("Part 2: "+count2);
  }
}
