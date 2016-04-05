package main
import "fmt"

func add(a int, b int) int {
	return a + b
}
func additionFloat(a float32, b float32) float32 {
	var c float32 = a + b
	return c
}
func sous(a int, b int) int {
	return a - b
}
func diff(a int, b int, c int) int {
	return sous(a, b) - c
}
func main(){
	fmt.Println("Test 4 :")
	var a int = 10
	var b int = 5
	var c int = 4
	var d float32 = 3.5
	var e float32 = 2.6
	a = add(a, b)
	fmt.Print("a = ")
	fmt.Println(a)
	d = additionFloat(d, e)
	fmt.Print("d = ")
	fmt.Println(d)
	a = diff(a, b, c)
	fmt.Print("a = ")
	fmt.Println(a)
}
