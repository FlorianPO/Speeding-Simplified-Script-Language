package main
import "fmt"

func main(){
	var a int
	var b int = 13
	fmt.Println(b)
	a = 15
	fmt.Println(15)
	a = b
	fmt.Println(a)
	var c int = a + 15
	fmt.Println(c)
	c = c - a
	fmt.Println(c)
	c = 4 / 2
	fmt.Println(c)
}
