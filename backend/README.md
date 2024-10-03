# How to build and run the FastAPI app in Docker

docker build -t myfastapiapp .
docker run -d --name myfastapiapp -p 8000:8000 myfastapiapp

# How to run the FastAPI app locally

```cmd
cd ./app
fastapi run main.py
```
