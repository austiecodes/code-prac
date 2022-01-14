package main

import "fmt"

func main() {
	var arr1 [100]int
	var slice1 []int = arr1[2:10]

	s := make([]byte, 5)

	fmt.Println(len(slice1))
	fmt.Println(cap(slice1))
	fmt.Println(len(s))
	fmt.Println(cap(s))

}

// in this program we can see the difference between cap(capacity) and len(length) of slice
