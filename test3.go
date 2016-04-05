package main
import "fmt"

func main(){
	fmt.Println("Test 3 :")
	var a int = 14
	fmt.Print("a = ")
	fmt.Println(a)
	var b int = 0
	var c int = 10
	if a == 14	{
		b = a + 2
		fmt.Print("b = ")
		fmt.Println(b)
	}
	for b < 1 || a > 10	{
		a = a - 2
		fmt.Println("boucle 1 : OR")
	}
	fmt.Println("boucle 2 : do while et AND ")
	for b < 1 && a <= 10	{
		fmt.Println("boucle 2 : do while et AND ")
	}
	for b != 2	{
		b = b - 2
		c = c + b
		for c >= 4		{
			c = c - 4
			fmt.Print("c = ")
			fmt.Println(c)
		}
	}
}