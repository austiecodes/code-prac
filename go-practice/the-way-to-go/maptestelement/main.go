package main

import (
	"fmt"
)

func main() {
	capitals := map[string]string{"France": "Paris", "Italy": "Rome", "Japan": "Tokyo"}
	for key := range capitals {
		fmt.Println("Map item: Capital of", key, "is", capitals[key])
	}
	// in this part you can see a strange thins: run this script couple times you can see the results dsiplayed in an uncertain order, which can not be explained now, but you will figure it out later

	weekdays := make(map[int]string)

	var dayName = [7]string{"Monday", "Tuesday", "Wednesdat", "Thursday", "Friday", "Saturday", "Sunday"}

	for i := range dayName {
		weekdays[i] = dayName[i]
	}

	for index, value := range weekdays {
		fmt.Printf("No.%d day in a week is %s\n", index+1, value)
	}

	mapsforrange()
}

func mapsforrange() {
	// Version A:
	items := make([]map[int]int, 5)
	for i := range items {
		items[i] = make(map[int]int, 1)
		items[i][1] = 2
	}
	fmt.Printf("Version A: Value of items: %v\n", items)

	// Version B: NOT GOOD!
	items2 := make([]map[int]int, 5)
	for _, item := range items2 {
		item = make(map[int]int, 1) // item is only a copy of the slice element.
		item[1] = 2                 // This 'item' will be lost on the next iteration.
	}
	fmt.Printf("Version B: Value of items: %v\n", items2)
}
