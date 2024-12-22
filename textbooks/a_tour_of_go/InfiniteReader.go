package main

import "golang.org/x/tour/reader"

type MyReader struct{}

func (r MyReader) Read(b []byte) (int, error) {
	for i := range b {
		b[i] = 'A' // Fill the byte slice with 'A'
	}
	return len(b), nil // Return the number of bytes written and no error
}

func main() {
	reader.Validate(MyReader{})
}
