from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/scan")
async def scan_car(file: UploadFile = File(...)):
    result = {
        "marca": "Ferrari",
        "modelo": "F40",
        "precio": "1,2M €",
        "unidades": 350,
        "rareza": "Mítico",
        "semicirculo": 0.85
    }
    return JSONResponse(content=result)
