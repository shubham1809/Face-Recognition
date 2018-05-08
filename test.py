from elasticsearch import Elasticsearch
import requests
es=Elasticsearch([{'host':'localhost','port':9200}])
res=requests.get('http://localhost:9200')
while(res.status_code==200):
    es.index(index='sss',doc_type="shubham",id=1,body={"name":"shubham","age":22})

es.get(index='sss',doc_type="shubham",id=1)
