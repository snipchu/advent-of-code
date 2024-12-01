package main

import (
  "fmt"
  "log"
  "os"
  "bufio"
  "strings"
)

func main() {
  log.SetFlags(0)

  // open file
  file, err := os.Open("./day1.txt")
  if err != nil {
    log.Fatal(err)
  }
  // iterate
  //col1 := make([]string, file.Stat().Size())
  //col2 := make([]string, file.Stat().Size())
  scanner := bufio.NewScanner(file)
  for scanner.Scan() {
    line := strings.Split(scanner.Text(), "   ")
  }
  fmt.Println("I'm gonna be dead honest I have zero idea how golang works")
}
