This provider needs:
script.module.beautifulsoup4    http://mirrors.kodi.tv/addons/frodo/script.module.beautifulsoup4/script.module.beautifulsoup4-4.3.2.zip
script.module.requests          https://github.com/beenje/script.module.requests/archive/v2.8.1.zip  



Introduction
===================
By default, the provider use the url address to search:
	movie:  Movie title
	episode: TV Show title plus S00E00
	general search: not change

If you want to add some word to the search, you can use the extra field. 
Ex: Swedish
It would add the word 'Swedish' to every search
	movie:  Movie title and year plus 'Swedish' or IMDB_ID
	episode: TV Show title plus S00E00 plus 'Swedish'

Advanced Filtering
===================
I want to look for files that includes 720P and HDTV or 1080p:

I need to write in the Accept files with:
	720p HDTV, 1080p
	
The space always will be as 'OR' operator and the comma ',' as 'AND' operator

