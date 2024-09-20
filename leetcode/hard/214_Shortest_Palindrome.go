func reverse(input string) string {
    runes := []rune(input)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}

func shortestPalindrome(s string) string {
    revS := reverse(s)

    for i:=0; i<len(s); i++ {
        ls := s[:len(s)-i]
        rs := revS[i:len(s)]
        if ls == rs {
            return revS + s[len(s)-i:]
        }
    }

    return s
}
