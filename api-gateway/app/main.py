from fastapi import FastAPI

app = FastAPI(title = "Api Gateaway")

@app.get("/health")
def health_check():
    return {"status": "API Gateway is running"}