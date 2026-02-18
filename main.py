from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import openai

# Pega aquí tu clave de OpenAI
openai.api_key = "TU_API_KEY_AQUI"

app = FastAPI()

@app.post("/scan")
async def scan_car(file: UploadFile = File(...)):
    # Leemos la imagen (en bytes)
    image_bytes = await file.read()

    # Llamada a OpenAI (aún simulada para prototipo)
    # En el futuro aquí pondremos la llamada real al modelo de visión
    result = {
        "marca": "Ferrari",
        "modelo": "F40",
        "precio": "1,2M €",
        "unidades": 350,
        "rareza": "Mítico",
        "semicirculo": 0.85
    }

    return JSONResponse(content=result)
