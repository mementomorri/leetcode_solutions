package main

import (
	"io"
	"os"
	"strings"
)

type rot13Reader struct {
	r io.Reader
}

func (r *rot13Reader) Read(b []byte) (int, error) {
	n, err := r.r.Read(b) // Read from the underlying reader
	if err != nil {
		return n, err
	}

	// Apply ROT13 transformation
	for i := 0; i < n; i++ {
		if b[i] >= 'A' && b[i] <= 'Z' {
			b[i] = (b[i]-'A'+13)%26 + 'A' // Rotate uppercase letters
		} else if b[i] >= 'a' && b[i] <= 'z' {
			b[i] = (b[i]-'a'+13)%26 + 'a' // Rotate lowercase letters
		}
	}

	return n, nil // Return the number of bytes read and no error
}

func main() {
	s := strings.NewReader("Lbh penpxrq gur pbqr!")
	r := rot13Reader{s}
	io.Copy(os.Stdout, &r)
}
