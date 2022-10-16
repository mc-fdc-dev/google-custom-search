from google_custom_search import CustomSearch, RequestsAdapter


customsearch = CustomSearch(RequestsAdapter("apikey", "engine_id"))
for item in customsearch.search("python"):
    print(item.title)
