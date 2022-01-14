package main

import (
	"fmt"
)

type Rectangle struct {
	long int
	wide int
}

type Address struct {
	nation   string
	province string
	city     string
	street   string
}

type Vcard struct {
	name string
	add  Address
	bday string
}

func (r *Rectangle) Area() int {
	return r.long * r.wide
}

func (r *Rectangle) Perimeter() int {
	return 2 * (r.long + r.wide)
}
func main() {
	r := Rectangle{7, 3}
	fmt.Println(r.Area())
	fmt.Println(r.Perimeter())

}
