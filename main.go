package main

import (
	"SimpleMath/meth"
	"fmt"
)

func main() {
	var (
		num1 float32
		num2 float32
		num3 int
	)
	fmt.Print("enter the first number : ")
	fmt.Scanln(&num1)
	fmt.Print("enter the second number : ")
	fmt.Scanln(&num2)
	fmt.Print(`1 for addition
2 for subtraction 
3 for multiipacation 
4 for division`)
	fmt.Scanln(&num3)

	switch num3 {
	case 1:
		fmt.Print("the sum is :", meth.Add(num1, num2))
	case 2:
		fmt.Print("the difference is :", meth.Sub(num1, num2))
	case 3:
		fmt.Print("the product is :", meth.Mul(num1, num2))
	case 4:
		fmt.Print("the quotient is :", meth.Div(num1, num2))
	default:
		fmt.Print("invalid int!!")
	}

}
