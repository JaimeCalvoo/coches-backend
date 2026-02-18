from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import os
from openai import OpenAI

app = FastAPI()

# Cargar la API key desde Render
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/scan")
async def scan_car(file: UploadFile = File(...)):
    image_bytes = await file.read()

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": "Identifica la marca y modelo exacto del coche en esta imagen. Responde solo con: Marca - Modelo"},
                    {"type": "input_image", "image": image_bytes}
                ]
            }
        ]
    )

    detected_text = response.output_text

    return JSONResponse(content={
        "detected": detected_text
    })
