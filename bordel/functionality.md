index

	Index page is a comic page showing the latest comic. There are six buttons on the right side - next, previous, random, about, comics, top

	next button shows (current comics id plus one)
	previous button shows (current comics id minus one)
	random button shows random comics
	top button shows top page 
	comics button always returns to index
	about button shows about page

comic page
	
	is any page showing any kind of comic. it's basically index page, but it can contain any comics, not just the latest one. 

top page
	
	top page shows list of top ten comics. in the first run, top page will show manually picked strips, in later functionality when internal like button is added, it will show strips with the largest amount of likes. the list contains thumbnails of those strips, shows them in modal when clicked

about page
	
	is a simple page describing the history of the comics in few words, contains paypal button. 

index page functionality

	retrieve id of latest comic from database - write python function for that

To Do:

* make Previous, Random and Next buttons text black when viewing comics, make about and top buttons text black when visiting those pages
