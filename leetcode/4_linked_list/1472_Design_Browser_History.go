type Page struct {
	URL  string
	Prev string
	Next string
}

type BrowserHistory struct {
	currPage *Page
}

func Constructor(homepage string) BrowserHistory {
	currPage := &Page{homepage, "", ""}
	currPage.Next = homepage
	currPage.Prev = homepage
	return BrowserHistory{currPage}
}

func (this *BrowserHistory) Visit(url string) {
	this.currPage.Next = &Page{URL: url, Prev: this.currPage.URL, Next: this.currPage.URL}
	this.currPage = this.currPage.Next
}

func (this *BrowserHistory) Back(steps int) string {
	for i := 0; i < steps; i++ {
		if this.currPage == this.currPage.Prev {
			break
		}
		this.currPage = this.currPage.Prev
	}
	return this.currPage.URL
}

func (this *BrowserHistory) Forward(steps int) string {
	for i := 0; i < steps; i++ {
		if this.currPage == this.currPage.Next {
			break
		}
		this.currPage = this.currPage.Next
	}
	return this.currPage.URL
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * obj := Constructor(homepage);
 * obj.Visit(url);
 * param_2 := obj.Back(steps);
 * param_3 := obj.Forward(steps);
 */
