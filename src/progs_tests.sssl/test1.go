package main
import "fmt"

func main() {
	fmt.Println("Test 1 :")
	var a float32
	var b int = 13
	fmt.Print("b = ")
	fmt.Println(b)
	a = 15.3
	fmt.Println(15)
	fmt.Print("a = ")
	fmt.Println(a)
	var c int = b + 15
	fmt.Print("c = ")
	fmt.Println(c)
	c = c - b
	fmt.Print("c = ")
	fmt.Println(c)
	c = 4 / 2
	fmt.Print("c = ")
	fmt.Println(c)
	var test bool = true
	fmt.Println(test)
	var blabla string = "hello"
	fmt.Println(blabla + " you <3")
}