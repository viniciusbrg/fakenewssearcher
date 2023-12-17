from elasticsearch import Elasticsearch

client = Elasticsearch(
    "https://localhost:9200",
    api_key="WC1RaWM0d0IyQWpXMURDU1AyT2o6Z1Z3WTQ0OHVUcnFaLWdzaTNjXzN5QQ==",
    verify_certs=False
)

# API key should have cluster monitor rights
# print(client.info())

print(client.search(index="ze", q="snow"))