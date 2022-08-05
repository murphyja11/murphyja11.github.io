f = open("bookshelf.html", "w")
# add header
f.write("<!DOCTYPE html><html><body><h1>Bookshelf</h1>")
f.write("<p><div style='color:blue'>read</div><div style='color:green'>partly read</div><div style='color:orange'>unread</div></p>")

f.write("<ul>")
# add book list
books = {}
books["The Pocket Thich Naht Hanh"] = [2, "https://www.amazon.com/Pocket-Thich-Nhat-Shambhala-Classics/dp/1590309367"]
books["Chaos"] = [2, "https://www.amazon.com/Chaos-Making-Science-James-Gleick/dp/0143113453"]
books["The Mind-Gut Connection"] = [2, "https://www.amazon.com/Mind-Gut-Connection-Conversation-Impacts-Choices/dp/0062376551"]
books["This Is Your Brain On Food"] = [2, "https://www.amazon.com/This-Your-Brain-Food-Indispensable/dp/0316536822/ref=pd_lpo_2?pd_rd_i=0316536822&psc=1"]
books["Breath"] = [2, "https://www.amazon.com/Breath-New-Science-Lost-Art/dp/0735213615"]
books["The Story of the Human Body"] = [2, "https://www.amazon.com/Story-Human-Body-Evolution-Disease/dp/030774180X"]
books["The Oxygen Advantage"] = [0, "https://www.amazon.com/Oxygen-Advantage-Scientifically-Breathing-Techniques/dp/0062349473"]
books["Why We Sleep"] = [0, "https://www.amazon.com/Why-We-Sleep-Unlocking-Dreams/dp/1501144316"]
books["Atomic Habits"] = [1, "https://www.amazon.com/Atomic-Habits-Proven-Build-Break/dp/0735211299"]
books["The Big Book of Endurance Training and Racing"] = [1, "https://www.amazon.com/Big-Book-Endurance-Training-Racing/dp/1616080655"]
books["The Alchemist"] = [2, "https://www.amazon.com/Alchemist-Paulo-Coelho/dp/0061122416"]
books["Godel, Escher, Bach"] = [1, "https://www.amazon.com/G%C3%B6del-Escher-Bach-Eternal-Golden/dp/0465026567"]
books["Team of Rivals"] = [0, "https://www.amazon.com/Team-Rivals-Political-Abraham-Lincoln/dp/0743270754"]
books["Siddhartha"] = [1, "https://www.google.com/search?q=siddhartha&oq=siddhartha&aqs=chrome..69i57j46i433i512j0i512j0i20i263i512j46i433i512l2j0i512l4.2025j0j4&sourceid=chrome&ie=UTF-8"]
books["A Manual for Living"] = [0, "https://www.amazon.com/Manual-Living-Little-Wisdom-Francisco/dp/0062511114"]
books["Man's Search for Meaning"] = [0, "https://www.google.com/search?sxsrf=ALiCzsapoQYx_nEaT3Oj91JXHmwXC3Gbfg:1659009208759&q=Man%27s+Search+for+Meaning&stick=H4sIAAAAAAAAAONQFuLRT9c3NErKNbYsyTZQ4tTP1TcwrDRKKz_FiCJzihFZCsLOKjOvOsXIBWKbVOaWmBueYuQF6TFMTy8yL8pLqYRKmuUVpOVU_GK0DErNSSxJTVEoyVcIyUhVcCwqUchPUwjILy7OTMrMySypVEjMS1FwVMhNzCtNzFFIyy9SyMksy8xL38WC4phdLEjmLmKV8E3MUy9WCE5NLErOAOvyTU3MA2qbwMZ4i02SwfRjK9NNz_otUv_tClgvdH3pnfTx3hv1qGYAu22H1v4AAAA&sa=X"]
books["Why Zebras Don't Get Ulcers"] = [2, "https://www.amazon.com/Why-Zebras-Dont-Ulcers-Third/dp/0805073698/ref=pd_lpo_3?pd_rd_i=0805073698&psc=1"]
books["Behave"] = [0, "https://www.amazon.com/Behave-Biology-Humans-Best-Worst/dp/0143110918/ref=pd_lpo_2?pd_rd_i=0143110918&psc=1"]
books["The Information"] = [0, "https://www.amazon.com/Information-History-Theory-Flood/dp/1400096235/ref=pd_lpo_1?pd_rd_i=1400096235&psc=1"]
books["Statistics As Principled Argument"] = [0, "https://www.amazon.com/Statistics-Principled-Argument-Robert-Abelson/dp/0805805281"]
books["101 Essays that will Change the way You Think"] = [0, "https://www.amazon.com/Essays-That-Will-Change-Think/dp/1945796065/ref=asc_df_1945796065/?tag=hyprod-20&linkCode=df0&hvadid=312021238077&hvpos=&hvnetw=g&hvrand=5987409625835280258&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9002001&hvtargid=pla-634062587037&psc=1"]
books["Extreme Ownership"] = [0, ""]
books["Improv(e) your conversations"] = [0, ""]
books["Training for the Uphill Athlete"] = [0, ""]
books["The Triathlete's Training Bible"] = [0, ""]

colors = ["orange", "green", "blue"]

for book, [read, link] in books.items():
  color = colors[read]
  item = "<li><a href='{}' style='color:{}'>{}</a></li>".format(link, color, book)
  f.write(item)

f.write("</ul>")

# Other book lists
f.write("<h3>Other book lists</h3><ul>")
lists = {}
lists["Patrick Collison"] = "https://patrickcollison.com/bookshelf"
lists["James Clear"] = "https://jamesclear.com/best-books/wisdom"
lists["Shane Parrish"] = "https://fs.blog/the-most-page-for-page-wisdom/"
lists["Shane Parrish #2"] = "https://fs.blog/five-books/"
lists["Shane Parrish #3"] = "https://fs.blog/books-that-changed-my-life/"

for person, link in lists.items():
  f.write("<li><a href='{}'>{}</a></li>".format(link, person))
f.write("</ul>")

# How to read
f.write("<h3>Reading tips</h3><ul>")
f.write("<li><a href='https://fs.blog/how-to-read-a-book/'>How to Read a Book</a></li>")
f.write("<li><a href='https://fs.blog/reading/'>Reading Better</a></li>")
f.write("</ul>")

# close file
f.write(
  "</body></html>"
)
f.close()
