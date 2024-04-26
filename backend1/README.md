docker build -t myfastapiapp .
docker run -d --name myfastapiapp -p 8000:8000 myfastapiapp
