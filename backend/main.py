import uvicorn

# RUN THE API 
if __name__ == "__main__":
    uvicorn.run("server.app:app", port=3000, reload=True)