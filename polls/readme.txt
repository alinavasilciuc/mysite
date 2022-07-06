1. Our browser sent a message to the Django development server requesting it return 
content located at the root URL (http://localhost:8000/polls/).
2. Django then looked for a URL pattern matching the request, by first searching 
the site level mysite/urls.py, and then each of the apps for a urls.py file containing a 
pattern that matches.
3. Django checks the first pattern (admin/) in our site level urls.py which doesn’t 
match and moves on to the second line in which the patter (polls/) matches.
4. The matching pattern includes the polls/urls.py from the polls app. Basically, this 
include says “go look in the polls app for a pattern that matches”.
5. Once in the app-level urls.py, the empty string matches, so the request is sent 
to the index view.
6. The index view then renders our simple HTML message to a HttpResponse and sends 
it to the browser.
7. The browser renders the response and we see our page heading.

Every Django application follows this same basic process each time it receives 
a request from the browser.